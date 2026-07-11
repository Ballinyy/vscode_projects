"""
Animazione Manim: Teorema della Curva Invariante (Moser, 1962)
================================================================
Precursore del teorema KAM. Mostra:
  1) la mappa di twist integrabile T0 con curve invarianti r = cost.
  2) la perturbazione T_eps
  3) la dicotomia: curve diofantee sopravvivono deformate,
     curve risonanti si rompono in catene di isole (Poincaré-Birkhoff)
  4) l'enunciato del teorema

Render:
    manim -pql invariant_curve_theorem.py InvariantCurveTheorem   # bassa qualità, veloce
    manim -pqh invariant_curve_theorem.py InvariantCurveTheorem   # alta qualità
"""

from manim import *
import numpy as np


class InvariantCurveTheorem(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f17"
        self.intro()
        self.wait(0.5)
        self.integrable_twist_map()
        self.wait(0.5)
        self.perturbation_intro()
        self.wait(0.5)
        self.kam_result()
        self.wait(0.5)
        self.closing_statement()

    # ------------------------------------------------------------------
    def intro(self):
        title = Text("Il Teorema della Curva Invariante", font_size=44, color=YELLOW)
        subtitle = Text(
            "(Moser, 1962 — precursore della teoria KAM)",
            font_size=28, color=GRAY_B
        )
        subtitle.next_to(title, DOWN)
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

    # ------------------------------------------------------------------
    def integrable_twist_map(self):
        header = Text("Il sistema integrabile: una mappa di twist", font_size=32).to_edge(UP)
        self.play(Write(header))

        radii = np.linspace(0.6, 3.2, 6)
        circles = VGroup(*[
            Circle(radius=r, color=interpolate_color(BLUE_E, TEAL_A, i / 5), stroke_width=2)
            for i, r in enumerate(radii)
        ])
        self.play(LaggedStart(*[Create(c) for c in circles], lag_ratio=0.15))

        # punti che rappresentano orbite; ogni cerchio ruota col proprio "numero di rotazione"
        omegas = np.linspace(0.15, 0.55, 6)
        dots = VGroup(*[
            Dot(point=[r, 0, 0], radius=0.06, color=WHITE) for r in radii
        ])
        self.play(FadeIn(dots))

        formula = MathTex(
            r"T_0(\theta, r) = \big(\theta + 2\pi\,\omega(r),\; r\big)",
            font_size=36
        ).to_edge(DOWN)
        self.play(Write(formula))

        def make_updater(omega):
            def updater(mob, dt):
                mob.rotate(angle=dt * omega * TAU * 0.4, about_point=ORIGIN)
            return updater

        for dot, om in zip(dots, omegas):
            dot.add_updater(make_updater(om))

        self.wait(4)

        for dot in dots:
            dot.clear_updaters()

        self.play(FadeOut(formula))

        note = Text(
            "Ogni cerchio ruota con velocità propria ω(r):\n"
            "il 'twist' dipende dal raggio",
            font_size=26, color=GRAY_B
        ).to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)

        self.play(FadeOut(header), FadeOut(note), FadeOut(circles), FadeOut(dots))

    # ------------------------------------------------------------------
    def perturbation_intro(self):
        header = Text("Perturbiamo la mappa", font_size=32).to_edge(UP)
        self.play(Write(header))

        formula0 = MathTex(
            r"T_0(\theta, r) = \big(\theta + 2\pi\,\omega(r),\; r\big)"
        ).shift(UP * 0.5)
        arrow = MathTex(r"\Longrightarrow").next_to(formula0, DOWN)
        formula1 = MathTex(
            r"T_\varepsilon(\theta, r) = \big(\theta + 2\pi\,\omega(r) "
            r"+ \varepsilon\, f(\theta, r),\;\; r + \varepsilon\, g(\theta, r)\big)"
        ).next_to(arrow, DOWN)

        self.play(Write(formula0))
        self.play(Write(arrow))
        self.play(Write(formula1))
        self.wait(2)

        question = Text(
            "Domanda: sopravvivono le curve invarianti r = cost.?",
            font_size=28, color=YELLOW
        ).to_edge(DOWN)
        self.play(Write(question))
        self.wait(2)

        self.play(
            FadeOut(header), FadeOut(formula0), FadeOut(arrow),
            FadeOut(formula1), FadeOut(question)
        )

    # ------------------------------------------------------------------
    def kam_result(self):
        header = Text(
            "Risposta di Moser: dipende dall'aritmetica di ω(r)", font_size=30
        ).to_edge(UP)
        self.play(Write(header))

        axes_note = Text(
            "Sezione radiale della mappa perturbata", font_size=24, color=GRAY_B
        ).next_to(header, DOWN)
        self.play(FadeIn(axes_note))

        # --- curva invariante che sopravvive (rotazione diofantea) ---
        base_radius = 2.0

        def survive_curve(t):
            r = base_radius + 0.15 * np.cos(5 * t) + 0.05 * np.sin(3 * t)
            return np.array([r * np.cos(t), r * np.sin(t), 0])

        surviving = ParametricFunction(survive_curve, t_range=[0, TAU], color=GREEN)
        surv_label = Text(
            "ω diofanteo: la curva sopravvive, solo deformata",
            font_size=22, color=GREEN
        ).to_edge(DOWN)

        self.play(Create(surviving))
        self.play(Write(surv_label))
        self.wait(2)
        self.play(FadeOut(surviving), FadeOut(surv_label))

        # --- curva risonante: si rompe in catene di isole ---
        n_islands = 5
        R = 1.1
        island_group = VGroup()
        for k in range(n_islands):
            angle = k * TAU / n_islands
            center = R * np.array([np.cos(angle), np.sin(angle), 0])
            island = Ellipse(width=0.6, height=0.35, color=RED)
            island.rotate(angle + PI / 2)
            island.move_to(center)
            island_group.add(island)

        guide_circle = Circle(radius=R, color=GRAY_D, stroke_opacity=0.4)
        res_label = Text(
            "ω razionale (risonante): la curva si rompe in catene di isole\n"
            "(teorema di Poincaré–Birkhoff)",
            font_size=22, color=RED
        ).to_edge(DOWN)

        self.play(Create(guide_circle))
        self.play(LaggedStart(*[Create(isl) for isl in island_group], lag_ratio=0.2))
        self.play(Write(res_label))
        self.wait(2)

        self.play(
            FadeOut(header), FadeOut(axes_note), FadeOut(guide_circle),
            FadeOut(island_group), FadeOut(res_label)
        )

    # ------------------------------------------------------------------
    def closing_statement(self):
        title = Text(
            "Teorema della Curva Invariante (Moser, 1962)",
            font_size=32, color=YELLOW
        ).to_edge(UP)
        self.play(Write(title))

        statement = Text(
            "Se la mappa di twist T0 è sufficientemente liscia e il twist\n"
            "non è degenere, allora per ogni ω che soddisfa una condizione\n"
            "diofantea\n\n"
            "        |ω − p/q| ≥ c / q^(2+δ)   per ogni p/q ∈ ℚ,\n\n"
            "la corrispondente curva invariante {r = cost.} persiste,\n"
            "deformata ma non distrutta, per perturbazioni ε\n"
            "sufficientemente piccole.",
            font_size=26,
            line_spacing=1.2,
        ).next_to(title, DOWN, buff=0.6)

        self.play(Write(statement))
        self.wait(4)

        moral = Text(
            "La maggior parte dei tori (in misura di Lebesgue) sopravvive:\n"
            "è il germe della teoria KAM.",
            font_size=26, color=BLUE_B
        ).to_edge(DOWN)
        self.play(FadeIn(moral, shift=UP))
        self.wait(3)
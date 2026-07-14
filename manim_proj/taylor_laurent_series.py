"""
Serie di Taylor e Serie di Laurent per funzioni olomorfe -- animazione Manim
=============================================================================

Due scene indipendenti, nello stile di cauchy_goursat.py:

- TaylorSeriesScene : dimostrazione della serie di Taylor a partire dalla
  formula integrale di Cauchy, espandendo il nucleo 1/(w-z) in serie
  geometrica sul disco |z - z0| < r.

- LaurentSeriesScene : dimostrazione della serie di Laurent su un anello
  r < |z - z0| < R, tramite due contorni (esterno e interno) e due
  espansioni geometriche diverse (potenze positive e negative).

Layout: il disegno geometrico (piano complesso) sta a sinistra, la
derivazione in LaTeX si accumula a destra, passo dopo passo.

Render:
    manim -pql taylor_laurent.py TaylorSeriesScene
    manim -pql taylor_laurent.py LaurentSeriesScene
"""

from manim import *
import numpy as np

# --------------------------------------------------------------------------
# Colori (stessa palette di cauchy_goursat.py, con l'aggiunta di R/r)
# --------------------------------------------------------------------------
COL_TEXT = WHITE
COL_ACCENT = "#4FC3F7"      # azzurro chiaro
COL_RESULT = "#00E676"      # verde acceso per il risultato finale
COL_R = "#2979FF"           # contorno esterno (raggio R) -- ben distinto da COL_ACCENT
COL_r = "#FF5252"           # contorno interno (raggio r)
COL_Z0 = "#FFCA28"          # centro z0
COL_Z = "#EC407A"           # punto z -- distinto da COL_RESULT (verde)
COL_ANNULUS = "#7E57C2"     # riempimento anello


def fit_width(mobj, max_w=6.2, max_h=None):
    """Evita che le formule LaTeX escano dallo schermo (in larghezza e, se richiesto, altezza)."""
    if mobj.width > max_w:
        mobj.scale_to_fit_width(max_w)
    if max_h is not None and mobj.height > max_h:
        mobj.scale_to_fit_height(max_h)
    return mobj


class ComplexPlaneScene(MovingCameraScene):
    """Classe base con utilità condivise dalle due dimostrazioni."""

    def make_axes(self):
        axes = Axes(
            x_range=[-3.2, 3.2, 1], y_range=[-3.2, 3.2, 1],
            x_length=6.4, y_length=6.4,
            axis_config={"color": GRAY_C, "stroke_width": 1.5},
            tips=False,
        )
        axes.to_edge(LEFT, buff=0.7)
        labels = VGroup(
            MathTex(r"\mathrm{Re}", font_size=24, color=GRAY_C).next_to(axes.x_axis, RIGHT, buff=0.15),
            MathTex(r"\mathrm{Im}", font_size=24, color=GRAY_C).next_to(axes.y_axis, UP, buff=0.15),
        )
        return axes, labels

    def add_step(self, stack, mobj, buff=0.35, max_w=6.2):
        """Aggiunge un passaggio alla colonna di destra e lo mostra."""
        fit_width(mobj, max_w)
        if len(stack) == 0:
            mobj.to_edge(RIGHT, buff=0.6).shift(UP * 2.2)
        else:
            mobj.next_to(stack[-1], DOWN, buff=buff, aligned_edge=LEFT)
        stack.add(mobj)
        self.play(FadeIn(mobj, shift=UP * 0.15))
        return mobj

    def clear_stack(self, stack, extra=None):
        group = VGroup(*stack.submobjects)
        if extra is not None:
            group = VGroup(group, extra)
        self.play(FadeOut(group))
        stack.submobjects = []


# ==========================================================================
# 1. SERIE DI TAYLOR
# ==========================================================================
class TaylorSeriesScene(ComplexPlaneScene):

    def construct(self):
        self.title_and_statement()
        self.setup_geometry()
        self.cauchy_formula()
        self.geometric_expansion()
        self.swap_sum_integral()
        self.final_result()

    # ------------------------------------------------------------
    def title_and_statement(self):
        title = Text("Serie di Taylor", font_size=48, weight=BOLD, color=COL_TEXT)
        title.to_edge(UP, buff=0.6)

        hyp = Tex(
            r"Sia $f$ olomorfa su un aperto $\Omega$ e sia $D(z_0,R) \subset \Omega$",
            font_size=30, color=COL_TEXT,
        )
        arrow = MathTex(r"\Downarrow", font_size=30, color=COL_TEXT)
        concl = MathTex(
            r"f(z) = \sum_{n=0}^{\infty} a_n (z-z_0)^n, \quad \forall\, |z-z_0| < R",
            font_size=36, color=COL_RESULT,
        )
        coeff = MathTex(
            r"a_n = \frac{1}{2\pi i}\oint_{\gamma} \frac{f(w)}{(w-z_0)^{n+1}}\, dw"
            r"= \frac{f^{(n)}(z_0)}{n!}",
            font_size=28, color=COL_ACCENT,
        )
        for m in (hyp, arrow, concl, coeff):
            fit_width(m, 11.5)

        stack = VGroup(hyp, arrow, concl, coeff).arrange(DOWN, buff=0.4)
        fit_width(stack, 11.5, max_h=5.6)
        stack.next_to(title, DOWN, buff=0.6)

        self.play(Write(title))
        self.wait(0.4)
        self.play(FadeIn(hyp, shift=UP * 0.2))
        self.play(Write(arrow))
        self.play(Write(concl))
        self.wait(1.5)
        self.play(FadeIn(coeff, shift=UP * 0.2))
        self.wait(3)
        self.play(FadeOut(VGroup(title, hyp, arrow, concl, coeff)))
        self.wait(0.3)

    # ------------------------------------------------------------
    def setup_geometry(self):
        axes, axes_labels = self.make_axes()

        z0 = np.array([0.0, 0.0])
        r_big = 2.6   # raggio del disco di olomorfia (bordo di Omega, tratteggiato)
        r_gamma = 1.7  # raggio del contorno gamma su cui si integra
        z_pt = np.array([0.55, 0.35])  # punto z interno a gamma

        omega_boundary = DashedVMobject(
            Circle(radius=r_big, color=GRAY_B, stroke_width=2).move_to(axes.c2p(*z0)),
            num_dashes=40,
        )
        gamma = Circle(radius=r_gamma, color=COL_ACCENT, stroke_width=3).move_to(axes.c2p(*z0))

        dot_z0 = Dot(axes.c2p(*z0), color=COL_Z0)
        label_z0 = MathTex("z_0", font_size=28, color=COL_Z0).next_to(dot_z0, DOWN, buff=0.15)

        dot_z = Dot(axes.c2p(*z_pt), color=COL_Z)
        label_z = MathTex("z", font_size=28, color=COL_Z).next_to(dot_z, UR, buff=0.1)

        r_line = Line(axes.c2p(*z0), axes.c2p(r_gamma, 0), color=COL_ACCENT, stroke_width=2)
        r_label = MathTex("r", font_size=26, color=COL_ACCENT).next_to(r_line, DOWN, buff=0.1)

        omega_label = MathTex(r"\Omega", font_size=30, color=GRAY_B)
        omega_label.move_to(axes.c2p(r_big * 0.72, r_big * 0.72))

        gamma_label = MathTex(r"\gamma", font_size=28, color=COL_ACCENT)
        gamma_label.move_to(axes.c2p(r_gamma * 0.75, r_gamma * 0.75))

        self.play(FadeIn(axes), FadeIn(axes_labels))
        self.play(Create(omega_boundary), FadeIn(omega_label))
        self.play(FadeIn(dot_z0), Write(label_z0))
        self.play(Create(gamma), FadeIn(gamma_label))
        self.play(Create(r_line), Write(r_label))
        self.play(FadeIn(dot_z), Write(label_z))
        self.wait(1)

        note = Tex(r"$\gamma$: circonferenza $|w-z_0|=r$, con $|z-z_0|<r<R$",
                    font_size=24, color=COL_TEXT)
        fit_width(note, 11.5)
        note.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note, shift=UP * 0.15))
        self.wait(2)
        self.play(FadeOut(note))

        # salva riferimenti per le fasi successive
        self.axes = axes
        self.geometry = VGroup(
            axes, axes_labels, omega_boundary, omega_label,
            dot_z0, label_z0, gamma, gamma_label, r_line, r_label,
            dot_z, label_z,
        )
        self.stack = VGroup()

    # ------------------------------------------------------------
    def cauchy_formula(self):
        heading = Text("Formula integrale di Cauchy", font_size=26,
                        weight=BOLD, color=COL_TEXT)
        heading.to_edge(UP, buff=0.4).shift(RIGHT * 3)
        self.play(FadeIn(heading, shift=DOWN * 0.2))
        self.heading = heading

        f1 = MathTex(
            r"f(z) = \frac{1}{2\pi i} \oint_{\gamma} \frac{f(w)}{w - z}\, dw",
            font_size=34, color=COL_TEXT,
        )
        self.add_step(self.stack, f1)
        self.wait(2)

    # ------------------------------------------------------------
    def geometric_expansion(self):
        f2 = MathTex(
            r"\frac{1}{w-z} = \frac{1}{(w-z_0)-(z-z_0)}",
            font_size=32, color=COL_TEXT,
        )
        self.add_step(self.stack, f2)
        self.wait(1.5)

        f3 = MathTex(
            r"= \frac{1}{w-z_0} \cdot \frac{1}{1 - \dfrac{z-z_0}{w-z_0}}",
            font_size=32, color=COL_TEXT,
        )
        self.add_step(self.stack, f3)
        self.wait(1.5)

        note = Tex(
            r"su $\gamma$: $\left|\dfrac{z-z_0}{w-z_0}\right| = \dfrac{|z-z_0|}{r} < 1$",
            font_size=26, color=COL_ACCENT,
        )
        self.add_step(self.stack, note, buff=0.3)
        self.wait(1.5)

        f4 = MathTex(
            r"\frac{1}{w-z} = \sum_{n=0}^{\infty} \frac{(z-z_0)^n}{(w-z_0)^{n+1}}",
            font_size=32, color=COL_RESULT,
        )
        self.add_step(self.stack, f4)
        self.wait(1)

        note2 = Tex(r"(serie geometrica, converge uniformemente per $w \in \gamma$)",
                     font_size=22, color=GRAY_B)
        self.add_step(self.stack, note2, buff=0.25)
        self.wait(2)

        # ripulisce lo stack, mantenendo solo il risultato dell'espansione
        self.play(FadeOut(VGroup(*[m for m in self.stack if m is not f4])))
        self.stack.submobjects = [f4]
        f4_new = f4.copy().to_edge(RIGHT, buff=0.6).shift(UP * 2.2)
        self.play(Transform(f4, f4_new))
        self.wait(0.5)

    # ------------------------------------------------------------
    def swap_sum_integral(self):
        f5 = MathTex(
            r"f(z) = \frac{1}{2\pi i} \oint_{\gamma} f(w) \sum_{n=0}^{\infty} \frac{(z-z_0)^n}{(w-z_0)^{n+1}}\, dw",
            font_size=28, color=COL_TEXT,
        )
        self.add_step(self.stack, f5)
        self.wait(2)

        note = Tex(
            r"convergenza uniforme $\Rightarrow$ si scambiano $\sum$ e $\oint$",
            font_size=24, color=COL_ACCENT,
        )
        self.add_step(self.stack, note, buff=0.3)
        self.wait(1.5)

        f6 = MathTex(
            r"f(z) = \sum_{n=0}^{\infty} (z-z_0)^n \left[ \frac{1}{2\pi i} \oint_{\gamma} \frac{f(w)}{(w-z_0)^{n+1}}\, dw \right]",
            font_size=26, color=COL_TEXT,
        )
        self.add_step(self.stack, f6)
        self.wait(2.5)

        f7 = MathTex(
            r"a_n := \frac{1}{2\pi i} \oint_{\gamma} \frac{f(w)}{(w-z_0)^{n+1}}\, dw = \frac{f^{(n)}(z_0)}{n!}",
            font_size=28, color=COL_ACCENT,
        )
        self.add_step(self.stack, f7)
        self.wait(2.5)

        self.clear_stack(self.stack, extra=self.heading)

    # ------------------------------------------------------------
    def final_result(self):
        heading = Text("Conclusione", font_size=28, weight=BOLD, color=COL_TEXT)
        heading.to_edge(UP, buff=0.4).shift(RIGHT * 3)

        result = MathTex(
            r"f(z) = \sum_{n=0}^{\infty} a_n\,(z-z_0)^n",
            font_size=36, color=COL_RESULT,
        )
        box = SurroundingRectangle(result, color=COL_RESULT, buff=0.3)
        note = Tex(
            r"valida per ogni $z$ nel disco $|z-z_0| < R$",
            font_size=24, color=COL_TEXT,
        )

        group = VGroup(result, note).arrange(DOWN, buff=0.5)
        group.next_to(heading, DOWN, buff=0.7)
        fit_width(result, 6.0)
        fit_width(note, 6.0)
        box = SurroundingRectangle(result, color=COL_RESULT, buff=0.3)

        self.play(FadeIn(heading, shift=DOWN * 0.2))
        self.play(Write(result))
        self.play(Create(box))
        self.wait(1)
        self.play(FadeIn(note, shift=UP * 0.15))
        self.wait(2.5)

        qed = Text("Q.E.D.", font_size=26, color=GRAY_B)
        qed.next_to(group, DOWN, buff=0.5)
        self.play(FadeIn(qed))
        self.wait(3)


# ==========================================================================
# 2. SERIE DI LAURENT
# ==========================================================================
class LaurentSeriesScene(ComplexPlaneScene):

    def construct(self):
        self.title_and_statement()
        self.setup_geometry()
        self.two_contours_formula()
        self.expand_outer()
        self.expand_inner()
        self.combine_result()

    # ------------------------------------------------------------
    def title_and_statement(self):
        title = Text("Serie di Laurent", font_size=48, weight=BOLD, color=COL_TEXT)
        title.to_edge(UP, buff=0.6)

        hyp = Tex(
            r"Sia $f$ olomorfa sull'anello $A = \{\, r < |z-z_0| < R \,\}$",
            font_size=30, color=COL_TEXT,
        )
        arrow = MathTex(r"\Downarrow", font_size=30, color=COL_TEXT)
        concl = MathTex(
            r"f(z) = \sum_{n=-\infty}^{\infty} c_n (z-z_0)^n, \quad \forall\, z \in A",
            font_size=34, color=COL_RESULT,
        )
        coeff = MathTex(
            r"c_n = \frac{1}{2\pi i}\oint_{\gamma} \frac{f(w)}{(w-z_0)^{n+1}}\,dw,"
            r"\quad n \in \mathbb{Z}",
            font_size=28, color=COL_ACCENT,
        )
        for m in (hyp, arrow, concl, coeff):
            fit_width(m, 11.5)

        stack = VGroup(hyp, arrow, concl, coeff).arrange(DOWN, buff=0.4)
        fit_width(stack, 11.5, max_h=5.6)
        stack.next_to(title, DOWN, buff=0.6)

        self.play(Write(title))
        self.wait(0.4)
        self.play(FadeIn(hyp, shift=UP * 0.2))
        self.play(Write(arrow))
        self.play(Write(concl))
        self.wait(1.5)
        self.play(FadeIn(coeff, shift=UP * 0.2))
        self.wait(3)
        self.play(FadeOut(VGroup(title, hyp, arrow, concl, coeff)))
        self.wait(0.3)

    # ------------------------------------------------------------
    def setup_geometry(self):
        axes, axes_labels = self.make_axes()

        z0 = np.array([0.0, 0.0])
        R1 = 2.6   # raggio del contorno esterno gamma_R
        r1 = 1.0   # raggio del contorno interno gamma_r
        z_pt = np.array([1.1, 0.9])  # punto z nell'anello, r1 < |z-z0| < R1

        outer_disk = Circle(radius=R1, color=COL_R, stroke_width=0,
                             fill_color=COL_ANNULUS, fill_opacity=0.25).move_to(axes.c2p(*z0))
        inner_disk = Circle(radius=r1, color=BLACK, stroke_width=0,
                             fill_color=BLACK, fill_opacity=1.0).move_to(axes.c2p(*z0))
        annulus = VGroup(outer_disk, inner_disk)

        gamma_R = Circle(radius=R1, color=COL_R, stroke_width=3).move_to(axes.c2p(*z0))
        gamma_r = Circle(radius=r1, color=COL_r, stroke_width=3).move_to(axes.c2p(*z0))

        dot_z0 = Dot(axes.c2p(*z0), color=COL_Z0)
        label_z0 = MathTex("z_0", font_size=28, color=COL_Z0).next_to(dot_z0, DOWN, buff=0.15)

        dot_z = Dot(axes.c2p(*z_pt), color=COL_Z)
        label_z = MathTex("z", font_size=28, color=COL_Z).next_to(dot_z, UR, buff=0.1)

        gR_label = MathTex(r"\gamma_R", font_size=28, color=COL_R)
        gR_label.move_to(axes.c2p(R1 * 0.75, R1 * 0.75))
        gr_label = MathTex(r"\gamma_r", font_size=24, color=COL_r)
        gr_label.move_to(axes.c2p(r1 * 1.15, r1 * 1.15))

        self.play(FadeIn(axes), FadeIn(axes_labels))
        self.play(FadeIn(annulus))
        self.play(Create(gamma_R), FadeIn(gR_label))
        self.play(Create(gamma_r), FadeIn(gr_label))
        self.play(FadeIn(dot_z0), Write(label_z0))
        self.play(FadeIn(dot_z), Write(label_z))
        self.wait(1)

        note = Tex(r"anello $A$: $r < |z-z_0| < R$, con $\gamma_r, \gamma_R \subset A$",
                    font_size=24, color=COL_TEXT)
        fit_width(note, 11.5)
        note.to_edge(DOWN, buff=0.4)
        self.play(FadeIn(note, shift=UP * 0.15))
        self.wait(2)
        self.play(FadeOut(note))

        self.axes = axes
        self.geometry = VGroup(
            axes, axes_labels, annulus, gamma_R, gR_label, gamma_r, gr_label,
            dot_z0, label_z0, dot_z, label_z,
        )
        self.stack = VGroup()

    # ------------------------------------------------------------
    def two_contours_formula(self):
        heading = Text("Cauchy su un dominio con un buco", font_size=24,
                        weight=BOLD, color=COL_TEXT)
        heading.to_edge(UP, buff=0.4).shift(RIGHT * 3)
        self.play(FadeIn(heading, shift=DOWN * 0.2))
        self.heading = heading

        note = Tex(
            r"tagliando l'anello con due segmenti radiali si ottiene un "
            r"dominio semplicemente connesso: i due tagli si percorrono "
            r"due volte in senso opposto e si cancellano",
            font_size=22, color=COL_TEXT,
        )
        self.add_step(self.stack, note, max_w=5.8)
        self.wait(2.5)

        f1 = MathTex(
            r"f(z) = \frac{1}{2\pi i}\oint_{\gamma_R}\!\frac{f(w)}{w-z}\,dw"
            r"\; - \;\frac{1}{2\pi i}\oint_{\gamma_r}\!\frac{f(w)}{w-z}\,dw",
            font_size=26, color=COL_TEXT,
        )
        self.add_step(self.stack, f1, max_w=5.8)
        self.wait(2.5)

        self.clear_stack(self.stack, extra=self.heading)

    # ------------------------------------------------------------
    def expand_outer(self):
        heading = Text("Contorno esterno: potenze positive", font_size=24,
                        weight=BOLD, color=COL_TEXT)
        heading.to_edge(UP, buff=0.4).shift(RIGHT * 3)
        self.play(FadeIn(heading, shift=DOWN * 0.2))
        self.heading = heading

        note = Tex(r"su $\gamma_R$: $|z-z_0| < |w-z_0|$, come nel caso di Taylor",
                    font_size=24, color=COL_ACCENT)
        self.add_step(self.stack, note, max_w=5.8)
        self.wait(1.5)

        f1 = MathTex(
            r"\frac{1}{w-z} = \sum_{n=0}^{\infty} \frac{(z-z_0)^n}{(w-z_0)^{n+1}}",
            font_size=30, color=COL_TEXT,
        )
        self.add_step(self.stack, f1)
        self.wait(1.5)

        f2 = MathTex(
            r"\frac{1}{2\pi i}\oint_{\gamma_R}\!\frac{f(w)}{w-z}\,dw"
            r"= \sum_{n=0}^{\infty} c_n\,(z-z_0)^n",
            font_size=26, color=COL_TEXT,
        )
        self.add_step(self.stack, f2, max_w=5.8)
        self.wait(1.5)

        f3 = MathTex(
            r"c_n := \frac{1}{2\pi i}\oint_{\gamma_R} \frac{f(w)}{(w-z_0)^{n+1}}\,dw,"
            r"\quad n \ge 0",
            font_size=24, color=COL_R,
        )
        self.add_step(self.stack, f3, max_w=5.8)
        self.wait(2.5)

        self.clear_stack(self.stack, extra=self.heading)

    # ------------------------------------------------------------
    def expand_inner(self):
        heading = Text("Contorno interno: potenze negative", font_size=24,
                        weight=BOLD, color=COL_TEXT)
        heading.to_edge(UP, buff=0.4).shift(RIGHT * 3)
        self.play(FadeIn(heading, shift=DOWN * 0.2))
        self.heading = heading

        note = Tex(r"su $\gamma_r$: $|w-z_0| < |z-z_0|$, si scambiano i ruoli",
                    font_size=24, color=COL_ACCENT)
        self.add_step(self.stack, note, max_w=5.8)
        self.wait(1.5)

        f1 = MathTex(
            r"\frac{1}{w-z} = -\frac{1}{z-z_0}\cdot\frac{1}{1-\dfrac{w-z_0}{z-z_0}}"
            r"= -\sum_{n=0}^{\infty} \frac{(w-z_0)^n}{(z-z_0)^{n+1}}",
            font_size=24, color=COL_TEXT,
        )
        self.add_step(self.stack, f1, max_w=5.8)
        self.wait(2)

        f2 = MathTex(
            r"-\frac{1}{2\pi i}\oint_{\gamma_r}\!\frac{f(w)}{w-z}\,dw"
            r"= \sum_{m=1}^{\infty} c_{-m}\,(z-z_0)^{-m}",
            font_size=24, color=COL_TEXT,
        )
        self.add_step(self.stack, f2, max_w=5.8)
        self.wait(1.5)

        f3 = MathTex(
            r"c_{-m} := \frac{1}{2\pi i}\oint_{\gamma_r} f(w)\,(w-z_0)^{m-1}\,dw,"
            r"\quad m \ge 1",
            font_size=22, color=COL_r,
        )
        self.add_step(self.stack, f3, max_w=5.8)
        self.wait(2.5)

        self.clear_stack(self.stack, extra=self.heading)

    # ------------------------------------------------------------
    def combine_result(self):
        heading = Text("Serie di Laurent", font_size=28, weight=BOLD, color=COL_TEXT)
        heading.to_edge(UP, buff=0.4).shift(RIGHT * 3)

        result = MathTex(
            r"f(z) = \sum_{n=-\infty}^{\infty} c_n\,(z-z_0)^n",
            font_size=34, color=COL_RESULT,
        )
        coeff = MathTex(
            r"c_n = \frac{1}{2\pi i}\oint_{\gamma} \frac{f(w)}{(w-z_0)^{n+1}}\,dw,"
            r"\quad n \in \mathbb{Z}",
            font_size=24, color=COL_TEXT,
        )
        note = Tex(
            r"$\gamma$ è una qualunque circonferenza $|w-z_0|=\rho$ con "
            r"$r<\rho<R$: l'integrando è olomorfo nell'anello, quindi "
            r"l'integrale non dipende dalla scelta di $\rho$",
            font_size=20, color=GRAY_B,
        )

        for m in (result, coeff, note):
            fit_width(m, 6.0)

        group = VGroup(result, coeff, note).arrange(DOWN, buff=0.45)
        group.next_to(heading, DOWN, buff=0.6)
        box = SurroundingRectangle(result, color=COL_RESULT, buff=0.3)

        self.play(FadeIn(heading, shift=DOWN * 0.2))
        self.play(Write(result))
        self.play(Create(box))
        self.wait(1)
        self.play(FadeIn(coeff, shift=UP * 0.15))
        self.wait(1.5)
        self.play(FadeIn(note, shift=UP * 0.15))
        self.wait(3)

        summary = Tex(
            r"Taylor: solo potenze $n\ge 0$, valida sul disco $|z-z_0|<R$ "
            r"$\;\Longrightarrow\;$ caso particolare di Laurent quando $r=0$",
            font_size=22, color=COL_ACCENT,
        )
        fit_width(summary, 6.0)
        summary.next_to(group, DOWN, buff=0.5)
        self.play(FadeIn(summary, shift=UP * 0.15))
        self.wait(3)

        qed = Text("Q.E.D.", font_size=26, color=GRAY_B)
        qed.next_to(summary, DOWN, buff=0.4)
        self.play(FadeIn(qed))
        self.wait(3)
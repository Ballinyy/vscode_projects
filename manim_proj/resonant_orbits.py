from manim import *
import numpy as np

# ==============================================================================
# SCENA 1 (3D): CASO RISONANTE (k · alpha = 0) -> Traiettorie Chiuse
# ==============================================================================
class ResonantOrbit3D(ThreeDScene):
    def construct(self):
        # 1. Orientamento della telecamera 3D
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES, zoom=0.8)
        self.begin_ambient_camera_rotation(rate=0.08)

        # 2. Testi e Formule (Fissati alla telecamera 2D/Fixed in Frame)
        title = Text("Caso risonante: moto periodico", font_size=32, color=WHITE).to_edge(UP)
        formula = Tex(
            r"esiste $k \in \mathbb{Z}^2 \setminus \{(0,0)\}$ tale che $k \cdot \alpha = 0$",
            font_size=28, color=YELLOW
        ).next_to(title, DOWN, buff=0.2)
        
        freq_info = MathTex(
            r"\alpha = (3.0, 2.0) \implies \frac{\alpha_1}{\alpha_2} = \frac{3}{2} \in \mathbb{Q}",
            font_size=24, color=BLUE_B
        ).to_edge(DOWN, buff=0.3)

        self.add_fixed_in_frame_mobjects(title, formula, freq_info)
        self.play(Write(title), Write(formula), Write(freq_info))

        # 3. Elementi dello Spazio 3D
        axes = ThreeDAxes(x_range=[-4, 4], y_range=[-4, 4], z_range=[-3, 3], axis_config={"stroke_width": 1})
        center_sun = Sphere(center=ORIGIN, radius=0.25, color=RED).set_color(RED)
        
        r1, r2 = 2.2, 3.4
        alpha1, alpha2 = 3.0, 2.0  # Risonanti con k = (2, -3) -> 2*3.0 + (-3)*2.0 = 0
        inc1, inc2 = 20 * DEGREES, -15 * DEGREES  # Inclinazioni orbite 3D

        # Tracker del tempo
        t_tracker = ValueTracker(0)

        # Pianeti 3D (Sfere)
        planet1 = Sphere(radius=0.1, color=BLUE)
        planet2 = Sphere(radius=0.12, color=ORANGE)

        # Tracce tridimensionali
        trace1 = TracedPath(planet1.get_center, stroke_color=BLUE, stroke_width=2.5, stroke_opacity=0.8)
        trace2 = TracedPath(planet2.get_center, stroke_color=ORANGE, stroke_width=2.5, stroke_opacity=0.8)

        # Equazioni parametriche del moto inclinato nello spazio 3D
        def pos_p1(t):
            x = r1 * np.cos(alpha1 * t)
            y = r1 * np.sin(alpha1 * t) * np.cos(inc1)
            z = r1 * np.sin(alpha1 * t) * np.sin(inc1)
            return np.array([x, y, z])

        def pos_p2(t):
            x = r2 * np.cos(alpha2 * t) * np.cos(inc2)
            y = r2 * np.sin(alpha2 * t)
            z = r2 * np.cos(alpha2 * t) * np.sin(inc2)
            return np.array([x, y, z])

        planet1.add_updater(lambda m: m.move_to(pos_p1(t_tracker.get_value())))
        planet2.add_updater(lambda m: m.move_to(pos_p2(t_tracker.get_value())))

        # 4. Rendering dell'animazione
        self.add(axes, center_sun, planet1, planet2, trace1, trace2)
        
        # Animazione di lunga durata (30 secondi)
        self.play(t_tracker.animate.set_value(12 * TAU), run_time=30, rate_func=linear)
        self.wait(2)

        # Pulizia scena
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(Group(*self.mobjects)))


# ==============================================================================
# SCENA 2 (3D): CASO NON RISONANTE (k · alpha != 0) -> Moto Quasi-Periodico
# ==============================================================================
class NonResonantOrbit3D(ThreeDScene):
    def construct(self):
        # 1. Orientamento della telecamera 3D
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES, zoom=0.8)
        self.begin_ambient_camera_rotation(rate=0.08)

        # 2. Testi e Formule (Fissati alla telecamera 2D/Fixed in Frame)
        title = Text("Caso non risonante: moto quasi-periodico", font_size=32, color=WHITE).to_edge(UP)
        formula = Tex(
            r"Per ogni $k \in \mathbb{Z}^2$ si ha $k \cdot \alpha \neq 0$",
            font_size=28, color=RED_B
        ).next_to(title, DOWN, buff=0.2)
        
        freq_info = MathTex(
            r"\alpha = (1.0, \sqrt{2}) \implies \frac{\alpha_1}{\alpha_2} \notin \mathbb{Q}",
            font_size=24, color=GREEN_B
        ).to_edge(DOWN, buff=0.3)

        self.add_fixed_in_frame_mobjects(title, formula, freq_info)
        self.play(Write(title), Write(formula), Write(freq_info))

        # 3. Elementi dello Spazio 3D
        axes = ThreeDAxes(x_range=[-4, 4], y_range=[-4, 4], z_range=[-3, 3], axis_config={"stroke_width": 1})
        center_sun = Sphere(center=ORIGIN, radius=0.25, color=RED).set_color(RED)

        r1, r2 = 2.2, 3.4
        alpha1, alpha2 = 1.0, np.sqrt(2)  # Rapporto irrazionale (incommensurabile)
        inc1, inc2 = 25 * DEGREES, -20 * DEGREES  # Inclinazioni orbite 3D

        t_tracker = ValueTracker(0)

        planet1 = Sphere(radius=0.1, color=BLUE)
        planet2 = Sphere(radius=0.12, color=ORANGE)

        # Opacità ridotta sulle tracce per evidenziare la densità del moto nel tempo
        trace1 = TracedPath(planet1.get_center, stroke_color=BLUE, stroke_width=1.5, stroke_opacity=0.4)
        trace2 = TracedPath(planet2.get_center, stroke_color=ORANGE, stroke_width=1.5, stroke_opacity=0.4)

        def pos_p1(t):
            x = r1 * np.cos(alpha1 * t)
            y = r1 * np.sin(alpha1 * t) * np.cos(inc1)
            z = r1 * np.sin(alpha1 * t) * np.sin(inc1)
            return np.array([x, y, z])

        def pos_p2(t):
            x = r2 * np.cos(alpha2 * t) * np.cos(inc2)
            y = r2 * np.sin(alpha2 * t)
            z = r2 * np.cos(alpha2 * t) * np.sin(inc2)
            return np.array([x, y, z])

        planet1.add_updater(lambda m: m.move_to(pos_p1(t_tracker.get_value())))
        planet2.add_updater(lambda m: m.move_to(pos_p2(t_tracker.get_value())))

        # 4. Rendering del moto quasi-periodico
        self.add(axes, center_sun, planet1, planet2, trace1, trace2)
        
        # Animazione estesa (35 secondi per apprezzare il riempimento continuo dello spazio)
        self.play(t_tracker.animate.set_value(20 * TAU), run_time=35, rate_func=linear)
        self.wait(2)
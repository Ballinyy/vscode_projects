from manim import *
import numpy as np

class TangentPlane(ThreeDScene):
    def construct(self):
        # Assi 3D
        axes = ThreeDAxes()

        # Superficie: z = x^2 + y^2 (paraboloide)
        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                u**2 + v**2
            ]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(30, 30),
            fill_opacity=0.6,
            checkerboard_colors=[BLUE_D, BLUE_E]
        )

        # Punto di tangenza
        x0, y0 = 1, 1
        z0 = x0**2 + y0**2

        point = Dot3D(point=[x0, y0, z0], color=RED)

        # Piano tangente: z = 2x0(x-x0) + 2y0(y-y0) + z0
        plane = Surface(
            lambda u, v: np.array([
                u,
                v,
                2*x0*(u - x0) + 2*y0*(v - y0) + z0
            ]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(10, 10),
            fill_opacity=0.4,
            checkerboard_colors=[YELLOW_D, YELLOW_E]
        )

        # Animazione camera 3D
        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)

        # Sequenza animata
        self.play(Create(axes))
        self.play(Create(surface))
        self.play(FadeIn(point))
        self.wait(0.5)
        self.play(Create(plane))
        self.wait(2)
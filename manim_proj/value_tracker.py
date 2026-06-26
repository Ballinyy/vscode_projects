from manim import *

class tut4(Scene):
    def construct(self):

        r = ValueTracker(0.5) # traccia il valore del raggio del cerchio

        circle=always_redraw(lambda: 
        Circle(radius=r.get_value(), stroke_color=ORANGE, stroke_width=5)
        ) # always_redraw è simila a add.updater, tuttavia non può essere rimosso in futuro

        line_radius=always_redraw(lambda:
        Line(start=circle.get_center(), end=circle.get_bottom(), stroke_color=BLUE, stroke_width=10)
        )

        line_circumference=always_redraw(lambda:
        Line(stroke_color=ORANGE, stroke_width=5).set_length(2*r.get_value()*PI).next_to(circle, DOWN, buff=0.2)
        ) # r.get_value() tiene conto del valore di r, che poi faremo variare con animate

        triangle=always_redraw(lambda:
        Polygon(circle.get_top(), circle.get_left(), circle.get_right(), fill_color=GREEN)
        )

        self.play(LaggedStart(
            Create(circle), DrawBorderThenFill(line_radius), DrawBorderThenFill(triangle), run_time=4, lag_ratio=0.75
        ))
        self.play(ReplacementTransform(circle.copy(), line_circumference), run_time=2)
        self.play(r.animate.set_value(2), run_time=5) # animazione del cambiamento di r da 0.5 a 2
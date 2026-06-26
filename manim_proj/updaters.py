from manim import *

class Updaters(Scene):
    def construct(self):
        rectangle=RoundedRectangle(stroke_width=6, stroke_color=WHITE, width=4.5, height=2).shift(UP*3+LEFT*4)

        mathtext=MathTex(r"f(x) = \cos x", font_size=50)
        mathtext.move_to(rectangle.get_center())
        mathtext.add_updater(lambda x : x.move_to(rectangle.get_center())) # fissa mathtext al centro del rettangolo in modo tale che lo segua se si sposta, ovvero mathtext è vincolare a stare al centro del rettangolo ovunque quest'ultimo venga spostato.

        self.play(FadeIn(rectangle))
        self.play(FadeIn(mathtext))
        self.play(rectangle.animate.shift(RIGHT*4+DOWN*3), run_time=6)
        self.wait()
        mathtext.clear_updaters() # rimuove il comando updater, dunque mathtext non è più vincolato a stare al centro del rettangolo
        self.play(rectangle.animate.shift(LEFT*4+UP*3), run_time=6)
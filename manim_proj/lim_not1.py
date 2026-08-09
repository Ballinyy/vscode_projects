from manim import *
import numpy as np

class DimostrazioneLimite(Scene):
    def construct(self):
        # -------------------------------------------------------------
        # SCENA 1: Introduzione
        # -------------------------------------------------------------
        title = Tex(r"\textbf{Calcolo del limite notevole}").scale(1.2).set_color(BLUE)
        title.to_edge(UP, buff=1)
        
        formula_main = MathTex(r"\lim_{x \rightarrow 0} \frac{e^x - 1}{x}").scale(1.5)
        
        self.play(Write(title))
        self.play(FadeIn(formula_main, shift=UP))
        self.wait(2)
        
        # Transizione: spostiamo la formula principale in alto a sinistra
        self.play(
            FadeOut(title),
            formula_main.animate.scale(0.8).to_corner(UL)
        )
        self.wait(1)
        
        # -------------------------------------------------------------
        # SCENA 2: Convessità e disuguaglianza fondamentale (Destro)
        # -------------------------------------------------------------
        # Testo a sinistra
        text2 = VGroup(
            Tex(r"La funzione $x \mapsto e^x$ è convessa in $\mathbf{R}$:"),
            MathTex(r"\frac{d^2}{dx^2}(e^x) = e^x > 0 \qquad \forall x \in \mathbf{R}"),
            Tex(r"Dato che $e^0 = 1$ e per la retta tangente:"),
            MathTex(r"\frac{d^2}{dx^2}(x + 1) = 0 \qquad \forall x \in \mathbf{R}"),
            Tex(r"Poiché combaciano solo per $x=0$, si ottiene:"),
            MathTex(r"e^x \geq x + 1 \qquad \forall x \in \mathbf{R}")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.65).next_to(formula_main, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        
        self.play(Write(text2[:2]))
        
        # Assi a destra
        ax1 = Axes(
            x_range=[-1, 2.5, 1],
            y_range=[-1, 5, 1],
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": True, "font_size": 24},
        ).to_edge(RIGHT, buff=0.5)
        
        self.play(Create(ax1))
        
        # Grafico di e^x
        graph_exp = ax1.plot(lambda x: np.exp(x), x_range=[-1, 1.7], color=BLUE)
        label_exp = MathTex(r"e^x", color=BLUE).next_to(ax1.c2p(1.7, np.exp(1.7)), LEFT+UP, buff=0.1)
        
        self.play(Create(graph_exp), Write(label_exp))
        self.wait(1)
        
        self.play(Write(text2[2:4]))
        
        # Grafico di x+1
        graph_tangent = ax1.plot(lambda x: x + 1, x_range=[-1, 2.5], color=YELLOW)
        label_tangent = MathTex(r"x + 1", color=YELLOW).next_to(ax1.c2p(2.2, 3.2), RIGHT+DOWN, buff=0.1)
        
        self.play(Create(graph_tangent), Write(label_tangent))
        self.wait(1)
        
        self.play(Write(text2[4:]))
        
        # Evidenziazione area per mostrare e^x >= x+1
        area_above_tangent = ax1.get_area(graph_exp, [-0.8, 1.5], bounded_graph=graph_tangent, color=BLUE, opacity=0.2)
        self.play(FadeIn(area_above_tangent))
        self.wait(2)
        
        # -------------------------------------------------------------
        # SCENA 3: Intersezione con \lambda x + 1
        # -------------------------------------------------------------
        self.play(FadeOut(text2), FadeOut(area_above_tangent))
        
        text3 = VGroup(
            Tex(r"Inoltre osserviamo che per ogni $\lambda > 1$ esiste un"),
            Tex(r"intervallo $[a_\lambda, b_\lambda] \subset [0, +\infty)$ tale che:"),
            MathTex(r"e^x \leq \lambda x + 1 \qquad \forall x \in [a_\lambda, b_\lambda]"),
            Tex(r"Infatti l'equazione $e^x = \lambda x + 1$"),
            Tex(r"ammette $x=0$ e una seconda soluzione $x_0>0$,"),
            Tex(r"la cui esistenza è garantita dal"),
            Tex(r"\textit{teorema dello zero}.")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).scale(0.65).next_to(formula_main, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        
        self.play(Write(text3[:3]))
        
        # Grafico y = \lambda x + 1 (Scegliamo \lambda = 2 per chiarezza grafica)
        lambda_val = 2.0
        graph_lambda = ax1.plot(lambda x: lambda_val * x + 1, x_range=[-1, 2.1], color=GREEN)
        label_lambda = MathTex(r"\lambda x + 1", color=GREEN).next_to(ax1.c2p(1.9, 1.9*lambda_val+1), LEFT+UP, buff=0.1)
        
        self.play(Create(graph_lambda), Write(label_lambda))
        self.wait(1)
        
        self.play(Write(text3[3:]))
        
        # Intersezione in x_0
        x0 = 1.256 # Approssimazione numerica per e^x = 2x + 1
        dot_x0 = Dot(ax1.c2p(x0, np.exp(x0)), color=RED)
        line_x0 = ax1.get_vertical_line(ax1.c2p(x0, np.exp(x0)), color=RED, line_func=DashedLine)
        label_x0 = MathTex(r"x_0", color=RED).scale(0.8).next_to(ax1.c2p(x0, 0), DOWN, buff=0.1)
        
        self.play(Create(dot_x0), Create(line_x0), Write(label_x0))
        self.wait(1)
        
        # Evidenziazione area per mostrare la stima superiore
        area_lambda = ax1.get_area(graph_lambda, [0, x0], bounded_graph=graph_exp, color=GREEN, opacity=0.3)
        self.play(FadeIn(area_lambda))
        self.wait(2)
        
        # -------------------------------------------------------------
        # SCENA 4: Teorema dei Carabinieri
        # -------------------------------------------------------------
        self.play(
            FadeOut(text3),
            FadeOut(ax1), FadeOut(graph_exp), FadeOut(label_exp), 
            FadeOut(graph_tangent), FadeOut(label_tangent),
            FadeOut(graph_lambda), FadeOut(label_lambda),
            FadeOut(dot_x0), FadeOut(line_x0), FadeOut(label_x0), FadeOut(area_lambda)
        )
        
        text4 = VGroup(
            Tex(r"Riassumendo quanto dedotto, concludiamo che"),
            Tex(r"per ogni $\lambda > 1$ si ha:"),
            MathTex(r"1 = \frac{x + 1 - 1}{x} \leq \frac{e^x - 1}{x} \leq \frac{\lambda x + 1 - 1}{x} = \lambda"),
            MathTex(r"\forall x \in \mathbf{R}_{\geq 0}"),
            Tex(r"Pertanto, per il \textit{teorema dei carabinieri}:"),
            MathTex(r"1 \leq \lim_{x \rightarrow 0^+} \frac{e^x - 1}{x} \leq \lambda"),
            Tex(r"per ogni $\lambda > 1$, ovvero:"),
            MathTex(r"\lim_{x \rightarrow 0^+} \frac{e^x - 1}{x} = 1")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).scale(0.65).next_to(formula_main, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        
        self.play(Write(text4[:4]))
        
        # Nuovi assi per il rapporto f(x) = (e^x - 1)/x
        ax2 = Axes(
            x_range=[0, 1.5, 0.5],
            y_range=[0.5, 2.5, 0.5],
            x_length=6,
            y_length=5,
            axis_config={"include_numbers": True, "font_size": 20},
        ).to_edge(RIGHT, buff=0.5)
        
        self.play(Create(ax2))
        
        # Grafico del rapporto
        graph_ratio = ax2.plot(lambda x: (np.exp(x)-1)/x if x!=0 else 1, x_range=[0.01, 1.5], color=BLUE)
        label_ratio = MathTex(r"\frac{e^x - 1}{x}", color=BLUE).next_to(ax2.c2p(1.3, (np.exp(1.3)-1)/1.3), UP+LEFT, buff=0.1)
        
        # Stime costanti (1 e \lambda)
        graph_lower = ax2.plot(lambda x: 1, x_range=[0, 1.5], color=YELLOW)
        label_lower = MathTex(r"1", color=YELLOW).next_to(ax2.c2p(1.3, 1), DOWN, buff=0.2)
        
        lambda_tracker = ValueTracker(2.0)
        graph_upper = always_redraw(lambda: ax2.plot(lambda x: lambda_tracker.get_value(), x_range=[0, 1.5], color=GREEN))
        label_upper = always_redraw(lambda: MathTex(r"\lambda", color=GREEN).next_to(ax2.c2p(1.3, lambda_tracker.get_value()), UP, buff=0.2))
        
        self.play(Create(graph_ratio), Write(label_ratio))
        self.play(Create(graph_lower), Write(label_lower))
        self.play(Create(graph_upper), Write(label_upper))
        self.wait(1)
        
        self.play(Write(text4[4:6]))
        
        # Animazione del teorema dei carabinieri: \lambda si abbassa schiacciando la curva verso 1
        self.play(lambda_tracker.animate.set_value(1.01), run_time=3.5)
        self.wait(1)
        
        self.play(Write(text4[6:]))
        self.wait(2)
        
        # -------------------------------------------------------------
        # SCENA 5: Limite Sinistro e Conclusione
        # -------------------------------------------------------------
        self.play(
            FadeOut(text4), FadeOut(formula_main),
            FadeOut(ax2), FadeOut(graph_ratio), FadeOut(label_ratio),
            FadeOut(graph_lower), FadeOut(label_lower),
            FadeOut(graph_upper), FadeOut(label_upper)
        )
        
        text5_title = Tex(r"Consideriamo ora il limite sinistro:").scale(1.1).to_edge(UP, buff=1)
        
        # Sequenza perfetta allineata come nel testo
        text5_eq = MathTex(
            r"\begin{aligned}",
            r"\lim_{x \rightarrow 0^-} \frac{e^x - 1}{x} &= \lim_{x \rightarrow 0^+} \frac{e^{-x} - 1}{-x} \\",
            r"&= \lim_{x \rightarrow 0^+} -\frac{e^{-x} - 1}{x} \\",
            r"&= \lim_{x \rightarrow 0^+} \frac{1 - e^{-x}}{x} \\",
            r"&= \lim_{x \rightarrow 0^+} e^{-x}\frac{e^x - 1}{x} = 1",
            r"\end{aligned}"
        ).scale(0.9).next_to(text5_title, DOWN, buff=0.5)
        
        text5_note = MathTex(
            r"\text{infatti } \lim_{x \rightarrow 0^+} \frac{e^x - 1}{x} = 1 \qquad \lim_{x \rightarrow 0^+} e^{-x} = 1"
        ).scale(0.7).next_to(text5_eq, DOWN, buff=0.5)
        
        final_conclusion = MathTex(
            r"\implies \lim_{x \rightarrow 0} \frac{e^x - 1}{x} = 1"
        ).scale(1.5).set_color(YELLOW).next_to(text5_note, DOWN, buff=1)
        
        self.play(Write(text5_title))
        self.wait(0.5)
        self.play(Write(text5_eq))
        self.wait(1)
        self.play(Write(text5_note))
        self.wait(1)
        
        self.play(Write(final_conclusion))
        box = SurroundingRectangle(final_conclusion, color=RED, buff=0.2)
        self.play(Create(box))
        self.wait(4)
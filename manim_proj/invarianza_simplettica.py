from manim import *
import numpy as np

class SymplecticInvariance(Scene):
    def construct(self):
        # 1. Testi e Formule
        title = Text("Invarianza della Forma Simplettica", font_size=36, color=YELLOW).to_edge(UP)
        formula = MathTex(r"\phi_t^* \omega = \omega \implies \text{Area = Costante}", font_size=32).next_to(title, DOWN)
        
        self.play(Write(title), Write(formula))
        
        # 2. Configurazione dello Spazio delle Fasi (q, p)
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={"include_tip": True},
            x_length=10,
            y_length=6
        ).shift(DOWN * 0.5)
        
        axes_labels = axes.get_axis_labels(x_label="q", y_label="p")
        
        self.play(Create(axes), Write(axes_labels))

        # 3. Definizione del Campo Hamiltoniano (Pendolo Matematico)
        # H(q, p) = p^2 / 2 - cos(q)
        # dq/dt = p
        # dp/dt = -sin(q)
        def hamiltonian_flow(pos):
            q, p = pos[0], pos[1]
            dq = p
            dp = -np.sin(q)
            return np.array([dq, dp, 0])

        # Creazione del campo vettoriale in background
        vector_field = ArrowVectorField(
            lambda pos: hamiltonian_flow(axes.point_to_coords(pos)),
            x_range=[-4, 4, 0.5],
            y_range=[-3, 3, 0.5],
            opacity=0.3
        )
        self.play(FadeIn(vector_field))

        # 4. Creazione dell'Insieme Iniziale (La 2-forma integrata)
        num_points = 100
        radius = 0.6
        # Posizioniamo la "goccia" iniziale in una zona dove subirà distorsione
        center_q, center_p = -1.5, 1.0 
        
        # Generazione dei vertici del poligono nelle coordinate di Manim
        points = []
        for angle in np.linspace(0, TAU, num_points, endpoint=False):
            q = center_q + radius * np.cos(angle)
            p = center_p + radius * np.sin(angle)
            points.append(axes.coords_to_point(q, p))
            
        blob = Polygon(*points, color=BLUE, fill_opacity=0.6, stroke_width=2)
        
        self.play(DrawBorderThenFill(blob))

        # 5. Funzione per calcolare l'area del poligono (Formula di Gauss / Shoelace)
        def get_polygon_area(polygon):
            pts = [axes.point_to_coords(pt) for pt in polygon.get_vertices()]
            pts = np.array(pts)
            x = pts[:, 0]
            y = pts[:, 1]
            # Area = 0.5 * |sum(x_i * y_{i+1} - y_i * x_{i+1})|
            area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
            return area

        # Testo dinamico per l'area
        initial_area = get_polygon_area(blob)
        area_text = Text("Area: ", font_size=24).to_corner(DL).shift(UP*0.5)
        area_number = DecimalNumber(initial_area, num_decimal_places=4, font_size=24).next_to(area_text, RIGHT)
        
        self.play(Write(area_text), FadeIn(area_number))

        # 6. Integrazione di Runge-Kutta (RK4) per l'Updater
        def update_blob(mob, dt):
            new_points = []
            for pt in mob.get_vertices():
                # Estraiamo le coordinate fisiche 2D
                c = axes.point_to_coords(pt)
                
                # Convertiamo in array 3D aggiungendo lo 0 per l'asse z
                # Questo previene il ValueError di broadcasting (2,) + (3,)
                coords = np.array([c[0], c[1], 0.0]) 
                
                # RK4 Step
                k1 = hamiltonian_flow(coords)
                k2 = hamiltonian_flow(coords + 0.5 * dt * k1)
                k3 = hamiltonian_flow(coords + 0.5 * dt * k2)
                k4 = hamiltonian_flow(coords + dt * k3)
                
                new_coords = coords + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
                
                # Riconvertiamo nelle coordinate dello schermo (estraendo solo q e p)
                new_points.append(axes.coords_to_point(*new_coords[:2]))
                
            mob.become(Polygon(*new_points, color=BLUE, fill_opacity=0.6, stroke_width=2))
            # Aggiorna il numero dell'area
            area_number.set_value(get_polygon_area(mob))

        # 7. Esecuzione dell'evoluzione temporale
        blob.add_updater(update_blob)
        
        # Facciamo evolvere il sistema per 6 secondi
        self.wait(6)
        
        blob.remove_updater(update_blob)
        
        # Conclusione
        conclusion = Text("La forma si distorce, ma l'area si conserva!", font_size=28, color=GREEN).to_corner(DR).shift(UP*0.5)
        self.play(Write(conclusion))
        self.wait(2)
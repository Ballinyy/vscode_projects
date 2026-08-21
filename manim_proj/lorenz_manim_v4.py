from manim import *
import numpy as np

class LorenzAttractor(ThreeDScene):
    def construct(self):
        # 1. Configurazione iniziale della scena 3D
        # Impostiamo l'orientamento della telecamera per una vista prospettica ottimale
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # 2. Parametri del sistema di Lorenz (da oscillatore_lorentz.md)
        sigma = 10.0
        rho = 28.0
        beta = 8.0 / 3.0
        
        # Fattore di scala e offset per centrare l'attrattore nella finestra di Manim
        # L'attrattore di Lorenz si sviluppa principalmente in:
        # X in [-20, 20], Y in [-30, 30], Z in [0, 50]
        scale_factor = 0.12
        z_offset = 25.0  # Spostiamo il centro in Z per bilanciare l'oscillazione nello schermo
        
        # Definizione delle equazioni differenziali di Lorenz
        def lorenz_deriv(state):
            x, y, z = state
            dx = sigma * (y - x)
            dy = x * (rho - z) - y
            dz = x * y - beta * z
            return np.array([dx, dy, dz])
            
        # Metodo di integrazione numerica Runge-Kutta del 4° ordine (RK4)
        def rk4_step(state, h):
            k1 = lorenz_deriv(state)
            k2 = lorenz_deriv(state + 0.5 * h * k1)
            k3 = lorenz_deriv(state + 0.5 * h * k2)
            k4 = lorenz_deriv(state + h * k3)
            return state + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            
        # Condizioni iniziali delle due traiettorie (da oscillatore_lorentz.md)
        # Mostrano l'effetto farfalla (sensibilità alle condizioni iniziali)
        init_state1 = np.array([-8.0, 8.0, 27.0])
        init_state2 = np.array([-8.001, 8.0, 27.0])
        
        # Funzione helper per mappare le coordinate di Lorenz allo spazio Manim
        def to_manim_coords(state):
            return np.array([
                state[0],
                state[1],
                state[2] - z_offset
            ]) * scale_factor

        # 3. Creazione degli oggetti grafici (Mobjects)
        # Assi cartesiani 3D per dare profondità alla scena
        axes = ThreeDAxes(
            x_range=[-25, 25, 10],
            y_range=[-25, 25, 10],
            z_range=[0, 50, 10],
            x_length=50 * scale_factor,
            y_length=50 * scale_factor,
            z_length=50 * scale_factor,
        )
        # Centriamo l'asse Z traslandolo verso il basso nello spazio Manim
        axes.move_to(np.array([0, 0, -z_offset * scale_factor]))
        
        # Etichette degli assi
        labels = axes.get_axis_labels(
            Tex("x").scale(0.7), Tex("y").scale(0.7), Tex("z").scale(0.7)
        )
        
        # Punti tridimensionali (Dot3D) che si muoveranno nello spazio
        dot1 = Dot3D(point=to_manim_coords(init_state1), color=BLUE, radius=0.06)
        dot2 = Dot3D(point=to_manim_coords(init_state2), color=RED, radius=0.06)
        
        # Tracciati che disegnano la linea percorsa dai punti
        path1 = TracedPath(dot1.get_center, stroke_color=BLUE, stroke_width=2.5, stroke_opacity=0.8)
        path2 = TracedPath(dot2.get_center, stroke_color=RED, stroke_width=2.5, stroke_opacity=0.8)
        
        # Aggiungiamo elementi 2D fissi sullo schermo (Titolo e Legenda)
        title = Text("Attrattore di Lorenz (Effetto Farfalla)", font_size=32, color=WHITE)
        title.to_edge(UP, buff=0.4)
        
        legenda = VGroup(
            Text("Traiettoria 1 (x0 = -8.000)", font_size=18, color=BLUE),
            Text("Traiettoria 2 (x0 = -8.001)", font_size=18, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        legenda.to_edge(DOWN).to_edge(LEFT, buff=0.5)
        
        # Mettiamo questi elementi grafici 2D "fissi" rispetto alla camera rotante
        self.add_fixed_in_frame_mobjects(title, legenda)
        
        # Aggiungiamo gli assi alla scena 3D
        self.add(axes, labels)
        
        # Animazione di comparsa degli elementi principali
        self.play(
            Create(axes),
            Write(labels),
            FadeIn(dot1),
            FadeIn(dot2),
            run_time=2
        )
        
        # Aggiungiamo i tracciati alla scena
        self.add(path1, path2)
        
        # 4. Definizione degli Updater per simulare l'evoluzione in tempo reale
        # Teniamo traccia dello stato interno con un dizionario mutabile per ciascuna traiettoria
        tracker_state1 = {"current": init_state1.copy()}
        tracker_state2 = {"current": init_state2.copy()}
        
        # Velocità della simulazione (passo d'integrazione ad ogni frame)
        dt_step = 0.008
        steps_per_frame = 4  # Suddividiamo ogni frame in micro-passi per stabilità con RK4
        
        # Utilizziamo *args per accogliere in modo robusto qualunque parametro passi Manim (mobject o mobject + dt)
        def update_dot1(mob, *args):
            for _ in range(steps_per_frame):
                tracker_state1["current"] = rk4_step(tracker_state1["current"], dt_step)
            mob.move_to(to_manim_coords(tracker_state1["current"]))
            
        def update_dot2(mob, *args):
            for _ in range(steps_per_frame):
                tracker_state2["current"] = rk4_step(tracker_state2["current"], dt_step)
            mob.move_to(to_manim_coords(tracker_state2["current"]))
            
        # Colleghiamo le funzioni di aggiornamento ai rispettivi punti
        dot1.add_updater(update_dot1)
        dot2.add_updater(update_dot2)
        
        # 5. Esecuzione dell'animazione con movimento di telecamera
        # Avviamo una rotazione automatica e lenta della telecamera (0.05 radianti al secondo)
        self.begin_ambient_camera_rotation(rate=0.05)
        
        # Facciamo scorrere il tempo di animazione (25 secondi totali)
        # Durante questo tempo, le traiettorie si svilupperanno mostrando la divergenza caotica
        self.wait(25)
        
        # Fermiamo la rotazione e l'aggiornamento alla fine
        self.stop_ambient_camera_rotation()
        dot1.clear_updaters()
        dot2.clear_updaters()
        self.wait(2)

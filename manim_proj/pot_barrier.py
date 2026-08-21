"""
Effetto tunnel attraverso una barriera di potenziale finita -- animazione 3D
=============================================================================

Un'unica scena 3D (ThreeDScene) che mostra, nello stesso spazio R^3:
  1. la particella fisica che arriva da (-inf, 0, 0) e urta la barriera
     (superficie ortogonale all'asse x) posta in x=0;
  2. nell'istante dell'urto, la sua natura ondulatoria: la funzione
     d'onda psi(x,t) e' costruita davvero come pacchetto d'onda
     (sovrapposizione di Fourier di autostati di scattering, ottenuti
     risolvendo le condizioni di continuita' di psi e psi' in x=0,L --
     vedi le note di teoria) e viene disegnata come un "tubo" attorno
     all'asse x, di raggio |psi(x,t)|: oscilla prima della barriera,
     si assottiglia esponenzialmente dentro la barriera, e ricompare
     (piu' debole) dopo -- l'effetto tunnel;
  3. l'esito finale, con la particella che riappare come trasmessa o
     riflessa con probabilita' T e R.

Camera fissa in (theta, phi) = (3/2 pi, pi/2), come richiesto: e' una
vista "di lato" lungo l'asse y, con x orizzontale e z verticale.

Render (qualita' bassa, veloce, per controllare il risultato):
    manim -pql tunneling_barrier.py Tunneling3D
Per l'alta qualita' sostituire -pql con -pqh.

Richiede: manim (Community Edition) e numpy.
"""

import numpy as np
from manim import *

# ======================================================================
# 1. FISICA -- parametri, autostati di scattering, pacchetto d'onda
# ======================================================================

HBAR = 1.0
M = 1.0

PHI0 = 2.5      # altezza della barriera
L_BAR = 0.8     # larghezza della barriera
K0 = 1.5        # numero d'onda centrale del pacchetto incidente
SIGMA_K = 0.35  # larghezza in k del pacchetto (spread di Fourier)
X0 = -6.0       # centro iniziale del pacchetto
X_MIN, X_MAX = -8.0, 8.0

def energy(k):
    """Relazione di dispersione E(k) = hbar^2 k^2 / 2m."""
    return HBAR**2 * k**2 / (2 * M)

E0 = energy(K0)
assert E0 < PHI0, "Il pacchetto deve avere energia media minore di phi0 (regime tunnel)."

def kappa(k):
    """Numero d'onda 'interno' alla barriera, in generale complesso:
    reale -> decadimento esponenziale (E<phi0, effetto tunnel);
    immaginario puro -> oscillazione (E>phi0, sopra la barriera).
    Un'unica formula complessa evita di distinguere i due regimi."""
    return np.sqrt(2 * M * (PHI0 - energy(k)) + 0j) / HBAR

def scattering_coeffs(k):
    """Risolve il sistema lineare 4x4 dato dalla continuita' di psi e
    psi' in x=0 e x=L (vedi note), con onda incidente di ampiezza
    unitaria da sinistra (A1=1) e nessuna onda entrante da destra
    (B3=0). Ritorna (A1,B1,A2,B2,A3)."""
    kp = kappa(k)
    A1 = 1.0 + 0j
    sys_matrix = np.array([
        [1, -1, -1, 0],
        [-1j * k, -kp, kp, 0],
        [0, np.exp(kp * L_BAR), np.exp(-kp * L_BAR), -np.exp(1j * k * L_BAR)],
        [0, kp * np.exp(kp * L_BAR), -kp * np.exp(-kp * L_BAR), -1j * k * np.exp(1j * k * L_BAR)],
    ], dtype=complex)
    rhs = np.array([-A1, -1j * k * A1, 0, 0], dtype=complex)
    B1, A2, B2, A3 = np.linalg.solve(sys_matrix, rhs)
    return A1, B1, A2, B2, A3

# Coefficienti di trasmissione/riflessione in probabilita' (dalla
# corrente j = -hbar/m Im(psi* psi')), valutati sul k centrale del
# pacchetto: T = |A3/A1|^2, R = |B1/A1|^2, con T+R=1 (verificato
# numericamente).
_, _B1_0, _, _, _A3_0 = scattering_coeffs(K0)
T_COEFF = float(abs(_A3_0) ** 2)
R_COEFF = float(abs(_B1_0) ** 2)

N_K = 35
_k_grid = np.linspace(K0 - 4 * SIGMA_K, K0 + 4 * SIGMA_K, N_K)
K_VALS = _k_grid[_k_grid > 0.05]
DK = K_VALS[1] - K_VALS[0]
WEIGHTS = np.exp(-(K_VALS - K0) ** 2 / (2 * SIGMA_K ** 2))
COEFFS_LIST = [scattering_coeffs(k) for k in K_VALS]

def _psi_region_vec(x, k, coeffs):
    """Valuta l'autostato di scattering per un dato k su un array x."""
    A1, B1, A2, B2, A3 = coeffs
    kp = kappa(k)
    out = np.zeros_like(x, dtype=complex)
    left = x < 0
    mid = (x >= 0) & (x <= L_BAR)
    right = x > L_BAR
    out[left] = A1 * np.exp(1j * k * x[left]) + B1 * np.exp(-1j * k * x[left])
    out[mid] = A2 * np.exp(kp * x[mid]) + B2 * np.exp(-kp * x[mid])
    out[right] = A3 * np.exp(1j * k * x[right])
    return out

def psi_of_x_t(x_array, t):
    """psi(x,t) = somma_k w(k) e^{-ikX0} phi_k(x) e^{-iE(k)t/hbar} dk
    (il fattore e^{-ikX0} centra il pacchetto in X0 al tempo t=0)."""
    psi = np.zeros_like(x_array, dtype=complex)
    for k, w, coeffs in zip(K_VALS, WEIGHTS, COEFFS_LIST):
        time_phase = np.exp(-1j * energy(k) * t / HBAR)
        space_phase = np.exp(-1j * k * X0)
        psi += w * space_phase * time_phase * _psi_region_vec(x_array, k, coeffs)
    return psi * DK

_x_probe = np.linspace(X_MIN, X_MAX, 400)
_PEAK0 = np.max(np.abs(psi_of_x_t(_x_probe, 0.0)))
RADIUS_SCALE = 0.7 / _PEAK0          # scala grafica del raggio del "tubo"
RADIUS_CAP = 1.3                     # raggio massimo (resta dentro la barriera)

V_GROUP = HBAR * K0 / M
T_PEAK = (0.0 - X0) / V_GROUP        # istante in cui il picco arriva in x=0
T_START_WAVE = max(0.0, T_PEAK - 2.0)
T_MAX = (X_MAX - X0) / V_GROUP + 1.0


# ======================================================================
# 2. SCENA 3D UNICA
# ======================================================================

class Tunneling3D(ThreeDScene):
    def construct(self):
        # camera richiesta: (theta, phi) = (3/2 pi, pi/2) -- vista di
        # lato lungo l'asse y, x orizzontale, z verticale
        self.set_camera_orientation(phi=PI / 2, theta=3 * PI / 2)

        # ---- HUD (testo sempre fisso rispetto allo schermo) ----
        title = Tex("Urto con una barriera di potenziale: particella e onda", font_size=28)
        title.to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        caption = Tex("La particella si avvicina alla barriera", font_size=24)
        caption.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(caption)
        self.play(FadeIn(caption))

        # ---- ambientazione 3D: asse x e barriera ----
        x_axis = Line([X_MIN - 0.5, 0, 0], [X_MAX + 0.5, 0, 0], color=GRAY_C, stroke_width=2)
        ticks = VGroup(*[
            Line([x, -0.08, 0], [x, 0.08, 0], color=GRAY_C, stroke_width=2)
            for x in range(int(X_MIN), int(X_MAX) + 1, 2)
        ])

        barrier = Cube(
            side_length=1.0, fill_color=YELLOW, fill_opacity=0.28,
            stroke_color=YELLOW_E, stroke_width=1,
        )
        barrier.stretch(L_BAR, dim=0)
        barrier.stretch(3.2, dim=1)
        barrier.stretch(3.2, dim=2)
        barrier.move_to([L_BAR / 2, 0, 0])

        self.play(Create(x_axis), FadeIn(ticks))
        self.play(FadeIn(barrier))

        # ---- fase 1: la particella (immagine classica) ----
        particle = Sphere(radius=0.18, resolution=(14, 14))
        particle.set_color(BLUE)
        particle.move_to([X_MIN, 0, 0])
        self.play(FadeIn(particle))
        self.play(
            particle.animate.move_to([0, 0, 0]),
            run_time=(0 - X_MIN) / V_GROUP,
            rate_func=linear,
        )

        # ---- fase 2: urto -> natura ondulatoria ----
        new_caption = Tex("Urto: emerge la natura ondulatoria (possibile effetto tunnel)", font_size=24)
        new_caption.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(new_caption)

        t_tracker = ValueTracker(T_START_WAVE)
        N_TUBE_X = 60

        def radius_profile(t):
            xs = np.linspace(X_MIN, X_MAX, N_TUBE_X)
            r = np.abs(psi_of_x_t(xs, t)) * RADIUS_SCALE
            return xs, np.clip(r, 0, RADIUS_CAP)

        def make_tube():
            xs, r = radius_profile(t_tracker.get_value())
            def param_func(u, v):
                radius = np.interp(u, xs, r)
                return np.array([u, radius * np.cos(v), radius * np.sin(v)])
            surf = Surface(
                param_func, u_range=[X_MIN, X_MAX], v_range=[0, TAU],
                resolution=(48, 20),
            )
            surf.set_fill_by_checkerboard(BLUE_D, BLUE_E, opacity=0.4)
            surf.set_stroke(width=0)
            return surf

        def make_phase_curve():
            xs = np.linspace(X_MIN, X_MAX, 240)
            psi_vals = psi_of_x_t(xs, t_tracker.get_value())
            r = np.clip(np.abs(psi_vals) * RADIUS_SCALE, 0, RADIUS_CAP)
            phase = np.angle(psi_vals)
            pts = [np.array([x, ri * np.cos(p), ri * np.sin(p)])
                   for x, ri, p in zip(xs, r, phase)]
            curve = VMobject(color=WHITE, stroke_width=2, stroke_opacity=0.85)
            curve.set_points_smoothly(pts)
            return curve

        tube = always_redraw(make_tube)
        phase_curve = always_redraw(make_phase_curve)

        self.play(
            FadeOut(particle), FadeOut(caption), FadeIn(new_caption),
            FadeIn(tube), FadeIn(phase_curve),
            run_time=0.8,
        )
        self.add(tube, phase_curve)

        self.play(t_tracker.animate.set_value(T_MAX), run_time=13, rate_func=linear)

        # ---- fase 3: esito -- riflessione o trasmissione ----
        final_caption = Tex("Esito: riflessione o trasmissione, con probabilità R e T", font_size=24)
        final_caption.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(final_caption)

        self.play(FadeOut(tube), FadeOut(phase_curve), FadeOut(new_caption), FadeIn(final_caption))

        transmitted = Sphere(radius=0.16, resolution=(14, 14)).set_color(GREEN)
        transmitted.set_opacity(T_COEFF ** 0.5 + 0.15)
        transmitted.move_to([L_BAR, 0, 0])
        reflected = Sphere(radius=0.16, resolution=(14, 14)).set_color(RED)
        reflected.set_opacity(R_COEFF ** 0.5 + 0.15)
        reflected.move_to([0, 0, 0])
        self.play(FadeIn(transmitted), FadeIn(reflected))
        self.play(
            transmitted.animate.move_to([X_MAX, 0, 0]),
            reflected.animate.move_to([X_MIN, 0, 0]),
            run_time=4.5, rate_func=linear,
        )

        self.wait(2)
"""
Teorema di Cauchy-Goursat -- animazione Manim
======================================================================

Struttura:
1. Titolo + enunciato in termini matematici.
2. Curva gamma e ricoprimento con celle adattate al bordo.
3. I quadrati si rimpiccioliscono, epsilon -> 0.
3bis. Zoom su due celle verdi adiacenti: i lati interni si cancellano.
4. Maggiorazione della funzione e conclusione del teorema.

Correzioni in questa versione:
- Le celle di bordo NON sono più costruite raccogliendo punti e
  ordinandoli per angolo polare (metodo che poteva produrre poligoni
  storti/auto-intersecanti quando la curva attraversava la cella in
  modo non convesso). Ora si usa un vero algoritmo di clipping
  poligonale (Sutherland-Hodgman) che calcola l'intersezione ESATTA
  tra ogni quadrato della griglia e l'interno di gamma. Questo elimina
  sia i poligoni storti sia le celle di bordo mancanti.
- Le celle interamente interne a gamma vengono riconosciute con un
  test veloce sulla distanza dall'origine (curva "stellata" rispetto
  all'origine) ed usano il quadrato esatto, senza passare dal clipping,
  così restano quadrati perfetti e il rendering è più rapido.
- Corretto un bug (variabile `limit_lable` non definita, ora
  `self.eps_label`) che avrebbe causato un crash nella scena 3bis.
"""

from manim import *
import numpy as np

# --------------------------------------------------------------------------
# Colori
# --------------------------------------------------------------------------
COL_CURVE = YELLOW
COL_IN = GREEN
COL_EDGE = "#FF8C00"        # arancione acceso
COL_TEXT = WHITE
COL_ACCENT = "#4FC3F7"      # azzurro chiaro
COL_RESULT = "#00E676"      # verde acceso per il risultato finale


# --------------------------------------------------------------------------
# Geometria della curva chiusa semplice gamma
# --------------------------------------------------------------------------

def curve_point(t):
    r = 2.1 + 0.35 * np.cos(3 * t) + 0.15 * np.sin(2 * t)
    return np.array([r * np.cos(t), r * np.sin(t), 0.0])


N_POLY_SAMPLES = 400
_ts = np.linspace(0, TAU, N_POLY_SAMPLES, endpoint=False)
POLY_VERTICES = [tuple(curve_point(t)[:2]) for t in _ts]

# Raggi minimo e massimo di gamma rispetto all'origine: la curva e'
# "stellata" rispetto all'origine (r(theta) > 0 sempre), quindi ogni
# punto piu' vicino di _R_MIN e' garantito interno, e ogni punto piu'
# lontano di _R_MAX e' garantito esterno.
_ALL_R = [np.hypot(x, y) for x, y in POLY_VERTICES]
_R_MIN = min(_ALL_R)
_R_MAX = max(_ALL_R)


def polygon_area(pts):
    """Area di un poligono semplice (formula di Gauss/shoelace)."""
    n = len(pts)
    if n < 3:
        return 0.0
    total = 0.0
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        total += x1 * y2 - x2 * y1
    return abs(total) / 2.0


def clip_polygon_to_rect(subject, xmin, xmax, ymin, ymax):
    """
    Algoritmo di Sutherland-Hodgman: restituisce l'intersezione ESATTA
    tra il poligono `subject` (la curva gamma, chiusa) e il rettangolo
    [xmin,xmax] x [ymin,ymax]. Il rettangolo, essendo convesso, rende
    l'algoritmo esatto anche se `subject` non e' convesso.
    """
    clip_verts = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]

    def is_inside(p, a, b):
        return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]) >= -1e-12

    def intersect(s, e, a, b):
        x1, y1 = s
        x2, y2 = e
        x3, y3 = a
        x4, y4 = b
        d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if abs(d) < 1e-15:
            return e
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))

    output = list(subject)
    cp1 = clip_verts[-1]
    for cp2 in clip_verts:
        input_list = output
        output = []
        if not input_list:
            break
        s = input_list[-1]
        for e in input_list:
            e_in = is_inside(e, cp1, cp2)
            s_in = is_inside(s, cp1, cp2)
            if e_in:
                if not s_in:
                    output.append(intersect(s, e, cp1, cp2))
                output.append(e)
            elif s_in:
                output.append(intersect(s, e, cp1, cp2))
            s = e
        cp1 = cp2
    return output


def fit_width(mobj, max_w=5.6):
    """Evita che le formule LaTeX escano dallo schermo."""
    if mobj.width > max_w:
        mobj.scale_to_fit_width(max_w)
    return mobj


# --------------------------------------------------------------------------
# Scena principale
# --------------------------------------------------------------------------

class CauchyGoursat(MovingCameraScene):

    def construct(self):
        self.title_and_statement()
        self.curve_and_covering()
        self.shrinking_squares()
        self.zoom_on_cancellation()
        self.bound_and_conclusion()

    # ------------------------------------------------------------
    # 1. Titolo + enunciato matematico
    # ------------------------------------------------------------
    def title_and_statement(self):
        title = Text("Teorema di Cauchy-Goursat", font_size=48,
                      weight=BOLD, color=COL_TEXT)
        title.to_edge(UP, buff=1.0)

        hyp = Tex(
            r"Siano $f$ olomorfa su $\Omega \subset \mathbb{C}$ semplicemente connesso e \\"
            r"$\gamma$ una curva chiusa semplice con supporto in $\Omega$",
            font_size=32, color=COL_TEXT,
        )
        arrow = MathTex(r"\Downarrow", font_size=34, color=COL_TEXT)
        concl = MathTex(
            r"\oint_{\gamma} f(z)\, dz = 0",
            font_size=52, color=COL_RESULT,
        )

        for m in (hyp, arrow, concl):
            fit_width(m, 11.5)

        stack = VGroup(hyp, arrow, concl).arrange(DOWN, buff=0.5)
        stack.next_to(title, DOWN, buff=1.0)

        self.play(Write(title))
        self.wait(0.4)
        self.play(FadeIn(hyp, shift=UP * 0.2))
        self.play(Write(arrow))
        self.play(Write(concl))
        self.wait(3)

        self.play(FadeOut(VGroup(title, hyp, arrow, concl)))
        self.wait(0.3)

    # ------------------------------------------------------------
    # helper: costruisce la griglia di celle adattate al bordo
    # ------------------------------------------------------------
    def build_grid(self, axes, step):
        """
        Restituisce un VGroup di celle (poligoni) e una lista di tuple
        (centro_x, centro_y, step) per ogni cella.

        Ogni cella e' l'intersezione ESATTA tra il quadrato della
        griglia e l'interno di gamma (via clipping poligonale), quindi
        le celle di bordo seguono fedelmente il contorno della curva
        senza risultare storte o essere saltate per errore.
        """
        grid = VGroup()
        cell_info = []  # (cx, cy, step) per ogni cella
        xmin, xmax, ymin, ymax = -3.0, 3.0, -3.0, 3.0
        nx = int(np.ceil((xmax - xmin) / step))
        ny = int(np.ceil((ymax - ymin) / step))

        for i in range(nx):
            for j in range(ny):
                cx = xmin + (i + 0.5) * step
                cy = ymin + (j + 0.5) * step
                half = step / 2
                sx_min, sx_max = cx - half, cx + half
                sy_min, sy_max = cy - half, cy + half

                # Test veloce basato sulla distanza dall'origine
                # (gamma e' stellata rispetto all'origine).
                corners = [
                    (sx_min, sy_min), (sx_max, sy_min),
                    (sx_max, sy_max), (sx_min, sy_max),
                ]
                corner_r = [np.hypot(vx, vy) for vx, vy in corners]

                if max(corner_r) < _R_MIN:
                    # Cella interamente interna: quadrato esatto, niente clipping.
                    pts = corners
                    is_internal = True
                elif min(corner_r) > _R_MAX:
                    # Cella interamente esterna: nessun contributo.
                    continue
                else:
                    # Cella potenzialmente di bordo: intersezione esatta.
                    pts = clip_polygon_to_rect(POLY_VERTICES, sx_min, sx_max, sy_min, sy_max)
                    if len(pts) < 3:
                        continue  # nessuna intersezione reale (cella esterna)
                    area = polygon_area(pts)
                    full_area = step * step
                    is_internal = area >= 0.999 * full_area

                color = COL_IN if is_internal else COL_EDGE

                scene_pts = [axes.c2p(x, y) for x, y in pts]
                poly = Polygon(*scene_pts, color=color, fill_color=color,
                               fill_opacity=0.35, stroke_width=1.5)
                grid.add(poly)
                cell_info.append((cx, cy, step))

        return grid, cell_info

    # ------------------------------------------------------------
    # helper: trova due celle verdi adiacenti
    # ------------------------------------------------------------
    def find_green_adjacent_pair(self, grid, cell_info, axes):
        """
        Cerca due celle verdi (COL_IN) che siano adiacenti (distanza tra centri ~ step).
        Restituisce i due oggetti VMobject o None.
        """
        if len(grid) < 2:
            return None
        # Raccogli le celle verdi con le loro coordinate
        green_cells = []
        for idx, (cx, cy, step) in enumerate(cell_info):
            obj = grid[idx]
            if obj.fill_color == COL_IN:
                green_cells.append((obj, cx, cy, step))
        if len(green_cells) < 2:
            return None
        # Cerca la coppia più vicina al centro
        best_pair = None
        best_dist_to_origin = None
        for i in range(len(green_cells)):
            for j in range(i + 1, len(green_cells)):
                obj1, cx1, cy1, step1 = green_cells[i]
                obj2, cx2, cy2, step2 = green_cells[j]
                # La distanza tra i centri deve essere circa step (o step medio)
                d = np.hypot(cx1 - cx2, cy1 - cy2)
                if np.isclose(d, (step1 + step2) / 2, atol=0.1 * (step1 + step2) / 2):
                    mid_x = (cx1 + cx2) / 2
                    mid_y = (cy1 + cy2) / 2
                    dist_o = np.hypot(mid_x, mid_y)
                    if best_pair is None or dist_o < best_dist_to_origin:
                        best_pair = (obj1, obj2)
                        best_dist_to_origin = dist_o
        return best_pair

    # ------------------------------------------------------------
    # 2. Curva gamma + ricoprimento con celle adattate
    # ------------------------------------------------------------
    def curve_and_covering(self):
        axes = Axes(
            x_range=[-3.2, 3.2, 1], y_range=[-3.2, 3.2, 1],
            x_length=6.6, y_length=6.6,
            axis_config={"color": GRAY_C, "stroke_width": 1.5},
            tips=False,
        )
        axes.to_edge(LEFT, buff=0.8)

        curve = ParametricFunction(
            lambda t: axes.c2p(*curve_point(t)[:2]),
            t_range=[0, TAU], color=COL_CURVE, stroke_width=4,
        )

        # legenda a destra
        gamma_item = VGroup(
            Line(ORIGIN, RIGHT * 0.5, color=COL_CURVE, stroke_width=4),
            MathTex(r"\gamma", font_size=30, color=COL_TEXT),
        ).arrange(RIGHT, buff=0.25)
        in_item = VGroup(
            Square(side_length=0.35, color=COL_IN, fill_color=COL_IN, fill_opacity=0.35),
            Text("cella interna", font_size=26, color=COL_TEXT),
        ).arrange(RIGHT, buff=0.25)
        edge_item = VGroup(
            Square(side_length=0.35, color=COL_EDGE, fill_color=COL_EDGE, fill_opacity=0.35),
            Text("cella di bordo", font_size=26, color=COL_TEXT),
        ).arrange(RIGHT, buff=0.25)

        legend = VGroup(gamma_item, in_item, edge_item)
        legend.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        legend.to_edge(RIGHT, buff=0.8)

        self.play(FadeIn(axes))
        self.play(Create(curve), run_time=2)
        self.play(FadeIn(legend, shift=LEFT * 0.2))
        self.wait(0.5)

        grid, cell_info = self.build_grid(axes, 0.6)
        self.grid_objects = grid
        self.cell_info = cell_info
        self.play(LaggedStartMap(FadeIn, grid, lag_ratio=0.03), run_time=2)
        self.wait(1.5)

        self.axes = axes
        self.curve = curve
        self.legend = legend

    # ------------------------------------------------------------
    # 3. I quadrati si rimpiccioliscono: epsilon -> 0
    # ------------------------------------------------------------
    def shrinking_squares(self):
        heading1 = Text("Ricoprimento con celle quadrate", font_size=30,
                        weight=BOLD, color=COL_TEXT)
        heading1.to_edge(UP, buff=0.8).shift(RIGHT * 3)

        sub1 = Tex(
            r"La regione racchiusa dalla curva $\gamma$, compresa $\gamma$ stessa, è compatta, \\"
            r"pertanto possiamo ricoprirla con un numero finito di celle quadrate di lato $\varepsilon > 0$",
            font_size=24, color=COL_TEXT
        )
        eps_label = MathTex(r"\varepsilon = 0.6", font_size=36, color=COL_ACCENT)
        eps_label.next_to(self.legend, DOWN, buff=0.8)

        self.play(FadeIn(eps_label))
        self.wait(0.5)

        fit_width(sub1, 11.5)
        sub1.next_to(heading1, DOWN, buff=0.5)

        self.play(FadeIn(heading1, shift=DOWN * 0.2))
        self.play(FadeIn(sub1, shift=UP * 0.2))
        self.wait(1)


        steps = [0.4, 0.25, 0.15, 0.08]
        current_grid = self.grid_objects
        current_info = self.cell_info
        for s in steps:
            new_grid, new_info = self.build_grid(self.axes, s)
            new_label = MathTex(rf"\varepsilon = {s}", font_size=36, color=COL_ACCENT)
            new_label.move_to(eps_label)
            self.play(
                FadeOut(current_grid), FadeIn(new_grid),
                Transform(eps_label, new_label),
                run_time=1.3,
            )
            current_grid = new_grid
            current_info = new_info
            self.wait(0.3)

        limit_label = MathTex(r"\varepsilon \to 0", font_size=36, color=COL_ACCENT)
        limit_label.move_to(eps_label)
        self.play(Transform(eps_label, limit_label))
        self.wait(1.5)
        self.play(FadeOut(heading1), FadeOut(sub1))

        self.grid_objects = current_grid
        self.cell_info = current_info
        self.eps_label = eps_label

    # ------------------------------------------------------------
    # 3bis. Zoom su due celle verdi adiacenti: cancellazione dei lati interni
    # ------------------------------------------------------------
    def zoom_on_cancellation(self):
        heading2 = Text("Cancellazione dei contributi interni", font_size=30,
                        weight=BOLD, color=COL_TEXT)
        heading2.to_edge(UP, buff=0.8).shift(RIGHT * 3)

        sub2 = Tex(
            r"Il contributo dovuto all'integrazione di $f$ sui lati interni delle celle si \\"
            r"cancella, infatti vengono percorsi due volte, ma in senso opposto.",
            font_size=24, color=COL_TEXT
        )
        fit_width(sub2, 11.5)
        sub2.next_to(heading2, DOWN, buff=0.5)

        # Cerca una coppia di celle verdi adiacenti
        pair = self.find_green_adjacent_pair(self.grid_objects, self.cell_info, self.axes)
        if pair is None:
            return
        sq_a, sq_b = pair

        # Usiamo .submobjects per ottenere l'indice
        idx_a = self.grid_objects.submobjects.index(sq_a)
        idx_b = self.grid_objects.submobjects.index(sq_b)
        cx_a, cy_a, step_a = self.cell_info[idx_a]
        cx_b, cy_b, step_b = self.cell_info[idx_b]

        # Centro medio
        mid_x = (cx_a + cx_b) / 2
        mid_y = (cy_a + cy_b) / 2
        mid = self.axes.c2p(mid_x, mid_y)
        # Direzione e perpendicolare
        dir_vec = np.array([cx_b - cx_a, cy_b - cy_a, 0])
        dir_vec = dir_vec / np.linalg.norm(dir_vec)
        perp = np.array([-dir_vec[1], dir_vec[0], 0])
        # Lunghezza del lato (approssimativa)
        side = (step_a + step_b) / 2
        # Offset per le frecce
        offset = dir_vec * side * 0.09
        half_len = side * 0.32

        # Frecce sui lati interni (opposte)
        arrow_a = Arrow(
            mid - perp * half_len - offset, mid + perp * half_len - offset,
            buff=0, color="#FF5252", stroke_width=3,
            max_tip_length_to_length_ratio=0.35,
        )
        arrow_b = Arrow(
            mid + perp * half_len + offset, mid - perp * half_len + offset,
            buff=0, color="#40C4FF", stroke_width=3,
            max_tip_length_to_length_ratio=0.35,
        )

        # Zoom sulla coppia
        self.play(FadeIn(heading2, shift=DOWN * 0.2))
        self.play(FadeIn(sub2, shift=UP * 0.2))
        self.wait(7)
        self.play(FadeOut(heading2), FadeOut(sub2))

        self.camera.frame.save_state()
        self.play(
            self.camera.frame.animate.set(width=side * 7).move_to(mid),
            run_time=2,
        )
        self.wait(0.3)
        self.play(GrowArrow(arrow_a), GrowArrow(arrow_b))
        self.wait(1.2)

        self.play(FadeOut(arrow_a), FadeOut(arrow_b))
        self.wait(0.3)

        # Torna alla vista d'insieme
        self.play(Restore(self.camera.frame), run_time=2)
        self.wait(0.2)
        self.play(FadeOut(self.legend))
        self.play(FadeOut(self.eps_label))

        conclusion_line = Tex(
            r"Sommando su tutte le celle resta solo il contributo lungo $\gamma$",
            font_size=24, color=COL_TEXT,
        )
        equat = MathTex(
            r"\sum_j\int_{\gamma_j} f(z) \, dz = \int_\gamma f(z) \, dz",
            font_size=28, color=COL_ACCENT,
        )
        fit_width(conclusion_line, 11.5)
        conclusion_line.to_edge(UP, buff=1.8).shift(RIGHT * 3)
        equat.next_to(conclusion_line, DOWN, buff=0.8)

        self.play(FadeIn(conclusion_line, shift=DOWN * 0.2))
        self.wait(0.5)
        self.play(FadeIn(equat, shift=UP * 0.2))
        self.wait(5)
        self.play(FadeOut(conclusion_line))
        self.play(FadeOut(equat))
        self.wait(0.3)

    # ------------------------------------------------------------
    # 4. Maggiorazione e conclusione
    # ------------------------------------------------------------
    def bound_and_conclusion(self):
        # Rimpicciolisci il disegno a sinistra
        picture = VGroup(self.axes, self.curve, self.grid_objects)
        self.play(
            picture.animate.scale(0.85).to_edge(LEFT, buff=0.4),
        )

        # Quadrato finito di lato D che contiene interamente gamma
        # (usiamo lo stesso range -3..3 con cui e' stata costruita la
        # griglia in build_grid, che copre sempre l'intera curva).
        d_corners = [
            self.axes.c2p(-3, -3), self.axes.c2p(3, -3),
            self.axes.c2p(3, 3), self.axes.c2p(-3, 3),
        ]
        bound_square = Polygon(*d_corners, color=COL_ACCENT,
                                stroke_width=2.5, fill_opacity=0)
        d_brace = Brace(bound_square, direction=DOWN, color=COL_ACCENT)
        d_label = d_brace.get_tex("D").set_color(COL_ACCENT)
 
        self.play(Create(bound_square))
        self.play(GrowFromCenter(d_brace), Write(d_label))
        self.wait(0.7)

        heading = Text("Maggiorazione e conclusione", font_size=28,
                        weight=BOLD, color=COL_TEXT)
        heading.to_edge(UP, buff=0.5).shift(RIGHT * 2)

        line1 = Tex(
            r"Su ogni cella la funzione è vicina alla sua "
            r"approssimazione lineare, a meno di un errore $< \varepsilon$. \\"
            r"Questo perché $f$ è olomorfa su $\Omega$, per ipotesi, e quindi \\"
            r"il limite del rapporto incrementale converge alla derivata prima \\"
            r"uniformemente in ogni cella quadrata.",
            font_size=22, color=COL_TEXT,
        )
        bound = MathTex(
            r"\left| \oint_{\gamma} f(z)\, dz \right| \le C \cdot \varepsilon",
            font_size=28, color=COL_ACCENT,
        )
        line2 = Tex(
            r"In particolare",
            font_size=22, color=COL_TEXT,
        )
        bound2 = MathTex(
            r"C = \sqrt{2}D(4D + 1)",
            font_size=28, color=COL_ACCENT,
        )
        line3 = Tex(
            r"dove $D$ è il lato di un qualsiasi quadrato finito che contiene $\gamma$ \\",
            r"Poiché $\varepsilon > 0$ è arbitrario, mandando $\varepsilon \to 0$:",
            font_size=22, color=COL_TEXT,
        )
        result = MathTex(
            r"\oint_{\gamma} f(z)\, dz = 0",
            font_size=32, color=COL_RESULT,
        )

        for m in (line1, bound, line2, bound2, line3, result):
            fit_width(m, 6.2)

        stack = VGroup(line1, bound, line2, bound2, line3, result).arrange(DOWN, buff=0.4)
        stack.next_to(heading, DOWN, buff=0.6)


        self.play(FadeIn(heading, shift=DOWN * 0.2))
        self.play(Write(line1))
        self.wait(0.5)
        self.play(Write(bound))
        self.wait(1)
        self.play(Write(line2))
        self.wait(0.5)
        self.play(Write(bound2))
        self.wait(0.5)
        self.play(Write(line3))
        self.wait(0.5)
        self.play(Write(result))
        self.wait(2.5)

        qed = Text("Q.E.D.", font_size=28, color=GRAY_B)
        qed.next_to(stack, DOWN, buff=0.5)
        self.play(FadeIn(qed))
        self.wait(4)
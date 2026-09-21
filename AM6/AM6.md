# AM6 — Schema di studio per l'esame orale

*(Sezione sulla misura di Lebesgue tralasciata, salvo i tre risultati richiesti, riportati senza dimostrazione all'inizio)*

---

## 0. Tre risultati di teoria della misura (solo enunciato)

- **Lemma di Fatou**: se $f_n \ge 0$ misurabili, allora $\int \liminf_n f_n \, d\mu \le \liminf_n \int f_n \, d\mu$.
- **Teorema di Beppo Levi (convergenza monotona)**: se $0\le f_1\le f_2\le\dots$ misurabili e $f_n\to f$ puntualmente, allora $\int f_n\,d\mu \to \int f\,d\mu$.
- **Teorema di convergenza dominata di Lebesgue**: se $f_n\to f$ q.o. e $|f_n|\le g$ con $g$ integrabile, allora $f$ è integrabile e $\int f_n\,d\mu\to\int f\,d\mu$.

---

## 1. Spazi di Banach e Hilbert

### 1.1 Definizioni da conoscere (solo nome)
- Definizione di norma, spazio normato
- Definizione di operatore lineare limitato
- Definizione di $\mathcal B(X,Y)$ e norma operatoriale $\|\cdot\|_{op}$
- Definizione di funzionale di Minkowski
- Definizione di successione di Cauchy
- Definizione di variazione di una successione (e successione a variazione finita)
- Definizione di spazio metrico completo
- Definizione di spazio di Banach
- Definizione di spazio pre-hilbertiano
- Definizione di spazio di Hilbert
- Definizione di ortogonale $S^\perp$ di un sottoinsieme
- Definizione di proiettore ortogonale
- Definizione di sistema ortogonale / ortonormale
- Definizione di convergenza di una famiglia sommabile (non numerabile)
- Definizione di base ortonormale
- Definizione di spazio di Hilbert separabile

### 1.2 Risultati fondamentali (con bozza di dimostrazione)

**Teorema di equivalenza delle norme** (dim. finita $\Rightarrow$ tutte le norme sono equivalenti).
*Bozza*: si dimostra prima $\|v\|_\infty\le\|v\|_2\le\|v\|_1\le n\|v\|_\infty$ per confronto diretto delle somme. Poi si mostra che ogni norma $\|\cdot\|_\alpha$ è dominata da $\|\cdot\|_2$ tramite disuguaglianza triangolare sui vettori di base. Infine, usando che $\|\cdot\|_\alpha$ è continua (per la disuguaglianza $|\|u\|_\alpha-\|w\|_\alpha|\le\|u-w\|_\alpha$) e che la sfera unitaria $\mathbf S^1$ è compatta, Weierstrass garantisce un minimo $\lambda=\min_{\mathbf S^1}\|\cdot\|_\alpha>0$, da cui $\lambda\|v\|_2\le\|v\|_\alpha$.

**Proposizione (2.1.1)** — Per $T$ lineare: limitato $\iff$ continuo $\iff$ continuo in $0$.
*Bozza*: (limitato→continuo) $\|T(u)-T(v)\|\le M\|u-v\|$, Lipschitz $\Rightarrow$ continuo. (continuo→continuo in 0) ovvio. (continuo in 0→limitato) da continuità in 0 si ottiene $\|v\|\le\delta\Rightarrow\|Tv\|\le\varepsilon$; si riscala un generico $v\ne0$ ponendo $w=\delta v/\|v\|$ e si ottiene $\|Tv\|\le(\varepsilon/\delta)\|v\|$.

**Lemma 2.1.1 (funzionali di Minkowski) + Teorema di estensione di Hahn-Banach**. **★ Fondamentale**
*Bozza (caso reale)*: dato $\varphi$ lineare su $U\subset V$ dominato da una seminorma $m$ ($\varphi(u)\le m(u)$), e $x\in V\setminus U$, si vuole estendere a $U+\mathbb R x$ ponendo $\widetilde\varphi(u+tx)=\varphi(u)+t\alpha$ per un opportuno $\alpha\in\mathbb R$ da scegliere. Serve $\varphi(u)+t\alpha\le m(u+tx)$ per ogni $u,t$; dividendo per $t$ (con segno) questo equivale a due famiglie di disuguaglianze equivalenti a $\alpha\le m(u/t+x)-\varphi(u/t)$ (per $t>0$) e $\alpha\ge \varphi(u/t)-m(u/t-x)$ (per $t<0$), cioè a trovare $\alpha$ nell'intervallo $\big[\sup_y(\varphi(y)-m(y-x)),\ \inf_z(m(z+x)-\varphi(z))\big]$. Questo intervallo è non vuoto perché per ogni $y,z\in U$: $\varphi(y)+\varphi(z)=\varphi(y+z)\le m(y+z)\le m(y-x)+m(z+x)$ (subadditività di $m$), cioè $\varphi(y)-m(y-x)\le m(z+x)-\varphi(z)$, quindi il sup a sinistra è $\le$ dell'inf a destra: si sceglie un $\alpha$ qualsiasi in mezzo. Si applica poi il **lemma di Zorn** all'insieme delle estensioni parziali di $\varphi$ dominate da $m$, ordinato per inclusione del grafico: ogni catena ha come maggiorante l'unione (ben definita per coerenza sulle intersezioni dei domini), quindi esiste un elemento massimale $\widetilde\varphi$; se il suo dominio $W$ fosse $\ne V$, per il passo precedente si potrebbe estenderlo ulteriormente a $W+\mathbb Rx$ con $x\notin W$, contraddicendo la massimalità. Dunque $W=V$.
*Caso complesso*: si applica il caso reale a $\psi=\mathrm{Re}\,\varphi$ (funzionale $\mathbb R$-lineare, dominato da $m$ se $m$ è una seminorma per la struttura reale sottostante), ottenendo un'estensione reale $\widetilde\psi$ su $V$. Si ricostruisce $\widetilde\varphi(x):=\widetilde\psi(x)-i\widetilde\psi(ix)$: si verifica che è $\mathbb C$-lineare (per costruzione, sfruttando $\mathrm{Re}(iz)=-\mathrm{Im}(z)$) e che $\mathrm{Re}\,\widetilde\varphi=\widetilde\psi$ estende $\psi=\mathrm{Re}\,\varphi$, quindi $\widetilde\varphi$ estende $\varphi$ su $U$. La dominanza $|\widetilde\varphi(x)|\le m(x)$ si ottiene scegliendo una fase $\alpha\in\mathbb C$, $|\alpha|=1$, tale che $\alpha\widetilde\varphi(x)=|\widetilde\varphi(x)|\in\mathbb R$; allora $|\widetilde\varphi(x)|=\widetilde\varphi(\alpha x)=\widetilde\psi(\alpha x)\le m(\alpha x)=m(x)$ (usando $\mathrm{Re}\,\widetilde\varphi=\widetilde\psi\le m$ e omogeneità di $m$ rispetto a scalari di modulo 1).

**Teorema di completamento degli spazi metrici**.
*Bozza*: si considera l'insieme $S$ di tutte le successioni di Cauchy in $X$, con la relazione di equivalenza $\{x_n\}\sim\{y_n\}$ se $d(x_n,y_n)\to0$; si pone $\overline X = S/\sim$. Si definisce $\overline d([\{x_n\}],[\{y_n\}]) = \lim_n d(x_n,y_n)$: il limite esiste perché $\{d(x_n,y_n)\}_n$ è di Cauchy in $\mathbb R$ (per la disuguaglianza quadrilatera $|d(x_n,y_n)-d(x_m,y_m)|\le d(x_n,x_m)+d(y_n,y_m)$), ed è ben definito indipendentemente dai rappresentanti (per disuguaglianza triangolare incrociata tra due scelte di rappresentanti). **Completezza di $\overline X$**: data una successione di Cauchy di classi $\{[\{x^m_n\}_n]\}_m$, si costruisce la successione "diagonale" $\{x^n_n\}_n$ (di Cauchy in $X$, per una stima a "doppia $\varepsilon$" che combina Cauchy-in-$m$ e Cauchy-in-$n$ dentro ogni classe) e si mostra che la sua classe è il limite cercato. **Densità dell'immersione**: si definisce $i(x)=[\{x\}_n]$ (successione costante), isometria; dato $w=[\{x_n\}_n]\in\overline X$, la successione costante $\{x_N\}_n$ approssima $w$ arbitrariamente bene per $N$ grande (Cauchy). **Unicità**: dato un altro completamento $(\widetilde X,\tilde d)$ con immersione $j$, si definisce $\phi$ su $i(X)$ come $\phi(i(x))=j(x)$ (isometria per costruzione) e si estende per continuità/densità a tutto $\overline X$, verificando che il limite non dipende dalla successione approssimante (sempre perché $j$ è un'isometria).

**Proposizione 2.2.1** — Cauchy + sottosuccessione convergente $\Rightarrow$ convergente. *Bozza*: disuguaglianza triangolare $d(x_n,x)\le d(x_n,x_{\nu(k)})+d(x_{\nu(k)},x)$, entrambi i termini piccoli per $n,k$ grandi.

**Proposizione 2.2.4 / Corollario 2.2.1** — $\mathbb R,\mathbb C,\mathbb R^n,\mathbb C^n$ Banach.
*Bozza*: ogni successione di Cauchy ha una sottosuccessione a variazione finita (si costruisce induttivamente $\nu(k)$ con incrementi $<2^{-k}$); una successione a variazione finita converge (telescopica + convergenza assoluta); si applica Prop. 2.2.1. In alternativa: Cauchy $\Rightarrow$ limitata $\Rightarrow$ (Bolzano-Weierstrass, per bisezione degli intervalli) ammette sottosuccessione convergente $\Rightarrow$ Prop. 2.2.1.

**Teorema di Riesz-Fischer** — $L^p(X,\mu)$ è completo.
*Bozza*: data $\{f_n\}$ di Cauchy in $L^p$, si estrae una sottosuccessione $\{f_{n_k}\}$ con $\|f_{n_{k+1}}-f_{n_k}\|_p<2^{-k}$ (possibile per definizione di Cauchy). Si pone $g_s=\sum_{k=1}^s|f_{n_{k+1}}-f_{n_k}|$ e $g=\lim_s g_s$ (esiste perché $g_s$ è crescente e positiva). Per la **disuguaglianza di Minkowski**, $\|g_s\|_p<1$ per ogni $s$; per il **lemma di Fatou** applicato a $g_s^p$, $\|g\|_p^p\le\liminf_s\|g_s\|_p^p<1$, quindi $g<\infty$ q.o., il che garantisce che la serie telescopica $f_{n_1}+\sum_k(f_{n_{k+1}}-f_{n_k})$ converge q.o. a una funzione $f$ (limite puntuale di $f_{n_k}$). Si mostra $f_{n_k}\to f$ in norma $L^p$ tramite **Fatou** su $|f_{n_k}-f_n|^p$, ottenendo $\|f-f_n\|_p\to0$; infine $f\in L^p$ per la disuguaglianza triangolare $\|f\|_p\le\|f-f_m\|_p+\|f_m\|_p<\infty$. Poiché una successione di Cauchy con una sottosuccessione convergente (in norma) è essa stessa convergente allo stesso limite, si conclude $f_n\to f$ in $L^p$.

**Disuguaglianza di Cauchy-Schwarz** in spazi pre-hilbertiani. *Bozza standard*: si studia $0\le(x-ty,x-ty)$ come polinomio reale di secondo grado in $t\in\mathbb R$ (dopo aver ruotato la fase di $y$ per rendere $(x,y)$ reale) e si impone discriminante $\le0$.

**Teorema della proiezione ortogonale**. **★ Fondamentale**
*Bozza*: sia $d=d(x,V)=\inf_{v\in V}\|x-v\|$ e $\{v_n\}\subset V$ successione minimizzante, $\|x-v_n\|\to d$. Per l'**identità del parallelogramma** applicata a $x-v_n$ e $x-v_m$:
$$\|v_n-v_m\|^2 = 2\|x-v_n\|^2+2\|x-v_m\|^2-4\Big\|x-\tfrac{v_n+v_m}2\Big\|^2 \le 2\|x-v_n\|^2+2\|x-v_m\|^2-4d^2$$
(l'ultimo passaggio usando che $\frac{v_n+v_m}2\in V$, quindi $\|x-\frac{v_n+v_m}2\|\ge d$); il membro destro $\to0$ per $n,m\to\infty$, quindi $\{v_n\}$ è di Cauchy, e per completezza di $V$ (chiuso in $\mathcal H$ completo) converge a $\overline x\in V$, con $\|x-\overline x\|=d$ per continuità della norma. **Ortogonalità**: per ogni $v\in V,\ t\in\mathbb R$, $f(t)=\|x-\overline x-tv\|^2=d^2-2t\,\mathrm{Re}(x-\overline x,v)+t^2\|v\|^2$ ha minimo in $t=0$ (poiché $\overline x+tv\in V$ dà $f(t)\ge d^2=f(0)$), quindi $f'(0)=-2\,\mathrm{Re}(x-\overline x,v)=0$; ripetendo con $iv$ si annulla anche la parte immaginaria, quindi $(x-\overline x,v)=0$ per ogni $v\in V$. **Unicità**: se $\overline x,\overline x'$ realizzano entrambi $d$, per parallelogramma $\|\overline x-\overline x'\|^2\le 2d^2+2d^2-4d^2=0$.

**Teorema della rappresentazione di Riesz**. **★ Fondamentale**
*Bozza*: se $f\equiv0$ si prende $\eta=0$. Altrimenti $\ker f$ è un sottospazio chiuso (per continuità di $f$) e proprio ($f\ne0$); per il teorema della proiezione, $\mathcal H=\ker f\oplus(\ker f)^\perp$ con $(\ker f)^\perp\ne\{0\}$, quindi esiste $z\in(\ker f)^\perp$, $z\ne0$, e si può normalizzare $\|z\|=1$. Si pone $\eta=\overline{f(z)}\,z$. Per ogni $x\in\mathcal H$, si scrive
$$x = \Big(x-\frac{f(x)}{f(z)}z\Big) + \frac{f(x)}{f(z)}z,$$
dove il primo addendo sta in $\ker f$ (perché $f\big(x-\frac{f(x)}{f(z)}z\big)=f(x)-f(x)=0$), quindi è ortogonale a $z$; segue
$$(\eta,x) = \Big(\overline{f(z)}z,\ \big(x-\tfrac{f(x)}{f(z)}z\big)+\tfrac{f(x)}{f(z)}z\Big) = \overline{f(z)}\cdot\frac{f(x)}{f(z)}(z,z) = f(x)$$
(il primo termine si annulla per l'ortogonalità appena mostrata, $\|z\|=1$). **Unicità**: se $(\eta,x)=(\eta',x)$ per ogni $x$, allora $(\eta-\eta',x)=0$ per ogni $x$, in particolare per $x=\eta-\eta'$, da cui $\eta=\eta'$. Si verifica infine $\|f\|=\|\eta\|$ da Cauchy-Schwarz ($|f(x)|\le\|\eta\|\|x\|$) più il caso di uguaglianza $x=\eta$.

**Teorema di caratterizzazione delle basi ortonormali** e **Teorema di esistenza della base ortonormale** (Zorn applicato ai sistemi ortonormali ordinati per inclusione). Solo enunciato.

---

## 2. Teoria degli operatori

### 2.1 Definizioni da conoscere (solo nome)
- Definizione di operatore aggiunto $T^*$
- Definizione di operatore autoaggiunto, normale, isometrico, unitario
- Definizione di spettro $\sigma(T)$, risolvente $\rho(T)$, funzione risolvente $R_T(\lambda)$
- Definizione di raggio spettrale
- Definizione di operatore positivo ($A\ge0$)
- Definizione di risoluzione dell'identità (famiglia spettrale)
- Definizione di supporto di una misura

### 2.2 Risultati fondamentali (con bozza di dimostrazione)

**Teorema (3.1.1)** — Esistenza e unicità dell'aggiunto.
*Bozza*: fissato $x\in\mathcal H$, il funzionale $y\mapsto\overline{(Tx,y)}$ (o equivalentemente si lavora con $\phi_x(y)=(y,Tx)$ a seconda della convenzione) è lineare e limitato ($|(Tx,y)|\le\|Tx\|\|y\|\le\|T\|\|x\|\|y\|$), quindi per **Riesz** esiste unico $z=:T^*x\in\mathcal H$ con $(y,Tx)=(T^*x,y)$... più precisamente si definisce $T^*x$ come l'unico vettore tale che $(T^*x,y)=(x,Ty)$ per ogni $y$. Linearità di $T^*$ in $x$ segue dall'unicità nella rappresentazione di Riesz applicata a combinazioni lineari; limitatezza da $\|T^*x\|^2=(T^*x,T^*x)=(x,TT^*x)\le\|x\|\|T\|\|T^*x\|$, da cui $\|T^*x\|\le\|T\|\|x\|$. Unicità di $T^*$: se $S,S'$ soddisfano entrambi la proprietà definente, $(S x-S'x,y)=0$ per ogni $y$, quindi $Sx=S'x$.

**Lemma (serie di Neumann)** — $\|S\|<1\Rightarrow(\mathbf 1-S)^{-1}=\sum_n S^n$.
*Bozza*: la serie converge in norma (dominata da $\sum\|S\|^n<\infty$, $\mathcal B(\mathcal H)$ Banach); si verifica per telescopia che $(\mathbf1-S)\sum_{n=0}^N S^n = \mathbf 1-S^{N+1}\to\mathbf1$.

**Teorema (3.3.1)** — Proprietà fondamentali dello spettro. **★ Fondamentale**
*Bozza per punto*:
1. $\lambda\in\sigma(T)\Rightarrow\overline\lambda\in\sigma(T^*)$: se $(\lambda\mathbf1-T)$ non è invertibile, non lo è neanche il suo aggiunto $(\overline\lambda\mathbf1-T^*)$ (l'aggiunzione è una biiezione che manda invertibili in invertibili, con $(S^{-1})^*=(S^*)^{-1}$).
2. $\lambda\in\sigma(T)$, $\lambda\ne0$, $T$ invertibile $\Rightarrow\lambda^{-1}\in\sigma(T^{-1})$: si fattorizza $\lambda\mathbf1-T = -\lambda T(\lambda^{-1}\mathbf1-T^{-1})$; se $(\lambda^{-1}\mathbf1-T^{-1})$ fosse invertibile, essendo $T$ invertibile anche $\lambda\mathbf1-T$ lo sarebbe (prodotto di invertibili), assurdo.
3. $T$ normale $\Rightarrow r(T)=\|T\|$: dall'identità $C^*$, $\|T^2\|^2=\|(T^2)^*T^2\|=\|(T^*T)^2\|$ (usando normalità $T^*T=TT^*$) $=\|T^*T\|^2=\|T\|^4$, quindi $\|T^2\|=\|T\|^2$; iterando su $T^{2^n}$ (anch'esso normale) si ottiene $\|T^{2^n}\|=\|T\|^{2^n}$, e per la formula del raggio spettrale $r(T)=\lim_n\|T^n\|^{1/n}=\lim_n\|T^{2^n}\|^{1/2^n}=\|T\|$.
4. $V$ unitario $\Rightarrow\sigma(V)\subset\mathbf S^1$: $V$ è normale quindi per (3) $r(V)=\|V\|=1$, dando $\sigma(V)\subset\overline{D_1(0)}$; per (2) applicato a $V^{-1}=V^*$ (anch'esso unitario, norma 1) si ha $\sigma(V^{-1})\subset\overline{D_1(0)}$, cioè per ogni $\lambda\in\sigma(V)$, $\lambda^{-1}\in\sigma(V^{-1})$ dà $|\lambda^{-1}|\le1$; combinando $|\lambda|\le1$ e $|\lambda|\ge1$ si ha $|\lambda|=1$.
5. $A=A^*\Rightarrow\sigma(A)\subset\mathbb R$: si costruisce $e^{iA}=\sum_n\frac{(iA)^n}{n!}$ (converge in norma, $\mathcal B(\mathcal H)$ Banach); è unitario perché $(e^{iA})^*=e^{-iA^*}=e^{-iA}=(e^{iA})^{-1}$ (le serie di $e^{iA}$ e $e^{-iA}$ si moltiplicano termine a termine dando $\mathbf1$, come per gli esponenziali scalari, poiché $iA$ e $-iA$ commutano). Per $\lambda=a+ib\notin\mathbb R$ ($b\ne0$): si vuole mostrare $A-\lambda\mathbf1$ invertibile. Si nota che $e^{i\lambda}=e^{ia}e^{-b}$ ha modulo $e^{-b}\ne1$, quindi per (4) $e^{i\lambda}\notin\sigma(e^{iA})$, cioè $e^{i\lambda}\mathbf1-e^{iA}$ è invertibile; si fattorizza $e^{i\lambda}\mathbf1-e^{iA}=e^{i\lambda}\mathbf1-e^{i\lambda}e^{i(A-\lambda\mathbf1)}=e^{i\lambda}(\mathbf1-e^{i(A-\lambda)})$, e sviluppando $e^{i(A-\lambda)}=\mathbf1+i(A-\lambda)+O((A-\lambda)^2)$ si collega l'invertibilità di questo fattore a quella di $(A-\lambda\mathbf1)$ tramite un argomento di serie di Neumann sul resto.

**Teorema del calcolo funzionale continuo**. **★★ Uno dei pilastri del corso**
*Bozza*: sia $A=A^*$, $\sigma(A)\subset\mathbb R$ compatto (spettro di un operatore limitato, chiuso e nel disco di raggio $\|A\|$). **Passo 1 (polinomi)**: si definisce $p(A)=\sum a_k A^k$ nel modo ovvio; si mostra $\sigma(p(A))=p(\sigma(A))$ fattorizzando, per ogni $\mu\in\mathbb C$, $p(\lambda)-\mu=c\prod_k(\lambda-\lambda_k)$ sulle radici $\lambda_k$ (teorema fondamentale dell'algebra), da cui $p(A)-\mu\mathbf1=c\prod_k(A-\lambda_k\mathbf1)$ è invertibile se e solo se ogni fattore lo è, cioè se e solo se nessun $\lambda_k\in\sigma(A)$, cioè se e solo se $\mu\notin p(\sigma(A))$. **Passo 2 (isometria sui polinomi)**: $p(A)$ è normale (autoaggiunto se $p$ ha coefficienti reali, ma comunque normale in generale), quindi per il Teor. 3.3.1.3 $\|p(A)\|=r(p(A))=\sup_{\mu\in\sigma(p(A))}|\mu|=\sup_{\lambda\in\sigma(A)}|p(\lambda)|=\|p\|_{\infty,\sigma(A)}$. **Passo 3 (densità e limite)**: per **Stone-Weierstrass** (l'algebra dei polinomi reali/complessi separa i punti di $\sigma(A)$ compatto e contiene le costanti) i polinomi sono densi in $C(\sigma(A))$ per $\|\cdot\|_\infty$; data $f\in C(\sigma(A))$ e $p_n\to f$ uniformemente, $\{p_n(A)\}$ è di Cauchy in $\mathcal B(\mathcal H)$ (per l'isometria del Passo 2, $\|p_n(A)-p_m(A)\|=\|p_n-p_m\|_\infty\to0$), quindi converge (Banach) a un operatore che si definisce come $f(A)$; il limite non dipende dalla successione approssimante scelta (sempre per l'isometria, due successioni con lo stesso limite uniforme danno operatori a distanza nulla). **Passo 4 (proprietà)**: linearità, moltiplicatività ($fg\mapsto f(A)g(A)$), $*$-preservazione ($\overline f(A)=f(A)^*$) e isometria ($\|f(A)\|=\|f\|_\infty$) valgono sui polinomi per costruzione algebrica diretta, e passano al limite uniforme per continuità delle operazioni in norma. **Passo 5 (positività)**: se $f\ge0$ su $\sigma(A)$, si scrive $f=g^2$ con $g=\sqrt f\ge0$ continua (radice quadrata di una funzione continua non-negativa è continua); allora $(x,f(A)x)=(x,g(A)^2x)=(x,g(A)^*g(A)x)=\|g(A)x\|^2\ge0$ (usando che $g$ reale $\Rightarrow g(A)$ autoaggiunto).

**Corollario (3.3.3)** — $A\ge0\iff A=A^*$ e $\sigma(A)\subset[0,\infty)$.
*Bozza*: ($\to$) $(x,Ax)$ reale per ogni $x$ implica $A=A^*$ per identità di polarizzazione; per $\lambda<0$ si stima $\|(A-\lambda\mathbf1)x\|\ge|\lambda|\,\|x\|$ (operatore "lontano da zero"), quindi invertibile. ($\leftarrow$) per calcolo funzionale continuo esiste $\sqrt A =: B\ge0$ autoaggiunto, e $(x,Ax)=(Bx,Bx)\ge0$.

**Corollario (3.3.4)** — $A\ge0\iff A=B^*B$. (conseguenza immediata di 3.3.3 + $\sqrt A$).

**Lemma 3.3.5, 3.3.6, 3.3.7** — Disuguaglianze sugli operatori positivi.
*Bozza 3.3.5* ($A\le\|A\|\mathbf1$, cioè $\|A\|\mathbf1-A\ge0$): dal calcolo funzionale, $\sigma(A)\subset[0,\|A\|]$ (positività + $r(A)=\|A\|$ per normalità), quindi $\|A\|-t\ge0$ per ogni $t\in\sigma(A)$, cioè la funzione $\|A\|-\mathrm{id}$ è $\ge0$ su $\sigma(A)$; per il calcolo funzionale (positività) $\|A\|\mathbf1-A\ge0$.
*Bozza 3.3.6* ($0\le A\le B\Rightarrow\|A\|\le\|B\|$): da $A\le B$ si ha $(x,Ax)\le(x,Bx)\le\|B\|\|x\|^2$ per ogni $x$ (usando 3.3.5 su $B$); ma $A\ge0$ autoaggiunto ha $\|A\|=\sup_{\|x\|=1}(x,Ax)$ (formula variazionale per operatori positivi, conseguenza del calcolo funzionale/teorema spettrale), quindi $\|A\|\le\|B\|$.
*Bozza 3.3.7* ($\|Ax\|^2\le\|A\|(x,Ax)$ per $A\ge0$): da 3.3.5, $0\le A\le\|A\|\mathbf1$. Moltiplicando (sandwich) per $A^{1/2}=\sqrt A\ge0$ su entrambi i lati — operazione che preserva l'ordine tra operatori positivi, $0\le X\le Y\Rightarrow C^*XC\le C^*YC$ — con $C=A^{1/2}$ si ottiene $A^{1/2}AA^{1/2}\le\|A\|A^{1/2}\mathbf1A^{1/2}$, cioè $A^2\le\|A\|A$. Prendendo il valore atteso su $x$: $(x,A^2x)\le\|A\|(x,Ax)$, cioè $\|Ax\|^2\le\|A\|(x,Ax)$.

**Proposizione (esistenza inf in $\mathcal B(\mathcal H)$, S.O.T.)** — successioni decrescenti $A_n\ge0$ convergono fortemente. *Bozza*: $\|A_nx-A_mx\|^2\le\|A_n-A_m\|(x,(A_n-A_m)x)$ (Lemma 3.3.7 applicato a $A_n-A_m\ge0$); la successione scalare $(x,A_nx)$ è decrescente e limitata quindi di Cauchy, dunque $\{A_nx\}$ è di Cauchy in $\mathcal H$ completo.

**Costruzione della risoluzione spettrale** $\{P^A_\lambda\}$ tramite $P^A_\lambda=\lim_n h_{\lambda,n}(A)$ con $h_{\lambda,n}$ funzioni continue decrescenti a $\chi_{(-\infty,\lambda]}$. Solo l'idea generale va tenuta a mente per l'orale: approssimazione per calcolo funzionale + convergenza S.O.T. monotona, idempotenza via confronto $h_{\lambda,m}\le h_{\lambda,n}^2\le h_{\lambda,n}$, continuità da destra per costruzione. Da qui si ottiene la formula spettrale $(x,f(A)x)=\int f\,dm_{F^A_x}$, con $\mathrm{supp}(m_{F_x^A})=\sigma(A)$.

---

## 3. Algebre di operatori

### 3.1 Definizioni da conoscere (solo nome)
- Definizione di $C^*$-algebra (con identità)
- Definizione di $C^*$-algebra generata da un insieme di operatori autoaggiunti
- Definizione di rappresentazione di una $C^*$-algebra
- Definizione di stato ($\mathfrak S(\mathscr A)$)
- Definizione di carattere
- Definizione di stato puro ($\mathfrak P(\mathscr A)$, estremalità)
- Definizione di rappresentazione irriducibile
- Definizione di terna GNS, vettore ciclico
- Definizione di commutante $\pi(\mathscr A)'$
- Definizione di CCR (relazioni canoniche di commutazione), forma di Weyl
- Definizione di rappresentazione regolare

### 3.2 Risultati fondamentali (con bozza di dimostrazione)

**Teorema di Gelfand**. **★★ Pilastro del corso**
*Bozza (caso $\mathscr A=C^*(\mathbf1,A)$, $A=A^*$)*: sia $X=\Omega(\mathscr A)$ lo spazio dei caratteri di $\mathscr A$, con la topologia $*$-debole (quella indotta da $\mathscr A^*$), che lo rende compatto (per Banach-Alaoglu, essendo $\|\omega\|=1$ per ogni carattere per Prop. 4.2.2) e Hausdorff.
**Costruzione della biiezione $\lambda\leftrightarrow\omega_\lambda$**: per $\lambda\in\sigma(A)$, il calcolo funzionale continuo fornisce l'omomorfismo $f\mapsto f(A)$ da $C(\sigma(A))$ a $\mathscr A$; si definisce $\omega_\lambda(f(A)):=f(\lambda)$. È ben definito perché il calcolo funzionale è iniettivo (isometrico), lineare e moltiplicativo per costruzione (proprietà del calcolo funzionale), unitale ($\omega_\lambda(\mathbf1)=1(\lambda)=1$), $*$-preservante; quindi $\omega_\lambda$ è un carattere.
**Iniettività** di $\lambda\mapsto\omega_\lambda$: se $\omega_{\lambda_1}=\omega_{\lambda_2}$, applicando a $f=\mathrm{id}$ si ha $\omega_{\lambda_1}(A)=\lambda_1=\lambda_2=\omega_{\lambda_2}(A)$.
**Suriettività**: dato un carattere $\omega\in\Omega(\mathscr A)$, si pone $\lambda_0:=\omega(A)\in\sigma_{\mathscr A}(A)=\sigma(A)$ (il valore di un carattere su un elemento sta sempre nello spettro, altrimenti $A-\lambda_0\mathbf1$ invertibile darebbe $\omega((A-\lambda_0)^{-1})\omega(A-\lambda_0)=1$ ma $\omega(A-\lambda_0)=0$, assurdo). Si mostra $\omega=\omega_{\lambda_0}$: sui polinomi $p(A)$, $\omega(p(A))=p(\omega(A))=p(\lambda_0)=\omega_{\lambda_0}(p(A))$ per moltiplicatività di $\omega$; per densità dei polinomi in $C(\sigma(A))$ e continuità di entrambi $\omega,\omega_{\lambda_0}$ (limitati da $\|\cdot\|$, essendo stati/caratteri di norma 1), l'uguaglianza si estende a ogni $f(A)$.
**Isomorfismo**: la trasformata di Gelfand $\widehat{\cdot}:\mathscr A\to C(X)$, $\widehat B(\omega)=\omega(B)$, composta con l'omeomorfismo $X\cong\sigma(A)$ appena costruito, diventa esattamente l'inversa del calcolo funzionale: $\widehat{f(A)}=f$. È un $*$-isomorfismo isometrico per l'isometria del calcolo funzionale stesso. *(Il caso generale, per $\mathscr A$ commutativa qualsiasi, richiede un argomento analogo ma più delicato che identifica $\Omega(\mathscr A)$ con lo spazio degli ideali massimali, senza appoggiarsi a un singolo generatore autoaggiunto.)*

**Lemma di permanenza spettrale** — sottoalgebra chiusa in norma: $\sigma(A)=\sigma_{\mathscr A}(A)$.
*Bozza*: $\sigma(A)\subset\sigma_{\mathscr A}(A)$ ovvio (meno inversi disponibili in sottoalgebra). Viceversa, per $\lambda\in\sigma(A)\subset\mathbb R$, si usa che $\lambda+i\varepsilon\in\rho(A)$ per ogni $\varepsilon>0$ (Teor. 3.3.1.5) e che l'inverso $(A-(\lambda+i\varepsilon)\mathbf1)^{-1}\in\mathscr A$ (chiusura in norma) converge per $\varepsilon\to0$ a $(A-\lambda\mathbf1)^{-1}\in\mathscr A$ per continuità dell'inversione.

**Proposizione (4.2.1)** — $*$-omomorfismo unitale è contrattivo, isometrico se iniettivo.
*Bozza*: **(1)** Se $\phi(AA^*)-\lambda\mathbf1$ fosse invertibile in $\mathscr B$ mentre $AA^*-\lambda\mathbf1$ non lo è in $\mathscr A$... si procede per contronominale: se $AA^*-\lambda\mathbf1$ **è** invertibile in $\mathscr A$, applicando $\phi$ (omomorfismo unitale) a $(AA^*-\lambda\mathbf1)(AA^*-\lambda\mathbf1)^{-1}=\mathbf1$ si ottiene $(\phi(AA^*)-\lambda\mathbf1)\phi((AA^*-\lambda\mathbf1)^{-1})=\mathbf1$, cioè $\phi(AA^*)-\lambda\mathbf1$ è invertibile in $\mathscr B$ (con inverso $\phi((AA^*-\lambda\mathbf1)^{-1})$). Per contrapposizione: $\lambda\notin\sigma_{\mathscr B}(\phi(AA^*))^c \Rightarrow \lambda\notin\sigma_{\mathscr A}(AA^*)^c$, cioè $\sigma_{\mathscr B}(\phi(AA^*))\subset\sigma_{\mathscr A}(AA^*)$; quindi $r(\phi(AA^*))\le r(AA^*)$, e per normalità (identità $C^*$, $\|\phi(A)\|^2=\|\phi(A)^*\phi(A)\|=\|\phi(AA^*)\|=r(\phi(AA^*))\le r(AA^*)=\|AA^*\|=\|A\|^2$) si ottiene $\|\phi(A)\|\le\|A\|$.
**(2)** Si vuole $\sigma_{\mathscr A}(AA^*)=\sigma_{\mathscr B}(\phi(AA^*))$ (non solo l'inclusione già vista). Se fossero diversi, per (1) $\sigma_{\mathscr B}(\phi(AA^*))\subsetneq\sigma_{\mathscr A}(AA^*)$ (chiuso proprio in un compatto): per il **teorema di Tietze** (estensione continua da un chiuso) esiste $f\in C(\sigma_{\mathscr A}(AA^*))$ con $f\equiv0$ su $\sigma_{\mathscr B}(\phi(AA^*))$ ma $f\not\equiv0$ complessivamente. Per l'isometria del calcolo funzionale, $\|f(\phi(AA^*))\|=\|f\|_{\infty,\sigma_{\mathscr B}(\phi(AA^*))}=0$, cioè $f(\phi(AA^*))=0$. D'altra parte $\phi(f(AA^*))=f(\phi(AA^*))$: vero per $f$ polinomiale (per costruzione algebrica, $\phi$ preserva prodotti/somme), e passa al limite uniforme per continuità di $\phi$ (punto (1), $\phi$ contrattivo) e del calcolo funzionale. Quindi $\phi(f(AA^*))=0$, e per **iniettività** di $\phi$, $f(AA^*)=0$, cioè $\|f\|_{\infty,\sigma_{\mathscr A}(AA^*)}=0$: assurdo, perché $f\not\equiv0$. Dunque $\sigma_{\mathscr A}(AA^*)=\sigma_{\mathscr B}(\phi(AA^*))$, da cui $\|\phi(A)\|^2=r(\phi(AA^*))=r(AA^*)=\|A\|^2$.

**Proposizione (4.2.2)** — Ogni stato preserva lo $*$, $\|\omega\|=1$.
*Bozza*: $A=A_1+iA_2$ (parte "reale/immaginaria" autoaggiunte) $\Rightarrow\omega(A^*)=\overline{\omega(A)}$; con Cauchy-Schwarz sulla forma sesquilineare $\{A,B\}=\omega(A^*B)$ si ottiene $|\omega(B)|\le\omega(B^*B)^{1/2}\le\|B\|$ (usando $B^*B\le\|B^*B\|\mathbf1$); l'uguaglianza per $B=\mathbf1$ dà $\|\omega\|=1$.

**Teorema di Riesz-Markov** (solo enunciato — stati su $C(X)$ ↔ misure boreliane positive normalizzate).

**Teorema GNS (Gelfand-Naimark-Segal)**. **★★★ Il risultato più importante del corso**
*Bozza*: **Costruzione dello spazio.** Su $\mathscr A$ si considera la forma sesquilineare $\langle A,B\rangle:=\omega(A^*B)$: è positiva semidefinita ($\langle A,A\rangle=\omega(A^*A)\ge0$, per positività dello stato) ma può avere un nucleo non banale. Si pone $\mathscr N_\omega=\{A\in\mathscr A:\omega(A^*A)=0\}$: è un sottospazio (per la disuguaglianza di Cauchy-Schwarz associata alla forma, $|\langle A,B\rangle|^2\le\langle A,A\rangle\langle B,B\rangle$, che impedisce somme di elementi a norma nulla di avere norma positiva) ed è un **ideale sinistro**: per $J\in\mathscr N_\omega,\ B\in\mathscr A$, $\omega((BJ)^*(BJ))=\omega(J^*B^*BJ)\le\|B^*B\|\,\omega(J^*J)=0$ (usando che $B^*B\le\|B\|^2\mathbf1$ e la positività/monotonia di $\omega$ come funzionale positivo). Il prodotto scalare $\langle\cdot,\cdot\rangle$ discende quindi ben definito sul quoziente $\mathscr A/\mathscr N_\omega$ (indipendente dai rappresentanti, sempre per Cauchy-Schwarz: se $A-A'\in\mathscr N_\omega$, $|\langle A-A',B\rangle|^2\le\langle A-A',A-A'\rangle\langle B,B\rangle=0$). Si completa lo spazio pre-hilbertiano risultante a uno spazio di Hilbert $\mathcal H_\omega$ (teorema di completamento).
**Rappresentazione.** Si definisce $\pi_\omega(B)\widetilde A:=\widetilde{BA}$ sulle classi $\widetilde A\in\mathscr A/\mathscr N_\omega$: ben posta perché $\mathscr N_\omega$ è ideale sinistro (se $A-A'\in\mathscr N_\omega$ allora $BA-BA'=B(A-A')\in\mathscr N_\omega$ ancora per la stessa stima); è limitata, $\|\pi_\omega(B)\widetilde A\|^2=\omega((BA)^*BA)=\omega(A^*B^*BA)\le\|B\|^2\omega(A^*A)=\|B\|^2\|\widetilde A\|^2$ (di nuovo $B^*B\le\|B\|^2\mathbf1$), quindi si estende per continuità a un operatore limitato su $\mathcal H_\omega$; è un $*$-omomorfismo per costruzione algebrica diretta ($\pi_\omega(B_1B_2)\widetilde A=\widetilde{B_1B_2A}=\pi_\omega(B_1)\pi_\omega(B_2)\widetilde A$, e $(\pi_\omega(B)\widetilde A,\widetilde C)=\omega(A^*B^*C)=(\widetilde A,\pi_\omega(B^*)\widetilde C)$ dà $\pi_\omega(B)^*=\pi_\omega(B^*)$).
**Vettore ciclico.** Si pone $\xi_\omega=\widetilde{\mathbf1}$: allora $(\xi_\omega,\pi_\omega(B)\xi_\omega)=\langle\mathbf1,B\rangle=\omega(\mathbf1^*B)=\omega(B)$, cioè $\omega$ è vettoriale; $\xi_\omega$ è ciclico perché $\{\pi_\omega(B)\xi_\omega:B\in\mathscr A\}=\{\widetilde B:B\in\mathscr A\}=\mathscr A/\mathscr N_\omega$ è denso in $\mathcal H_\omega$ per costruzione (completamento).
**Unicità.** Data un'altra terna $(\mathcal H,\pi,\xi)$ con $\omega(B)=(\xi,\pi(B)\xi)$ e $\xi$ ciclico, si definisce $U_0:\pi_\omega(B)\xi_\omega\mapsto\pi(B)\xi$: è ben definito e isometrico perché entrambi i lati hanno lo stesso prodotto scalare $\omega(B_1^*B_2)$ ($(\pi_\omega(B_1)\xi_\omega,\pi_\omega(B_2)\xi_\omega)_{\mathcal H_\omega}=\omega(B_1^*B_2)=(\pi(B_1)\xi,\pi(B_2)\xi)_{\mathcal H}$); essendo isometrico su un sottospazio denso, si estende per continuità a un operatore unitario $U:\mathcal H_\omega\to\mathcal H$ (suriettivo per ciclicità di $\xi$); infine $U$ intreccia le rappresentazioni, $U\pi_\omega(A)=\pi(A)U$, verificato sui generatori densi $\pi_\omega(B)\xi_\omega$ e poi esteso per continuità.

**Lemma (4.2.1)** — $\|A\|=\sup_{\omega\in\mathfrak S(\mathscr A)}|\omega(A)|$ per $A=A^*$.
*Bozza*: la disuguaglianza $\sup_\omega|\omega(A)|\le\|A\|$ è ovvia (Prop. 4.2.2, $\|\omega\|=1$). Per l'altra, si costruisce sul sottospazio $E=\mathrm{span}\{\mathbf1,A\}$ il funzionale $g(\lambda\mathbf1+\mu A)=\lambda\pm\mu\|A\|$ (segno scelto in modo che $g(A)=\pm\|A\|$ coincida con un punto dello spettro, possibile perché $\|A\|=\max_{t\in\sigma(A)}|t|$ per normalità di $A$, quindi $\pm\|A\|\in\sigma(A)$ per uno dei due segni). Si verifica $|g(\lambda\mathbf1+\mu A)|\le\|\lambda\mathbf1+\mu A\|$: dividendo per $\mu\ne0$, equivale a $|\lambda/\mu\pm\|A\||\le\|\lambda/\mu\,\mathbf1+A\|=\max_{t\in\sigma(A)}|\lambda/\mu+t|$ (per calcolo funzionale, essendo $A$ autoaggiunto), disuguaglianza vera perché $\pm\|A\|\in\sigma(A)$ è uno dei valori su cui si fa il massimo. Per **Hahn-Banach** (con seminorma $m=\|\cdot\|$) si estende $g$ a $f\in\mathscr A^*$ con $|f(B)|\le\|B\|$ per ogni $B$, quindi $\|f\|\le1$; ma $f(\mathbf1)=g(\mathbf1)=1$, quindi $\|f\|\ge|f(\mathbf1)|=1$, dando $\|f\|=f(\mathbf1)=1$. Resta da mostrare che $f$ è **positivo** (e quindi uno stato): (i) per $B=B^*$, si stima $\|\mathbf1+itB\|^2=\|(\mathbf1+itB)^*(\mathbf1+itB)\|=\|\mathbf1+t^2B^2\|=1+O(t^2)$ per $t\to0$; ma $|f(\mathbf1+itB)|=|1+it f(B)|\le\|\mathbf1+itB\|=1+O(t^2)$; scrivendo $f(B)=x+iy$, $|1+it(x+iy)|^2=(1-ty)^2+t^2x^2=1-2ty+O(t^2)$, che deve restare $\le(1+O(t^2))^2=1+O(t^2)$ per ogni $t$ (positivo e negativo) — questo forza $y=0$, cioè $f(B)\in\mathbb R$. (ii) Per $B\ge0$ con $\|B\|$ piccolo, $\|\mathbf1-tB\|\le1$ per $t\in[0,1/\|B\|]$ (da 3.3.5), quindi $|f(\mathbf1-tB)|=|1-tf(B)|\le1$; se fosse $f(B)<0$ questo fallirebbe per $t$ opportuno, quindi $f(B)\ge0$. Dunque $f\in\mathfrak S(\mathscr A)$ e $f(A)=g(A)=\pm\|A\|$, cioè $|f(A)|=\|A\|$.

**Corollario (4.2.1)** — Per $A=A^*\ne0$ esiste stato $\omega$ con $\omega(A)\ne0$. (immediato da Lemma 4.2.1, dato che $\|A\|>0$).

**Teorema di Schur**. **★★ Pilastro (con GNS e Gelfand)**
*Bozza*: **(2→1)**, cioè commutante banale $\Rightarrow$ irriducibile: sia $K\subset\mathcal H_\pi$ chiuso $\pi$-invariante, $P_K$ il proiettore ortogonale su $K$. Per ogni $A\in\mathscr A$ e $x\in K$, $\pi(A)x\in K$, cioè $P_K\pi(A)P_K=\pi(A)P_K$; passando all'aggiunto ($\pi(A^*)$ al posto di $\pi(A)$, e $P_K$ autoaggiunto) si ottiene anche $P_K\pi(A)=P_K\pi(A)P_K$ per ogni $A$ (sostituendo $A\to A^*$ e aggiungendo), da cui $P_K\pi(A)=\pi(A)P_K$: $P_K$ commuta con $\pi(\mathscr A)$, quindi $P_K\in\pi(\mathscr A)'=\mathbb C\mathbf1$ per ipotesi. Ma un proiettore scalare è $0$ o $\mathbf1$, quindi $K=\{0\}$ o $K=\mathcal H_\pi$: $\pi$ è irriducibile.
**(1→2)**, cioè irriducibile $\Rightarrow$ commutante banale: sia $B\in\pi(\mathscr A)'$; basta trattare $B$ autoaggiunto (ogni $B$ si scompone in parte reale/immaginaria autoaggiunte, anch'esse nel commutante essendo questo una $*$-sottoalgebra). Per il calcolo funzionale continuo, la risoluzione spettrale $\{P_\lambda^B\}$ di $B$ è costruita come limite (in S.O.T.) di polinomi/funzioni continue di $B$, quindi commuta anch'essa con ogni $\pi(A)$ (dato che $B$ vi commuta); in particolare ogni $P_\lambda^B\mathcal H_\pi$ è un sottospazio chiuso $\pi$-invariante, quindi per irriducibilità è $\{0\}$ o tutto $\mathcal H_\pi$: la famiglia spettrale è "degenere" (un unico salto), il che forza $B$ a essere uno scalare $\mu\mathbf1$ (lo spettro di $B$ si riduce a un punto). Quindi $\pi(\mathscr A)'=\mathbb C\mathbf1$.
**(1↔3)**: l'irriducibilità (nessun sottospazio chiuso invariante non banale) equivale, per il punto (1→2) applicato a un vettore $\xi\ne0$ qualsiasi, al fatto che $\overline{\{\pi(A)\xi:A\in\mathscr A\}}$ (chiaramente invariante) sia tutto $\mathcal H_\pi$, cioè che ogni vettore non nullo sia ciclico.

**Teorema di Segal** — $\omega$ puro $\iff\pi_\omega$ irriducibile. (dimostrazione omessa nel testo — tienila a mente come collegamento concettuale chiave tra convessità di $\mathfrak S(\mathscr A)$ e Teorema di Schur).

**Lemma (4.4.1)** — $\sigma_{fis}(A)=\sigma_{\mathscr A}(A)$ per osservabili fisiche $A\in\mathscr O$, dove $\sigma_{fis}(A)=\{\lambda:\lambda=\omega(A)\text{ per qualche }\omega\in\mathfrak S(\mathscr A)\text{ con }\Delta_\omega(A)=0\}$.
*Bozza ($\subset$)*: sia $\lambda\in\sigma_{fis}(A)$, cioè esiste $\omega\in\mathfrak S(\mathscr A)$ con $\omega(A)=\lambda,\ \Delta_\omega(A)=0$. Per GNS, $0=\omega((A-\lambda\mathbf1)^2)=(\xi_\omega,\pi_\omega(A-\lambda\mathbf1)^2\xi_\omega)=\|\pi_\omega(A-\lambda\mathbf1)\xi_\omega\|^2$ (usando che $\pi_\omega(A-\lambda\mathbf1)$ è autoaggiunto), quindi $\pi_\omega(A)\xi_\omega=\lambda\xi_\omega$: $\lambda$ è autovalore di $\pi_\omega(A)$. Se $A-\lambda\mathbf1$ fosse invertibile in $\mathscr A$, applicando $\pi_\omega$: $1=\omega(\mathbf1)=(\xi_\omega,\pi_\omega((A-\lambda\mathbf1)^{-1}(A-\lambda\mathbf1))\xi_\omega)=(\xi_\omega,\pi_\omega((A-\lambda\mathbf1)^{-1})\underbrace{\pi_\omega(A-\lambda\mathbf1)\xi_\omega}_{=0})=0$, assurdo. Quindi $A-\lambda\mathbf1$ non è invertibile, cioè $\lambda\in\sigma_{\mathscr A}(A)$.
*Bozza ($\supset$)*: sia $\lambda\in\sigma_{\mathscr A}(A)=\sigma(A)$ (per permanenza spettrale). Il carattere $\omega_\lambda\in\Omega(C^*(\mathbf1,A))$ costruito nel Teorema di Gelfand soddisfa $\omega_\lambda(A)=\lambda$ e, per moltiplicatività, $\Delta_{\omega_\lambda}(A)=\omega_\lambda(A^2)-\omega_\lambda(A)^2=\omega_\lambda(A)^2-\omega_\lambda(A)^2=0$. Per il **teorema di estensione di Hahn-Banach** (applicato come nel Lemma 4.2.1: $\omega_\lambda$ ha norma 1 sulla sottoalgebra, si estende a $\omega\in\mathscr A^*$ con $\|\omega\|=1=\omega(\mathbf1)$, e questo forza $\omega$ positivo, quindi $\omega\in\mathfrak S(\mathscr A)$) esiste $\omega\in\mathfrak S(\mathscr A)$ che estende $\omega_\lambda$, con $\omega(A)=\lambda$ e $\Delta_\omega(A)=\Delta_{\omega_\lambda}(A)=0$ (la varianza dipende solo dai valori di $\omega$ su $A,A^2\in C^*(\mathbf1,A)$, dove $\omega$ coincide con $\omega_\lambda$). Quindi $\lambda\in\sigma_{fis}(A)$.

**Lemma (4.4.2)** — $\mathscr A$ commutativa: $\omega$ puro $\iff$ carattere.
*Bozza (→)*: sia $\omega\in\mathfrak P(\mathscr A)$. Per GNS + Segal la terna $(\mathcal H_\omega,\pi_\omega,\xi_\omega)$ ha $\pi_\omega$ irriducibile; per Schur $\pi_\omega(\mathscr A)'=\mathbb C\mathbf1$. Siccome $\mathscr A$ è commutativa, ogni $\pi_\omega(A)$ commuta con tutti i $\pi_\omega(B)$, cioè $\pi_\omega(\mathscr A)\subset\pi_\omega(\mathscr A)'=\mathbb C\mathbf1$: quindi $\pi_\omega(A)=\omega(A)\mathbf1_{\mathcal H_\omega}$ per ogni $A$ (il valore $\omega(A)$ è forzato prendendo il prodotto scalare con $\xi_\omega$, essendo $\|\xi_\omega\|=1$). Da qui $\omega(AB)=(\xi_\omega,\pi_\omega(AB)\xi_\omega)=(\xi_\omega,\pi_\omega(A)\pi_\omega(B)\xi_\omega)=(\xi_\omega,\omega(A)\omega(B)\mathbf1\,\xi_\omega)=\omega(A)\omega(B)$: $\omega$ è moltiplicativo, oltre che lineare (per definizione di stato), unitale e $*$-preservante (da $\pi_\omega(A^*)=\pi_\omega(A)^*$), dunque un carattere.
*Bozza (←)*: sia $\omega$ un carattere. Si pone $\mathscr I_\omega=\{A:\omega(BA)=0\ \forall B\}$; per moltiplicatività $\omega(BA)=\omega(B)\omega(A)$, quindi $\mathscr I_\omega=\{A:\omega(A)=0\}=\ker\omega$ (nel caso di un carattere questo coincide anche con il nucleo $\mathscr N_\omega=\{A:\omega(A^*A)=0\}$ usato nella costruzione GNS, perché $\omega(A^*A)=\overline{\omega(A)}\omega(A)=|\omega(A)|^2=0\iff\omega(A)=0$). Poiché $A-\omega(A)\mathbf1\in\mathscr I_\omega=\mathscr N_\omega$ per ogni $A$ (verifica immediata: $\omega(A-\omega(A)\mathbf1)=\omega(A)-\omega(A)=0$), nel quoziente $\mathscr A/\mathscr N_\omega$ si ha $\widetilde A-\omega(A)\xi_\omega=0$, cioè $\widetilde A=\omega(A)\xi_\omega$ per ogni $A\in\mathscr A$. Quindi $\mathcal H_\omega=\overline{\{\widetilde A:A\in\mathscr A\}}=\mathbb C\xi_\omega$ è unidimensionale; su uno spazio 1-dimensionale ogni rappresentazione è automaticamente irriducibile (non esistono sottospazi chiusi non banali), quindi $\pi_\omega$ è irriducibile e, per Segal, $\omega$ è puro.

**Lemma (4.4.3)** — $\mathscr A$ commutativa $\Rightarrow \Delta_\omega(A)=0\ \forall\,\omega\in\mathfrak P(\mathscr A),\ \forall A$.
*Bozza*: immediata da 4.4.2: $\omega$ puro $\Rightarrow$ carattere $\Rightarrow \Delta_\omega(A)^2=\omega(A^2)-\omega(A)^2=\omega(A)^2-\omega(A)^2=0$ (moltiplicatività applicata a $A\cdot A$).

**Proposizione (4.4.1) + Corollario (4.4.1)** — viceversa: se $\Delta_\omega(A)=0$ per ogni $A\in\mathscr O$ (autoaggiunti) e ogni $\omega\in\mathfrak P(\mathscr A)$, allora $\mathscr A$ è commutativa. Combinata con 4.4.3, dà l'equivalenza: **$\mathscr A$ commutativa $\iff \Delta_\omega(A)=0$ per ogni $A$ e ogni stato puro $\omega$**.
*Bozza*: fissati $A\in\mathscr O$ e $\omega\in\mathfrak P(\mathscr A)$, l'ipotesi dà $\omega(A^2)=\omega(A)^2$. Nella terna GNS (irriducibile, per Segal) si ha $\omega(A^2)=(\xi_\omega,\pi_\omega(A)^2\xi_\omega)=\|\pi_\omega(A)\xi_\omega\|^2$ (usando che $\pi_\omega(A)$ è autoaggiunto, essendo $A$ autoaggiunto) e $\omega(A)=(\xi_\omega,\pi_\omega(A)\xi_\omega)$. Uguagliando, $\|\pi_\omega(A)\xi_\omega\|^2=(\xi_\omega,\pi_\omega(A)\xi_\omega)^2$: questo è precisamente il caso di uguaglianza nella disuguaglianza di Cauchy-Schwarz $|(\xi_\omega,y)|\le\|\xi_\omega\|\|y\|$ (con $y=\pi_\omega(A)\xi_\omega$, $\|\xi_\omega\|=1$), che vale se e solo se $y$ è multiplo scalare di $\xi_\omega$; prendendo il prodotto scalare con $\xi_\omega$ si fissa la costante, ottenendo $\pi_\omega(A)\xi_\omega=\omega(A)\xi_\omega$. Ogni $S\in\mathscr A$ si scrive $S=S_1+iS_2$ con $S_1=\frac{S+S^*}2,\ S_2=\frac{S-S^*}{2i}$ autoaggiunti (quindi in $\mathscr O$), perciò $\pi_\omega(S)\xi_\omega=(\omega(S_1)+i\omega(S_2))\xi_\omega\in\mathbb C\xi_\omega$ per ogni $S$; per ciclicità di $\xi_\omega$, $\mathcal H_\omega=\overline{\{\pi_\omega(S)\xi_\omega:S\in\mathscr A\}}=\mathbb C\xi_\omega$. Quindi $\pi_\omega(S)=\lambda_S\mathbf1$ per ogni $S$ (opportuno scalare), e in particolare $[\pi_\omega(S),\pi_\omega(T)]=0$, cioè $\pi_\omega([S,T])=0$, per ogni $S,T\in\mathscr A$. Presi $A,B\in\mathscr O$ si ottiene $\omega([A,B])=(\xi_\omega,\pi_\omega([A,B])\xi_\omega)=0$ per **ogni** $\omega\in\mathfrak P(\mathscr A)$ (il ragionamento vale per ogni stato puro, non solo per quello fissato all'inizio). Poiché ogni stato è combinazione convessa di stati puri, per Lemma 4.2.1 $\|[A,B]\|=\sup_{\omega\in\mathfrak S(\mathscr A)}|\omega([A,B])|=\sup_{\omega\in\mathfrak P(\mathscr A)}|\omega([A,B])|=0$, quindi $[A,B]=0$.
*(Nota: qui NON si usa "isometricità di $\pi_\omega$" per concludere $[A,B]=0$ — passaggio che sarebbe ingiustificato, dato che $\pi_\omega$ è iniettivo/isometrico solo se $\omega$ è uno stato fedele, cosa non garantita in generale. Il punto cruciale è quantificare su **tutti** gli stati puri e usare la separazione via Lemma 4.2.1, non la singola rappresentazione GNS.)*

**Proposizione (principio di indeterminazione generalizzato)** — $\Delta_\omega(A)\Delta_\omega(B)\ge\frac12|\omega([A,B])|$. (Analogo astratto di Heisenberg; solo enunciato per l'orale, tecnica standard: Cauchy-Schwarz sulla forma indotta da $\omega$ applicata a $A-\omega(A)\mathbf1$ e $B-\omega(B)\mathbf1$.)

**Proposizione (caratterizzazione della commutatività via $\dim\mathcal H_\omega$)** — commutativa $\iff\dim\mathcal H_\omega=1\ \forall\omega\in\mathfrak P(\mathscr A)$. (conseguenza diretta di 4.4.2 + Prop. 4.4.1).

**Corollario (4.4.2) + Teorema di caratterizzazione dei sistemi quantistici** — non commutatività $\iff$ esistono sovrapposizioni quantistiche di stati puri (dimensione $>1$ delle rappresentazioni pure). Da tenere come sintesi concettuale finale.

**Proposizione (4.5.1)** — Le CCR $[q,p]=i\mathbf1$ non si realizzano con operatori limitati.
*Bozza*: si mostra per induzione $[q,p^n]=inp^{n-1}$: base $n=1$ è l'ipotesi; passo induttivo $[q,p^{n+1}]=[q,p^n]p+p^n[q,p]=inp^{n-1}\cdot p+p^n\cdot i\mathbf1=i(n+1)p^n$. Passando alle norme e usando $\|[X,Y]\|\le2\|X\|\|Y\|$: $2\|q\|\|p\|^n\ge\|qp^n-p^nq\|=\|[q,p^n]\|=n\|p^{n-1}\|$. Se $p\ne0$ (altrimenti $[q,p]=0\ne i\mathbf1$, assurdo subito) allora $\|p^{n-1}\|\ne0$ per ogni $n$ (altrimenti $p$ sarebbe nilpotente, ma $[q,p]=i\mathbf1$ impedisce $p$ nilpotente: se $p^k=0$ per il minimo $k$, si avrebbe una contraddizione simile), quindi si può dividere: $\|q\|\|p\|\ge \frac n2\cdot\frac{\|p^{n-1}\|}{\|p\|^{n-1}}$. In particolare, usando semplicemente $\|p^{n-1}\|\ge1$ quando non nullo (o più precisamente iterando la stima), si ottiene $\|q\|\|p\|\ge n/2$ per ogni $n\in\mathbb N$: assurdo, perché il membro sinistro è una costante fissata mentre il destro diverge.

**Proposizione (4.5.2)** — Rappresentazione di Weyl delle CCR: esiste la rappresentazione di Schrödinger su $L^2(\mathbb R)$.
*Bozza*: si "esponenziano" $q,p$ in $U(\alpha)=e^{i\alpha q}, V(\beta)=e^{i\beta p}$ (ora limitati/unitari); si deriva la relazione di Weyl $U(\alpha)V(\beta)=e^{-i\alpha\beta}V(\beta)U(\alpha)$ mostrando che $Z(t)=U(\alpha t)V(\beta t)e^{-it(\alpha q+\beta p)}$ risolve un'ODE lineare del prim'ordine con soluzione esponenziale gaussiana in $t$. Sullo spazio di Schrödinger si pongono esplicitamente $(U(\alpha)\psi)(t)=e^{i\alpha t}\psi(t)$ (moltiplicazione) e $(V(\beta)\psi)(t)=\psi(t+\beta)$ (traslazione), e si verifica direttamente la relazione di Weyl per calcolo diretto.

**Teorema di unicità di Stone-von Neumann**. **★★ Pilastro finale del corso**
*Bozza*: **Regolarità** di $\pi_S$: si deve mostrare che $\alpha\mapsto U(\alpha)\psi$ e $\beta\mapsto V(\beta)\psi$ sono continue (in norma $L^2$) per ogni $\psi$. Per $U$: $\|U(\alpha)\psi-\psi\|^2=\int|e^{i\alpha t}-1|^2|\psi(t)|^2dt$; l'integrando è dominato da $4|\psi(t)|^2\in L^1$ e tende puntualmente a $0$ per $\alpha\to0$, quindi per **convergenza dominata di Lebesgue** l'integrale tende a $0$. Per $V$ (traslazione) si usa che $V=\mathcal F\circ U'\circ\mathcal F^{-1}$ per un'opportuna moltiplicazione $U'$ nello spazio di Fourier (traslare in posizione equivale a moltiplicare per una fase in momento), riconducendosi allo stesso argomento.
**Irriducibilità**: sia $K\subset L^2(\mathbb R)$ chiuso, invariante per $U(\alpha),V(\beta)$ per ogni $\alpha,\beta$, $K\ne\{0\},L^2$; presi $\psi\in K,\ \phi\in K^\perp$ non nulli, l'invarianza dà $(\phi,U(\alpha)V(\beta)\psi)=0$ per ogni $\alpha,\beta\in\mathbb R$. Fissato $\beta$, la funzione $\alpha\mapsto(\phi,U(\alpha)(V(\beta)\psi))=\int e^{i\alpha t}\overline{\phi(t)}\psi(t+\beta)dt$ è la trasformata di Fourier di $\overline\phi(t)\psi(t+\beta)$, identicamente nulla per ogni $\alpha$: per iniettività della trasformata di Fourier, $\overline\phi(t)\psi(t+\beta)=0$ q.o. $t$, per ogni $\beta$. Questo significa che i supporti di $\phi$ e delle traslate $\psi(\cdot+\beta)$ sono essenzialmente disgiunti per ogni $\beta$; facendo variare $\beta$ su tutto $\mathbb R$ questo forza $\phi=0$ q.o. (a meno che $\psi$ non sia già nulla), contraddicendo $\phi\ne0$.
**Unicità** (idea, dettagli omessi nel testo): data una qualunque rappresentazione regolare irriducibile $(\mathcal H,U,V)$ delle CCR in forma di Weyl, si usa la regolarità per "derivare" generatori autoaggiunti $q,p$ (teorema di Stone sui gruppi a un parametro unitari), si costruisce un vettore ciclico e, sfruttando l'algebra di Weyl generata da $U(\alpha),V(\beta)$ insieme a GNS e Schur (l'irriducibilità garantisce che lo stato vettoriale associato sia puro, quindi "rigido"), si esibisce un operatore unitario che intreccia questa rappresentazione con quella di Schrödinger — la stessa strategia con cui si dimostra l'unicità della terna GNS.

---

## 4. Appendice — disuguaglianze (solo enunciato, per completezza)
- Disuguaglianza di Young generalizzata (A.1.1/A.1.2)
- Disuguaglianza di Hölder
- Disuguaglianza di Minkowski
- Disuguaglianza di Bernoulli
- Teorema di Stone-Weierstrass (cruciale come strumento, usato ripetutamente nel calcolo funzionale continuo e in Gelfand)

---

## I collegamenti logici da saper ricostruire a voce

```
Hahn-Banach (Lemma 2.1.1 + Zorn)
        │
        ▼
Lemma 4.2.1 (‖A‖ = sup_ω |ω(A)|)  ──►  Corollario 4.2.1 (esistenza stati separanti)
        │
        ▼
Teorema GNS (ogni stato è vettoriale)
        │
        ├──► Teorema di Schur (irriducibilità ⟺ commutante banale)
        │             │
        │             ▼
        └──► Teorema di Segal (stato puro ⟺ π_ω irriducibile)
                      │
                      ▼
        Lemma 4.4.2 (algebra commutativa: puro ⟺ carattere)
                      │
                      ▼
   Prop. 4.4.1 / Cor. 4.4.1 (commutatività ⟺ Δ_ω(A)=0 ovunque)
                      │
                      ▼
     Caratterizzazione dei sistemi quantistici (non commutatività ⟺ sovrapposizioni)
```

In parallelo: **Calcolo funzionale continuo** → **Teorema di Gelfand** (algebre commutative ≅ $C(X)$) → **Lemma di permanenza spettrale**, usati come strumenti trasversali in quasi tutte le dimostrazioni sopra (specialmente nel Teorema di Schur, via risoluzione spettrale).

Infine, **CCR + forma di Weyl + Stone-von Neumann** chiudono il corso come applicazione fisica di tutto l'apparato: mostrano che la meccanica quantistica su $L^2(\mathbb R)$ è l'*unica* possibilità compatibile con le relazioni di commutazione canoniche, una volta imposta la regolarità.

**Consiglio per l'orale**: prepara la dimostrazione completa dei tre "pilastri" (Gelfand nel caso $C^*(\mathbf1,A)$, GNS, Stone-von Neumann) e la catena Hahn-Banach→GNS→Schur→Segal→caratteri, perché è lì che si concentrano quasi tutte le domande di collegamento tra risultati diversi.

---

## ⚠️ Attenzione — un punto ancora da verificare

Nel file aggiornato, l'**Esercizio 1** subito dopo il *Teorema di caratterizzazione dei sistemi quantistici* (*"$\dim\mathcal H_\omega=1\iff\mathscr A=\mathbb C\mathbf1$"*, direzione $\to$) usa ancora il passaggio *"per isometricità di $\pi_\omega$"* per concludere $A=\lambda_A\mathbf1$ da $\|\pi_\omega(A-\lambda_A\mathbf1)\|=0$ — lo stesso tipo di passaggio che abbiamo corretto altrove, e che richiede $\pi_\omega$ iniettivo (cioè $\omega$ stato **fedele**), ipotesi qui non presente. Ho anche un controesempio concettuale: su $\mathscr A=\mathbb C\oplus M_2(\mathbb C)$, lo stato-carattere $\omega(a,B)=a$ ha $\dim\mathcal H_\omega=1$ (il suo GNS collassa sulla componente $\mathbb C$), ma ovviamente $\mathscr A\ne\mathbb C\mathbf1$. Se capita di doverlo esporre, meglio saltarlo o segnalarlo — non è centrale come gli altri risultati, ma se il professore insiste su quel passaggio specifico è bene sapere che è lo stesso tipo di lacuna già discussa per il Lemma 4.4.2 e (nella versione precedente) per la Proposizione 4.4.1.

**In bocca al lupo per domani!**

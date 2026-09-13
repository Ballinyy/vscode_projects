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
*Bozza (caso reale)*: dato $x\notin U$, si estende $\varphi$ a $U+\mathbb R x$ scegliendo $\alpha=\widetilde\varphi(x)$ in un intervallo non vuoto determinato dalla subadditività di $m$: $\sup_y(\varphi(y)-m(y-x)) \le \inf_z(m(z+x)-\varphi(z))$, disuguaglianza che segue da $m(z+x)+m(y-x)\ge m(y+z)\ge\varphi(y+z)$. Poi si applica il **lemma di Zorn** all'insieme delle estensioni parziali ordinato per inclusione (ogni catena ha maggiorante = unione), ottenendo un elemento massimale che deve essere definito su tutto $V$.
*Caso complesso*: si estende $\mathrm{Re}\,\varphi$ come funzionale reale con il caso reale, poi si ricostruisce $\widetilde\varphi(x)=\psi(x)-i\psi(ix)$, che è $\mathbb C$-lineare e ha la parte reale corretta; la dominanza da $m$ segue scegliendo una fase $\alpha$ con $|\alpha|=1$ tale che $\widetilde\varphi(\alpha x)\ge0$.

**Teorema di completamento degli spazi metrici**.
*Bozza*: si considera l'insieme $S$ di tutte le successioni di Cauchy in $X$, con la relazione di equivalenza $\{x_n\}\sim\{y_n\}$ se $d(x_n,y_n)\to0$; si pone $\overline X = S/\sim$. Si definisce $\overline d([\{x_n\}],[\{y_n\}]) = \lim_n d(x_n,y_n)$: il limite esiste perché $\{d(x_n,y_n)\}_n$ è di Cauchy in $\mathbb R$ (per la disuguaglianza quadrilatera $|d(x_n,y_n)-d(x_m,y_m)|\le d(x_n,x_m)+d(y_n,y_m)$), ed è ben definito indipendentemente dai rappresentanti (per disuguaglianza triangolare incrociata tra due scelte di rappresentanti). **Completezza di $\overline X$**: data una successione di Cauchy di classi $\{[\{x^m_n\}_n]\}_m$, si costruisce la successione "diagonale" $\{x^n_n\}_n$ (di Cauchy in $X$, per una stima a "doppia $\varepsilon$" che combina Cauchy-in-$m$ e Cauchy-in-$n$ dentro ogni classe) e si mostra che la sua classe è il limite cercato. **Densità dell'immersione**: si definisce $i(x)=[\{x\}_n]$ (successione costante), isometria; dato $w=[\{x_n\}_n]\in\overline X$, la successione costante $\{x_N\}_n$ approssima $w$ arbitrariamente bene per $N$ grande (Cauchy). **Unicità**: dato un altro completamento $(\widetilde X,\tilde d)$ con immersione $j$, si definisce $\phi$ su $i(X)$ come $\phi(i(x))=j(x)$ (isometria per costruzione) e si estende per continuità/densità a tutto $\overline X$, verificando che il limite non dipende dalla successione approssimante (sempre perché $j$ è un'isometria).

**Proposizione 2.2.1** — Cauchy + sottosuccessione convergente $\Rightarrow$ convergente. *Bozza*: disuguaglianza triangolare $d(x_n,x)\le d(x_n,x_{\nu(k)})+d(x_{\nu(k)},x)$, entrambi i termini piccoli per $n,k$ grandi.

**Proposizione 2.2.4 / Corollario 2.2.1** — $\mathbb R,\mathbb C,\mathbb R^n,\mathbb C^n$ Banach.
*Bozza*: ogni successione di Cauchy ha una sottosuccessione a variazione finita (si costruisce induttivamente $\nu(k)$ con incrementi $<2^{-k}$); una successione a variazione finita converge (telescopica + convergenza assoluta); si applica Prop. 2.2.1. In alternativa: Cauchy $\Rightarrow$ limitata $\Rightarrow$ (Bolzano-Weierstrass, per bisezione degli intervalli) ammette sottosuccessione convergente $\Rightarrow$ Prop. 2.2.1.

**Teorema di Riesz-Fischer** — $L^p(X,\mu)$ è completo.
*Bozza*: data $\{f_n\}$ di Cauchy in $L^p$, si estrae una sottosuccessione $\{f_{n_k}\}$ con $\|f_{n_{k+1}}-f_{n_k}\|_p<2^{-k}$ (possibile per definizione di Cauchy). Si pone $g_s=\sum_{k=1}^s|f_{n_{k+1}}-f_{n_k}|$ e $g=\lim_s g_s$ (esiste perché $g_s$ è crescente e positiva). Per la **disuguaglianza di Minkowski**, $\|g_s\|_p<1$ per ogni $s$; per il **lemma di Fatou** applicato a $g_s^p$, $\|g\|_p^p\le\liminf_s\|g_s\|_p^p<1$, quindi $g<\infty$ q.o., il che garantisce che la serie telescopica $f_{n_1}+\sum_k(f_{n_{k+1}}-f_{n_k})$ converge q.o. a una funzione $f$ (limite puntuale di $f_{n_k}$). Si mostra $f_{n_k}\to f$ in norma $L^p$ tramite **Fatou** su $|f_{n_k}-f_n|^p$, ottenendo $\|f-f_n\|_p\to0$; infine $f\in L^p$ per la disuguaglianza triangolare $\|f\|_p\le\|f-f_m\|_p+\|f_m\|_p<\infty$. Poiché una successione di Cauchy con una sottosuccessione convergente (in norma) è essa stessa convergente allo stesso limite, si conclude $f_n\to f$ in $L^p$.

**Disuguaglianza di Cauchy-Schwarz** in spazi pre-hilbertiani. *Bozza standard*: si studia $0\le(x-ty,x-ty)$ come polinomio reale di secondo grado in $t\in\mathbb R$ (dopo aver ruotato la fase di $y$ per rendere $(x,y)$ reale) e si impone discriminante $\le0$.

**Teorema della proiezione ortogonale**. **★ Fondamentale**
*Bozza*: dato $x\in\mathcal H$, si prende una successione minimizzante $v_n\in V$ con $\|x-v_n\|\to d(x,V)$; tramite l'**identità del parallelogramma** applicata a $x-v_n$ e $x-v_m$ si mostra che $\{v_n\}$ è di Cauchy, quindi converge (per completezza di $V$ chiuso) a $\overline x\in V$ che realizza la distanza minima; si mostra poi che $x-\overline x \perp V$ usando che per ogni $v\in V$ e $t\in\mathbb R$ la funzione $t\mapsto\|x-\overline x-tv\|^2$ ha minimo in $t=0$. Unicità dalla stretta convessità della norma hilbertiana.

**Teorema della rappresentazione di Riesz**. **★ Fondamentale**
*Bozza*: se $f=0$ banale. Altrimenti $\ker f$ è un sottospazio chiuso proprio; per la proiezione ortogonale esiste $z\perp\ker f$, $z\ne0$; si normalizza e si pone $\eta = \overline{f(z)}\,z/\|z\|^2$ (a meno di costanti); si verifica $f(x)=(\eta,x)$ scrivendo $x = x - \frac{f(x)}{f(z)}z + \frac{f(x)}{f(z)}z$ e notando che il primo termine sta in $\ker f$, quindi è ortogonale a $z$.

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

**Teorema (3.1.1)** — Esistenza e unicità dell'aggiunto. (Riesz applicato a $y\mapsto(y,Tx)$ per ogni $x$ fissato).

**Lemma (serie di Neumann)** — $\|S\|<1\Rightarrow(\mathbf 1-S)^{-1}=\sum_n S^n$.
*Bozza*: la serie converge in norma (dominata da $\sum\|S\|^n<\infty$, $\mathcal B(\mathcal H)$ Banach); si verifica per telescopia che $(\mathbf1-S)\sum_{n=0}^N S^n = \mathbf 1-S^{N+1}\to\mathbf1$.

**Teorema (3.3.1)** — Proprietà fondamentali dello spettro. **★ Fondamentale**
*Bozza per punto*:
1. $\lambda\in\sigma(T)\Rightarrow\lambda^*\in\sigma(T^*)$: si aggiunge $(\lambda\mathbf1-T)$.
2. $\lambda\in\sigma(T)$, $T$ invertibile $\Rightarrow\lambda^{-1}\in\sigma(T^{-1})$: si fattorizza $\lambda\mathbf1-T = -\lambda T(\lambda^{-1}\mathbf1-T^{-1})$.
3. $T$ normale $\Rightarrow r(T)=\|T\|$: dall'identità $C^*$ si ottiene $\|T^2\|=\|T\|^2$ e iterando $\|T^{2^n}\|=\|T\|^{2^n}$; si conclude con Gelfand/formula del raggio spettrale.
4. $V$ unitario $\Rightarrow\sigma(V)\subset\mathbf S^1$: da (2) e (3) si ha $\sigma(V),\sigma(V^{-1})\subset\overline{D_1(0)}$, quindi $|\lambda|\le1$ e $1/|\lambda|\le1$.
5. $A=A^*\Rightarrow\sigma(A)\subset\mathbb R$: si costruisce $e^{iA}$ unitario (serie esponenziale, $(e^{iA})^*=e^{-iA}$); per $\lambda\notin\mathbb R$, $e^{i\lambda}\notin\mathbf S^1$ quindi per (4) $(e^{i\lambda}\mathbf1-e^{iA})$ invertibile; si fattorizza per ottenere l'invertibilità di $(A-\lambda\mathbf1)$ tramite serie di Neumann.

**Teorema del calcolo funzionale continuo**. **★★ Uno dei pilastri del corso**
*Bozza*: si definisce $p(A)$ per polinomi; si mostra $\sigma(p(A))=p(\sigma(A))$ fattorizzando $p(\lambda)-p(x)$ sulle radici (teorema fondamentale dell'algebra); da qui, poiché $p(A)$ è normale, $\|p(A)\|=r(p(A))=\sup_{\lambda\in\sigma(A)}|p(\lambda)|=\|p\|_\infty$ (isometria sui polinomi). Per Stone-Weierstrass i polinomi sono densi in $C(\sigma(A))$ (spettro compatto), quindi si definisce $f(A):=\lim_n p_n(A)$ per $p_n\to f$ uniformemente; il limite non dipende dalla successione approssimante (per l'isometria) e tutte le proprietà (1)-(4) passano al limite per continuità. La positività (6) segue scrivendo $f=g^2$ con $g$ reale, così $(x,f(A)x)=\|g(A)x\|^2\ge0$.

**Corollario (3.3.3)** — $A\ge0\iff A=A^*$ e $\sigma(A)\subset[0,\infty)$.
*Bozza*: ($\to$) $(x,Ax)$ reale per ogni $x$ implica $A=A^*$ per identità di polarizzazione; per $\lambda<0$ si stima $\|(A-\lambda\mathbf1)x\|\ge|\lambda|\,\|x\|$ (operatore "lontano da zero"), quindi invertibile. ($\leftarrow$) per calcolo funzionale continuo esiste $\sqrt A =: B\ge0$ autoaggiunto, e $(x,Ax)=(Bx,Bx)\ge0$.

**Corollario (3.3.4)** — $A\ge0\iff A=B^*B$. (conseguenza immediata di 3.3.3 + $\sqrt A$).

**Lemma 3.3.5, 3.3.6, 3.3.7** — Disuguaglianze sugli operatori positivi. Idee: $A\le\|A\|\mathbf1$ da $(x,Ax)\le\|A\|\|x\|^2$; $0\le A\le B\Rightarrow\|A\|\le\|B\|$ da Cauchy-Schwarz sulla forma $(x,Ay)$ e Riesz; $\|Ax\|^2\le\|A\|(x,Ax)$ da $A=(\sqrt A)^2$ e Cauchy-Schwarz.

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
*Bozza (caso $\mathscr A=C^*(\mathbf1,A)$)*: si definisce $\omega_\lambda(f(A))=f(\lambda)$ per $\lambda\in\sigma(A)$, usando il calcolo funzionale continuo; si verifica che $\omega_\lambda$ è lineare, moltiplicativo, unitale, $*$-preservante (cioè un carattere), e che $\lambda\mapsto\omega_\lambda$ è biiettiva su $X$: iniettività dalla separazione dei punti di $C(\sigma(A))$; suriettività mostrando che ogni carattere $\omega$ soddisfa $\omega=\omega_{\omega(A)}$ (si verifica prima sui polinomi per moltiplicatività, poi si passa al limite usando che $|\omega(S)|\le\|S\|$, quindi $\omega$ è continuo). Compattezza/Hausdorff di $X$ dalla corrispondenza con $\sigma(A)$ (compatto) e dalla topologia $*$-debole. L'isomorfismo $\wedge$ è per costruzione l'inverso del calcolo funzionale ($\widehat{f(A)}=f$). *(Il caso generale si ottiene applicando questo argomento algebra per algebra generata da un singolo autoaggiunto e incollando.)*

**Lemma di permanenza spettrale** — sottoalgebra chiusa in norma: $\sigma(A)=\sigma_{\mathscr A}(A)$.
*Bozza*: $\sigma(A)\subset\sigma_{\mathscr A}(A)$ ovvio (meno inversi disponibili in sottoalgebra). Viceversa, per $\lambda\in\sigma(A)\subset\mathbb R$, si usa che $\lambda+i\varepsilon\in\rho(A)$ per ogni $\varepsilon>0$ (Teor. 3.3.1.5) e che l'inverso $(A-(\lambda+i\varepsilon)\mathbf1)^{-1}\in\mathscr A$ (chiusura in norma) converge per $\varepsilon\to0$ a $(A-\lambda\mathbf1)^{-1}\in\mathscr A$ per continuità dell'inversione.

**Proposizione (4.2.1)** — $*$-omomorfismo unitale è contrattivo, isometrico se iniettivo.
*Bozza*: (1) si mostra $\sigma_{\mathscr B}(\phi(AA^*))\subset\sigma_{\mathscr A}(AA^*)$ (se $\phi(AA^*)-\lambda\mathbf1$ non invertibile in $\mathscr B$ allora $AA^*-\lambda\mathbf 1$ non invertibile in $\mathscr A$, per contrapposizione preservando gli inversi tramite $\phi$); segue $\|\phi(A)\|\le\|A\|$ via identità $C^*$ e raggio spettrale. (2) Se $\phi$ iniettivo, si suppone per assurdo $\sigma_{\mathscr B}(\phi(AA^*))\subsetneq\sigma_{\mathscr A}(AA^*)$, si costruisce (Tietze) $f\ne0$ nulla sul primo spettro ma non sul secondo, si ottiene $f(\phi(AA^*))=0=\phi(f(AA^*))$, quindi $f(AA^*)=0$ per iniettività, assurdo per l'arbitrarietà di $A$.

**Proposizione (4.2.2)** — Ogni stato preserva lo $*$, $\|\omega\|=1$.
*Bozza*: $A=A_1+iA_2$ (parte "reale/immaginaria" autoaggiunte) $\Rightarrow\omega(A^*)=\overline{\omega(A)}$; con Cauchy-Schwarz sulla forma sesquilineare $\{A,B\}=\omega(A^*B)$ si ottiene $|\omega(B)|\le\omega(B^*B)^{1/2}\le\|B\|$ (usando $B^*B\le\|B^*B\|\mathbf1$); l'uguaglianza per $B=\mathbf1$ dà $\|\omega\|=1$.

**Teorema di Riesz-Markov** (solo enunciato — stati su $C(X)$ ↔ misure boreliane positive normalizzate).

**Teorema GNS (Gelfand-Naimark-Segal)**. **★★★ Il risultato più importante del corso**
*Bozza*: si definisce la forma sesquilineare $(A,B)\mapsto\omega(A^*B)$ su $\mathscr A$; si pone $\mathscr N_\omega=\{A:\omega(A^*A)=0\}$, sottospazio (per Cauchy-Schwarz sulla forma) e in realtà **ideale sinistro** ($\omega((BJ)^*(BJ))\le\|B\|^2\omega(J^*J)=0$); il prodotto scalare discende bene al quoziente $\mathscr A/\mathscr N_\omega$ (indipendenza dal rappresentante, sempre via Cauchy-Schwarz); si completa a spazio di Hilbert $\mathcal H_\omega$. Si definisce $\pi_\omega(B)\widetilde A=\widetilde{BA}$, ben posta perché $\mathscr N_\omega$ è ideale, limitata ($\|\pi_\omega(B)\widetilde A\|^2\le\|B\|^2\|\widetilde A\|^2$) e $*$-omomorfismo (per costruzione algebrica). Si pone $\xi_\omega=\widetilde{\mathbf1}$: allora $(\xi_\omega,\pi_\omega(B)\xi_\omega)=\omega(B)$ e $\xi_\omega$ è ciclico per densità di $\mathscr A/\mathscr N_\omega$. **Unicità**: data un'altra terna $(\mathcal H,\pi,\xi)$, si definisce $U_0(\pi_\omega(B)\xi_\omega)=\pi(B)\xi$, ben definito e isometrico (stesso prodotto scalare $\omega(B^*B)$ da entrambe le parti), si estende per densità/completamento a un unitario $U$ che intreccia le rappresentazioni ($U\pi_\omega(A)=\pi(A)U$).

**Lemma (4.2.1)** — $\|A\|=\sup_{\omega\in\mathfrak S(\mathscr A)}|\omega(A)|$ per $A=A^*$.
*Bozza*: si costruisce $g$ su $E=\mathrm{span}\{\mathbf1,A\}$ ponendo $g(\lambda\mathbf1+\mu A)=\lambda+\mu\|A\|$ (o con segno opposto a seconda di dove sta $\pm\|A\|$ nello spettro), dominato dalla norma perché $\|A\|=\max_{\sigma(A)}|t|$; si estende con **Hahn-Banach** a $f$ su $\mathscr A$ dominato da $\|\cdot\|$; si mostra che $f$ è automaticamente unitale ($\|f\|=f(\mathbf1)=1$) e **positivo** (usando la stima $\|\mathbf1+itB\|^2=1+O(t^2)$ contro $|1+itf(B)|^2=1+O(t)$ per dedurre $f(B)\in\mathbb R$, poi $|f(\mathbf1-tB)|\le1$ per $B\ge0$ piccolo dà $f(B)\ge0$). Quindi $f\in\mathfrak S(\mathscr A)$ e $f(A)=\|A\|$.

**Corollario (4.2.1)** — Per $A=A^*\ne0$ esiste stato $\omega$ con $\omega(A)\ne0$. (immediato da Lemma 4.2.1, dato che $\|A\|>0$).

**Teorema di Schur**. **★★ Pilastro (con GNS e Gelfand)**
*Bozza*: (1→2) basta lavorare su $B$ autoaggiunto nel commutante; per calcolo funzionale continuo la risoluzione spettrale $\{P_\lambda^B\}$ commuta anch'essa con $\pi(\mathscr A)$, quindi ogni $P_\lambda^B\mathcal H_\pi$ è $\pi$-invariante, quindi banale per irriducibilità; questo forza $B=\mu\mathbf1$. (2→1) dato $K$ chiuso invariante, il proiettore $P_K$ commuta con $\pi(\mathscr A)$ (si mostra separatamente su $K$ e $K^\perp$, usando che $\pi$ preserva lo $*$ per mostrare che anche $K^\perp$ è invariante), quindi $P_K\in\mathbb C\mathbf1$, quindi $K=\{0\}$ o $\mathcal H_\pi$. (1↔3) equivalenza diretta con la definizione di ciclicità/invarianza.

**Teorema di Segal** — $\omega$ puro $\iff\pi_\omega$ irriducibile. (dimostrazione omessa nel testo — tienila a mente come collegamento concettuale chiave tra convessità di $\mathfrak S(\mathscr A)$ e Teorema di Schur).

**Lemma (4.4.1)** — $\sigma_{fis}(A)=\sigma_{\mathscr A}(A)$ per osservabili fisiche. *Bozza*: si usa l'estensione (alla Hahn-Banach) di un carattere $\omega_\lambda$ definito sulla sottoalgebra $C^*(\mathbf 1,A)$ a uno stato $\omega$ su tutta $\mathscr A$; la positività dell'estensione segue dal criterio $\varphi(\mathbf1)=\|\varphi\|\Rightarrow\varphi\ge0$ (si veda l'analisi dettagliata già discussa).

**Lemma (4.4.2)** — $\mathscr A$ commutativa: $\omega$ puro $\iff$ carattere.
*Bozza (→)*: GNS + Schur/Segal danno $\pi_\omega(A)=\omega(A)\mathbf1$ (perché il commutante è banale e, essendo $\mathscr A$ commutativa, $\pi_\omega(\mathscr A)\subset\pi_\omega(\mathscr A)'$), da cui $\omega(AB)=\omega(A)\omega(B)$.
*Bozza (←)*: usando che $A-\omega(A)\mathbf1\in\mathscr N_\omega=\{A:\omega(A^*A)=0\}$ (si verifica con moltiplicatività + $*$-preservazione del carattere), si ottiene $\widetilde A=\omega(A)\xi_\omega$ per ogni $A$, quindi $\mathcal H_\omega=\mathbb C\xi_\omega$ è unidimensionale, quindi $\pi_\omega$ automaticamente irriducibile, quindi $\omega$ puro per Segal.

**Lemma (4.4.3) + Proposizione (4.4.1) + Corollario (4.4.1)** — commutatività $\iff \Delta_\omega(A)=0\ \forall A,\omega$ puro.
*Bozza (4.4.3)*: immediata da 4.4.2, $\Delta_\omega(A)=\omega(A^2)-\omega(A)^2=\omega(A)^2-\omega(A)^2=0$.
*Bozza (4.4.1, viceversa)*: da $\omega(A^2)=\omega(A)^2$ e GNS si ottiene $\|\pi_\omega(A)\xi_\omega\|^2=(\xi_\omega,\pi_\omega(A)\xi_\omega)^2$, cioè uguaglianza nel caso limite di Cauchy-Schwarz, quindi $\pi_\omega(A)\xi_\omega=\omega(A)\xi_\omega$; per ciclicità di $\xi_\omega$ e scomponendo ogni operatore in parte reale/immaginaria autoaggiunta, si ottiene $\mathcal H_\omega=\mathbb C\xi_\omega$ per ogni stato puro, quindi $\pi_\omega(S)$ scalare per ogni $S$; per isometricità di $\pi_\omega$ i commutatori $[S,T]$ si annullano in $\mathscr A$.

**Proposizione (principio di indeterminazione generalizzato)** — $\Delta_\omega(A)\Delta_\omega(B)\ge\frac12|\omega([A,B])|$. (Analogo astratto di Heisenberg; solo enunciato per l'orale, tecnica standard: Cauchy-Schwarz sulla forma indotta da $\omega$ applicata a $A-\omega(A)\mathbf1$ e $B-\omega(B)\mathbf1$.)

**Proposizione (caratterizzazione della commutatività via $\dim\mathcal H_\omega$)** — commutativa $\iff\dim\mathcal H_\omega=1\ \forall\omega\in\mathfrak P(\mathscr A)$. (conseguenza diretta di 4.4.2 + Prop. 4.4.1).

**Corollario (4.4.2) + Teorema di caratterizzazione dei sistemi quantistici** — non commutatività $\iff$ esistono sovrapposizioni quantistiche di stati puri (dimensione $>1$ delle rappresentazioni pure). Da tenere come sintesi concettuale finale.

**Proposizione (4.5.1)** — Le CCR $[q,p]=i\mathbf1$ non si realizzano con operatori limitati.
*Bozza*: per induzione $[q,p^n]=inp^{n-1}$; passando alle norme, $2\|q\|\|p\|^n\ge\|qp^n-p^nq\|=n\|p^{n-1}\|$; se $\|p^{n-1}\|\ne0$ per ogni $n$ si ottiene $\|q\|\|p\|\ge n/2$ per ogni $n$, assurdo per operatori limitati.

**Proposizione (4.5.2)** — Rappresentazione di Weyl delle CCR: esiste la rappresentazione di Schrödinger su $L^2(\mathbb R)$.
*Bozza*: si "esponenziano" $q,p$ in $U(\alpha)=e^{i\alpha q}, V(\beta)=e^{i\beta p}$ (ora limitati/unitari); si deriva la relazione di Weyl $U(\alpha)V(\beta)=e^{-i\alpha\beta}V(\beta)U(\alpha)$ mostrando che $Z(t)=U(\alpha t)V(\beta t)e^{-it(\alpha q+\beta p)}$ risolve un'ODE lineare del prim'ordine con soluzione esponenziale gaussiana in $t$. Sullo spazio di Schrödinger si pongono esplicitamente $(U(\alpha)\psi)(t)=e^{i\alpha t}\psi(t)$ (moltiplicazione) e $(V(\beta)\psi)(t)=\psi(t+\beta)$ (traslazione), e si verifica direttamente la relazione di Weyl per calcolo diretto.

**Teorema di unicità di Stone-von Neumann**. **★★ Pilastro finale del corso**
*Bozza*: si mostra che $\pi_S$ è **regolare** (continuità S.O.T. di $U(\alpha),V(\beta)$ in $\alpha,\beta$, usando **convergenza dominata di Lebesgue** per $U$ e la trasformata di Fourier $V=F\circ U\circ F^{-1}$ per $V$) ed **irriducibile** (dato $K$ invariante non banale, si prendono $\psi\in K,\phi\in K^\perp$; l'ortogonalità $(\phi,U(\alpha)V(\beta)\psi)=0$ per ogni $\alpha,\beta$ implica, tramite trasformata di Fourier, che i supporti di $\phi$ e delle traslate di $\psi$ si intersecano in insiemi di misura nulla per ogni traslazione, il che forza $\phi=0$ q.o., assurdo). L'unicità (a meno di equivalenza unitaria) è la parte più delicata (nel testo omessa in dettaglio): l'idea è costruire, a partire da una qualunque rappresentazione regolare irriducibile, un vettore ciclico e ricondursi, tramite l'algebra di Weyl generata, a un isomorfismo con lo spazio di Schrödinger, sfruttando ancora GNS e Schur.

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

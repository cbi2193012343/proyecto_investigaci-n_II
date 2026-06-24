# Proposiciones nuevas — ProyectoII

Notación heredada de ProyectoI y ProyectoII:
$\mathcal{K}_\varepsilon = \{K \in \mathcal{S}_n : K_{ij} \geq \varepsilon > 0\}$,
$\mathcal{U}_R = \{v \in \mathbb{R}^n : \|v\|_\infty \leq R\}$,
$B_L(X)_i = X_i L_i / \langle X, L\rangle$,
$\mathcal{D}_{K,L}(X) = B_L(XK) - B_L(X)K$,
$J(X;K,L) = D_{\mathrm{KL}}(P \| B_L(XK))$,
$J(X;L,K) = D_{\mathrm{KL}}(P \| B_L(X)K)$.

---

## Sección 0 — Preliminares

### Observación 0.1 — Justificación topológica de la dirección de $D_{\mathrm{KL}}$ en el costo terminal

El funcional de costo del Problema 2 utiliza $D_{\mathrm{KL}}(P \| X_T)$ como término terminal, no $D_{\mathrm{KL}}(X_T \| P)$.

La elección no es de conveniencia sino topológica. Si el controlador aplica $B_L$ de manera reiterada, el estado $X_t$ puede colapsar hacia la cara de máxima verosimilitud de $\partial\Delta_n$: existe $j$ tal que $X_t(j) \to 0$. Si $P(j) > 0$, entonces

$$D_{\mathrm{KL}}(P \| X_T) = \sum_i P_i \log \frac{P_i}{X_T(i)} \to +\infty.$$

La dirección inversa, $D_{\mathrm{KL}}(X_T \| P) = \sum_i X_T(i) \log \frac{X_T(i)}{P(i)}$, permanece acotada incluso cuando $X_T(j) \to 0$ (pues $X_T(j) \log X_T(j) \to 0$), y por tanto no penaliza el colapso de soporte.

La elección $D_{\mathrm{KL}}(P \| X_T)$ garantiza que el controlador no puede ignorar ningún índice que tenga masa positiva en el objetivo $P$, obligándolo a usar $L_K$ para reintroducir masa cuando sea necesario.

---

## Sección 1 — Problema 1: Alcanzabilidad restringida

### Lema 1.0a — Bound de desplazamiento markoviano

**Hipótesis.**
Sea $K \in \mathcal{K}_\varepsilon$, es decir, $K \in \mathcal{S}_n$ con $K_{ij} \geq \varepsilon > 0$ para todo $i, j$.
Sea $X \in \Delta_n$.

**Consecuencia.**
$$\| L_K(X) - X \|_1 \leq 2(1 - \varepsilon).$$

La cota es uniforme en $X$ y en la elección específica de $K \in \mathcal{K}_\varepsilon$.

*Rol en la cadena:* Reemplaza el bound incorrecto $2(1-n\varepsilon)$ del esbozo actual de Prop 1.1. Junto con Lema 1.0b, establece la cota de desplazamiento total por paso que hace no trivial la inalcanzabilidad.

---

### Lema 1.0b — Bound de desplazamiento bayesiano

**Hipótesis.**
Sea $L \in \mathbb{R}_{>0}^n$ con $\log L \in \mathcal{U}_R$, es decir, $e^{-R} \leq L_i \leq e^R$ para todo $i$.
Sea $X \in \Delta_n^\circ$.

**Consecuencia.**
$$\| B_L(X) - X \|_1 \leq e^{2R} - 1.$$

La cota depende únicamente de $R$, no de $X$ ni de la elección específica de $L$.

*Rol en la cadena:* Proporciona la constante $C(R) = e^{2R}-1$ que el esbozo actual de Prop 1.1 deja sin computar.

---

### Proposición 1.1 (corregida) — Inalcanzabilidad en tiempo finito

**Hipótesis.**
Sean $\varepsilon > 0$ y $R > 0$ los parámetros de las restricciones $(\mathcal{K}_\varepsilon, \mathcal{U}_R)$.
Sea $X_0 \in \Delta_n^\circ$.
Sea $t \geq 1$ un horizonte finito.

**Consecuencia.**
Para todo $P \in \Delta_n^\circ$ que satisfaga

$$\| P - X_0 \|_1 > t \cdot \max\!\bigl(2(1-\varepsilon),\; e^{2R}-1\bigr),$$

se tiene $P \notin \mathcal{R}_t(X_0)$.

En particular, el conjunto $\mathcal{R}_t(X_0)$ está contenido en la bola $L^1$ de radio $t \cdot \max(2(1-\varepsilon), e^{2R}-1)$ centrada en $X_0$, de modo que existen siempre puntos de $\Delta_n^\circ$ inalcanzables en $t$ pasos.

*Rol en la cadena:* Es la proposición que justifica la no trivialidad del problema de control restringido. La versión anterior usaba el bound incorrecto $2(1-n\varepsilon)$; esta versión usa los Lemas 1.0a y 1.0b.

---

## Sección 2 — Problema 2: Control óptimo informacional

### Definición 2.4 — Variable de ordenamiento

En cada paso $t$, el controlador elige una acción compuesta

$$u_t = (K_t,\, L_t,\, \sigma_t)$$

donde $K_t \in \mathcal{K}_\varepsilon$, $\log L_t \in \mathcal{U}_R$, y $\sigma_t \in \{MB, BM\}$ es la **variable de ordenamiento**.

La dinámica resultante es:

$$X_{t+1} = \begin{cases} B_{L_t}(X_t K_t) & \text{si } \sigma_t = MB, \\ B_{L_t}(X_t)\, K_t & \text{si } \sigma_t = BM. \end{cases}$$

El espacio de acciones se extiende de $\{M, B\}$ (Def 2.1 actual) a $\mathcal{K}_\varepsilon \times \mathcal{U}_R \times \{MB, BM\}$, haciendo el orden una decisión explícita del controlador.

*Rol en la cadena:* Hace precisa la pregunta del Problema 3: el defecto $\mathcal{D}_{K,L}(X)$ mide exactamente la diferencia entre los dos estados producidos por $\sigma=MB$ y $\sigma=BM$ para la misma acción $(K,L)$.

---

### Definición 2.5 — Costos secuenciales ordenados

Para $X \in \Delta_n^\circ$, $K \in \mathcal{K}_\varepsilon$, $\log L \in \mathcal{U}_R$, se definen los **costos de un paso compuesto** según el orden elegido:

$$c_{MB}(X; K, L) := c_M(K, X) + c_B(L, XK) = D_{\mathrm{KL}}(XK \| X) + D_{\mathrm{KL}}(B_L(XK) \| XK),$$

$$c_{BM}(X; K, L) := c_B(L, X) + c_M(K, B_L(X)) = D_{\mathrm{KL}}(B_L(X) \| X) + D_{\mathrm{KL}}(B_L(X)K \| B_L(X)).$$

Ambos costos son no negativos y se anulan simultáneamente si y solo si $K = I$ y $L \equiv \mathrm{const}$.

*Rol en la cadena:* Reemplaza la Def 1.2 actual que solo define costos de un operador individual. Los costos $c_{MB}$ y $c_{BM}$ son distintos porque el estado base de la segunda operación depende del orden, y su diferencia contribuye a $|Q_\tau^{MB} - Q_\tau^{BM}|$.

---

### Definición 2.6 — Q-funciones por orden

Para $\tau \geq 1$, $X \in \Delta_n^\circ$, $K \in \mathcal{K}_\varepsilon$, $\log L \in \mathcal{U}_R$, se definen las **funciones de acción-valor** acopladas al ordenamiento:

$$Q_\tau^{MB}(X; K, L) := c_{MB}(X; K, L) + V_{\tau-1}(B_L(XK)),$$

$$Q_\tau^{BM}(X; K, L) := c_{BM}(X; K, L) + V_{\tau-1}(B_L(X)K),$$

donde $V_\tau$ es la función de valor óptimo de la Def 2.3 y $V_0(X) = D_{\mathrm{KL}}(P\|X)$.

La diferencia $Q_\tau^{MB}(X;K,L) - Q_\tau^{BM}(X;K,L)$ mide el costo de elegir el orden incorrecto cuando el controlador dispone de $\tau$ pasos. El objeto central de la Conjetura 3.3' es acotar esta diferencia en función de $\|\mathcal{D}_{K,L}(X)\|_1$.

*Rol en la cadena:* Las Q-funciones son la formulación correcta de la pregunta de ordenamiento en el marco de programación dinámica. Son las que aparecen en la Conjetura 3.3'.

---

### Proposición 2.2 — Continuidad local de la función de valor

**Hipótesis.**
Sea $P \in \Delta_n^\circ$ el objetivo fijo.
Sean $\lambda > 0$, $\varepsilon > 0$, $R > 0$ los parámetros del problema.
Sea $\tau \geq 0$.
Sea $\mathcal{C} \subset \Delta_n^\circ$ un subconjunto compacto.
Denótese $m(\mathcal{C}) := \min_{X \in \mathcal{C}} \min_i X_i > 0$.

**Consecuencia.**
La función de valor $V_\tau : \Delta_n^\circ \to [0, +\infty)$ es continua en $\Delta_n^\circ$. Más aún, existe una constante $L_\tau(\mathcal{C}) > 0$ tal que para todo $X, Y \in \mathcal{C}$:

$$| V_\tau(X) - V_\tau(Y) | \leq L_\tau(\mathcal{C})\, \| X - Y \|_1.$$

La constante satisface la recurrencia $L_0(\mathcal{C}) \leq 1/m(\mathcal{C})$ para el caso base, y $L_\tau(\mathcal{C})$ crece en $\tau$ a través de la composición de los operadores de la ecuación de Bellman.

*Rol en la cadena:* Es el ingrediente que permite controlar el término $|V_{\tau-1}(B_L(XK)) - V_{\tau-1}(B_L(X)K)|$ en la diferencia $Q_\tau^{MB} - Q_\tau^{BM}$, usando que los dos argumentos difieren exactamente en $\mathcal{D}_{K,L}(X)$.

---

## Sección 3 — Problema 3: Defecto de ordenamiento

### Lema 3.0 — Fórmula explícita del defecto $\mathcal{D}_{K,L}(X)$

**Hipótesis.**
Sean $K \in \mathcal{K}_\varepsilon$, $L \in \mathbb{R}_{>0}^n$ con $\log L \in \mathcal{U}_R$, y $X \in \Delta_n^\circ$.

Denótense:
- $Z := XK \in \Delta_n^\circ$ (estado post-Markov),
- $\widetilde{X} := X \circ L \in \mathbb{R}_{>0}^n$ (producto componente a componente),
- $\alpha := \langle Z, L \rangle = \langle XK, L \rangle > 0$,
- $\beta := \langle X, L \rangle = \|\widetilde{X}\|_1 > 0$.

**Consecuencia.**
Las coordenadas del defecto de ordenamiento admiten la representación explícita

$$\mathcal{D}_{K,L}(X)_i
= \frac{Z_i\, L_i}{\alpha} - \frac{(\widetilde{X} K)_i}{\beta}, \qquad i = 1, \dots, n.$$

Equivalentemente: el primer término es $B_L(XK)_i$ y el segundo es $B_L(X)_i$ seguido de la aplicación de $K$, ambos escritos directamente en términos de los objetos $Z$, $\widetilde{X}$, $\alpha$, $\beta$.

*Rol en la cadena:* Sin esta fórmula no es posible calcular $\|\mathcal{D}_{K,L}(X)\|_1$ explícitamente ni establecer cuándo $\mathcal{D}=0$. Es el punto de partida para Prop 3.3 (caso $n=2$) y para el análisis en la demostración de Prop 3.4.

---

### Proposición 3.3 — Caso $n=2$: defecto escalar y subvariedad de conmutación

**Hipótesis.**
Sea $n = 2$.
Sea $K = \begin{pmatrix} 1-k_{12} & k_{12} \\ k_{21} & 1-k_{21} \end{pmatrix}$ con $k_{12}, k_{21} \in [\varepsilon, 1-\varepsilon]$.
Sea $L = (L_1, L_2)$ con $e^{-R} \leq L_i \leq e^R$.
Sea $X = (x, 1-x)$ con $x \in (0,1)$.

Denótense $z(x) := x(1-k_{12}) + (1-x)k_{21}$, $\alpha(x) := z(x) L_1 + (1-z(x)) L_2$ y $\beta(x) := xL_1 + (1-x)L_2$.

**Consecuencia.**
El defecto se reduce a un escalar $d(x) := \mathcal{D}_{K,L}(X)_1 = -\mathcal{D}_{K,L}(X)_2$ dado por

$$d(x) = \frac{z(x)\, L_1}{\alpha(x)} - \frac{x L_1(1-k_{12}) + (1-x) L_2 k_{21}}{\beta(x)}.$$

La función $d:(0,1) \to \mathbb{R}$ es el cociente de dos funciones racionales en $x$.
La subvariedad de conmutación $\mathcal{M}_{K,L} = \{x \in (0,1) : d(x) = 0\}$ satisface:

1. Si $L_1 = L_2$ ó $K = I$, entonces $d \equiv 0$ en $(0,1)$, es decir, $\mathcal{M}_{K,L} = (0,1)$.
2. Si $L_1 \neq L_2$ y $k_{12}, k_{21} > 0$ con $k_{12} + k_{21} \neq 1$, entonces $d(x) \neq 0$ para genéricamente todo $x \in (0,1)$, y $\mathcal{M}_{K,L}$ es un conjunto finito (posiblemente vacío) de puntos aislados.
3. En el caso degenerado $k_{12} + k_{21} = 1$ (convergencia en un paso), la condición $d \equiv 0$ requiere además $L_1 = L_2$.

*Rol en la cadena:* Confirma que $\mathcal{D}$ es generalmente no nulo y da la base computacional para el Problema abierto 3.2 (caracterización algebraica de $\mathcal{D} \equiv 0$). Además, proporciona el caso tratable para verificar numéricamente Prop 3.4 antes de abordar $n \geq 3$.

---

### Lema 3.4 — Lipschitz local de $D_{\mathrm{KL}}(P \| \cdot)$

**Hipótesis.**
Sea $P \in \Delta_n^\circ$.
Sean $Y_1, Y_2 \in \Delta_n^\circ$ tales que $\min_i Y_{1,i} \geq m > 0$ y $\min_i Y_{2,i} \geq m > 0$ para alguna constante $m$.

**Consecuencia.**

$$| D_{\mathrm{KL}}(P \| Y_1) - D_{\mathrm{KL}}(P \| Y_2) | \leq \frac{1}{m}\, \| Y_1 - Y_2 \|_1.$$

*Rol en la cadena:* Es el lema pivote de toda la sección. Aplicado con $Y_1 = B_L(XK)$ y $Y_2 = B_L(X)K$ — que difieren en $\mathcal{D}_{K,L}(X)$ — y con $m = m_*(\varepsilon, R)$ (cota inferior sobre coordenadas derivada de $\mathcal{K}_\varepsilon$ y $\mathcal{U}_R$), produce directamente Prop 3.4. También produce la cota en el término de valor en $|Q_\tau^{MB} - Q_\tau^{BM}|$ cuando se usa con Prop 2.2.

---

### Proposición 3.4 — Cota de suboptimalidad de un paso

**Hipótesis.**
Sean $\varepsilon > 0$, $R > 0$.
Sea $K \in \mathcal{K}_\varepsilon$ y $L \in \mathbb{R}_{>0}^n$ con $\log L \in \mathcal{U}_R$.
Sea $X \in \Delta_n^\circ$.
Sea $P \in \Delta_n^\circ$ el objetivo.

**Consecuencia.**

$$| J(X; K, L) - J(X; L, K) | \leq \frac{e^{2R}}{\varepsilon}\, \| \mathcal{D}_{K,L}(X) \|_1,$$

donde la constante $e^{2R}/\varepsilon$ depende únicamente de $\varepsilon$ y $R$, y es uniforme en $X$, $P$, $K$, $L$.

En particular, si $\mathcal{D}_{K,L}(X) = 0$, entonces $J(X;K,L) = J(X;L,K)$: el costo terminal es independiente del orden.

*Rol en la cadena:* Esta proposición es la que originalmente aparecía como Conjetura 3.3 en ProyectoII. Dado que $J(X;K,L) = D_{\mathrm{KL}}(P \| B_L(XK))$ y $J(X;L,K) = D_{\mathrm{KL}}(P \| B_L(X)K)$, y que $B_L(XK) - B_L(X)K = \mathcal{D}_{K,L}(X)$, la proposición se obtiene aplicando Lema 3.4 con $Y_1 = B_L(XK)$, $Y_2 = B_L(X)K$, y $m = m_*(\varepsilon,R) = \varepsilon e^{-2R}$. **Esta proposición es demostrable con el aparato construido.**

---

### Lema 3.5 — Diferencia de costos secuenciales

**Hipótesis.**
Sean $\varepsilon > 0$, $R > 0$.
Sea $K \in \mathcal{K}_\varepsilon$, $\log L \in \mathcal{U}_R$, $X \in \Delta_n^\circ$.
Sea $\mathcal{C} \subset \Delta_n^\circ$ un compacto que contiene a $X$, $XK$, $B_L(X)$, $B_L(XK)$ y $B_L(X)K$.

**Consecuencia.**
Existe una constante $M(\mathcal{C}, \varepsilon, R) > 0$, dependiente del compacto pero no de la elección específica de $(X, K, L)$ en $\mathcal{C} \times \mathcal{K}_\varepsilon \times \mathcal{U}_R$, tal que

$$| c_{MB}(X; K, L) - c_{BM}(X; K, L) | \leq M(\mathcal{C}, \varepsilon, R)\, \| \mathcal{D}_{K,L}(X) \|_1.$$

*Rol en la cadena:* Este lema es el eslabón que conecta la diferencia de costos intermedios con el defecto geométrico. Es necesario para pasar de Prop 3.4 (un paso, solo costo terminal) a Conjetura 3.3' (múltiples pasos, costos acumulados). **Es el lema técnicamente más exigente** y su demostración requiere el análisis algebraico de $c_{MB} - c_{BM}$ a través de la fórmula del Lema 3.0.

---

### Conjetura 3.3' — Cota de suboptimalidad multi-paso (Q-función)

**Hipótesis.**
Sean $\varepsilon > 0$, $R > 0$, $\lambda > 0$, $\tau \geq 1$.
Sea $K \in \mathcal{K}_\varepsilon$, $\log L \in \mathcal{U}_R$, $X \in \Delta_n^\circ$.

**Consecuencia conjeturada.**
Existe una constante $C_\tau(\varepsilon, R) > 0$ tal que

$$| Q_\tau^{MB}(X; K, L) - Q_\tau^{BM}(X; K, L) | \leq C_\tau(\varepsilon, R)\, \| \mathcal{D}_{K,L}(X) \|_1.$$

En particular, si $\mathcal{D}_{K,L}(X) = 0$, entonces $Q_\tau^{MB} = Q_\tau^{BM}$: en un estado donde los operadores conmutan, la política óptima de $\tau$ pasos no depende del ordenamiento elegido en el paso actual.

*Estructura de la demostración esperada:*
$$|Q_\tau^{MB} - Q_\tau^{BM}| \leq \underbrace{|c_{MB} - c_{BM}|}_{\leq M\|\mathcal{D}\|_1 \text{ (Lema 3.5)}} + \underbrace{|V_{\tau-1}(B_L(XK)) - V_{\tau-1}(B_L(X)K)|}_{\leq L_{\tau-1}\|\mathcal{D}\|_1 \text{ (Prop 2.2 + Lema 3.4)}}$$

lo que daría $C_\tau = M + L_{\tau-1}$.

La conjetura queda abierta porque Lema 3.5 no está demostrado. Una demostración de Lema 3.5 implicaría automáticamente esta conjetura con constante $C_\tau = M(\mathcal{C},\varepsilon,R) + L_{\tau-1}(\mathcal{C})$.

---

## Resumen de dependencias

```
Lema 1.0a ──┐
             ├──► Prop 1.1 (inalcanzabilidad, corregida)
Lema 1.0b ──┘

Def 2.4 ──────────────────────────────────────────────────────────────────┐
Def 2.5 ──────────────────────────────────────────────────────────────────┤
Def 2.6 ──────────────────────────────────────────────────────────────────┤
Prop 2.2 ──────────────────────────────────────────────────────────────┐  │
                                                                        │  │
Lema 3.0 ──► Prop 3.3 (n=2)                                            │  │
                                                                        │  │
Lema 3.4 ──────────────────────────────────────► Prop 3.4 ★            │  │
           │                                    (conjetura resuelta)    │  │
           └──► Prop 2.2 ──────────────────────────────────────────────┤  │
                                                                        │  │
Lema 3.5 (abierto) ─────────────────────────────────────────────────► Conj 3.3'
         (si se demuestra)                                             (multi-paso)
```

★ **Prop 3.4 es una proposición demostrable**, no una conjetura. Su demostración
requiere solo Lema 3.4 (con $m_* = \varepsilon e^{-2R}$) y la definición de $\mathcal{D}$.
Constituye la resolución de la Conjetura 3.3 original de ProyectoII.


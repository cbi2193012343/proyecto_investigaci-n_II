# Mapeo Estructural CI

## 1. Mapeo Topologico y Cinematico (Conexion MD -> TEX)

| Elemento en MD | Base en TEX | Referencia estructural | Rol tecnico |
|---|---|---|---|
| Observacion 0.1 | Seccion D, Def. `\ref{def:KL}`; Seccion F, Obs. `\ref{obs:interior_markov}` y Prop. `\ref{prop:markov_es_local}` | La KL terminal explota en frontera si `P_i>0` y `X_i\to 0`; el operador Markov local no garantiza permanencia en el interior | Justifica usar `D_{KL}(P \mid X_T)` como barrera contra colapso de soporte |
| Lema 1.0a | Seccion F, Def. `\ref{def:Sn_markov}` y Prop. `\ref{prop:simplex_invariante}` | `K \in S_n` preserva `\Delta_n`, pero el bound uniforme de desplazamiento no esta explicitado en el tex | Suministra la cota de paso markoviano para la inalcanzabilidad finita |
| Lema 1.0b | Seccion C, Def. `\ref{def:Tglobal}` y Obs. `\ref{obs:coordenadasLog}` | La normalizacion multiplicativa `T_Y` actua sobre factores positivos; la cota depende de una ventana logaritmica `\log L \in U_R` | Suministra la cota de paso bayesiano para completar la cota total por iteracion |
| Proposicion 1.1 (corregida) | Seccion F, Prop. `\ref{prop:simplex_invariante}`; Seccion C, Def. `\ref{def:Tglobal}`; Seccion D, Def. `\ref{def:KL}` | La invariancia del simplex y la KL terminal sostienen el argumento; el resultado de radio finito no aparece como proposicion propia en el tex | Formula la inalcanzabilidad en tiempo finito como sintesis externa del marco existente |
| Definicion 2.4 | Seccion C, Def. `\ref{def:Tglobal}`; Seccion F, Prop. `\ref{prop:markov_es_local}` | Introduce la eleccion explicita del orden `MB/BM` sobre dos operadores ya presentes: local y global | Convierte el orden en variable de control |
| Definicion 2.5 | Seccion D, Def. `\ref{def:KL}`; Seccion E, Prop. `\ref{prop:bayes_como_TY}` | Los costos secuenciales son sumas de KL en dos ramas operativas; el tex solo contiene los bloques de KL y el operador bayesiano | Descompone el costo de un paso compuesto segun el orden |
| Definicion 2.6 | Seccion E, Prop. `\ref{prop:bayes_como_TY}`; Seccion D, Prop. `\ref{prop:gradKL}` | La recursion de `Q_tau` usa valor terminal y composicion ordenada; no existe ecuacion de Bellman explicita en el tex | Inserta la capa de programacion dinamica que falta en el manuscrito actual |
| Proposicion 2.2 | Seccion D, Prop. `\ref{prop:gradKL}` y Prop. `\ref{prop:solucionExplicita}` | La suavidad del flujo Fisher-KL en `\Delta_n^\circ` es el soporte mas cercano; la Lipschitz regularidad del valor no esta demostrada en el tex | Aporta continuidad/Lipschitz de `V_tau` como extension externa |
| Lema 3.0 | Seccion C, Def. `\ref{def:Tglobal}`; Seccion F, Prop. `\ref{prop:markov_es_local}` | El defecto `\mathcal{D}_{K,L}(X)` compara la composicion global despues o antes del paso Markov | Da la formula algebraica del desajuste de orden |
| Proposicion 3.3 | Seccion F, Prop. `\ref{prop:markov_es_local}`; Seccion C, Def. `\ref{def:Tglobal}` | El caso `n=2` es la reduccion escalar del choque entre una mezcla lineal y una renormalizacion multiplicativa | Aisla la subvariedad de conmutacion en dimension minima |
| Lema 3.4 | Seccion D, Def. `\ref{def:KL}`; Prop. `\ref{prop:gradKL}` | La KL es suave en compactos del interior del simplex y admite cota local tipo Lipschitz | Transfiere defecto geometrico a defecto de costo |
| Proposicion 3.4 | Seccion D, Def. `\ref{def:KL}`; Seccion E, Prop. `\ref{prop:bayes_como_TY}`; Seccion F, Prop. `\ref{prop:markov_es_local}` | `J(X;K,L)` y `J(X;L,K)` son KL evaluadas sobre estados obtenidos por dos ordenes distintos | Convierte la conjetura original en una cota de suboptimalidad de un paso |
| Lema 3.5 | Seccion D, Prop. `\ref{prop:gradKL}`; Seccion E, Cor. `\ref{cor:bayes_secuencial}` | La diferencia entre costos intermedios requiere control de propagacion a traves de composiciones sucesivas | Cierra el puente entre orden local y costo acumulado |
| Conjetura 3.3' | Seccion D, Prop. `\ref{prop:gradKL}`; Seccion E, Cor. `\ref{cor:bayes_secuencial}`; Seccion F, Prop. `\ref{prop:trayectoria_markov_CI}` | La recursion `Q_tau^{MB}/Q_tau^{BM}` no esta formalizada en el tex; depende de la dinamica iterada y de la composicion bayesiana | Formula la version multi-paso de la suboptimalidad por orden |

Notas de trazabilidad:

- Las filas marcadas como sintesis externa usan el tex como soporte conceptual, no como enunciado identico.
- El tex actual sostiene con claridad la parte bayesiana, la parte markoviana y la geometria KL, pero no contiene aun la capa completa de programacion dinamica por orden.

## 2. Mapeo Bibliografico Estructural (Los 4 Roles de la Literatura)

| Rol | Elementos MD | Referencias del workspace | Funcion estructural |
|---|---|---|---|
| A. Fundacion (El espacio) | Observacion 0.1; Def. 2.4, 2.5, 2.6; Lema 3.0 | `ref1` (Pistone-Shoaib 2024), `ref3` (Amari 2016), `ref4` (Egozcue et al. 2003), `ref5` (Pawlowsky-Glahn et al. 2011), `ref6` (Bayes spaces 2013) | Sostiene el simplex como espacio composicional, la normalizacion multiplicativa y la lectura geometrica del estado como punto positivo |
| B. Definiciones Prestadas (La difusion) | Lema 1.0a; Prop. 1.1; Seccion F del marco Markov | `ref10` (Dobrushin coefficient on cones), `ref9` (Markov Chains) | Sostiene la contraccion del operador de Markov, la cota de ergodicidad y el paso de cadena de Markov a dinamica contractiva |
| C. Delegacion Tecnica (Las cotas) | Lema 3.4; Prop. 3.4; Lema 3.5; Conj. 3.3' | `ref11` (Local Lipschitz Stability of Bayesian Inverse Problems), `ref12` (Lipschitz continuous dynamic programming) | Sostiene la regularidad Lipschitz de la posterior y la regularidad del valor/Bellman; aqui se apoya la cota de defecto a costo |
| D. Contraste (El problema a resolver) | Def. 2.4, 2.5, 2.6; Lema 3.0; Prop. 3.3; Lema 3.5; Conj. 3.3' | `ref15` (Optimal control as a graphical model inference problem), `ref13` (Efficient computation of optimal actions), `ref14` (A linear theory for control of non-linear stochastic systems) | La literatura de control como inferencia trata la minimizacion KL y la politica optima, pero no modela la friccion por no conmutatividad entre `MB` y `BM` ni el defecto `\mathcal{D}_{K,L}` como objeto central |

Cobertura bibliografica usada en este mapeo:

- Geometria composicional y Bayes space: `ref1`, `ref4`, `ref5`, `ref6`.
- Geometria de la informacion: `ref3`.
- Contraccion markoviana y ergodicidad: `ref9`, `ref10`.
- Estabilidad Lipschitz bayesiana: `ref11`.
- Regularidad de programacion dinamica: `ref12`.
- Control como inferencia y control optimo: `ref13`, `ref14`, `ref15`.

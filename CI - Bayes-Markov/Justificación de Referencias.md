# Justificación de Referencias

Este documento es una base de trabajo para justificar, con apoyo bibliográfico tomado solo de los `.md` de `Referencias/`, el contenido ya escrito en [`CI_Bayes.tex`](./CI_Bayes.tex).

No introduce contenido nuevo en el manuscrito. Su función es dejar trazable qué parte del texto ya existente puede sostenerse con qué referencia, y qué partes todavía conviene respaldar mejor antes de pasar a una redacción formal en `.tex`.

## Criterio de uso

- `Respaldada directamente`: la referencia dice explícitamente la idea o algo muy cercano.
- `Respaldada indirectamente`: la referencia no lo formula idéntico, pero el soporte conceptual es claro.
- `Respaldo temático`: la referencia toca el mismo marco general, pero no prueba la afirmación con precisión.
- `Sin respaldo suficiente`: por ahora no hay soporte claro en los `.md` disponibles.

## Referencias prioritarias

1. `ref6.md`: Bayes spaces, distribuciones impropias, verosimilitudes no integrables, perturbación y familias exponenciales.
2. `ref1.md`: geometría afín del símplex, Bayes space, flujo de gradiente y optimización variacional.
3. `ref3.md`: geometría de la información, métrica de Fisher, variedades estadísticas.
4. `ref2.md`: statistical bundle, acción lagrangiana, Euler-Lagrange.
5. `ref4.md`: transformaciones ilr, geometría de Aitchison, perturbación y closure.
6. `ref5.md`: notas de análisis composicional, estructura del símplex, log-ratios y bases ortonormales.

## Mapa general de justificación

| Bloque en `CI_Bayes.tex` | Afirmación central | Referencia principal | Referencias complementarias | Estado |
|---|---|---|---|---|
| Sección A | El estado informacional discreto vive en el símplex de probabilidad | `ref4`, `ref5`, `ref1` | `ref3` | Respaldada directamente |
| Sección A | El operador de cierre conserva información relativa | `ref4`, `ref5` | `ref1` | Respaldada directamente |
| Sección B | La actualización local preserva la masa total | `ref4`, `ref6` | `ref1` | Respaldada indirectamente |
| Sección B | La corrección local se interpreta como cambio de medida | `ref6` | `ref1` | Respaldada directamente |
| Sección C | La corrección global es multiplicativa y luego se normaliza | `ref6`, `ref1` | `ref4` | Respaldada directamente |
| Sección C | La composición de operadores globales corresponde a producto coordenado | `ref6`, `ref1` | `ref4` | Respaldada directamente |
| Sección D | La divergencia KL y el gradiente Fisher son la dinámica natural | `ref3` | `ref1`, `ref2` | Respaldada directamente |
| Sección D | El flujo explícito converge al objetivo \(P\) | `ref3` | `ref2` | Respaldada indirectamente |
| Sección E0 | La verosimilitud puede verse como corrección global | `ref6` | `ref1` | Respaldada directamente |
| Sección E0 | Bayes es un caso particular de `T_Y` | `ref6` | `ref1`, `ref3` | Respaldada directamente |
| Sección E0 | La corrección óptima hacia el posterior es proporcional a \(\pi_i/X_i\) | `ref6` | `ref1` | Respaldada indirectamente |
| Sección E0 | La actualización conjugada suma parámetros naturales | `ref1`, `ref2` | `ref6` | Respaldada directamente |
| Sección E0 (modelos continuos) | La inferencia bayesiana se apoya en la posterior y en las densidades predictivas | `ref7` | `ref6` | Respaldada indirectamente |

## Justificación por bloque

### 1. Sección A: probabilidad, particiones y símplex

#### Afirmaciones ya bien justificadas

- El paso de una medida \(P\) a un vector discreto \(X\in\Delta_n\) está alineado con la geometría del símplex que aparece en `ref4.md` y `ref5.md`.
- La interpretación de `\mathscr C` como cierre que conserva proporciones está muy bien respaldada por `ref4.md`.
- La idea de trabajar con composiciones positivas normalizadas también aparece en `ref5.md`.

#### Comentario bibliográfico

- `ref4.md` es la mejor base para el lenguaje de Aitchison geometry, perturbation y closure.
- `ref5.md` funciona como apoyo didáctico general para la geometría composicional.
- `ref1.md` conecta ese símplex con geometría afín, Bayes space e información.

### 2. Sección B: correcciones locales y cambio de medida

#### Afirmaciones ya bien justificadas

- La corrección local preserva la suma total y puede interpretarse como una reponderación de masa.
- La identificación con una medida nueva \(Q_Y\) es coherente con la lectura de `ref6.md`, donde las densidades proporcionales y la evidencia aparecen como objetos de Bayes spaces.

#### Comentario bibliográfico

- `ref6.md` es central aquí porque trata explícitamente Bayes spaces, perturbation y el uso de densidades como evidencia.
- Aunque la formulación exacta de `Q_Y` es propia del manuscrito, la idea conceptual está claramente alineada con `ref6.md`.

### 3. Sección C: operadores globales multiplicativos

#### Afirmaciones ya bien justificadas

- La actualización multiplicativa con normalización es compatible con la formulación de Bayes spaces en `ref6.md`.
- La composición de factores positivos como producto coordenado encaja con la lectura de perturbation como multiplicación de densidades.
- La representación en coordenadas logarítmicas es coherente con la literatura composicional de `ref4.md` y `ref5.md`.

#### Comentario bibliográfico

- `ref6.md` respalda muy bien la idea de Bayes theorem como operación lineal en un espacio de densidades proporcionales.
- `ref1.md` ayuda a justificar la geometría afín y el lenguaje de flujo o corrección sobre el símplex.

### 4. Sección D: KL, Fisher y dinámica inducida

#### Afirmaciones ya bien justificadas

- La métrica de Fisher está soportada por `ref3.md`.
- La interpretación geométrica de gradientes y dinámicas de descenso está soportada por `ref3.md` y también por la línea de trabajo de `ref2.md`.
- El vínculo con una dinámica tipo flujo es compatible con la literatura de geometría de la información y con el enfoque variacional de `ref2.md`.

#### Comentario bibliográfico

- `ref3.md` es la referencia más fuerte para esta sección.
- `ref2.md` refuerza la lectura variacional, aunque no sustituye a `ref3.md`.

### 5. Sección E0: semántica bayesiana

#### Afirmaciones ya bien justificadas

- La definición de probabilidad condicional en el espacio conjunto es una construcción elemental, y el paso a la verosimilitud está completamente alineado con el marco de Bayes spaces de `ref6.md`.
- La verosimilitud como corrección global está respaldada de forma muy natural por `ref6.md`, donde Bayes theorem aparece como perturbation.
- El hecho de que la actualización bayesiana sea un caso particular de `T_Y` es una traducción conceptual directa del mismo artículo.
- La versión con modelos continuos discretizados es una extensión técnica propia del manuscrito; puede apoyarse conceptualmente en `ref6.md`, pero conviene tratarla como desarrollo propio.
- Para la motivación bayesiana de esa discretización, `ref7.md` aporta soporte útil al centrar la atención en la posterior y en las densidades predictivas como objetos fundamentales de la inferencia.

#### Comentario bibliográfico

- `ref6.md` debe ser la referencia central de esta sección.
- `ref1.md` ayuda a justificar la geometría del símplex y la lectura afín.
- `ref3.md` refuerza la parte de geometría de la información si se quiere hablar del posterior como punto en una variedad estadística.
- `ref7.md` es un apoyo puntual para la subsección de modelos continuos, no la base principal de la semántica bayesiana.

## Afirmaciones con respaldo fuerte

- Bayes theorem puede leerse como una operación multiplicativa/perturbativa en un espacio de densidades proporcionales.
- La verosimilitud se puede tratar como evidencia o corrección global.
- La actualización bayesiana puede representarse como un operador sobre estados del símplex.
- La familia exponencial encaja naturalmente en el marco de Bayes spaces.
- La métrica de Fisher es la estructura geométrica natural para la sección D.

## Afirmaciones que conviene seguir justificando mejor

- La “corrección óptima hacia el posterior” como enunciado formal del manuscrito.
- El paso continuo-discreto para modelos paramétricos concretos.
- La parte de universalidad de la actualización en CI, si se quiere presentarla como afirmación fuerte y no como interpretación.
- La comparación fina entre el marco Bayes y la representación local del cambio de medida.

## Observaciones sobre `ref6`

`ref6.md` es la columna vertebral bibliográfica de la parte bayesiana porque:

- trata explícitamente Bayes spaces;
- justifica el uso de distribuciones impropias y likelihoods no integrables;
- interpreta Bayes theorem como perturbation;
- introduce evidencia, densidades proporcionales y comparación de ratios;
- conecta la estructura con familias exponenciales y sensibilidad.

Por eso, casi todo lo que en `CI_Bayes.tex` se presenta como “corrección global”, “verosimilitud”, “actualización bayesiana” y “evidencia” debe pasar primero por `ref6.md`.

## Observaciones sobre `ref1`

`ref1.md` funciona como puente entre:

- geometría afín del símplex;
- Bayes space;
- flujo de gradiente;
- formulaciones variacionales.

Es útil para respaldar el tono geométrico del manuscrito, pero no sustituye a `ref6.md` cuando el tema es estrictamente bayesiano.

## Observaciones sobre `ref3`

`ref3.md` respalda la lectura diferencial y la métrica de Fisher:

- gradiente riemanniano;
- estructura de variedad estadística;
- interpretación geométrica local;
- lenguaje de la geometría de la información.

Si se habla de posterior como punto en una variedad o de flujo de descenso, esta referencia es la principal.

## Observaciones sobre `ref4` y `ref5`

Estas referencias son la base composicional:

- símplex;
- perturbación;
- closure;
- log-ratios;
- bases ortonormales;
- interpretación geométrica de composiciones.

Sirven como soporte de la intuición estructural, sobre todo para las secciones A, B y C.

## Observaciones sobre `ref7`

`ref7.md` es útil para la subsección de modelos continuos porque:

- enfatiza que las densidades predictivas son cantidades fundamentales en inferencia bayesiana;
- trata la distribución posterior como el objeto de interés para la concentración asintótica;
- presenta la posterior convergence rates como una propiedad central en problemas bayesianos;
- muestra que la actualización bayesiana puede estudiarse a través de las densidades predictivas.

No respalda directamente la partición paramétrica uniforme ni la discretización en sí, pero sí da soporte conceptual a la manera en que el manuscrito presenta esa discretización: como una representación finita de una inferencia bayesiana cuyo núcleo sigue siendo la posterior.

## Conclusión operativa

El orden más razonable para justificar y luego formalizar en `CI_Bayes.tex` es:

1. `ref4` y `ref5` para la base composicional del símplex.
2. `ref6` para la semántica bayesiana propiamente dicha.
3. `ref3` para la parte Fisher/KL/dinámica.
4. `ref1` y `ref2` para el puente geométrico y variacional.

La siguiente fase debe consistir en tomar esta base y convertirla en inserciones formales dentro del `.tex`, una sección a la vez.

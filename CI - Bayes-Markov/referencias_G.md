# Referencias G

Fichas ligeras para las referencias locales que sirven de apoyo a la Seccion G y al bloque comentado de continuacion. No se copian fragmentos largos; solo se resume lo que puede usarse y lo que debe evitarse.

## `GaubertQu2014`

- Clave BibTeX sugerida o existente: `GaubertQu2014`
- Objetivo principal: caracterizar la contraccion de operadores markovianos y su relacion con el coeficiente de Dobrushin, la norma `\ell^1`, la variacion total y los sistemas de consenso.
- Elemento exacto que puede usarse en la Seccion G: la identificacion de la escala natural `\ell^1` para cambios de masa probabilistica y la interpretacion de `\delta(K)` como coeficiente de contraccion abstracto.
- Elemento que no debe usarse: no debe usarse para afirmar que la cota `|XK-X|_1\le 2(1-\varepsilon)` sale directamente del coeficiente de Dobrushin.
- Lugar de uso permitido: observacion.
- Frase breve permitida para una observacion: "La norma `\ell^1` es la escala natural para cambios de masa probabilistica."
- Advertencias para evitar atribuciones incorrectas: usarla solo como contexto de lectura; la cota de desplazamiento markoviano debe probarse desde `K_{ab}\ge \varepsilon`.
- Puntos relevantes: introduccion, formula del coeficiente de Dobrushin, teorema 1.1, comentarios sobre total variation y consensus.

## `Sprungk2020`

- Clave BibTeX sugerida o existente: `Sprungk2020`
- Objetivo principal: estabilidad local Lipschitz de posteriores bayesianos frente a perturbaciones del prior y de la log-verosimilitud.
- Elemento exacto que puede usarse en la Seccion G: la lectura contextual de la correccion bayesiana como actualizacion posterior sensible a la verosimilitud, con control por hipotesis de acotacion.
- Elemento que no debe usarse: no debe presentarse como prueba de la cota `|B_L(X)-X|_1\le e^{2R}-1`.
- Lugar de uso permitido: observacion.
- Frase breve permitida para una observacion: "La estabilidad bayesiana local solo da contexto sobre sensibilidad de la posterior."
- Advertencias para evitar atribuciones incorrectas: la demostracion del lema debe seguir siendo algebraica y finita; la referencia no sustituye el calculo.
- Puntos relevantes: abstract, introduccion, secciones sobre total variation, Hellinger, Wasserstein y KL.

## `Norris1997`

- Clave BibTeX sugerida o existente: `Norris1997`
- Objetivo principal: base clasica sobre cadenas de Markov, matrices estocasticas, distribuciones invariantes y procesos de decision de Markov.
- Elemento exacto que puede usarse en la Seccion G: la idea de que una matriz estocastica por filas induce un paso markoviano sobre el símplex y la nocion basica de MDP.
- Elemento que no debe usarse: no debe usarse para justificar cotas de Dobrushin o la cota `2(1-\varepsilon)`.
- Lugar de uso permitido: observacion.
- Frase breve permitida para una observacion: "Una matriz estocastica por filas define un paso markoviano sobre el símplex."
- Advertencias para evitar atribuciones incorrectas: limitar el uso a definiciones y contexto; no convertirlo en prueba de resultados cuantitativos.
- Puntos relevantes: capitulo 1 (cadenas discretas), capitulo 5.4 (Markov decision processes), indice de procesos y politicas estacionarias.

## `MarotoMoran2005`

- Clave BibTeX sugerida o existente: `MarotoMoran2005`
- Objetivo principal: programacion dinamica Lipschitz con descuento; regularidad de la funcion de valor bajo hipotesis Lipschitz.
- Elemento exacto que puede usarse en la Seccion G: la afirmacion de que, bajo hipotesis Lipschitz, la funcion de valor es Lipschitz y el operador de Bellman admite analisis regular.
- Elemento que no debe usarse: no debe citarse como prueba de las cotas de desplazamiento bayesiano o markoviano.
- Lugar de uso permitido: observacion.
- Frase breve permitida para una observacion: "Bajo hipotesis Lipschitz, la funcion de valor es regular y computable."
- Advertencias para evitar atribuciones incorrectas: usar solo cuando entre el bloque de control y el bloque de inalcanzabilidad; no mezclarlo con las pruebas algebraicas actuales.
- Puntos relevantes: introduccion, seccion 2.1, comentario sobre Bellman y la regularidad Lipschitz.

## `Todorov2009EfficientComputationOptimalActions`

- Clave BibTeX sugerida o existente: `Todorov2009EfficientComputationOptimalActions`
- Objetivo principal: reformular el control optimo mediante una ecuacion lineal tipo Bellman, con procesos de decision markovianos y costo cuadratico/KL en versiones estructuradas.
- Elemento exacto que puede usarse en la Seccion G: la lectura de MDP y Bellman como marco conceptual para la parte de control que vendra despues.
- Elemento que no debe usarse: no debe invocarse para afirmar resultados de la Seccion G activa; tampoco para introducir costos o `Q` antes de tiempo.
- Lugar de uso permitido: observacion.
- Frase breve permitida para una observacion: "En la literatura de control, Bellman y MDP se usan como marco de programacion dinamica."
- Advertencias para evitar atribuciones incorrectas: no confundir el marco de control con la prueba de las cotas de desplazamiento; aqui solo sirve de contexto para el bloque comentado.
- Puntos relevantes: abstract, introduccion, seccion de reducing optimal control to a linear problem.

## `KappenGomezOpper2008`

- Clave BibTeX sugerida o existente: `KappenGomezOpper2008`
- Objetivo principal: reformular control optimo como problema de inferencia grafica con costo KL y dinamica markoviana.
- Elemento exacto que puede usarse en la Seccion G: la equivalencia conceptual entre control KL, inferencia y retropropagacion en cadenas.
- Elemento que no debe usarse: no debe presentarse como prueba de las cotas actuales ni como fundamento del defecto de ordenamiento.
- Lugar de uso permitido: observacion.
- Frase breve permitida para una observacion: "El control KL puede leerse como inferencia grafica."
- Advertencias para evitar atribuciones incorrectas: usarlo solo cuando el texto ya haya introducido el bloque de control y la funcion de valor.
- Puntos relevantes: introduccion y seccion 1.

## `Todorov2009EfficientComputationOptimalActions`

- Clave BibTeX sugerida o existente: `Todorov2009EfficientComputationOptimalActions`
- Objetivo principal: reformular problemas de control optimo y programacion dinamica mediante una estructura lineal compatible con MDP y Bellman.
- Elemento exacto que puede usarse en la Seccion G: la lectura estado--accion--transicion--costo y la interpretacion probabilistica de las divergencias entre distribuciones.
- Elemento que no debe usarse: no debe usarse para probar cotas de desplazamiento por paso ni resultados de conmutacion.
- Lugar de uso permitido: observacion.
- Frase breve permitida para una observacion: "La formulacion estado--accion--transicion--costo es compatible con la programacion dinamica discreta."
- Advertencias para evitar atribuciones incorrectas: usarla solo como marco conceptual para el bloque de control con variable de ordenamiento.
- Puntos relevantes: seccion de reducing optimal control to a linear problem, discusion sobre MDP y Bellman, aplicaciones a inference y policy improvement.

## `Kappen2005LinearTheoryForControlOfNonLinearStochasticSystems`

- Clave BibTeX sugerida o existente: `Kappen2005LinearTheoryForControlOfNonLinearStochasticSystems`
- Objetivo principal: conectar control estocastico no lineal con formulaciones de tipo integral de trayectoria, costo de trayectoria y costo terminal.
- Elemento exacto que puede usarse en la Seccion G: la separacion entre costo acumulado y costo terminal, y la lectura del control optimo como problema con contribucion de trayectoria.
- Elemento que no debe usarse: no debe usarse para derivar la cota `|B_L(X)-X|_1\le e^{2R}-1` ni la cota markoviana.
- Lugar de uso permitido: observacion.
- Frase breve permitida para una observacion: "La estructura de costo de trayectoria y costo terminal es compatible con el control estocastico no lineal."
- Advertencias para evitar atribuciones incorrectas: no confundir la descripcion de costo con una prueba algebraica del bloque activo.
- Puntos relevantes: abstract, introduccion, ecuaciones de HJB linealizadas, path integral y simetria rota.

## `PistoneShoaib2024Axioms`

- Clave BibTeX sugerida o existente: `PistoneShoaib2024Axioms`
- Objetivo principal: presentar una lectura axiomatica de la geometria afina, Bayes space, geometria de Aitchison y transporte sobre el símplex de probabilidad.
- Elemento exacto que puede usarse en la Seccion G: el lenguaje geometrico del símplex y la interpretacion afina/composicional de las actualizaciones multiplicativas.
- Elemento que no debe usarse: no debe usarse como prueba de las cotas de desplazamiento.
- Lugar de uso permitido: observacion.
- Frase breve permitida para una observacion: "El símplex admite una lectura geometrica afin y composicional."
- Advertencias para evitar atribuciones incorrectas: mantenerlo como soporte conceptual; no reemplaza las pruebas de la Seccion G.
- Puntos relevantes: secciones 1.1, 1.2, 1.4 y la parte sobre geometria del símplex.

## `EgozcueEtAl2013BayesSpaces`

- Clave BibTeX sugerida o existente: `EgozcueEtAl2013BayesSpaces`
- Objetivo principal: formalizar Bayes spaces, perturbacion como operacion tipo Bayes, distribuciones impropias y sensibilidad de densidades.
- Elemento exacto que puede usarse en la Seccion G: la lectura de la actualizacion bayesiana como perturbacion y normalizacion en un espacio de medidas positivas proporcionales.
- Elemento que no debe usarse: no debe emplearse para probar la cota `e^{2R}-1`.
- Lugar de uso permitido: observacion.
- Frase breve permitida para una observacion: "La actualizacion bayesiana puede leerse como perturbacion y cierre."
- Advertencias para evitar atribuciones incorrectas: usar solo como contexto semantico del paso bayesiano.
- Puntos relevantes: Bayes spaces, Bayes theorem and improper distributions, sensibilidad de densidades.

## `Amari2016`

- Clave BibTeX sugerida o existente: `Amari2016`
- Objetivo principal: geometria de la informacion, metrica de Fisher, manifolds estadisticas y conexiones con aprendizaje y MDP.
- Elemento exacto que puede usarse en la Seccion G: la lectura de la metrica de Fisher y, mas adelante, la conexion con procesos de decision y gradientes naturales.
- Elemento que no debe usarse: no debe usarse como soporte de las cotas de desplazamiento por paso.
- Lugar de uso permitido: observacion.
- Frase breve permitida para una observacion: "La metrica de Fisher da una escala geometrica natural para el símplex."
- Advertencias para evitar atribuciones incorrectas: reservarlo para contexto geometrico; no para resultados cuantitativos del defecto de ordenamiento.
- Puntos relevantes: capitulo sobre information geometry, metricas e incluso secciones sobre MDP y natural policy gradient.

## Nota de cobertura

- En la carpeta local no identifique una referencia explicita y claramente titulada sobre sistemas conmutados. Si aparece una fuente de ese tipo mas adelante, conviene crear su ficha aparte.

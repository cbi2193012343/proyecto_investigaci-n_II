# Seccion G - estado estructural vigente

Fuente activa: `CI - Bayes-Markov/CI_Bayes-Markov_copia.tex`

Alcance: desde `\begin{definicion}[Clases admisibles y ventanas de control]` hasta el bloque comentado final.

Nota: todo lo comentado se registra como continuidad prevista. Lo que ya esta reescrito dentro del bloque activo se considera vigente.

## Bloque activo

1. `Clases admisibles y ventanas de control` (`\label{def:clases_admisibles_G}`)
   - Funcion matematica: definir `\mathcal S_n`, `\mathcal K_\varepsilon` y `\mathcal U_R` como el marco admisible para matrices markovianas y verosimilitudes acotadas.
   - Dependencias anteriores: `\Delta_n`, `\Delta_n^\circ`, norma `\|\cdot\|_\infty`.
   - Habilita: definiciones de correccion bayesiana y markoviana admisibles.
   - Notacion introducida: `I`, `\mathcal S_n`, `\mathcal K_\varepsilon`, `\mathcal U_R`.
   - Advertencias de consistencia: `0<\varepsilon\le 1/n` fija una ventana uniforme; no es una cota de contraccion.

2. `Correccion bayesiana admisible` (`\label{def:correccion_bayesiana_G}`)
   - Funcion matematica: definir `B_L(X)_i = X_i L_i / \langle X,L\rangle` como actualizacion bayesiana normalizada.
   - Dependencias anteriores: `\Delta_n^\circ`, `\mathbb R_{>0}^n`, definicion de `\mathcal U_R`.
   - Habilita: observacion bayesiana, lema de cota de desplazamiento bayesiano y el defecto de ordenamiento.
   - Notacion introducida: `B_L`, `\langle X,L\rangle`, `\log L`.
   - Advertencias de consistencia: la demostracion de cotas debe ser algebraica; la referencia solo da contexto.

3. `Correccion markoviana admisible` (`\label{def:correccion_markoviana_G}`)
   - Funcion matematica: definir `M_K(X)=XK` y el campo local `Y_i^K(X)=(XK)_i/X_i-1`.
   - Dependencias anteriores: `\mathcal S_n`, `\mathcal K_\varepsilon`, `\Delta_n^\circ`.
   - Habilita: observacion markoviana, lema de cota de desplazamiento markoviano y el defecto de ordenamiento.
   - Notacion introducida: `M_K`, `Y^K(X)`.
   - Advertencias de consistencia: la restriccion a `\Delta_n^\circ` solo es necesaria para el campo local; la aplicacion `XK` vive en `\Delta_n`.

4. `Posibilidad de composicion sobre una base probabilistica comun` (`\begin{observacion}`)
   - Funcion matematica: fijar que las composiciones Bayes--Markov y Markov--Bayes se comparan sobre la misma ley discreta inducida por variables aleatorias.
   - Dependencias anteriores: definicion de `B_L`, `M_K`, `Z_0`, `Z_1`, estado informacional discreto.
   - Habilita: composicion Bayes--Markov y composicion Markov--Bayes.
   - Notacion introducida: `(\Omega,\mathcal F,\mathbb P)`, `Z_0`, `Z_1`, `X`.
   - Advertencias de consistencia: no introduce nuevo resultado, solo fija el marco probabilistico comun.

5. `Sentido Bayes--Markov` (`\begin{observacion}`)
   - Funcion matematica: interpretar `B_L` como filtrado previo por verosimilitud y `M_K` como propagacion posterior.
   - Dependencias anteriores: definiciones bayesiana y markoviana admisibles.
   - Habilita: `\begin{proposicion}[Composicion Bayes--Markov sobre una cadena observada]`.
   - Notacion introducida: ninguna nueva.
   - Advertencias de consistencia: la cita contextual debe quedarse en observacion; no debe migrar a lema o demostracion.

6. `Composicion Bayes--Markov sobre una cadena observada` (`\label{prop:composicion_BM_kolmogorov}`)
   - Funcion matematica: expresar la composicion `M_K(B_L(X))` en terminos de una cadena observada.
   - Dependencias anteriores: observacion `Sentido Bayes--Markov`, base probabilistica comun.
   - Habilita: comparacion con el orden Markov--Bayes.
   - Notacion introducida: `Z_0`, `Z_1`, `E_j^{(0)}`.
   - Advertencias de consistencia: la proposicion no debe usarse para deducir cotas de desplazamiento.

7. `Sentido Markov--Bayes` (`\begin{observacion}`)
   - Funcion matematica: interpretar `M_K` como ley predictiva y `B_L` como actualizacion posterior posterior a la propagacion.
   - Dependencias anteriores: observacion `Posibilidad de composicion sobre una base probabilistica comun`.
   - Habilita: `\begin{proposicion}[Composicion Markov--Bayes sobre una cadena observada]`.
   - Notacion introducida: ninguna nueva.
   - Advertencias de consistencia: la referencia a Markov chains solo es contexto; no prueba ninguna desigualdad del bloque.

8. `Composicion Markov--Bayes sobre una cadena observada` (`\label{prop:composicion_MB_kolmogorov}`)
   - Funcion matematica: escribir `B_L(M_K(X))` en la cadena observada correspondiente.
   - Dependencias anteriores: observacion `Sentido Markov--Bayes`.
   - Habilita: proposicion de conmutacion global.
   - Notacion introducida: `Z_1`, `E_j^{(1)}`.
   - Advertencias de consistencia: la igualdad formal depende de la misma base probabilistica que la composicion Bayes--Markov.

9. `Conmutacion global bajo positividad uniforme` (`\label{prop:conmutacion_global_MB_BM}`)
   - Funcion matematica: caracterizar cuando `B_L\circ M_K = M_K\circ B_L` globalmente.
   - Dependencias anteriores: definiciones admisibles, composiciones observadas.
   - Habilita: corolario de falla global para verosimilitudes no constantes.
   - Notacion introducida: ninguna nueva.
   - Advertencias de consistencia: no confundir igualdad global con igualdad puntual.

10. `Falla de conmutacion global para verosimilitudes no constantes` (`\label{cor:falla_conmutacion_global_L_no_constante}`)
    - Funcion matematica: deducir que, si `L` no es constante, la conmutacion global falla.
    - Dependencias anteriores: proposicion de conmutacion global.
    - Habilita: observacion de la falla global al defecto de ordenamiento.
    - Notacion introducida: ninguna nueva.
    - Advertencias de consistencia: la prueba no debe ser circular; debe depender de la proposicion de conmutacion ya probada.

11. `De la falla global al defecto de ordenamiento` (`\begin{observacion}`)
    - Funcion matematica: pasar de una falla global de conmutacion a una cuantificacion puntual por estado.
    - Dependencias anteriores: corolario de falla global.
    - Habilita: definicion del defecto de ordenamiento.
    - Notacion introducida: `X\in\Delta_n^\circ` como estado puntual.
    - Advertencias de consistencia: distingue igualdad global de igualdad puntual.

12. `Defecto de ordenamiento` (`\label{def:defecto_ordenamiento}`)
    - Funcion matematica: definir `\mathcal D_{K,L}(X)=B_L(XK)-B_L(X)K`.
    - Dependencias anteriores: correcciones admisibles y composiciones.
    - Habilita: observacion de paso al control por desplazamiento y la formula de diferencia entre ordenes.
    - Notacion introducida: `\mathcal D_{K,L}`.
    - Advertencias de consistencia: es un vector en el símplex tangente; no es un costo.

13. `Del defecto de ordenamiento a las cotas de desplazamiento por paso` (`\label{obs:defecto_a_cotas_desplazamiento}`)
    - Funcion matematica: convertir el defecto de ordenamiento en una motivacion para acotar `|B_L(X)-X|_1` y `|M_K(X)-X|_1`.
    - Dependencias anteriores: definicion del defecto de ordenamiento.
    - Habilita: lemas de cota de desplazamiento bayesiano y markoviano.
    - Notacion introducida: `v_B(R)=e^{2R}-1`, `v_M(\varepsilon)=2(1-\varepsilon)`.
    - Advertencias de consistencia: la comparacion correcta es en la escala `\ell^1`, no entre `R` y `\varepsilon`.

14. `Cota de desplazamiento bayesiana por paso y control logaritmico de la verosimilitud` (`\begin{observacion}`)
    - Funcion matematica: fijar el cociente `B_L(X)_i/X_i = L_i/\langle X,L\rangle` y explicar la restriccion `\log L\in\mathcal U_R`.
    - Dependencias anteriores: definicion de `B_L`, ventana `\mathcal U_R`.
    - Habilita: lema de cota bayesiana.
    - Notacion introducida: ninguna nueva.
    - Advertencias de consistencia: la referencia de estabilidad bayesiana es solo contexto; no prueba la cota.

15. `Cota de desplazamiento bayesiano por paso` (`\label{lem:cota_desplazamiento_bayesiano}`)
    - Funcion matematica: probar `|B_L(X)-X|_1\le e^{2R}-1` con hipotesis completas.
    - Dependencias anteriores: observacion bayesiana y `\mathcal U_R`.
    - Habilita: comparacion cuantitativa con la cota markoviana.
    - Notacion introducida: ninguna nueva.
    - Advertencias de consistencia: no llevar citas dentro del lema ni de su demostracion.

16. `Cota de desplazamiento markoviana por paso y variacion total` (`\begin{observacion}`)
    - Funcion matematica: fijar que `\ell^1` es la escala natural para cambios de masa probabilistica y que la cota se deduce de `K_{ab}\ge\varepsilon`.
    - Dependencias anteriores: definicion de `\mathcal K_\varepsilon`.
    - Habilita: lema de cota markoviana.
    - Notacion introducida: ninguna nueva.
    - Advertencias de consistencia: la referencia de Dobrushin no debe usarse como prueba directa de la cota.

17. `Cota de desplazamiento markoviano por paso` (`\label{lem:cota_desplazamiento_markoviano}`)
    - Funcion matematica: probar `|M_K(X)-X|_1=|XK-X|_1\le 2(1-\varepsilon)`.
    - Dependencias anteriores: observacion markoviana y positividad uniforme.
    - Habilita: preparacion para la inalcanzabilidad en pasos futuros.
    - Notacion introducida: ninguna nueva.
    - Advertencias de consistencia: la prueba debe permanecer algebraica y no atribuir el bound al coeficiente de Dobrushin.

18. `Control con variable de ordenamiento` (`\begin{observacion}`)
    - Funcion matematica: incorporar el orden de composicion como una decision discreta de control.
    - Dependencias anteriores: lemas de cota de desplazamiento bayesiano y markoviano, conmutacion global y su corolario.
    - Habilita: definicion de accion admisible con variable de ordenamiento.
    - Notacion introducida: ninguna nueva.
    - Advertencias de consistencia: las citas de control deben quedar solo aqui, en observacion.

19. `Accion admisible con variable de ordenamiento` (`\label{def:accion_admisible_ordenamiento}`)
    - Funcion matematica: definir `\mathcal A_{\varepsilon,R}` y una accion `u_t=(K_t,L_t,\sigma_t)`.
    - Dependencias anteriores: `\mathcal K_\varepsilon`, `\mathcal U_R`.
    - Habilita: transiciones controladas por orden.
    - Notacion introducida: `\mathcal A_{\varepsilon,R}`, `u_t`, `\sigma_t`.
    - Advertencias de consistencia: la variable de ordenamiento es discreta y binaria; no es un peso continuo.

20. `Transiciones controladas por orden` (`\label{def:transiciones_controladas_orden}`)
    - Funcion matematica: definir `T_{MB}^{K,L}`, `T_{BM}^{K,L}` y el defecto `\mathcal D_{K,L}` como diferencia de transiciones.
    - Dependencias anteriores: definicion de accion admisible con variable de ordenamiento.
    - Habilita: costos de etapa ordenados.
    - Notacion introducida: `T_{MB}^{K,L}`, `T_{BM}^{K,L}`, `T^u`.
    - Advertencias de consistencia: aqui ya aparece `\mathcal D_{K,L}` como identidad de transiciones; no sustituye su definicion previa.

21. `Costos de etapa ordenados` (`\label{def:costos_etapa_ordenados}`)
    - Funcion matematica: definir los costos `c_{MB}` y `c_{BM}` mediante divergencias KL.
    - Dependencias anteriores: transiciones controladas por orden.
    - Habilita: funcion de valor y funciones de accion--valor por orden.
    - Notacion introducida: `c_{MB}`, `c_{BM}`, `c(X,u)`.
    - Advertencias de consistencia: los costos se apoyan en KL; no deben reinterpretarse como velocidad ni como derivada temporal.

22. `Funcion de valor y funciones de accion--valor por orden` (`\label{def:valor_Q_ordenamiento}`)
    - Funcion matematica: definir `V_0`, `Q_\tau^{MB}`, `Q_\tau^{BM}` y la recurrencia de `V_\tau`.
    - Dependencias anteriores: costos de etapa ordenados.
    - Habilita: el bloque comentado siguiente sobre inalcanzabilidad y sus cotas acumuladas.
    - Notacion introducida: `V_0`, `V_\tau`, `Q_\tau^{MB}`, `Q_\tau^{BM}`.
    - Advertencias de consistencia: esta es la primera aparicion activa de `Q`; debe tratarse como funcion de accion--valor, no como operador nuevo.

## Continuacion comentada

23. `Seccion 1 -- Limites de velocidad` (bloque comentado actual)
    - Funcion matematica prevista: convertirse en el primer bloque de cotas de desplazamiento por paso e inalcanzabilidad.
    - Dependencias previstas: `v_B(R)` y `v_M(\varepsilon)` del bloque activo.
    - Habilita: lemas 1.0a y 1.0b, y la proposicion 1.1.
    - Advertencias de consistencia: el encabezado comentado aun usa lenguaje que debe ser reemplazado; no debe activarse tal cual.

24. `Lema 1.0a -- Limite de desplazamiento markoviano` (`\label{lem:limite_desplazamiento_markoviano}`)
    - Funcion matematica prevista: dar una version acumulada o preparatoria de la cota markoviana.
    - Dependencias previstas: `\mathcal K_\varepsilon`.
    - Habilita: proposicion 1.1.

25. `Lema 1.0b -- Limite de desplazamiento bayesiano` (`\label{lem:limite_desplazamiento_bayesiano}`)
    - Funcion matematica prevista: dar una version acumulada o preparatoria de la cota bayesiana.
    - Dependencias previstas: `\mathcal U_R`.
    - Habilita: proposicion 1.1.

26. `Proposicion 1.1 -- Inalcanzabilidad en tiempo finito` (`\label{prop:inalcanzabilidad_tiempo_finito}`)
    - Funcion matematica prevista: deducir una cota de radio alcanzable en `t` pasos.
    - Dependencias previstas: lemas 1.0a y 1.0b.
    - Habilita: definicion 2.4.

27. `Definicion 2.4 -- Variable de ordenamiento`
    - Funcion matematica prevista: introducir una variable de decision para elegir el orden Bayes/Markov.

28. `Definicion 2.5 -- Costos secuenciales ordenados`
    - Funcion matematica prevista: asociar costos a los ordenes de composicion.

29. `Definicion 2.6 -- Q-funciones por orden` (`\label{def:Q_funciones}`)
    - Funcion matematica prevista: definir funciones de accion-valor para los dos ordenes.

30. `Proposicion 2.2 -- Continuidad local de la funcion de valor` (`\label{prop:continuidad_valor}`)
    - Funcion matematica prevista: continuidad local de la funcion de valor bajo las cotas anteriores.

31. `Seccion 3 -- Defecto de ordenamiento`
    - Funcion matematica prevista: desarrollar formulas y cotas del defecto `\mathcal D_{K,L}`.

32. `Lema 3.0 -- Formula explicita del defecto \mathcal{D}_{K,L}(X)` (`\label{lem:defecto_explicito}`)
    - Funcion matematica prevista: expansion algebraica de `\mathcal D_{K,L}(X)`.

33. `Proposicion 3.3 -- Caso n=2: defecto escalar y subvariedad de conmutacion` (`\label{prop:defecto_n2}`)
    - Funcion matematica prevista: caracterizacion algebraica completa en dimension 2.

34. `Lema 3.4 -- Lipschitz local de D_{\mathrm{KL}}(P\|\cdot)` (`\label{lem:lipschitz_kl_local}`)
    - Funcion matematica prevista: control local de KL en el segundo argumento.

35. `Definicion -- Defecto de primer paso \delta_{K,L}(X)` (`\label{def:defecto_primer_paso}`)
    - Funcion matematica prevista: medir el desacuerdo de la primera aplicacion `XK` versus `B_L(X)`.

36. `Lema 3.4b -- Lipschitz conjunto de D_{\mathrm{KL}}(\cdot\|\cdot)` (`\label{lem:lipschitz_kl_conjunto}`)
    - Funcion matematica prevista: control conjunto de KL en ambos argumentos.

37. `Proposicion 3.4 -- Cota de suboptimalidad de un paso` (`\label{prop:cota_subopt_un_paso}`)
    - Funcion matematica prevista: ligar desplazamiento y costo de un solo paso.

38. `Lema 3.5'' -- Diferencia de costos secuenciales` (`\label{lem:diferencia_costos_secuenciales}`)
    - Funcion matematica prevista: comparar costos de ordenes distintos.

39. `Teorema 3.3'' -- Cota de suboptimalidad multi-paso (Q-funcion)` (`\label{teo:subopt_multi_paso}`)
    - Funcion matematica prevista: version multi-paso de la cota de suboptimalidad.

40. `Observacion -- Dos defectos, dos fuentes de suboptimalidad` (`\label{obs:dos_defectos}`)
    - Funcion matematica prevista: separar defecto de primer paso y defecto de ordenamiento.

41. `Seccion 4 -- Caracterizacion del defecto en n=2 y relevancia cuantitativa en n=3`
    - Funcion matematica prevista: cerrar el analisis exacto en dimension 2 y exhibir ejemplo numerico en dimension 3.

42. `Teorema -- Caracterizacion de \mathcal{D}_{K,L}\equiv 0 para n=2` (`\label{teo:caracterizacion_n2}`)
    - Funcion matematica prevista: identificar cuando el defecto desaparece identicamente.

43. `Corolario -- Cota de grado para \mathcal{M}_{K,L}` (`\label{cor:cota_grado}`)
    - Funcion matematica prevista: acotar el conjunto de ceros en dimension 2.

44. `Proposicion -- \mathcal{M}_{K,L}\cap(0,1)=\emptyset para \rho\le 0` (`\label{prop:vacio_rho_no_positivo}`)
    - Funcion matematica prevista: mostrar ausencia de ceros bajo una condicion estructural.

45. `Observacion -- Caso \rho>0` (`\label{obs:caso_rho_positivo}`)
    - Funcion matematica prevista: registrar el comportamiento fuera del caso monotono.

46. `Problema -- Desigualdad \phi(z(x))>\rho\,\phi(x) para \rho\in(0,1)` (`\label{prob:phi_rho}`)
    - Funcion matematica prevista: dejar una desigualdad pendiente que ampliaria el resultado anterior.

47. `Ejemplo -- Relevancia cuantitativa del defecto, n=3` (`\label{ej:n3_relevancia}`)
    - Funcion matematica prevista: mostrar que el defecto cambia cuantitativamente el costo de control.

48. `Corolario -- Sintesis: caracterizacion y relevancia` (`\label{cor:sintesis_n2_n3}`)
    - Funcion matematica prevista: condensar los resultados de n=2 y n=3.

## Advertencias globales

- No activar el bloque comentado sin reemplazar el lenguaje de `velocidad` por `cota de desplazamiento por paso`.
- No introducir `\sigma_t`, Bellman, costos ni `Q` antes de que el bloque de control quede estructuralmente definido.
- No poner citas dentro de lemas, proposiciones o demostraciones.
- Las referencias contextuales deben quedarse en observaciones.

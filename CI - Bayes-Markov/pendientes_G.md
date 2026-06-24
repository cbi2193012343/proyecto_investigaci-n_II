# Pendientes G

Estado resumido del trabajo en la Seccion G. Este archivo no modifica el `.tex`; solo deja rastreo de lo ya corregido, lo que sigue incompleto y el siguiente bloque matematico recomendado.

## Bloques ya corregidos

- `Clases admisibles y ventanas de control`
- `Correccion bayesiana admisible`
- `Correccion markoviana admisible`
- `Posibilidad de composicion sobre una base probabilistica comun`
- `Sentido Bayes--Markov`
- `Composicion Bayes--Markov sobre una cadena observada`
- `Sentido Markov--Bayes`
- `Composicion Markov--Bayes sobre una cadena observada`
- `Conmutacion global bajo positividad uniforme`
- `Falla de conmutacion global para verosimilitudes no constantes`
- `De la falla global al defecto de ordenamiento`
- `Defecto de ordenamiento`
- `Del defecto de ordenamiento a las cotas de desplazamiento por paso`
- `Cota de desplazamiento bayesiana por paso y control logaritmico de la verosimilitud`
- `Cota de desplazamiento bayesiano por paso`
- `Cota de desplazamiento markoviana por paso y variacion total`
- `Cota de desplazamiento markoviano por paso`
- `Control con variable de ordenamiento`
- `Accion admisible con variable de ordenamiento`
- `Transiciones controladas por orden`
- `Costos de etapa ordenados`
- `Funcion de valor y funciones de accion--valor por orden`

## Bloques incompletos

- Todo el bloque comentado que sigue a `\begin{comment}`.
- En particular, el inicio del bloque comentado sigue siendo un placeholder y debe migrar a lenguaje de cotas de desplazamiento por paso.
- La proposicion de inalcanzabilidad en tiempo finito aun no esta integrada en el bloque activo.
- La parte comentada que comienza con la inalcanzabilidad en tiempo finito sigue pendiente de activacion.

## Etiquetas pendientes

- En el bloque comentado siguen esperando activacion:
  - `lem:limite_desplazamiento_markoviano`
  - `lem:limite_desplazamiento_bayesiano`
  - `prop:inalcanzabilidad_tiempo_finito`
  - `def:Q_funciones`
  - `prop:continuidad_valor`
  - `lem:defecto_explicito`
  - `prop:defecto_n2`
  - `lem:lipschitz_kl_local`
  - `def:defecto_primer_paso`
  - `lem:lipschitz_kl_conjunto`
  - `prop:cota_subopt_un_paso`
  - `lem:diferencia_costos_secuenciales`
  - `teo:subopt_multi_paso`
  - `obs:dos_defectos`
  - `teo:caracterizacion_n2`
  - `cor:cota_grado`
  - `prop:vacio_rho_no_positivo`
  - `obs:caso_rho_positivo`
  - `prob:phi_rho`
  - `ej:n3_relevancia`
  - `cor:sintesis_n2_n3`

## Citas pendientes

- En el bloque activo de G, las citas contextuales `Sprungk2020` y `GaubertQu2014` ya estan definidas en la bibliografia local.
- En el bloque activo de control ya estan definidas las citas `Todorov2009EfficientComputationOptimalActions` y `Kappen2005LinearTheoryForControlOfNonLinearStochasticSystems`.
- En otras partes del documento siguen apareciendo advertencias de citacion para:
  - `DonovanMickey2019`
  - `MartinHong2018`
  - `Norris1997`
- Esas citas no pertenecen al bloque activo de G, pero conviene resolverlas despues si se quiere una compilacion limpia total.

## Palabras o expresiones que deben evitarse

- `velocidad`
- `rapidez`
- `limite de velocidad`
- `velocidad fisica`
- `derivada temporal`
- `Bellman`
- `sigma_t`

Sustitutos recomendados:

- `cota de desplazamiento por paso`
- `desplazamiento elemental`
- `desplazamiento acumulado`
- `radio alcanzable`

## Siguiente bloque matematico recomendado

- Activar y reescribir el bloque comentado que inicia con `Seccion 1` como primer bloque de cotas acumuladas e inalcanzabilidad.
- El objetivo inmediato deberia ser introducir la proposicion de inalcanzabilidad en tiempo finito a partir de `v_B(R)=e^{2R}-1` y `v_M(\varepsilon)=2(1-\varepsilon)`.
- Despues de eso, el siguiente paso natural es revisar la coherencia interna entre el bloque activo de control y el bloque comentado que sigue.

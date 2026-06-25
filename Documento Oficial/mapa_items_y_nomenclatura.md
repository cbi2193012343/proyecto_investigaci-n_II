# Mapa de items, hipótesis y nomenclatura

Archivo fuente: `Control Informacional.tex`

Objetivo de este documento: inventariar los items formales del manuscrito, indicar su función, registrar la notación que introducen o usan, y resumir los items demostrables en el esquema `Hipótesis -> Consecuencias`. Este mapa sirve como base para revisar si hay símbolos, nombres o términos que aparecen sin una función clara dentro de una definición, hipótesis, consecuencia o demostración.

Convención usada:

- **Definición / Observación:** se registra función y elementos.
- **Lema / Proposición / Corolario / Teorema / Ejercicio:** se registra función, elementos, `Hipótesis -> Consecuencias` e idea breve de demostración.
- **Elementos:** símbolos, operadores, conjuntos, parámetros o nombres técnicos relevantes.

## Sección 1 -- Fundamentos probabilísticos y geométricos del control informacional

### Subsección 1.1 -- Probabilidad, particiones y símplex

#### Observación inicial sobre medida y estado discreto

- **Función:** separar conceptualmente la medida original `P` del estado discreto inducido por una partición.
- **Elementos:** `(\Omega,\mathcal F,P)`, partición `\Pi`, estado discreto `X`.

#### Definición `def:espacio_prob` -- Espacio de probabilidad

- **Función:** fijar el dominio probabilístico base.
- **Elementos:** `\Omega`, `\mathcal F`, `P`, condición `P(\Omega)=1`.

#### Definición `def:particion` -- Partición medible finita

- **Función:** introducir la discretización finita del espacio de probabilidad.
- **Elementos:** `\Pi=\{E_1,\dots,E_n\}`, disjunción, cobertura de `\Omega`, no degeneración `P(E_i)>0`.

#### Observación sobre no degeneración

- **Función:** justificar por qué la positividad estricta no pertenece a la definición general, pero será necesaria para cocientes y logaritmos.
- **Elementos:** no degeneración, cocientes, logaritmos.

#### Definición `def:simplex` -- Símplex de probabilidad e interior

- **Función:** definir el espacio geométrico de estados.
- **Elementos:** `\Delta_n`, `\Delta_n^\circ`, coordenadas no negativas, suma unitaria, positividad estricta.

#### Observación sobre dominio general e interior

- **Función:** distinguir entre el dominio general `\Delta_n` y el dominio positivo `\Delta_n^\circ`.
- **Elementos:** `\Delta_n`, `\Delta_n^\circ`, cocientes, logaritmos.

#### Definición `def:estado` -- Estado informacional discreto

- **Función:** pasar de una partición medible finita a un vector de probabilidades.
- **Elementos:** `X=(X_1,\dots,X_n)`, `X_i=P(E_i)`, `\Pi`.

#### Proposición `prop:estado_simplex` -- Estado inducido en el símplex

- **Función:** verificar que el estado discreto pertenece al símplex.
- **Elementos:** `X`, `\Delta_n`, `\Delta_n^\circ`, partición no degenerada.
- **Hipótesis -> Consecuencias:** si `X_i=P(E_i)` para una partición finita, entonces `X\in\Delta_n`; si además `P(E_i)>0` para todo `i`, entonces `X\in\Delta_n^\circ`.
- **Idea breve de demostración:** usar no negatividad de la medida y aditividad sobre la unión disjunta de la partición.

#### Observación sobre dependencia de la partición

- **Función:** aclarar que `X` no representa toda la medida `P`, sino su agregación sobre `\Pi`.
- **Elementos:** `P`, `X`, `\Pi`, clases de observación.

### Subsección 1.2 -- Correcciones locales y cambio de medida

#### Definición `def:CX` -- Correcciones admisibles en `X`

- **Función:** definir perturbaciones locales que preservan no negatividad y masa total.
- **Elementos:** `C(X)`, `Y`, condiciones `X_i(1+Y_i)\ge 0`, `\sum_i X_i(1+Y_i)=1`.

#### Observación `obs:neutralidad` -- Neutralidad de masa

- **Función:** derivar la condición equivalente `\sum_i X_iY_i=0`.
- **Elementos:** `Y\in C(X)`, neutralidad de masa, producto ponderado por `X`.

#### Definición `def:Tloc` -- Operador informacional local

- **Función:** definir la actualización local inducida por una corrección admisible.
- **Elementos:** `T_Y^{\mathrm{loc}}(X)`, `X_i(1+Y_i)`, `Y\in C(X)`.

#### Observación `obs:frontera` -- Comportamiento en la frontera

- **Función:** aclarar que si `X_i=0`, la coordenada permanece en cero bajo el operador local.
- **Elementos:** frontera de `\Delta_n`, soporte, coordenadas nulas.

#### Proposición `prop:preservacionLocal` -- Preservación local del símplex

- **Función:** garantizar que `T_Y^{\mathrm{loc}}(X)` es un estado probabilístico.
- **Elementos:** `X`, `Y\in C(X)`, `T_Y^{\mathrm{loc}}`.
- **Hipótesis -> Consecuencias:** si `X\in\Delta_n` y `Y\in C(X)`, entonces `T_Y^{\mathrm{loc}}(X)\in\Delta_n`.
- **Idea breve de demostración:** las desigualdades de admisibilidad dan coordenadas no negativas y la condición de normalización da suma uno.

#### Proposición `prop:QYprobabilidad` -- Cambio de medida discreto inducido

- **Función:** construir una nueva medida discreta a partir de una corrección local.
- **Elementos:** `Q_Y`, partición `\Pi`, masas `Q_Y(E_i)=P(E_i)(1+Y_i)`.
- **Hipótesis -> Consecuencias:** si `Y\in C(X)` y `X_i=P(E_i)`, entonces `Q_Y` define una probabilidad sobre la partición.
- **Idea breve de demostración:** verificar no negatividad y suma total uno; extender por aditividad finita sobre uniones de celdas.

#### Proposición `prop:compatibilidadCambioMedida` -- Compatibilidad entre operador local y cambio de medida

- **Función:** identificar la actualización local con las masas de la medida `Q_Y`.
- **Elementos:** `T_Y^{\mathrm{loc}}(X)`, `Q_Y(E_i)`, partición.
- **Hipótesis -> Consecuencias:** si `Q_Y` se construye con `Y`, entonces `T_Y^{\mathrm{loc}}(X)_i=Q_Y(E_i)`.
- **Idea breve de demostración:** comparar directamente las dos fórmulas coordenada a coordenada.

#### Observación final de la subsección

- **Función:** interpretar el operador local como representación discreta de cambio de medida.
- **Elementos:** `Q_Y`, `T_Y^{\mathrm{loc}}`, partición original.

### Subsección 1.3 -- Operadores globales multiplicativos y composición

#### Definición `def:Cglob` -- Correcciones globales

- **Función:** definir factores multiplicativos positivos independientes del estado base.
- **Elementos:** `C_{\mathrm{glob}}`, `Y`, condición `1+Y_i>0`.

#### Definición `def:Tglobal` -- Operador informacional global

- **Función:** introducir la actualización multiplicativa normalizada.
- **Elementos:** `T_Y(X)`, `X_i(1+Y_i)/\sum_k X_k(1+Y_k)`, `X\in\Delta_n^\circ`.

#### Observación `obs:Tglobal-frontera` -- Extensión a la frontera

- **Función:** señalar que la fórmula tiene sentido en `\Delta_n`, aunque la estructura algebraica se estudie en el interior.
- **Elementos:** `\Delta_n`, `\Delta_n^\circ`, factores positivos.

#### Proposición `prop:interiorGlobal` -- Preservación del interior

- **Función:** asegurar que los operadores globales permanecen dentro del dominio positivo.
- **Elementos:** `T_Y`, `C_{\mathrm{glob}}`, `\Delta_n^\circ`.
- **Hipótesis -> Consecuencias:** si `X\in\Delta_n^\circ` y `Y\in C_{\mathrm{glob}}`, entonces `T_Y(X)\in\Delta_n^\circ`.
- **Idea breve de demostración:** cada coordenada es positiva por producto de positivos y el denominador normaliza a suma uno.

#### Observación `obs:localVsGlobal` -- Relación con operador local

- **Función:** comparar corrección local y corrección global normalizada.
- **Elementos:** `T_Y^{\mathrm{loc}}`, `T_Y`, renormalización, estado base.

#### Definición `def:G` -- Familia global de operadores

- **Función:** nombrar la familia de transformaciones globales inducidas por correcciones positivas.
- **Elementos:** `\mathcal G`, operadores `T_Y`, `Y\in C_{\mathrm{glob}}`.

#### Proposición `prop:composicionGlobal` -- Ley de composición

- **Función:** demostrar que la composición de operadores globales corresponde al producto coordenado de factores.
- **Elementos:** `T_Y`, `T_Z`, factor compuesto `(1+Y_i)(1+Z_i)`, `\mathcal G`.
- **Hipótesis -> Consecuencias:** si `Y,Z\in C_{\mathrm{glob}}`, entonces `T_Z\circ T_Y` es otro operador global con factor multiplicativo compuesto.
- **Idea breve de demostración:** sustituir la fórmula de `T_Y`, aplicar `T_Z`, cancelar normalizadores y reconocer el producto coordenado.

#### Corolario -- Estructura de grupo abeliano

- **Función:** registrar la estructura algebraica de la familia de operadores globales.
- **Elementos:** identidad, inverso, conmutatividad, producto coordenado.
- **Hipótesis -> Consecuencias:** bajo composición, la familia global forma un grupo abeliano.
- **Idea breve de demostración:** la composición se reduce al producto coordenado de factores positivos, que es asociativo, conmutativo y tiene inversos positivos.

#### Observación `obs:coordenadasLog` -- Coordenadas log-multiplicativas

- **Función:** interpretar productos multiplicativos como sumas en coordenadas logarítmicas.
- **Elementos:** factores positivos, logaritmos, estructura aditiva.

### Subsección 1.4 -- Divergencia KL, métrica de Fisher y dinámica inducida

#### Definición `def:KL` -- Divergencia de Kullback--Leibler discreta

- **Función:** introducir el funcional informacional principal.
- **Elementos:** `D_{\mathrm{KL}}(P\|X)`, `P`, `X`, suma `\sum_i P_i\log(P_i/X_i)`.

#### Observación `obs:KLsoporte` -- Dominio de `E_P`

- **Función:** fijar el interior como dominio para evitar singularidades logarítmicas.
- **Elementos:** `E_P`, `P\in\Delta_n^\circ`, `X\in\Delta_n^\circ`.

#### Definición `def:tangente` -- Espacio tangente del símplex

- **Función:** definir las direcciones admisibles de variación.
- **Elementos:** `T_X\Delta_n`, vectores `u`, condición `\sum_i u_i=0`.

#### Observación sobre independencia de `X`

- **Función:** notar que el espacio tangente es el mismo subespacio lineal para todo punto interior.
- **Elementos:** hiperplano de suma cero, `T_X\Delta_n`.

#### Definición `def:Fisher` -- Métrica de Fisher discreta

- **Función:** introducir la geometría riemanniana del interior del símplex.
- **Elementos:** `g_X(u,v)=\sum_i u_iv_i/X_i`, `T_X\Delta_n`.

#### Definición `def:gradienteFisher` -- Gradiente riemanniano respecto de Fisher

- **Función:** definir el gradiente usado para la dinámica.
- **Elementos:** `\mathrm{grad}_gE`, diferencial `dE_X`, métrica `g_X`.

#### Proposición `prop:gradKL` -- Gradiente Fisher de KL

- **Función:** calcular explícitamente el gradiente de `E_P`.
- **Elementos:** `E_P(X)=D_{\mathrm{KL}}(P\|X)`, `\mathrm{grad}_gE_P`, `X-P`.
- **Hipótesis -> Consecuencias:** si `P,X\in\Delta_n^\circ`, entonces `\mathrm{grad}_gE_P(X)=X-P`.
- **Idea breve de demostración:** derivar `E_P` en una dirección tangente, expresar el diferencial con `g_X`, y usar la condición de suma cero para identificar el vector tangente.

#### Definición `def:flujoFisherKL` -- Flujo de gradiente Fisher--KL

- **Función:** definir la ecuación continua de descenso.
- **Elementos:** `\dot X(t)=-\mathrm{grad}_gE_P(X(t))`, equivalente `\dot X=P-X`.

#### Proposición `prop:solucionExplicita` -- Solución explícita del flujo

- **Función:** resolver la dinámica continua hacia `P`.
- **Elementos:** `X(t)`, `X(0)`, `P`, exponencial `e^{-t}`.
- **Hipótesis -> Consecuencias:** si `X(0)\in\Delta_n^\circ`, entonces `X(t)=P+e^{-t}(X(0)-P)` y permanece en `\Delta_n^\circ`.
- **Idea breve de demostración:** resolver coordenada a coordenada la ecuación lineal `\dot X=P-X` y verificar positividad por combinación convexa.

#### Proposición `prop:Hteorema` -- Monotonicidad de `E_P`

- **Función:** mostrar disipación de KL a lo largo del flujo.
- **Elementos:** `E_P(X(t))`, `\mathrm{grad}_gE_P`, norma Fisher.
- **Hipótesis -> Consecuencias:** a lo largo del flujo Fisher--KL, `E_P` decrece y sólo es estacionaria en `X=P`.
- **Idea breve de demostración:** derivar `E_P(X(t))` y usar la identidad de descenso `-\|\mathrm{grad}_gE_P\|_g^2`.

#### Proposición `prop:minimoGlobalKL` -- Mínimo global de `E_P`

- **Función:** caracterizar el equilibrio como minimizador único.
- **Elementos:** `E_P`, `D_{\mathrm{KL}}`, `P`.
- **Hipótesis -> Consecuencias:** para todo `X\in\Delta_n^\circ`, `E_P(X)\ge 0`, con igualdad si y sólo si `X=P`.
- **Idea breve de demostración:** aplicar la desigualdad de Gibbs para KL.

#### Teorema `teo:equivalenciaCD` -- Equivalencia estructural entre operadores globales y dinámica Fisher--KL

- **Función:** conectar correcciones multiplicativas, pasos discretos y flujo Fisher--KL.
- **Elementos:** `Y^*(X,P)`, `T_{\alpha Y}`, `X_{k+1}`, `\dot X=P-X`.
- **Hipótesis -> Consecuencias:** bajo positividad e interior, la corrección ideal, la iteración discreta y el flujo continuo representan la misma dirección estructural hacia `P`.
- **Idea breve de demostración:** calcular la corrección ideal coordenada a coordenada, expandir el operador global para paso pequeño y comparar con el gradiente Fisher calculado previamente.

## Sección 5 -- Semántica bayesiana

### Definición `def:espacio_conjunto` -- Espacio Bayesiano

- **Función:** fijar el dominio conjunto de hipótesis y observaciones.
- **Elementos:** `\Pi_H`, `\Pi_E`, `H_i`, `E_j`, estado previo `X_i=P(H_i)`.

### Definición `def:prob_condicional` -- Probabilidad condicional

- **Función:** definir la verosimilitud elemental de observación dada hipótesis.
- **Elementos:** `P(E_j\mid H_i)`, compatibilidad `P(H_i\cap E_j)>0`.

### Definición `def:verosimilitud` -- Verosimilitud como corrección global

- **Función:** traducir una observación en factor multiplicativo.
- **Elementos:** `\ell^{(j)}`, `\ell_i^{(j)}=P(E_j\mid H_i)`, `Y^{\ell^{(j)}}`.

### Proposición `prop:bayes_como_TY` -- Operador bayesiano como caso particular de `T_Y`

- **Función:** demostrar que Bayes es una instancia del operador global.
- **Elementos:** `T_{Y^{\ell^{(j)}}}`, posterior `P(H_i\mid E_j)`, verosimilitud.
- **Hipótesis -> Consecuencias:** si la verosimilitud es positiva y `P(E_j)>0`, entonces `T_Y(X)` coincide con el posterior bayesiano.
- **Idea breve de demostración:** sustituir `X_i=P(H_i)` y `\ell_i=P(E_j\mid H_i)` en `T_Y`; el denominador es `P(E_j)` por la ley total.

### Proposición `prop:unicidad_bayes` -- Unicidad del operador coherente con `P`

- **Función:** mostrar que la actualización bayesiana queda determinada por la probabilidad conjunta.
- **Elementos:** `P`, `T_{Y^{\ell^{(j)}}}`, posterior.
- **Hipótesis -> Consecuencias:** si un operador reproduce la actualización condicional coherente con `P`, entonces coincide con `T_{Y^{\ell^{(j)}}}`.
- **Idea breve de demostración:** la fórmula de Bayes fija de manera única cada coordenada posterior.

### Corolario `cor:bayes_secuencial` -- Actualización secuencial como composición en `\mathcal G`

- **Función:** interpretar una secuencia de evidencias como composición de operadores globales.
- **Elementos:** `\mathcal G`, verosimilitudes sucesivas, producto de factores.
- **Hipótesis -> Consecuencias:** una sucesión de actualizaciones bayesianas con verosimilitudes positivas corresponde a un operador global con factor producto.
- **Idea breve de demostración:** aplicar la ley de composición global de la Subsección 1.3.

### Observación -- Criterio medible para discretización paramétrica

- **Función:** justificar que las masas por celdas pueden expresarse como integrales.
- **Elementos:** conjuntos borelianos, funciones indicadoras, integral de Lebesgue.

### Definición `def:particion_parametrica` -- Partición paramétrica uniforme

- **Función:** definir una discretización regular de un dominio paramétrico.
- **Elementos:** `\Omega`, celdas `E_i`, orden `n`.

### Proposición `prop:estado_parametrico_simplex` -- Estado previo inducido

- **Función:** verificar que las masas de una partición paramétrica forman un estado.
- **Elementos:** `X_i=P_0(E_i)`, `\Pi_n`, `\Delta_n`.
- **Hipótesis -> Consecuencias:** si `\Pi_n` es partición medible y `P_0` es probabilidad, entonces `X\in\Delta_n`; si todas las celdas tienen masa positiva, `X\in\Delta_n^\circ`.
- **Idea breve de demostración:** repetir el argumento de suma de masas de una partición finita.

### Observación -- Promedio condicional de la verosimilitud

- **Función:** explicar por qué una verosimilitud continua se resume por promedios en celdas.
- **Elementos:** `\ell`, `\int_{E_i}\ell\,dP_0`, normalización.

### Definición `def:verosimilitud_global` -- Verosimilitud discreta inducida

- **Función:** construir el vector de verosimilitudes por celda.
- **Elementos:** `\ell_i`, `P_0(E_i)`, integral sobre `E_i`.

### Proposición `prop:admisibilidad_verosimilitud_global` -- Admisibilidad de la corrección

- **Función:** garantizar que la verosimilitud discretizada define una corrección global.
- **Elementos:** `\ell_i`, `Y^\ell`, `C_{\mathrm{glob}}`.
- **Hipótesis -> Consecuencias:** si los promedios de verosimilitud son positivos y finitos, entonces `Y^\ell\in C_{\mathrm{glob}}`.
- **Idea breve de demostración:** positividad de cada `\ell_i` implica positividad de cada factor `1+Y_i^\ell`.

### Observación -- Radon--Nikodym y posterior

- **Función:** ubicar la construcción posterior como densidad normalizada respecto de `P_0`.
- **Elementos:** `\ell/Z`, `Z=\int_\Omega \ell\,dP_0`, continuidad absoluta.

### Lema `lem:verosimilitud_cambio_medida` -- Cambio de medida exacto por celdas

- **Función:** conectar posterior continua y masas discretas por celda.
- **Elementos:** `P_1`, `P_0`, `\ell/Z`, celdas `E_i`.
- **Hipótesis -> Consecuencias:** si `dP_1=(\ell/Z)dP_0`, entonces `P_1(E_i)` coincide con la normalización de los pesos `\int_{E_i}\ell\,dP_0`.
- **Idea breve de demostración:** integrar la densidad posterior sobre cada celda y dividir por el normalizador global.

### Observación -- Identidad entre actualización bayesiana y operador global

- **Función:** anticipar que el operador global recupera las masas posteriores.
- **Elementos:** `T_Y`, posterior por celdas, verosimilitud discreta.

### Proposición `prop:bayes_parametrico` -- Actualización bayesiana paramétrica en CI

- **Función:** demostrar que el operador global reproduce la discretización posterior.
- **Elementos:** `P_0`, `P_1`, `\Pi_n`, `X`, `T_Y(X)`.
- **Hipótesis -> Consecuencias:** si la posterior se define por una verosimilitud continua positiva, entonces el estado posterior discreto es `T_Y(X)`.
- **Idea breve de demostración:** usar el lema de cambio de medida por celdas y comparar con la fórmula del operador global.

### Observación -- Familias exponenciales y separación de niveles

- **Función:** separar conjugación continua de recuperación discreta de masas.
- **Elementos:** familia exponencial, parámetro natural, operador global.

### Proposición `prop:conjugado_exponencial_CI` -- Modelo conjugado exponencial

- **Función:** mostrar que la conjugación exponencial encaja en el marco CI.
- **Elementos:** parámetro natural, densidad previa, verosimilitud, posterior, partición.
- **Hipótesis -> Consecuencias:** si el producto previa-verosimilitud conserva la familia exponencial, entonces la posterior discreta sobre la partición se obtiene por el operador global.
- **Idea breve de demostración:** sumar parámetros naturales en el nivel continuo y aplicar la discretización por celdas ya probada.

### Definición `def:Tell_trayectorias` -- Operador bayesiano inducido por verosimilitud

- **Función:** abreviar `T_{Y^\ell}` como operador bayesiano asociado a `\ell`.
- **Elementos:** `T_\ell`, `Y^\ell`, `\ell\in\mathbb R_{>0}^n`.

### Definición -- Objetivo bayesiano interior

- **Función:** definir el estado objetivo para trayectorias bayesianas.
- **Elementos:** `\mathcal P`, `\Delta_n^\circ`, objetivo sobre hipótesis.

### Corolario -- Realización bayesiana del paso discreto determinista

- **Función:** identificar la verosimilitud que llevaría de `X` a `\mathcal P` en un paso.
- **Elementos:** `\ell_i=\mathcal P_i/X_i`, `T_\ell(X)=\mathcal P`.
- **Hipótesis -> Consecuencias:** si `X,\mathcal P\in\Delta_n^\circ`, entonces existe una verosimilitud positiva que realiza el salto exacto.
- **Idea breve de demostración:** sustituir `\ell_i=\mathcal P_i/X_i`; el producto `X_i\ell_i` da `\mathcal P_i` y el normalizador vale uno.

### Observación -- Selección observacional guiada

- **Función:** motivar la elección activa de observaciones por cercanía al objetivo.
- **Elementos:** observaciones disponibles, posterior inducido, divergencia KL.

### Definición -- Familia observacional admisible y posterior inducido

- **Función:** definir el conjunto de observaciones seleccionables y su posterior asociado.
- **Elementos:** `\mathcal E_t`, `E`, `\ell^{(E)}`, `X_t^E`.

### Definición -- Coeficiente de avance KL

- **Función:** medir la reducción relativa de divergencia hacia el objetivo.
- **Elementos:** `\alpha_{\mathrm{KL}}`, `D_{\mathrm{KL}}(\mathcal P\|X_t)`, `X_t^E`.

### Proposición -- Elección observacional óptima

- **Función:** caracterizar la observación que maximiza avance como la que minimiza KL posterior.
- **Elementos:** `E_t^\star`, `\alpha_{\mathrm{KL}}`, `D_{\mathrm{KL}}`.
- **Hipótesis -> Consecuencias:** si el denominador de avance es positivo, maximizar `\alpha_{\mathrm{KL}}` equivale a minimizar `D_{\mathrm{KL}}(\mathcal P\|X_t^E)`.
- **Idea breve de demostración:** el término inicial no depende de `E`; la transformación `1 - a/constante` invierte monotonía respecto de `a`.

### Definición -- Trayectoria bayesiana guiada por selección

- **Función:** definir la dinámica discreta inducida por elegir observaciones óptimas.
- **Elementos:** `X_{t+1}`, `E_t^\star`, `\mathcal E_t`, `\mathcal P`.

### Proposición -- Disipación y convergencia bajo progreso acumulado

- **Función:** dar una condición suficiente para converger al objetivo.
- **Elementos:** `\eta_t`, producto `\prod_t(1-\eta_t)`, KL, Pinsker.
- **Hipótesis -> Consecuencias:** si cada paso reduce KL por un factor acumulativamente disipativo, entonces `X_t\to\mathcal P`.
- **Idea breve de demostración:** iterar la desigualdad de reducción de KL y convertir convergencia KL en convergencia `\ell^1` mediante Pinsker.

### Ejercicio `ej:validacion_patogeno` -- Priorización secuencial de pruebas

- **Función:** ejemplificar la selección observacional con pruebas diagnósticas.
- **Elementos:** `X_0`, `\mathcal P`, `\ell^{(I)}`, `\ell^{(II)}`, `\ell^{(III)}`, `\delta`.
- **Hipótesis -> Consecuencias:** dadas pruebas disponibles por día y objetivo, se selecciona la prueba con mayor reducción KL y se verifica si se alcanza el umbral.
- **Idea breve de solución:** calcular posteriores normalizados para cada prueba disponible, comparar divergencias KL y elegir la menor.

## Sección 6 -- Semántica markoviana

### Definición `def:base_discreta_markov` -- Base discreta

- **Función:** fijar el conjunto finito de estados markovianos.
- **Elementos:** `I=\{1,\dots,n\}`, variable discreta.

### Lema `lem:distribucion_inducida_particion` -- Distribución inducida por partición

- **Función:** relacionar particiones y distribuciones finitas.
- **Elementos:** `Z`, `I`, `H_i`, vector de ley.
- **Hipótesis -> Consecuencias:** si una variable finita induce celdas medibles, sus probabilidades forman un vector del símplex.
- **Idea breve de demostración:** aplicar no negatividad y suma total sobre la partición inducida.

### Definición `def:Sn_markov` -- Matrices estocásticas por filas

- **Función:** definir los kernels markovianos usados.
- **Elementos:** `\mathcal S_n`, matriz `K`, `K_{ij}\ge0`, `\sum_jK_{ij}=1`.

### Observación -- Lectura markoviana

- **Función:** interpretar `K_{ij}` como probabilidad de transición.
- **Elementos:** `K`, estados `i,j`, operador fila.

### Proposición `prop:simplex_invariante_markov` -- Invarianza del símplex

- **Función:** probar que aplicar un kernel conserva distribuciones.
- **Elementos:** `XK`, `K\in\mathcal S_n`, `\Delta_n`.
- **Hipótesis -> Consecuencias:** si `X\in\Delta_n` y `K` es estocástica por filas, entonces `XK\in\Delta_n`.
- **Idea breve de demostración:** no negatividad por suma de no negativos; suma unitaria usando que cada fila de `K` suma uno.

### Observación `obs:interior_markov` -- Interior y correcciones locales

- **Función:** explicar cuándo el paso markoviano permite definir cocientes locales.
- **Elementos:** `X_i>0`, `(XK)_i/X_i`, interior.

### Proposición `prop:markov_como_correccion_local` -- Representación local de un paso markoviano

- **Función:** escribir `XK` como actualización local alrededor de `X`.
- **Elementos:** `Y^K(X)`, `XK`, `C(X)`, `T_Y^{\mathrm{loc}}`.
- **Hipótesis -> Consecuencias:** si `X\in\Delta_n^\circ` y `K\in\mathcal S_n`, existe `Y^K(X)\in C(X)` tal que `T_{Y^K(X)}^{\mathrm{loc}}(X)=XK`.
- **Idea breve de demostración:** definir `1+Y_i=(XK)_i/X_i`; sustituir y usar invarianza del símplex.

### Proposición `prop:markov_no_global` -- No globalidad de operador markoviano no trivial

- **Función:** mostrar que los pasos markovianos no suelen ser correcciones globales independientes de `X`.
- **Elementos:** `K`, `T_Y`, matriz identidad, factores globales.
- **Hipótesis -> Consecuencias:** salvo casos triviales, no existe un único factor multiplicativo global que represente `X\mapsto XK` para todo `X`.
- **Idea breve de demostración:** comparar la forma racional multiplicativa de `T_Y` con la acción lineal de `K` sobre varios estados; la igualdad global fuerza restricciones que llevan al caso trivial.

### Observación `obs:local_vs_global` -- Local frente a global

- **Función:** sintetizar la diferencia entre Markov local y Bayes global.
- **Elementos:** `Y^K(X)`, verosimilitud bayesiana, dependencia del estado base.

### Definición `def:estacionaria_markov` -- Distribución estacionaria

- **Función:** definir equilibrio markoviano.
- **Elementos:** `\pi`, `\pi K=\pi`, `\Delta_n^\circ`.

### Observación `obs:estacionaria_correccion_nula`

- **Función:** relacionar estacionariedad con corrección local cero.
- **Elementos:** `Y^K(\pi)`, `\pi K=\pi`.

### Lema `lem:estacionaria_implica_interior` -- Estacionariedad positiva

- **Función:** garantizar compatibilidad de la estacionaria con el interior bajo hipótesis de positividad.
- **Elementos:** `K`, `\pi`, `\Delta_n^\circ`.
- **Hipótesis -> Consecuencias:** si `\pi` es estacionaria positiva, entonces pertenece al dominio interior requerido para correcciones locales.
- **Idea breve de demostración:** la positividad se usa directamente para ubicar `\pi` en `\Delta_n^\circ`.

### Proposición `prop:disipacion_KL_markov` -- Disipación KL hacia la estacionaria

- **Función:** mostrar que el paso markoviano no aumenta KL hacia `\pi`.
- **Elementos:** `D_{\mathrm{KL}}(\pi\|X)`, `XK`, estacionaria `\pi`.
- **Hipótesis -> Consecuencias:** si `\pi K=\pi`, entonces la divergencia hacia `\pi` se disipa bajo la evolución markoviana.
- **Idea breve de demostración:** aplicar convexidad/log-sum inequality para comparar antes y después del kernel.

### Proposición `prop:trayectoria_markov_CI` -- Trayectoria markoviana como trayectoria local de CI

- **Función:** insertar una cadena markoviana dentro del formalismo de control informacional.
- **Elementos:** `X_t`, `X_{t+1}=X_tK`, `Y^K(X_t)`.
- **Hipótesis -> Consecuencias:** una trayectoria markoviana interior puede escribirse como sucesión de correcciones locales.
- **Idea breve de demostración:** aplicar la representación local de un paso en cada tiempo.

### Observación `obs:primitividad_convergencia_markov`

- **Función:** recordar que primitividad da convergencia a equilibrio.
- **Elementos:** kernel primitivo, distribución estacionaria única.

### Proposición `prop:convergencia_primitiva_markov` -- Convergencia hacia estacionaria

- **Función:** probar convergencia de la trayectoria markoviana bajo primitividad.
- **Elementos:** `K` primitiva, `X_t=X_0K^t`, `\pi`.
- **Hipótesis -> Consecuencias:** si `K` es primitiva, entonces `X_t\to\pi` y la KL hacia `\pi` tiende a cero.
- **Idea breve de demostración:** usar el teorema clásico de convergencia para matrices primitivas y continuidad de KL en el interior.

## Sección 7 -- Control Óptimo Informacional y Defecto de Ordenamiento

### Observación `obs:base_comun_global_local_BM`

- **Función:** fijar una base probabilística común para comparar órdenes Bayes--Markov y Markov--Bayes.
- **Elementos:** `Z_0`, `I`, `H_a^{(0)}`, kernel `K`, verosimilitud `L`.

### Proposición `prop:composicion_BM_kolmogorov` -- Composición efectiva `B\to M`

- **Función:** formalizar actualizar por Bayes y luego propagar por Markov.
- **Elementos:** `B_L(X)`, `K`, `B_L(X)K`, orden `BM`.
- **Hipótesis -> Consecuencias:** bajo base común, verosimilitud positiva y kernel admisible, la composición `B\to M` produce `B_L(X)K`.
- **Idea breve de demostración:** aplicar primero Bayes por normalización multiplicativa y luego la transición markoviana.

### Observación -- Sentido Markov--Bayes

- **Función:** explicar la lectura predictiva-filtrada del orden `M\to B`.
- **Elementos:** ley predictiva, `XK`, verosimilitud posterior.

### Proposición `prop:composicion_MB_kolmogorov` -- Composición Markov--Bayes

- **Función:** formalizar propagar por Markov y luego actualizar por Bayes.
- **Elementos:** `XK`, `B_L(XK)`, orden `MB`.
- **Hipótesis -> Consecuencias:** bajo las mismas condiciones, la composición `M\to B` produce `B_L(XK)`.
- **Idea breve de demostración:** aplicar primero `K` al estado y luego el operador bayesiano al estado predictivo.

### Proposición `prop:conmutacion_global_MB_BM` -- Conmutación global bajo positividad uniforme

- **Función:** caracterizar cuándo los dos órdenes coinciden globalmente.
- **Elementos:** `K`, `L`, `B_L(XK)`, `B_L(X)K`.
- **Hipótesis -> Consecuencias:** bajo positividad uniforme, la conmutación global fuerza que la verosimilitud no distinga coordenadas.
- **Idea breve de demostración:** imponer igualdad para todo `X` y comparar coordenadas; la positividad de `K` transmite las diferencias y obliga a constancia de `L`.

### Corolario `cor:falla_conmutacion_global_L_no_constante`

- **Función:** registrar que una verosimilitud no constante produce falla de conmutación en algún estado.
- **Elementos:** `L` no constante, defecto de orden.
- **Hipótesis -> Consecuencias:** si `L` no es constante, existe `X` donde `MB` y `BM` difieren.
- **Idea breve de demostración:** contraposición de la proposición de conmutación global.

### Observación -- De falla global a defecto de ordenamiento

- **Función:** pasar de no conmutación cualitativa a medición punto a punto.
- **Elementos:** defecto, estados terminales, comparación puntual.

### Definición `def:defecto_ordenamiento` -- Defecto de ordenamiento

- **Función:** definir la diferencia vectorial entre los dos órdenes.
- **Elementos:** `\mathcal D_{K,L}(X)`, `B_L(XK)`, `B_L(X)K`.

### Observación -- Defecto a cotas de desplazamiento

- **Función:** motivar la necesidad de controlar desplazamientos bayesianos y markovianos.
- **Elementos:** norma `\ell^1`, cotas por paso, defecto.

### Observación -- Cota bayesiana y control logarítmico

- **Función:** introducir la hipótesis de control sobre verosimilitudes.
- **Elementos:** `R`, `|\log L_i|`, `B_L(X)`.

### Lema `lem:cota_desplazamiento_bayesiano` -- Cota de desplazamiento bayesiano

- **Función:** acotar cuánto puede mover un paso bayesiano.
- **Elementos:** `B_L(X)`, `X`, `R`, norma `\ell^1`.
- **Hipótesis -> Consecuencias:** si la verosimilitud está log-acotada por `R`, entonces `\|B_L(X)-X\|_1` queda uniformemente acotado.
- **Idea breve de demostración:** controlar razón multiplicativa y normalizador con cotas exponenciales.

### Observación -- Cota markoviana y variación total

- **Función:** motivar el control del desplazamiento markoviano.
- **Elementos:** `XK-X`, norma `\ell^1`, variación total.

### Lema `lem:cota_desplazamiento_markoviano` -- Cota de desplazamiento markoviano

- **Función:** acotar el movimiento inducido por un kernel admisible.
- **Elementos:** `K`, `XK`, `X`, norma `\ell^1`.
- **Hipótesis -> Consecuencias:** bajo condiciones admisibles sobre `K`, el desplazamiento `\|XK-X\|_1` queda controlado.
- **Idea breve de demostración:** expandir `XK-X` por coordenadas y usar cotas de la matriz.

### Observación -- Control con variable de ordenamiento

- **Función:** introducir el orden como decisión de control.
- **Elementos:** acción, orden `MB/BM`, control discreto.

### Definición `def:accion_admisible_ordenamiento` -- Acción admisible

- **Función:** definir las decisiones disponibles en control.
- **Elementos:** `u=(K,L,\sigma)`, `\mathcal A_{\varepsilon,R}`, orden `\sigma`.

### Definición `def:transiciones_controladas_orden` -- Transiciones controladas

- **Función:** definir la transición inducida por una acción y un orden.
- **Elementos:** `T^u`, `T_{MB}^{K,L}`, `T_{BM}^{K,L}`.

### Proposición `prop:direccion_terminal_KL` -- Dirección terminal de KL bajo pérdida de soporte

- **Función:** controlar qué ocurre si el estado pierde soporte donde `P` es positivo.
- **Elementos:** `D_{\mathrm{KL}}(P\|X_k)`, coordenadas nulas, `+\infty`.
- **Hipótesis -> Consecuencias:** si una coordenada con `P_i>0` se aproxima o cae a cero, la KL diverge.
- **Idea breve de demostración:** el término `P_i\log(P_i/X_i)` tiende a `+\infty`.

### Observación `obs:necesidad_costos_valor_orden`

- **Función:** justificar costos de etapa y función de valor para decisiones secuenciales.
- **Elementos:** costo inmediato, costo futuro, Bellman.

### Definición `def:costos_etapa_ordenados` -- Costos de etapa ordenados

- **Función:** definir el costo de aplicar cada orden.
- **Elementos:** `c_{MB}`, `c_{BM}`, divergencias KL entre estados consecutivos.

### Definición `def:valor_Q_ordenamiento` -- Función de valor y Q-funciones

- **Función:** introducir evaluación dinámica de acciones.
- **Elementos:** `V_\tau`, `Q_\tau^{MB}`, `Q_\tau^{BM}`, horizonte `\tau`.

### Observación `obs:bellman_regularidad_local`

- **Función:** orientar el análisis hacia regularidad Lipschitz de Bellman.
- **Elementos:** recurrencia, estado inicial, constante `L_\tau`.

### Observación `obs:fuentes_regularidad_bellman`

- **Función:** identificar las piezas que deben ser regulares.
- **Elementos:** transiciones, costos, terminal `E_P`.

### Lema `lem:lipschitz_transiciones_ordenadas` -- Regularidad Lipschitz de transiciones

- **Función:** controlar la sensibilidad de las transiciones ordenadas respecto del estado.
- **Elementos:** `T_{MB}^{K,L}`, `T_{BM}^{K,L}`, constante Lipschitz.
- **Hipótesis -> Consecuencias:** bajo interioridad y cotas de `K,L`, las transiciones son Lipschitz en `\ell^1`.
- **Idea breve de demostración:** combinar cotas Lipschitz del operador bayesiano normalizado y del operador lineal markoviano.

### Lema `lem:invariancia_interior_transiciones_ordenadas`

- **Función:** garantizar que las transiciones controladas no salen de regiones interiores.
- **Elementos:** `\Delta_n(m)`, `\Delta_n(\alpha)`, `\varepsilon`, `R`.
- **Hipótesis -> Consecuencias:** si el estado inicial está en una región interior y los controles son admisibles, las imágenes quedan en otra región interior uniforme.
- **Idea breve de demostración:** usar positividad uniforme de `K` y cotas inferiores de los factores bayesianos.

### Lema `lem:cota_local_KL` -- Cota local para KL

- **Función:** acotar diferencias de KL en regiones interiores.
- **Elementos:** `D_{\mathrm{KL}}`, parámetro interior `\eta`, norma `\ell^1`.
- **Hipótesis -> Consecuencias:** en una región con coordenadas acotadas inferiormente, KL es localmente Lipschitz.
- **Idea breve de demostración:** usar que `\log x` tiene derivada acotada en intervalos `[m,1]`.

### Lema `lem:lipschitz_costos_etapa_ordenados`

- **Función:** probar regularidad de los costos de etapa.
- **Elementos:** `c_{MB}`, `c_{BM}`, constantes de Lipschitz, región interior.
- **Hipótesis -> Consecuencias:** bajo admisibilidad e interioridad, los costos ordenados son Lipschitz en el estado.
- **Idea breve de demostración:** aplicar la cota local KL a los pares de estados que definen cada costo y usar regularidad de transiciones.

### Observación `obs:propagacion_regularidad_bellman`

- **Función:** explicar cómo la regularidad se propaga en la recurrencia de Bellman.
- **Elementos:** `V_{\tau-1}`, `V_\tau`, costos, transiciones.

### Proposición `prop:lipschitz_V_tau_bellman`

- **Función:** establecer regularidad Lipschitz de la función de valor.
- **Elementos:** `V_\tau`, `L_\tau`, acciones admisibles.
- **Hipótesis -> Consecuencias:** si costos y transiciones son Lipschitz y `V_{\tau-1}` lo es, entonces `V_\tau` es Lipschitz.
- **Idea breve de demostración:** comparar valores para dos estados, usar la misma acción casi óptima y aplicar cotas de costos, transiciones e hipótesis inductiva.

### Corolario `cor:defecto_ordenamiento_valor_futuro`

- **Función:** controlar la diferencia de valor futuro mediante el defecto de ordenamiento.
- **Elementos:** `V_{\tau-1}`, `\mathcal D_{K,L}(X)`, constante Lipschitz.
- **Hipótesis -> Consecuencias:** si `V_{\tau-1}` es Lipschitz, la diferencia de valor futuro entre los dos órdenes se acota por `\|\mathcal D_{K,L}(X)\|_1`.
- **Idea breve de demostración:** aplicar directamente la desigualdad Lipschitz a los dos estados terminales.

### Observación `obs:regularidad_bellman_comparacion_ordenes`

- **Función:** conectar regularidad de Bellman con comparación de órdenes.
- **Elementos:** defecto de ordenamiento, funciones `Q`, costos.

### Definición `def:defecto_escalar_accion_valor_orden`

- **Función:** definir la diferencia escalar entre Q-funciones por orden.
- **Elementos:** `\eta_\tau(X;K,L)`, `Q_\tau^{MB}`, `Q_\tau^{BM}`, `\Delta\mathfrak c`, `\Delta\mathfrak v_\tau`.

### Lema `lem:control_defecto_costos_etapa`

- **Función:** acotar la diferencia de costos de etapa entre órdenes.
- **Elementos:** `c_{MB}-c_{BM}`, `\Gamma_{K,L}(X)`, `\mathcal D_{K,L}(X)`.
- **Hipótesis -> Consecuencias:** bajo interioridad y admisibilidad, la diferencia de costos se acota por desacoplamiento de primer paso y defecto de orden.
- **Idea breve de demostración:** descomponer diferencias de KL y aplicar cota local KL a cada par.

### Proposición `prop:control_defecto_escalar_accion_valor`

- **Función:** controlar la diferencia total entre Q-funciones de los dos órdenes.
- **Elementos:** `\eta_\tau`, `\Gamma_{K,L}`, `\mathcal D_{K,L}`, constante `C_\tau`.
- **Hipótesis -> Consecuencias:** la diferencia escalar entre `Q^{MB}` y `Q^{BM}` queda acotada por la suma del desacoplamiento y del defecto de orden.
- **Idea breve de demostración:** sumar el control de costos de etapa con el control del valor futuro por Lipschitz.

### Proposición `prop:suboptimalidad_un_paso_eleccion_orden`

- **Función:** cuantificar pérdida por elegir un orden no óptimo en un paso.
- **Elementos:** acción, orden elegido, orden óptimo, diferencia de `Q`.
- **Hipótesis -> Consecuencias:** si se elige el orden con menor `Q`, la suboptimalidad de elegir el otro se controla por el defecto escalar.
- **Idea breve de demostración:** comparar las dos Q-funciones y usar la cota del defecto escalar.

### Definición `def:trayectoria_admisible_ordenada_costo_realizado`

- **Función:** definir trayectorias controladas de varios pasos y su costo acumulado.
- **Elementos:** sucesión de acciones, estados `X_t`, costo realizado.

### Teorema `teo:subopt_multi_paso` -- Cota de suboptimalidad multi-paso

- **Función:** extender el control de suboptimalidad a horizontes múltiples.
- **Elementos:** horizonte `N`, `Q`, costos acumulados, constantes `C_\tau`.
- **Hipótesis -> Consecuencias:** bajo regularidad uniforme, la suboptimalidad acumulada queda acotada por la suma de defectos locales de ordenamiento.
- **Idea breve de demostración:** aplicar el control de un paso de forma iterada a lo largo de la trayectoria y sumar las cotas.

## Elementos globales a vigilar en la revisión de nomenclatura

Estos símbolos o nombres aparecen en varios items y conviene mantenerlos estables:

- `\Delta_n`, `\Delta_n^\circ`: símplex y su interior.
- `X`, `P`, `\mathcal P`, `\pi`: estado actual, referencia KL, objetivo bayesiano, estacionaria markoviana.
- `Y`, `C(X)`, `C_{\mathrm{glob}}`: corrección local, conjunto local, conjunto global.
- `T_Y^{\mathrm{loc}}`, `T_Y`, `T_\ell`, `B_L`: operador local, global, bayesiano abreviado y bayesiano por verosimilitud `L`.
- `K`, `\mathcal S_n`, `\mathcal K_\varepsilon`: kernel markoviano y clases admisibles.
- `L`, `\ell`, `Y^\ell`: verosimilitudes y correcciones inducidas.
- `D_{\mathrm{KL}}`, `E_P`, `g_X`, `\mathrm{grad}_g`: divergencia, energía, métrica Fisher y gradiente.
- `T_{MB}^{K,L}`, `T_{BM}^{K,L}`: transiciones controladas por orden.
- `\mathcal D_{K,L}(X)`, `\Gamma_{K,L}(X)`, `\eta_\tau(X;K,L)`: defecto vectorial de orden, desacoplamiento y defecto escalar de acción--valor.
- `V_\tau`, `Q_\tau^{MB}`, `Q_\tau^{BM}`: función de valor y funciones acción--valor.

## Posibles puntos de revisión posterior

- Algunos items demostrables carecen de `\label{...}` visible en el entorno, por ejemplo ciertos corolarios y definiciones de trayectorias bayesianas. Conviene decidir si todos los items formales deben tener etiqueta.
- Las nociones `objetivo bayesiano interior`, `posterior inducido`, `familia observacional admisible`, `coeficiente de avance KL` y `trayectoria bayesiana guiada` forman una cadena de dependencia; si una se renombra, deben actualizarse todas.
- En la Sección 7 conviene vigilar la consistencia entre orden textual `Markov--Bayes`, notación `MB`, transición `T_{MB}^{K,L}` y composición expresada como `B_L(XK)`.
- Los símbolos `P`, `\mathcal P` y `\pi` tienen roles distintos; deben evitarse frases que los llamen genéricamente "objetivo" sin especificación.

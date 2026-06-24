# CI+KL sobre Datos Reales: Diseño Experimental con Kaggle

> Afirmación central: CI+KL no es el único framework capaz de abordar estos problemas.
> Es el que requiere menor especificación previa para hacerlo, integra en una sola
> geometría restricciones que otros frameworks abordan con maquinaria separada,
> y produce una trayectoria formalmente auditable como objeto matemático.

---

## Qué entra y qué no de las revisiones

**Entran:**
- Criterio de selección sin δ_{s*}: solo para evaluación retrospectiva, nunca durante la política
- MIMIC-III: métrica → asociación retrospectiva, no mortalidad bajo política alternativa
- Bosch: estados → clusters de falla latente, no nombres causales (el dataset solo trae Response 0/1)
- CMAPSS: lenguaje → patrón compatible con modo, no identificación causal de modo
- Pregunta 2: convergencia a región D_{s*}, no a delta en punto fijo (estados reales derivan)
- Pregunta 4: reformulada como aproximación empírica a política óptima, no prueba de optimalidad
- Floor numérico X_t(i) ≥ ε para evitar colapso en frontera del símplex
- Dos variantes del criterio: CI+KL informacional y CI+KL decisional
- CMAPSS X₀ justificada como prior informado, no frecuencia empírica
- MIMIC-III puede responder Pregunta 1 (antibiótico modifica evidencia posterior)
- Flash Crash eliminado como caso de prueba si no hay datos intradía
- Fin SVB/CS: 2023, no 2022

**No entran:**
- Re-bajar trivialidad de Manufactura a 4/10: los argumentos para 1.5/10 siguen válidos
- Argumento O(n²) para LSTM: aplica a longitud de secuencia, no a número de variables

---

## 1. PROYECTO CORE — NASA CMAPSS (Turbofan Engine Degradation)

### Dataset

**Nombre**: NASA Turbofan Jet Engine Data Set (C-MAPSS)
**URL Kaggle**: `kaggle.com/datasets/behrad3d/nasa-cmaps`
**Fuente**: NASA Prognostics Center of Excellence, Ames Research Center
**Tamaño**: 4 subsets (FD001–FD004) · FD004: 248 motores entrenamiento, 249 prueba
**Estructura**: Series temporales por ciclo de operación por motor

```
Columnas:
unit_number         ID del motor (1..N)
time_in_cycles      ciclo de operación (tiempo)

Configuraciones operacionales:
  op_setting_1      altitud (correlada con presión)
  op_setting_2      aceleración throttle
  op_setting_3      velocidad relativa del ventilador [constante en FD001]

Sensores (21 señales s1–s21):
  s2, s3, s4        temperaturas en salidas de etapas
  s7, s8, s9        presión y velocidades
  s11, s12          presión estática HPC y flujo de combustible
  s13, s14          velocidades corregidas
  s15, s17, s20, s21 bypass ratio, flujos de enfriamiento

Nota: s1, s5, s6, s10, s16, s18, s19 tienen varianza ≈ 0 en FD001
→ llevan información nula, excluibles antes del experimento

RUL (en test set): ciclos restantes hasta falla
FD001: 1 modo de degradación · 1 condición operacional
FD003/FD004: 2 modos de degradación · múltiples condiciones operacionales
```

### Problema general

Los métodos de predicción de RUL usan las 21 señales simultáneamente en cada ciclo.
El problema real en sistemas embebidos (satélites, UAVs, plataformas de bajo cómputo)
es distinto: el sistema no puede transmitir o procesar todas las señales en cada ciclo
por restricciones de ancho de banda o energía.

La pregunta no es "¿cuántos ciclos le quedan al motor?"
La pregunta es: **"dado un presupuesto de k señales por ciclo, qué señales activar
para identificar el patrón de degradación dominante en el menor número de ciclos?"**

### Mapeo al Framework CI

```
FD001 — un patrón de degradación:
  S = {saludable, leve, moderado, severo}
  X_t ∈ Δ₃°

FD003/FD004 — dos patrones de degradación:
  S = {patron_HPC_leve, patron_HPC_severo,
       patron_ventilador_leve, patron_ventilador_severo}
  X_t ∈ Δ₃°

X₀ (prior informado, no frecuencia empírica):
  FD001: X₀ = (0.70, 0.20, 0.08, 0.02)
    Justificación: el prior NO es uniforme porque sabemos que un motor
    al inicio de su historial tiene alta probabilidad de estar sano.
    No es la frecuencia real (todos los motores en el dataset empiezan
    en estado saludable = (1,0,0,0)). Es un prior que incorpora
    variabilidad de fabricación y errores de medición inicial.

  FD003/FD004: X₀ = (0.25, 0.25, 0.25, 0.25)
    Justificación: sin historial previo del motor específico,
    la ignorancia sobre el patrón de degradación sí es honesta.

X* (región de decisión, no punto fijo):
  Mantenimiento inmediato:     X_t(severo) > 0.80
  Monitoreo intensificado:     X_t(moderado) > 0.70 y X_t(severo) < 0.30
  Operación normal:            X_t(saludable) + X_t(leve) > 0.90

Criterio de selección de señal (sin δ_{s*}):
  a_t* = argmax_a  E_{y|X_t,a}[KL(X_{t+1}(y) ‖ X_t)] / c(a)
  donde c(a) = costo de ancho de banda por señal (no costo de hardware)

Verosimilitud empírica:
  ℓᵢ(señal_k = v | patron_i) estimada por cuartil de RUL
  sobre el historial de los N motores del dataset de entrenamiento

Regularización de frontera:
  X_t(i) = max(X_t(i), ε)  con ε = 1e-8
  para evitar colapso numérico en la actualización multiplicativa
```

### Por qué los métodos existentes requieren maquinaria adicional

| Método | Capacidad base | Lo que necesita agregar | Por qué no lo hace nativamente |
|--------|---------------|------------------------|-------------------------------|
| LSTM/GRU-D | Maneja series irregulares | Mecanismo de selección activa de señal | Necesita entrenar una red por cada combinación de señales activas |
| T-LSTM | Maneja frecuencia irregular | Selección activa bajo presupuesto | Arquitectura fija: no puede cambiar qué señales leer en cada ciclo |
| IMM-Kalman | Identifica modos de degradación | Modelo lineal-gaussiano por modo + matrices de transición | Requiere especificación paramétrica previa de la dinámica |
| Active Learning (BALD) | Selección activa de instancias | Adaptación a series temporales con drift | Diseñado para i.i.d., no para degradación secuencial correlacionada |
| POMDP (SARSOP) | Selección óptima de acciones | Modelo completo P(s'|s,a) y R(s,a) | Intractable para espacios de estado continuos sin discretización fuerte |

### Pasos del Proyecto de Data Science

**Fase 0 — Configuración y adquisición**
```
1. Crear cuenta Kaggle y descargar dataset:
   URL: kaggle.com/datasets/behrad3d/nasa-cmaps
   Archivos: train_FD001.txt, test_FD001.txt, RUL_FD001.txt
             (repetir para FD003 y FD004)

2. Configurar entorno:
   pip install numpy pandas scikit-learn scipy matplotlib seaborn
   Estructura de carpetas:
   /data/raw/         → archivos .txt originales
   /data/processed/   → CSVs normalizados
   /src/ci_framework/ → implementación del framework
   /notebooks/        → análisis y visualización
```

**Fase 1 — EDA y preprocesamiento**
```
3. Cargar datos con columnas nombradas:
   cols = ['unit', 'cycle', 'op1', 'op2', 'op3',
           's1',...,'s21']
   df = pd.read_csv('train_FD001.txt', sep=' ', header=None,
                    names=cols, index_col=False)

4. Calcular RUL para el set de entrenamiento:
   max_cycle = df.groupby('unit')['cycle'].max()
   df['RUL'] = df.groupby('unit')['cycle'].transform('max') - df['cycle']

5. Identificar señales informativas (FD001):
   Eliminar s1, s5, s6, s10, s16, s18, s19 por varianza ≈ 0
   Confirmar con: df[sensor_cols].std().sort_values()

6. Discretizar RUL en estados:
   bins = [float('inf'), 125, 75, 30, 0]
   labels = ['saludable', 'leve', 'moderado', 'severo']
   df['estado'] = pd.cut(df['RUL'], bins=bins, labels=labels)

7. Normalizar señales por condición operacional (FD004):
   Agrupar por cluster de op_setting_1 + op_setting_2
   Normalizar (z-score) dentro de cada cluster
```

**Fase 2 — Construcción del framework CI**
```
8. Estimar verosimilitudes empíricas:
   Para cada señal k y cada estado i:
   ℓᵢ(s_k = v) = P(s_k ∈ bin(v) | estado = i)
   Usar KDE o histograma de 20 bins sobre ciclos de entrenamiento
   Almacenar como dict: likelihood[estado][señal] → distribución

9. Implementar operador de actualización:
   def update(X, likelihood_vector):
       X_new = X * likelihood_vector
       X_new = np.maximum(X_new, 1e-8)  # floor numérico
       return X_new / X_new.sum()       # normalización (operador cierre)

10. Implementar criterio de selección:
    def expected_kl(X, sensor_k, likelihoods, cost_k):
        # Promediar sobre posibles resultados de sensor_k
        gains = []
        for v in sensor_bins:
            p_v = sum(X[i] * likelihoods[i][sensor_k](v) for i in states)
            if p_v > 0:
                X_new = update(X, [likelihoods[i][sensor_k](v) for i in states])
                kl = scipy.special.kl_div(X_new, X).sum()
                gains.append(p_v * kl)
        return sum(gains) / cost_k

    def select_sensor(X, available_sensors, likelihoods, costs):
        return max(available_sensors,
                   key=lambda k: expected_kl(X, k, likelihoods, costs[k]))
```

**Fase 3 — Ablaciones (niveles 0 a 6)**
```
11. Nivel 0 (baseline pasivo): LSTM + GRU-D + IMM-Kalman con 21 señales
    Métrica: ciclos hasta RUL < 30 (proxy de estado severo)

12. Nivel 1 (CI aleatorio): selección aleatoria de señal en cada ciclo
    Métrica: ciclos hasta X_t(severo) > 0.80

13. Nivel 2 (CI + entropía greedy): seleccionar señal por máxima reducción de H(X)

14. Nivel 3 (CI + KL sin costo): seleccionar señal por máximo E[KL(X_{t+1}||X_t)]

15. Nivel 4 (CI + KL/costo): dividir por c(a) diferenciado por señal
    Asignar costos: c(s_k) proporcional a la varianza de la señal
    (señales más ruidosas = más costosas de interpretar)

16. Nivel 5 (+ drift): entre ciclos, aplicar operador de difusión hacia
    estados de mayor degradación:
    X_t_drift = (1 - α) * X_t + α * [0.1, 0.2, 0.3, 0.4]
    α = 0.02 (estimado de velocidad media de degradación en dataset)

17. Nivel 6 (configuración completa FD003/FD004):
    Añadir verosimilitud local estimada por condición operacional
    k-NN sobre op_settings para seleccionar motores similares
```

**Fase 4 — Evaluación y visualización**
```
18. Métrica principal: ciclos hasta cruzar X* con k ≤ 5 señales por ciclo
    Comparar todos los niveles con boxplot por motor

19. Visualizar trayectoria en símplex (proyección 2D vía coordenadas de Aitchison):
    from matplotlib import pyplot as plt
    # Proyectar X_t sobre plano (X_saludable, X_severo) por motor
    # Mostrar convergencia hacia vértice correcto

20. Verificar Pregunta 1 (¿importa el orden?):
    Para N motores, comparar T_{s7} ∘ T_{s8}(X₀) vs T_{s8} ∘ T_{s7}(X₀)
    Si la diferencia media > 0.05 en norma L1 → los operadores no conmutan

21. Reporte final:
    Tabla: Nivel | Ciclos medio | Señales/ciclo | % diagnóstico correcto
    Curva: Eficiencia informacional = reducción de H(X_t) / señales acumuladas
```

---

## 2. PROYECTO ESCALA — Bosch Production Line Performance

### Dataset

**Nombre**: Bosch Production Line Performance
**URL Kaggle**: `kaggle.com/c/bosch-production-line-performance`
**Organización**: Bosch (componentes automotrices y electrónicos)
**Tamaño**: 1,184,687 partes · ~4,000 features · 14.3 GB (3 archivos CSV)

```
Archivo numérico (train_numeric.csv):
  Id          identificador único de parte
  L{l}_S{s}_F{f}: medición del sensor F en estación S de línea L
  Response    0 = pasa QC, 1 = falla QC  [solo en numeric]

Archivo de timestamps (train_date.csv):
  Id
  L{l}_S{s}_D{f}: timestamp de cuando la parte pasó por esa estación-feature
  CLAVE: D = date/timestamp, NO columna categórica

Archivo categórico (train_categorical.csv):
  Id
  L{l}_S{s}_F{f}: estado discreto de la estación (configuración, herramienta)

Prevalencia: Response=1 es ~0.58% del total
Estructura NaN:
  NaN en numérico + timestamp presente  → medición inválida (falla en estación)
  NaN en numérico + timestamp ausente   → estación no visitada (ruta alternativa)
```

### Problema general

Cada parte sigue una ruta distinta por 4 líneas y 52 estaciones. El problema
no es "¿fallará esta parte?" con todos los datos ya disponibles.
El problema es: **"dado que la parte está en la estación S_k con las mediciones
acumuladas hasta aquí, qué riesgo tiene de falla y qué medición adicional
reduciría más la incertidumbre sin detener la línea?"**

La distinción NaN-ruta vs NaN-falla es el núcleo conceptual no trivial:
un NaN con timestamp es evidencia de algo; un NaN sin timestamp es silencio.
LightGBM con NaN como categoría especial no distingue estos dos casos.
CI los trata con operadores distintos.

### Mapeo al Framework CI

```
Estados (clusters latentes, no nombres causales):
  S = {sin_falla, cluster_falla_1, cluster_falla_2, cluster_falla_3}
  Los clusters se definen por k-means sobre las partes con Response=1
  Interpretación causal (dimensional/material/ensamblaje) solo después,
  si el análisis de features dominantes por cluster lo sugiere.
  El dataset solo certifica Response=0/1, no el tipo de falla.

X₀ (prior poblacional):
  X₀ = (0.9942, 0.0023, 0.0020, 0.0015)
  Justificación: la prevalencia real de fallas es ~0.58%.
  X₀ asimétrico plantea la pregunta dura: ¿qué evidencia en la ruta
  es suficientemente fuerte para mover una creencia de 99.4% a favor de calidad?

Dos tipos de corrección según el NaN:
  NaN con timestamp en S_k:
    ℓᵢ(timestamp_presente, valor_nulo | cluster_i)
    → actualiza: la medición inválida ES información
    → T_{Y^ℓ}(X_t) ≠ X_t

  NaN sin timestamp en S_k:
    ℓᵢ = 1 para todo i (operador identidad)
    → T_{Y^ℓ}(X_t) = X_t (silencio, no evidencia)

X* (dos regiones de decisión asimétricas):
  Desviar a inspección:
    X_t(cluster_1 ∪ cluster_2 ∪ cluster_3) > 0.30
    Umbral bajo: falso negativo es catastrófico (pieza defectuosa al cliente)

  Liberar sin inspección:
    X_t(sin_falla) > 0.998
    Umbral mayor que X₀: la evidencia debe superar el prior, no solo confirmarlo

Criterio de selección:
  a_t* = argmax_a  E[KL(X_{t+1} ‖ X_t)] / c(a)
  donde c(a) = costo temporal de la medición adicional en la estación
```

### Por qué los métodos existentes requieren maquinaria adicional

LightGBM (MCC público ≈ 0.49) trata NaN como categoría especial mediante
sparsity-aware splitting: aprende que "ausente en L1_S2_F47" predice falla.
Pero no distingue si esa ausencia fue por ruta o por falla en la estación.

Para hacer esa distinción, LightGBM necesitaría:
- Crear features explícitas de timestamp presencia/ausencia por estación
- Cruzarlas con las features numéricas correspondientes
- Esto duplica la dimensionalidad ya de por sí enorme (~8,000 features)

CI codifica la distinción nativamente: el tipo de corrección depende de
si existe timestamp, sin aumentar la dimensionalidad.

### Pasos del Proyecto de Data Science

**Fase 0 — Configuración (dataset grande, manejo por chunks)**
```
1. Descargar dataset desde Kaggle:
   kaggle competitions download -c bosch-production-line-performance
   Archivos: train_numeric.csv.zip (4.4GB), train_date.csv.zip (3.5GB),
             train_categorical.csv.zip (5.9GB)

2. Configurar lectura por chunks (RAM limitada):
   chunk_size = 50_000
   reader = pd.read_csv('train_numeric.csv', chunksize=chunk_size)

3. Estructura de directorios:
   /data/raw/          → archivos comprimidos originales
   /data/processed/    → features seleccionados, NaN clasificados
   /data/routes/       → mapa de rutas por parte (desde timestamps)
   /src/ci_framework/  → framework CI
   /src/baselines/     → LightGBM, XGBoost
```

**Fase 1 — EDA y clasificación de NaN**
```
4. Construir mapa de rutas desde train_date.csv:
   Para cada parte (Id), listar las estaciones con timestamp no nulo
   → ruta_parte[Id] = [(linea, estacion, timestamp), ...]
   → ordenar por timestamp para reconstruir el orden cronológico

5. Clasificar NaN en train_numeric.csv:
   Para cada feature L{l}_S{s}_F{f}:
     si train_date['L{l}_S{s}_D{f}'] es not null → NaN tipo FALLA
     si train_date['L{l}_S{s}_D{f}'] es null     → NaN tipo RUTA

6. Estadísticas de NaN por tipo:
   % NaN-ruta vs NaN-falla por estación
   Hipótesis: las estaciones con alto % NaN-falla tienen mayor tasa de Response=1

7. Análisis de prevalencia de falla por ruta:
   Comparar tasa de Response=1 para partes que pasaron por L3 vs las que no
   Si hay diferencia significativa → la ruta ES predictiva del outcome
```

**Fase 2 — Construcción de estados y verosimilitudes**
```
8. Clustering de fallas:
   Filtrar partes con Response=1 (~6,883 partes)
   Seleccionar features con mayor información en esas partes
   K-means con k=3 en el espacio de features no-NaN de fallas
   Etiquetar: cluster_falla_{1,2,3}

9. Estimar verosimilitudes diferenciadas:
   Para NaN-FALLA:
     ℓᵢ(NaN_falla_en_S_k | cluster_i) = frecuencia de NaN-falla en S_k
     sobre partes del cluster i
   
   Para NaN-RUTA:
     ℓᵢ = (1, 1, 1, 1) → operador identidad (no actualiza)
   
   Para medición válida v en S_k:
     ℓᵢ(v | cluster_i) usando distribución empírica de esa medición
     en partes del cluster i

10. Verificar calibración:
    Dividir partes con Response=1 en train/test
    Confirmar que las verosimilitudes estimadas producen posterior concentrado
    en el cluster correcto para el test set
```

**Fase 3 — Simulación de la política en tiempo de producción**
```
11. Para cada parte en test set:
    a. Inicializar X₀ = (0.9942, 0.0023, 0.0020, 0.0015)
    b. Procesar las estaciones en orden cronológico (usando timestamps)
    c. En cada estación S_k:
       - Determinar tipo de NaN (ruta o falla) o valor medido
       - Aplicar corrección local correspondiente
       - Calcular X_t actualizado
       - Verificar si X_t cruzó algún umbral de X*

12. Registrar: estación donde se cruzó el umbral de desvío (si ocurre)
    Comparar con Response final del dataset
```

**Fase 4 — Baselines y comparación**
```
13. LightGBM baseline:
    Features: numéricas + indicador binario de NaN por feature
    Evaluar con MCC (métrica oficial de la competencia)
    Cross-validación temporal (no aleatoria: respetar el orden de producción)

14. XGBoost con features de ruta:
    Agregar: número de estaciones visitadas, líneas visitadas,
             porcentaje de NaN-falla por línea

15. CI+KL:
    Métrica principal: estación de detección (no MCC global)
    Secundaria: MCC al final de la línea con umbral optimizado

16. Pregunta central a responder:
    ¿En qué estación de la ruta la trayectoria CI cruza el umbral
    de desvío para las partes que efectivamente fallaron?
    Si cruza antes del 50% de la ruta → detección temprana real.
```

---

## 3. PROYECTO APLICADO — MIMIC-III ICU Sepsis

### Dataset

**Nombre**: MIMIC-III Deep RL Sepsis Dataset
**URL Kaggle**: `kaggle.com/datasets/asjad99/mimiciii`
**Fuente original**: PhysioNet / MIT Lab · Beth Israel Deaconess MC · 2001–2012
**Nota**: Este subset es un preprocesado para sepsis/RL, no MIMIC-III completo.
Para acceso completo: `physionet.org/content/mimiciii/1.4/`

```
Columnas relevantes:
  Demográficas:     age, gender, weight
  Signos vitales:   heart_rate, sysbp, diasbp, meanbp,
                    resprate, temp, spo2        [cada hora]
  Laboratorio:      wbc, lactate, bicarbonate, creatinine,
                    bilirubin, platelet, inr    [cada 4-8h]
  Intervenciones:   vasopressor_flag, vent_flag,
                    antibiotic_flag, iv_fluid_volume  [acumulado por hora]
  Score clínico:    sofa_score, sirs_score, qsofa_score
  Outcome:          mortality_90d, sepsis_onset_time, icu_los
```

### Problema general

El problema no es predecir si el paciente tendrá sepsis (clasificación estática).
El problema es: **"¿qué medir o intervenir en cada hora para identificar el
estado clínico con menor número de intervenciones farmacológicas, y puede CI
cuantificar cuánta información se pierde cuando un antibiótico administrado
antes de la punción lumbar degrada la verosimilitud del hemocultivo posterior?"**

La métrica de evaluación correcta es asociación retrospectiva con
sepsis_onset_time, no mortalidad bajo política alternativa
(que requeriría evaluación causal off-policy).

### Mapeo al Framework CI

```
S = {no_sepsis, sepsis_declarada, sepsis_severa, shock_septico}
X_t ∈ Δ₃°

X₀ (función del SOFA de admisión, calculado en primeras 2h):
  SOFA ≤ 2:    X₀ = (0.65, 0.22, 0.10, 0.03)
  SOFA 3–5:    X₀ = (0.35, 0.33, 0.24, 0.08)
  SOFA 6–9:    X₀ = (0.12, 0.28, 0.38, 0.22)
  SOFA ≥ 10:   X₀ = (0.04, 0.14, 0.35, 0.47)
  Justificación: anclar X₀ en SOFA permite que el experimento pregunte
  "¿CI agrega valor después de SOFA?" no "¿CI reemplaza SOFA?"

Verosimilitud con deconfounding:
  ℓᵢ(medición = v | estado_i) estimada con propensity score IPW
  porque: P(medir_lactato | estado_i) ≠ P(medir_lactato | aleatorio)
  El médico mide lactato cuando sospecha deterioro → sesgo sistemático

  Implementación IPW:
    propensity = P(medir_lab | covariables_observadas_en_t)
    peso = 1 / propensity por observación
    ℓᵢ estimada sobre la muestra ponderada

  Limitación declarada: el propensity score requiere covariables
  del turno médico y saturación del laboratorio, que pueden no estar
  todas disponibles en este subset de MIMIC-III

Dependencia acción→evidencia (Pregunta 6):
  Si antibiotic_flag_t = 1:
    ℓ(hemocultivo | t+4h) se degrada por esterilización bacteriana
    Implementar: ℓ_hemocultivo *= factor_degradacion(horas_desde_antibiotico)
    factor_degradacion estimado de literatura clínica (AUC hemocultivo
    post-antibiótico vs pre-antibiótico en MIMIC-III)

X* (regiones que activan protocolos):
  Protocolo antibióticos + cultivos:
    X_t(sepsis ∪ severa ∪ shock) > 0.75
    Y t < sepsis_onset_time del dataset (detección anticipada)
  Protocolo vasopresores:
    X_t(shock_septico) > 0.70
  Continuar observación:
    X_t(no_sepsis) > 0.85
```

### Por qué los métodos existentes requieren maquinaria adicional

GRU-D (estado del arte para MIMIC-III con datos irregulares) maneja
la asincronía con mecanismos de decay: cada variable tiene su propio
coeficiente de desvanecimiento según el tiempo desde la última medición.
No puede modelar que administrar antibióticos cambia la informatividad
de las mediciones posteriores de hemocultivo. Para eso necesitaría:
- Agregar nodos de acción explícitos en la arquitectura
- Reentrenar por cada tipo de intervención posible
CI absorbe esa dependencia nativamente en la verosimilitud condicionada.

### Pasos del Proyecto de Data Science

**Fase 0 — Configuración y acceso**
```
1. Descargar subset de Kaggle:
   kaggle datasets download -d asjad99/mimiciii

   Para dataset completo (requiere acuerdo de uso):
   Registrar en physionet.org → solicitar acceso MIMIC-III
   Descarga desde: physionet.org/content/mimiciii/1.4/

2. Dependencias adicionales:
   pip install lifelines  # para análisis de tiempo hasta evento
   pip install statsmodels  # para propensity score
   pip install causalml  # para IPW
```

**Fase 1 — Preprocesamiento clínico**
```
3. Calcular SOFA score de admisión (primeras 2h):
   SOFA = suma de 6 componentes: respiratorio, coagulación,
          hepático, cardiovascular, neurológico, renal
   Cada componente 0-4 según umbrales de la definición Sepsis-3

4. Alinear variables temporales:
   Pivot por (icustay_id, hora_de_UCI):
   Signos vitales: disponibles cada hora
   Laboratorio: forward-fill hasta 8h, luego NaN (no extrapolar más)
   Intervenciones: flag binaria en la hora en que ocurrió

5. Crear variable objetivo temporal:
   Para cada (paciente, hora): ¿está a k horas del sepsis_onset_time?
   Crear etiqueta: horas_antes_onset = sepsis_onset_time - hora_actual
```

**Fase 2 — Deconfounding con propensity score**
```
6. Estimar propensity score para cada laboratorio:
   Ejemplo para lactato:
   y = [1 si se midió lactato en esta hora, 0 si no]
   X = [signos_vitales_hora_t, sofa_score, intervencion_previa,
        horas_en_UCI, lactato_previo_disponible]
   
   from sklearn.linear_model import LogisticRegression
   ps_model = LogisticRegression().fit(X_train, y_train)
   propensity = ps_model.predict_proba(X)[:, 1]
   weights = 1.0 / propensity  # IPW

7. Estimar ℓᵢ con pesos IPW:
   Para cada estado i y cada laboratorio k:
   ℓᵢ(v) = Σ [1(lab_k = v) * weight] / Σ weight
   sobre todas las horas en el estado i (según ground truth)

8. Documentar limitaciones:
   Las covariables del turno médico NO están en este subset
   → el propensity score es parcialmente confoundido
   → declarar esto como limitación explícita en el análisis
```

**Fase 3 — Implementación CI con asincronía**
```
9. Motor de actualización asíncrono:
   # El estado se actualiza cuando llega cada medición, no cada hora
   events = crear_timeline_de_eventos(paciente)
   # [(hora, tipo_medicion, valor, accion_previa), ...]
   
   X = X0_desde_SOFA(sofa_score_admision)
   for hora, tipo, valor, accion_previa in events:
       if tipo == 'lab' and accion_previa == 'antibiotico':
           factor = degradacion_hemocultivo(hora - hora_antibiotico)
           ℓ = likelihood_lab_degradada(tipo, valor, factor)
       else:
           ℓ = likelihood_normal(tipo, valor)
       X = update(X, ℓ)
       registrar(hora, X)

10. Detección:
    t_deteccion = primera hora donde X cruza umbral de X*
    anticipacion = sepsis_onset_time - t_deteccion
    Positivo si anticipacion > 0 (detectó antes del onset)
```

**Fase 4 — Evaluación y comparación**
```
11. Baselines:
    qSOFA estático (score de admisión, sin actualización)
    SOFA cada 6h (actualización periódica)
    GRU-D (estado del arte en MIMIC-III con datos irregulares)
    AI Clinician - Komorowski 2018 (DRL sobre MIMIC-III)

12. Métricas (NO mortalidad bajo política alternativa):
    Tiempo de anticipación al onset: distribución por cuartil de SOFA
    Número de labs ordenados antes de la detección
    Tasa de falsos positivos (X_t cruza umbral en pacientes sin sepsis)
    Calibración: ¿X_t(no_sepsis) en pacientes que no desarrollan sepsis
                 se mantiene alto a lo largo del tiempo?

13. Visualización de la Pregunta 6 (costo informacional del antibiótico):
    Para pacientes que recibieron antibiótico antes de punción:
    Graficar X_t antes y después del antibiótico
    Comparar con pacientes que no recibieron antibiótico
    Medir en unidades KL cuánto se "achataron" las distribuciones
    después de la intervención
```

---

## 4. FINANZAS — Motivación conceptual (no experimento central)

Finanzas queda como extensión post-publicación. La dificultad de definir un
ground truth no ambiguo (crisis financieras tienen causas interpretativas)
y el riesgo de hindsight bias hacen que la validación sea menos limpia.

Si se implementa en el futuro, los casos de prueba son:
- Crisis 2008 (datos diarios disponibles en Kaggle)
- Crisis COVID marzo 2020 (datos diarios)
- Crisis SVB/Credit Suisse 2023 (datos diarios)

El Flash Crash del 6 de mayo de 2010 queda excluido como caso de prueba
a menos que se dispongan de datos intradía (minuto a minuto): el evento
duró 36 minutos y datos diarios no pueden validar su detección.

---

## Sección A — Marco Matemático Preciso

### A.1 Separación de niveles

```
s_t  ∈ S               Estado real oculto
X_t  ∈ Δₙ°             Creencia del agente (distribución sobre S)
a_t  ∈ A_t             Acción disponible en t
y_t  ∈ Y               Observación tras ejecutar a_t
c(a_t) ∈ ℝ₊            Costo de la acción

Dinámica del mundo:
  s_{t+1} ~ P(s_{t+1} | s_t, a_t)     [puede ser desconocida]
  y_t     ~ P(y_t | s_t, a_t, h_{t-1}) [depende de acciones previas]

Actualización CI:
  X_{t+1} = T_{Y^{ℓ_t}}(X_t)
  donde ℓ_t(i) = P(y_t | s = i, a_t, h_{t-1})
```

### A.2 Criterio de selección (sin δ_{s*})

El estado verdadero s* es desconocido durante la decisión.
El criterio correcto usa ganancia de información esperada:

$$a_t^* = \arg\max_{a \in A_t} \frac{\mathbb{E}_{y \sim P(y|X_t,a)}\left[D_{KL}(X_{t+1}(y) \| X_t)\right]}{c(a)}$$

δ_{s*} solo aparece en la evaluación retrospectiva:
comparar X_T contra el estado verdadero del dataset.

**Variante decisional** (para problemas con costos asimétricos):

$$a_t^* = \arg\min_{a \in A_t} \mathbb{E}_{y|X_t,a}\left[R(X_{t+1}(y)) + \lambda c(a)\right]$$

donde $R(X) = 1 - \max_i X(i)$ (riesgo de no tener hipótesis dominante).

En medicina y Bosch (falso negativo costoso): R asimétrico, λ pequeño.
En CMAPSS (falso positivo costoso también): R simétrico, λ más grande.

Las ablaciones comparan ambas variantes para determinar cuándo conviene
maximizar información vs minimizar riesgo.

### A.3 Regularización de frontera

Para evitar colapso numérico cuando X_t(i) → 0:

$$X_t(i) = \max(X_t(i), \varepsilon), \quad \varepsilon = 10^{-8}$$

seguido de renormalización. Esto limita la recuperabilidad de hipótesis
extintas pero previene divisiones por cero y estabilidad numérica.

### A.4 Ventaja de CI: costo de especificación previa

| Framework | Puede modelar acción→evidencia | Especificación requerida | Trayectoria auditable |
|-----------|:---:|---|:---:|
| POMDP | ✓ | P(s'\|s,a), R(s,a), O(o\|s,a) completos | ✗ |
| DBN con nodos de acción | ✓ | Grafo causal + todas las CPTs | ✗ |
| IMM-Kalman | Parcial | Modelo lineal-gaussiano por modo | Parcial |
| Particle filter | ✓ | Función de propuesta + modelo observación | ✗ |
| Active Learning | ✓ | Función de adquisición i.i.d. | ✗ |
| **CI+KL** | ✓ | Verosimilitudes locales empíricas | **✓** |

---

## Sección B — Benchmarks Completos por Dataset

### B.1 CMAPSS

| Herramienta | Maneja irreg. temporal | Selección activa | Interpretable | Ref |
|-------------|:---:|:---:|:---:|---|
| LSTM estándar | ✗ | ✗ | ✗ | Hochreiter 1997 |
| T-LSTM | ✓ | ✗ | ✗ | Baytas 2017 |
| GRU-D | ✓ | ✗ | ✗ | Che 2018 |
| IMM-Kalman | ✓ | ✗ | ✓ | Bar-Shalom 1988 |
| Active Learning (BALD) | ✗ | ✓ | ✗ | Houlsby 2011 |
| POMDP (SARSOP) | ✓ | ✓ | ✗ | Kurniawati 2008 |
| **CI+KL** | ✓ | ✓ | ✓ | Este trabajo |

### B.2 Bosch

| Herramienta | MCC approx | Distingue NaN-ruta/falla | Trazable |
|-------------|:---:|:---:|:---:|
| XGBoost básico | 0.36 | ✗ | ✗ |
| LightGBM + features | 0.49 | ✗ | ✗ |
| LightGBM + timestamps | ~0.51? | Parcial | ✗ |
| Path-based imputation | — | ✓ | ✗ |
| **CI+KL** | A medir | ✓ | ✓ |

### B.3 MIMIC-III

| Herramienta | Asincronía | Modela acción→evidencia | Ref |
|-------------|:---:|:---:|---|
| SOFA/qSOFA | ✗ | ✗ | Singer 2016 |
| GRU-D | ✓ | ✗ | Che 2018 |
| AI Clinician (DRL) | ✓ | Parcial | Komorowski 2018 |
| POMDP clínico (VoI) | ✓ | ✓ | Ayer 2012 |
| **CI+KL + IPW** | ✓ | ✓ | Este trabajo |

---

## Sección C — Orden de Implementación

```
Fase 0 (1 sem): Sistema dinámico sintético controlado
  Objetivo: verificar T_{Y^ℓ} y criterio KL/costo antes de datos reales
  Validación matemática: X_t converge a D_{s*} en tiempo finito
  Experimento específico para Pregunta 3:
    Perturbar ℓ con ruido multiplicativo ε ∈ {0.01, 0.05, 0.10, 0.20}
    Medir: norma L1 entre X_T^{ℓ_ruidosa} y X_T^{ℓ_exacta}
    ¿Crece linealmente en ε o de manera superlineal?

Fase 1 (2 sem): NASA CMAPSS FD001
  Ablaciones Niveles 0–4
  Verificar Pregunta 1 (conmutatividad) en N=100 motores

Fase 2 (2 sem): NASA CMAPSS FD003/FD004
  Ablaciones Niveles 5–6
  Verificar Pregunta 5 (frontera del símplex con dos modos)

Fase 3 (3 sem): Bosch Production Line
  Implementar distinción NaN-ruta vs NaN-falla
  Verificar Pregunta 6 (NaN-falla como evidencia)

Fase 4 (4 sem): MIMIC-III con IPW
  Deconfounding previo obligatorio
  Evaluación retrospectiva (no contrafactual)
  Verificar Pregunta 6 (antibiótico degrada hemocultivo)

Finanzas: extensión post-publicación
```

---

## Sección D — Lenguaje Corregido

| Evitar | Usar |
|--------|------|
| "Los métodos no pueden formular el problema" | "Requieren maquinaria adicional separada" |
| "CI es estructuralmente necesario" | "CI integra con menor costo de especificación" |
| "Kalman no puede detectar spoofing" | "Kalman estándar puede ser evadido; necesita extender su espacio de hipótesis" |
| "Modo de falla activo" (CMAPSS) | "Patrón de degradación compatible con modo simulado" |
| "Falla dimensional/material" (Bosch) | "Cluster de falla latente" |
| "Mortalidad 90d bajo cada política" | "Asociación retrospectiva con mortalidad 90d" |
| "O(n) vs O(n³)" para MIMIC-III n=40 | Omitir; usar solo cuando n > 100 |
| "X_t converge a δ_{s*}" | "X_t converge a región D_{s*}" |

---

## Sección F — Estados Informacionales y Preguntas Fundamentales

### F.1 Preguntas del Framework CI

**Pregunta 1 — Conmutatividad de operadores**
> ¿Importa el orden de las observaciones?

$$T_{Y^{\ell_2}} \circ T_{Y^{\ell_1}}(X_0) \stackrel{?}{=} T_{Y^{\ell_1}} \circ T_{Y^{\ell_2}}(X_0)$$

Aclaración: la no conmutatividad solo aparece cuando
$\ell_t = \ell_t(a_t, h_{t-1})$, es decir, cuando la verosimilitud depende
de las acciones previas y el historial. Para verosimilitudes fijas e
independientes, los operadores multiplicativos sí conmutan.
El experimento prueba el caso no conmutativo (el que importa en práctica).

*Responde: CMAPSS, Bosch, MIMIC-III.*

---

**Pregunta 2 — Convergencia a región de decisión**
> ¿Bajo qué condiciones la trayectoria converge a la región D_{s*},
> y a qué velocidad?

Nota: en estados reales que derivan (motor que se degrada, paciente que empeora),
la convergencia no es hacia δ_{s*} en un punto fijo. Es hacia la vecindad de
la distribución del estado actual, con error acotado por la velocidad de cambio.
Formalmente: $D_{KL}(X_t \| P_{s_t}) \leq f(\text{velocidad de drift})$.

*Responde: todos los experimentos.*

---

**Pregunta 3 — Robustez a error en verosimilitudes**
> Si $\hat{\ell}$ estima $\ell$ con error $\varepsilon$, ¿cómo se propaga?

Experimento cuantitativo (Fase 0):
- Perturbar $\ell$ con ruido multiplicativo: $\hat{\ell}_i = \ell_i \cdot (1 + \varepsilon_i)$
- Medir: $\|X_T^{\hat{\ell}} - X_T^{\ell}\|_1$ para $\varepsilon \in \{0.01, 0.05, 0.10, 0.20\}$
- Si el error crece linealmente en $\varepsilon$ → símplex amortigua (CI es robusto)
- Si crece superlinealmente cerca de la frontera → CI requiere verosimilitudes de calidad

*Responde: Fase 0 sintética y MIMIC-III.*

---

**Pregunta 4 — KL/costo como aproximación a política óptima**
> ¿El criterio KL/costo se aproxima empíricamente a la política óptima?

Reformulación honesta: no se puede probar optimalidad formal en espacios grandes
(requeriría resolver el POMDP exacto). La pregunta verificable es:
en dominios donde el POMDP es soluble (n pequeño, FD001 con 4 estados),
¿el criterio KL/costo produce resultados comparables al POMDP óptimo?

Las ablaciones (Niveles 2–3 vs decisional) muestran si KL supera a entropía,
sin afirmar que sea globalmente óptimo.

*Responde: ablaciones CMAPSS FD001.*

---

**Pregunta 5 — Comportamiento en la frontera del símplex**
> ¿Qué ocurre cuando X_t(i) → 0?

La actualización multiplicativa hace que una hipótesis con probabilidad muy baja
sea difícil de recuperar aunque llegue evidencia fuerte. En la práctica:
- El floor numérico $\varepsilon = 10^{-8}$ limita la extinción completa
- Pero la recuperabilidad práctica cae drásticamente para $X_t(i) < 10^{-4}$
Esto se explora en FD003/FD004 cuando un modo de degradación recibe
evidencia contradictoria en los primeros ciclos.

*Responde: CMAPSS FD003/FD004 y Bosch.*

---

**Pregunta 6 — Cuantificación del costo informacional de acciones**
> Si $a_t$ degrada la evidencia futura, ¿puede CI cuantificarlo en unidades KL?

Esta es la pregunta más específica de CI. Se responde empíricamente:
comparar la reducción de $H(X_t)$ en pacientes que recibieron antibiótico
antes de punción vs los que no. Si la reducción de entropía es menor en el
primer grupo, eso muestra que CI captura el costo informacional de la acción.
En unidades KL: $\Delta_{KL} = D_{KL}(X_{t+1}^{\text{con ab}} \| X_{t+1}^{\text{sin ab}})$.

*Responde: MIMIC-III y Bosch (NaN-falla).*

---

### F.2 Estados por Proyecto

#### CMAPSS FD001 y FD003/FD004
```
Pregunta conceptual:
¿Puede un agente bajo presupuesto de señales construir creencia suficiente
para decisión de mantenimiento, y demuestra eso que el orden de observaciones
importa informativamente?

X₀ = (0.70, 0.20, 0.08, 0.02) para FD001
     Prior informado (no empírico: todos los motores empiezan sanos).
     Incorpora variabilidad de fabricación e incertidumbre de medición inicial.

X₀ = (0.25, 0.25, 0.25, 0.25) para FD003/FD004
     Ignorancia honesta sobre el patrón de degradación al inicio.

X* = región {X_t(severo) > 0.80} ∪ {X_t(saludable+leve) > 0.90}

Qué responde la trayectoria:
Si T_{s7} ∘ T_{s8}(X₀) ≠ T_{s8} ∘ T_{s7}(X₀) de manera consistente
entre motores del mismo modo → Pregunta 1 confirmada empíricamente.
```

#### Bosch
```
Pregunta conceptual:
¿Existe un punto en la ruta de producción donde la información acumulada
es suficiente para predecir la falla, usando solo el patrón de visitas
y la distinción entre ausencia de medición y medición inválida?

X₀ = (0.9942, 0.0023, 0.0020, 0.0015)
     Prior asimétrico que refleja la prevalencia real de fallas.
     Plantea la pregunta dura: ¿qué evidencia mueve una creencia de 99.4%?

X* = {X_t(cluster_1 ∪ 2 ∪ 3) > 0.30} (desviar)
   ∪ {X_t(sin_falla) > 0.998} (liberar)

Qué responde la trayectoria:
La estación donde X_t cruza el umbral de desvío es el
"punto de detección temprana". Si ocurre en el 50% de la ruta,
CI puede alertar antes que la inspección final.
```

#### MIMIC-III
```
Pregunta conceptual:
¿Puede CI cuantificar el costo informacional de una intervención médica
que degrada la evidencia posterior, y puede hacerlo de forma auditable?

X₀ = f(SOFA_admision)
     Ancla en herramienta clínica estándar.
     El experimento pregunta "¿CI agrega valor después de SOFA?"

X* = {X_t(sepsis ∪ severa ∪ shock) > 0.75 antes de sepsis_onset_time}
     Evaluación retrospectiva, no contrafactual.

Qué responde la trayectoria:
La diferencia en reducción de H(X_t) entre grupos con y sin antibiótico
previo a punción, medida en unidades KL, cuantifica el costo informacional
de la intervención. Eso no lo produce ningún otro framework nativamente.
```

---

### F.3 Mapa de Preguntas por Experimento

```
Pregunta fundamental            CMAPSS FD001   CMAPSS FD003/4   Bosch   MIMIC-III
────────────────────────────────────────────────────────────────────────────────────
1. ¿Importa el orden?               ✓               ✓               ✓        ✓*
2. ¿Converge a región D_{s*}?       ✓               ✓               ✓        ✓
3. ¿Robusto a error en ℓ?           ✓ (fase 0)      ✓               —        ✓
4. ¿KL/costo ≈ política óptima?     ✓ (ablaciones)  ✓               —        —
5. ¿Qué pasa en la frontera?        —               ✓               ✓        —
6. ¿Cuantifica costo informacional  —               —               ✓        ✓
   de acción que degrada evidencia?
────────────────────────────────────────────────────────────────────────────────────
* MIMIC-III responde P1 si el antibiótico modifica la verosimilitud del hemocultivo
  → orden importa porque la acción intermedia cambia el dominio informacional

Un experimento que responde 0 preguntas = benchmark.
Un experimento que responde ≥ 2 = contribución científica.
El conjunto responde las 6 = validación del framework en su dimensión epistemológica.
```


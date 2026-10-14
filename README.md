# Colección Práctica de Librerías Esenciales de Python

Repositorio educativo con **12 scripts prácticos, limpios y autocontenidos** que demuestran el uso de librerías fundamentales del ecosistema Python, abarcando desde utilidades nativas de la biblioteca estándar hasta librerías de visualización, análisis de datos, desarrollo web y aprendizaje automático.

---

## Estructura del Repositorio

```text
python-librerias-ejemplos/
│
├── 01_math_example.py        # 1. Librería estándar: math
├── 02_random_example.py      # 2. Librería estándar: random
├── 03_datetime_example.py    # 3. Librería estándar: datetime
├── 04_csv_example.py         # 4. Librería estándar: csv
├── 05_fpdf_example.py        # 5. Librería externa: fpdf2
├── 06_reportlab_example.py   # 6. Librería externa: reportlab
├── 07_numpy_example.py       # 7. Librería externa: numpy
├── 08_pandas_example.py      # 8. Librería externa: pandas
├── 09_matplotlib_example.py  # 9. Librería externa: matplotlib
├── 10_requests_example.py    # 10. Librería externa: requests
├── 11_flask_example.py       # 11. Librería externa: flask
├── 12_sklearn_example.py     # 12. Librería externa: scikit-learn
│
├── requirements.txt          # Dependencias externas
├── .gitignore                # Archivos y carpetas ignorados por Git
├── .vscode/
│   └── settings.json         # Configuración recomendada para Visual Studio Code
└── README.md                 # Documentación completa del proyecto
```

---

## Tabla Resumen de Scripts

| # | Archivo | Librería | Tipo | Propósito Principal |
|---|---|---|---|---|
| **01** | `01_math_example.py` | `math` | Estándar | Constantes, redondeos, trigonometría, combinatoria y precisión flotante. |
| **02** | `02_random_example.py` | `random` | Estándar | Muestreo aleatorio, permutaciones, distribución normal y contraseñas. |
| **03** | `03_datetime_example.py` | `datetime` | Estándar | Fechas, horas, parseo/formateo (`strftime`/`strptime`), `timedelta` y zonas horarias. |
| **04** | `04_csv_example.py` | `csv` | Estándar | Lectura y escritura con `writer`, `reader`, `DictWriter` y `DictReader`. |
| **05** | `05_fpdf_example.py` | `fpdf2` | Externa | Generación de reportes PDF estructurados con tablas, encabezados y pies de página. |
| **06** | `06_reportlab_example.py` | `reportlab` | Externa | Construcción de documentos PDF corporativos con flujo Platypus y estilos tipográficos. |
| **07** | `07_numpy_example.py` | `numpy` | Externa | Computación vectorial, manipulación de arreglos, estadística y álgebra lineal. |
| **08** | `08_pandas_example.py` | `pandas` | Externa | Análisis y limpieza de DataFrames, filtrado, imputación y agregaciones (`groupby`). |
| **09** | `09_matplotlib_example.py` | `matplotlib` | Externa | Visualización con subplots (líneas, barras, histogramas y dispersión). |
| **10** | `10_requests_example.py` | `requests` | Externa | Consumo de APIs REST (GET, POST), cabeceras HTTP, timeouts y manejo de errores. |
| **11** | `11_flask_example.py` | `flask` | Externa | Microservicio API REST con rutas dinámicas, validación JSON y servidor web. |
| **12** | `12_sklearn_example.py` | `scikit-learn` | Externa | Flujo integral de Machine Learning: partición, escalado, RandomForest y evaluación. |

---

## Instalación y Configuración del Entorno

### 1. Requisitos Previos
- Python 3.9 o superior instalado en el sistema.
- Gestor de paquetes `pip` actualizado.

### 2. Clonar o abrir la carpeta del proyecto
Abre una terminal en el directorio raíz del proyecto:
```bash
cd python-librerias-ejemplos
```

### 3. Crear y activar un entorno virtual (Recomendado)

- **En Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
  *(Si PowerShell restringe la ejecución de scripts, puedes habilitarla temporalmente con: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process`)*

- **En Windows (CMD):**
  ```cmd
  python -m venv venv
  venv\Scripts\activate.bat
  ```

- **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 4. Instalar las dependencias externas
Ejecuta el siguiente comando para instalar únicamente las librerías externas que los scripts requieren:
```bash
pip install -r requirements.txt
```

---

## Guía Detallada de Ejecución por Script

### Script 01: `math` (Librería Estándar)
Explora funciones matemáticas avanzadas sin requerir paquetes de terceros.
- **Conceptos:** Constantes ($\pi$, $e$, $\tau$), funciones de piso/techo (`ceil`, `floor`), máximo común divisor (`gcd`), combinaciones (`comb`), distancias euclidianas (`hypot`, `dist`) y comparaciones seguras de punto flotante (`isclose`).
- **Comando de ejecución:**
  ```bash
  python 01_math_example.py
  ```

---

### Script 02: `random` (Librería Estándar)
Demuestra la generación pseudoaleatoria de datos para simulaciones, juegos o pruebas.
- **Conceptos:** Números uniformes, elección ponderada con pesos (`choices`), selección sin reemplazo (`sample`), mezcla aleatoria de listas (`shuffle`), distribución gaussiana y fijación de semilla con `seed()`.
- **Comando de ejecución:**
  ```bash
  python 02_random_example.py
  ```

---

### Script 03: `datetime` (Librería Estándar)
Manipulación y cálculos temporales en Python.
- **Conceptos:** Fechas locales y en formato UTC, conversión de cadenas a objetos `datetime` (`strptime`) y viceversa (`strftime`), operaciones aritméticas de suma y resta con `timedelta`, cálculo de plazos y zonas horarias simples con `timezone`.
- **Comando de ejecución:**
  ```bash
  python 03_datetime_example.py
  ```

---

### Script 04: `csv` (Librería Estándar)
Lectura, escritura y procesamiento de archivos tabulares delimitados por comas o punto y coma.
- **Conceptos:** Uso de `csv.writer` / `csv.reader`, manejo limpio de delimitadores con `csv.DictWriter` y `csv.DictReader`, agregación de ingresos totales y extracción de reportes.
- **Comando de ejecución:**
  ```bash
  python 04_csv_example.py
  ```

---

### Script 05: `fpdf2` (Librería Externa)
Generación de documentos PDF vectoriales mediante código imperativo y orientado a objetos.
- **Conceptos:** Personalización de encabezados (`header`) y pies de página (`footer`) con numeración dinámica `{nb}`, cajas de texto destacadas (Callouts), diseño de tablas con cabeceras de color y filas alternas.
- **Comando de ejecución:**
  ```bash
  python 05_fpdf_example.py
  ```
- **Salida generada:** Archivo `reporte_fpdf.pdf`.

---

### Script 06: `reportlab` (Librería Externa)
Construcción de PDFs empresariales y de alta precisión tipográfica utilizando la arquitectura Platypus.
- **Conceptos:** `SimpleDocTemplate`, hojas de estilo (`getSampleStyleSheet`, `ParagraphStyle`), párrafos tipográficos, elementos `Spacer`, tablas con `TableStyle` y numeración precisa de dos pasadas mediante un `NumberedCanvas`.
- **Comando de ejecución:**
  ```bash
  python 06_reportlab_example.py
  ```
- **Salida generada:** Archivo `reporte_reportlab.pdf`.

---

### Script 07: `numpy` (Librería Externa)
Base del cálculo numérico y científico en Python.
- **Conceptos:** Creación de matrices y vectores (`ndarrays`), segmentación booleana de datos, operaciones vectorizadas sin bucles tradicionales, broadcasting, funciones de agregación por ejes (`axis=0`, `axis=1`) y operaciones de álgebra lineal (`@`, transpuesta, determinantes).
- **Comando de ejecución:**
  ```bash
  python 07_numpy_example.py
  ```

---

### Script 08: `pandas` (Librería Externa)
Manipulación estructurada y análisis exploratorio de datos.
- **Conceptos:** Creación de `DataFrame`, inspección rápida (`info`, `describe`), filtrado por múltiples condiciones booleanas, imputación de valores nulos (`fillna`), creación de columnas calculadas y agrupaciones analíticas con `groupby().agg()`.
- **Comando de ejecución:**
  ```bash
  python 08_pandas_example.py
  ```

---

### Script 09: `matplotlib` (Librería Externa)
Creación de gráficos estadísticos y analíticos con calidad de publicación.
- **Conceptos:** Creación de un panel de subgráficos 2x2:
  1. Gráfico de líneas temporales con área sombreada (`fill_between`).
  2. Gráfico de barras con etiquetas de valores calculadas.
  3. Histograma de distribución con estimación de media.
  4. Diagrama de dispersión (*Scatter plot*) con tamaño y mapa de color (*Colormap*).
- **Comando de ejecución:**
  ```bash
  python 09_matplotlib_example.py
  ```
- **Salida generada:** Archivo `grafico_matplotlib.png` a 300 DPI.

---

### Script 10: `requests` (Librería Externa)
Cliente HTTP estándar para interactuar con servicios web y APIs REST.
- **Conceptos:** Solicitudes `GET` con parámetros de consulta (`params`), cabeceras HTTP personalizadas, parseo directo de respuestas a formato JSON, solicitudes `POST` con envío de datos y gestión robusta de excepciones con `raise_for_status()`.
- **Comando de ejecución:**
  ```bash
  python 10_requests_example.py
  ```

---

### Script 11: `flask` (Librería Externa)
Creación de microservicios y APIs web ligeras.
- **Conceptos:** Rutas decoradas con `@app.route`, parámetros dinámicos en URL (`<int:id>`), serialización con `jsonify`, validación de cuerpo JSON en métodos `POST` y códigos de respuesta HTTP semánticos (200, 201, 400, 404).
- **Modos de ejecución:**
  - **Modo Pruebas Automáticas (no bloqueante):**
    ```bash
    python 11_flask_example.py
    ```
    *Ejecuta una batería completa de pruebas contra los endpoints utilizando el cliente interno `test_client()` de Flask.*
  - **Modo Servidor Web en Vivo:**
    ```bash
    python 11_flask_example.py --server
    ```
    *Inicia el servidor local en `http://127.0.0.1:5000` para probar desde el navegador o herramientas como Postman / cURL.*

---

### Script 12: `scikit-learn` (Librería Externa)
Implementación completa de un pipeline supervisado de Machine Learning.
- **Conceptos:** Carga del clásico dataset Iris, partición estratificada en entrenamiento y prueba (`train_test_split`), estandarización con `StandardScaler`, ajuste de un clasificador `RandomForestClassifier`, predicción, matriz de confusión, reporte de métricas (`precision`, `recall`, `f1-score`) y predicción probabilística (`predict_proba`) para nuevos casos.
- **Comando de ejecución:**
  ```bash
  python 12_sklearn_example.py
  ```

---

## Cómo abrir en Visual Studio Code

Este repositorio incluye una carpeta `.vscode/` configurada para brindar la mejor experiencia en Visual Studio Code.

1. Abre tu terminal en la carpeta del repositorio:
   ```bash
   code .
   ```
2. Si tienes instalada la extensión oficial de **Python** (Microsoft), VS Code detectará automáticamente tus archivos y te sugerirá seleccionar el intérprete del entorno virtual (`./venv`).
3. Puedes ejecutar cualquier script abriéndolo y presionando el botón **"Run Python File"** (ícono de reproducir en la esquina superior derecha) o pulsando `F5`.

---

## Licencia y Buenas Prácticas
Este código ha sido diseñado con fines educativos y de referencia rápida. Sigue los lineamientos de estilo de código [PEP 8](https://peps.python.org/pep-0008/) y cuenta con tipado estático indicativo para facilitar su comprensión y mantenimiento.

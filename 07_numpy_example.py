"""
07_numpy_example.py
Demostración práctica de la librería científica 'numpy'.
Instalación: pip install numpy

Cubre:
- Creación y propiedades de arreglos multidimensionales (ndarrays)
- Indexación avanzada, cortes (slicing) y máscaras booleanas
- Operaciones vectorizadas y broadcasting (sin bucles 'for')
- Estadísticas descriptivas y agregaciones por ejes (axis 0 y 1)
- Álgebra lineal: producto punto/matricial y determinantes (np.linalg)
- Manipulación de formas (reshape y flatten)
"""

import numpy as np


def encabezado(titulo: str):
    print("\n" + "=" * 60)
    print(f" {titulo.upper()} ")
    print("=" * 60)


def demo_creacion_y_atributos():
    encabezado("1. Creación de Arreglos y Atributos")
    # Arreglos 1D y 2D
    arr_1d = np.array([10, 20, 30, 40, 50], dtype=np.int32)
    matriz = np.array([[1.5, 2.0, 3.5], [4.0, 5.5, 6.0]], dtype=np.float64)

    # Generadores automáticos
    ceros = np.zeros((2, 3))
    unos = np.ones((2, 2))
    rango = np.arange(0, 20, 5)  # [0, 5, 10, 15]
    lineal = np.linspace(0.0, 1.0, 5)  # 5 puntos equidistantes entre 0 y 1

    print(f"Arreglo 1D          : {arr_1d}")
    print(f"Dimensiones matriz  : shape={matriz.shape}, ndim={matriz.ndim}, dtype={matriz.dtype}")
    print(f"Matriz de ceros:\n{ceros}")
    print(f"np.linspace(0, 1, 5): {lineal}")


def demo_indexacion_y_mascaras():
    encabezado("2. Indexación, Slicing y Máscaras Booleanas")
    datos = np.array([12, 45, 78, 23, 89, 34, 91, 15])
    print(f"Datos originales : {datos}")

    # Slicing básico [inicio:fin:paso]
    print(f"Subarreglo [2:6] : {datos[2:6]}")

    # Filtrado booleano (vectorizado)
    condicion = datos > 40
    print(f"Máscara (> 40)   : {condicion}")
    filtrados = datos[condicion]
    print(f"Elementos > 40   : {filtrados}")

    # Reemplazo condicional con np.where
    categorizado = np.where(datos >= 50, "Aprobado", "Reprobado")
    print(f"np.where (>=50)  : {categorizado}")


def demo_vectorizacion_y_broadcasting():
    encabezado("3. Operaciones Vectorizadas y Broadcasting")
    precios = np.array([100.0, 250.0, 400.0, 1500.0])
    iva = 1.16  # Escalar que se expande automáticamente (broadcasting)
    descuento_porcentual = np.array([0.05, 0.10, 0.15, 0.20])

    # Cálculo sin ningún bucle
    precios_con_iva = precios * iva
    precios_finales = precios_con_iva * (1 - descuento_porcentual)

    print(f"Precios base       : {precios}")
    print(f"Precios con IVA 16%: {np.round(precios_con_iva, 2)}")
    print(f"Precios finales    : {np.round(precios_finales, 2)}")


def demo_estadisticas_y_ejes():
    encabezado("4. Estadísticas Descriptivas y Operaciones por Eje")
    # Calificaciones de 4 alumnos en 3 exámenes
    calificaciones = np.array([
        [85, 90, 78],
        [92, 88, 95],
        [70, 65, 72],
        [88, 94, 91],
    ])

    print("Matriz de calificaciones (4 estudiantes x 3 materias):")
    print(calificaciones)

    print(f"\nMedia general           : {calificaciones.mean():.2f}")
    print(f"Desviación estándar     : {calificaciones.std():.2f}")
    print(f"Valor máximo absoluto   : {calificaciones.max()} en índice {calificaciones.argmax()}")

    # Agregación por columnas (axis=0) -> Promedio por examen
    promedio_examenes = calificaciones.mean(axis=0)
    print(f"Promedio por examen (axis=0): {np.round(promedio_examenes, 2)}")

    # Agregación por filas (axis=1) -> Promedio por estudiante
    promedio_alumnos = calificaciones.mean(axis=1)
    print(f"Promedio por alumno (axis=1): {np.round(promedio_alumnos, 2)}")


def demo_algebra_lineal_y_formas():
    encabezado("5. Álgebra Lineal y Reestructuración (Reshape)")
    # Reshape de 1D a 2D
    secuencia = np.arange(1, 10)  # 1 al 9
    matriz_3x3 = secuencia.reshape((3, 3))
    print("Matriz 3x3 generada con reshape:")
    print(matriz_3x3)

    # Transpuesta
    print("\nTranspuesta de la matriz:")
    print(matriz_3x3.T)

    # Multiplicación matricial (operador @)
    vector = np.array([1, 2, 3])
    producto = matriz_3x3 @ vector
    print(f"\nProducto matricial (Matriz 3x3 @ Vector [1, 2, 3]): {producto}")

    # Determinante e inversión con linalg
    matriz_invertible = np.array([[4, 7], [2, 6]])
    det = np.linalg.det(matriz_invertible)
    inversa = np.linalg.inv(matriz_invertible)
    print(f"\nDeterminante de [[4, 7], [2, 6]]: {det:.2f}")
    print("Matriz inversa:")
    print(inversa)


def main():
    print("============================================================")
    print("   DEMOSTRACIÓN DE LA LIBRERÍA: numpy                      ")
    print("============================================================")
    demo_creacion_y_atributos()
    demo_indexacion_y_mascaras()
    demo_vectorizacion_y_broadcasting()
    demo_estadisticas_y_ejes()
    demo_algebra_lineal_y_formas()
    print("\n[OK] Script de 'numpy' ejecutado correctamente.\n")


if __name__ == "__main__":
    main()

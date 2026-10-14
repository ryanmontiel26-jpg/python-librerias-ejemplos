"""
12_sklearn_example.py
Demostración práctica de la librería de Machine Learning 'scikit-learn'.
Instalación: pip install scikit-learn

Cubre:
- Carga y exploración de un conjunto de datos (Dataset Iris)
- División de datos en conjuntos de entrenamiento y prueba (train_test_split)
- Preprocesamiento y normalización de variables con StandardScaler
- Entrenamiento y ajuste de un modelo clasificador (RandomForestClassifier)
- Inferencia y predicción en datos no vistos
- Evaluación del modelo: Exactitud (Accuracy), Matriz de Confusión y Classification Report
- Predicción probabilística sobre un nuevo espécimen (predict_proba)
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def encabezado(titulo: str):
    print("\n" + "=" * 60)
    print(f" {titulo.upper()} ")
    print("=" * 60)


def demo_carga_y_exploracion():
    encabezado("1. Carga del Conjunto de Datos (Iris Dataset)")
    iris = load_iris()
    X = iris.data
    y = iris.target
    nombres_caracteristicas = iris.feature_names
    nombres_clases = iris.target_names

    print(f"Número total de muestras   : {X.shape[0]}")
    print(f"Número de características : {X.shape[1]}")
    print(f"Nombres de características: {nombres_caracteristicas}")
    print(f"Clases a clasificar       : {list(nombres_clases)} (0, 1, 2)")
    print(f"Primeras 3 muestras:\n{X[:3]}")

    return X, y, nombres_caracteristicas, nombres_clases


def demo_division_y_escalado(X, y):
    encabezado("2. División de Datos (Train/Test) y Escalado")
    # División 70% entrenamiento y 30% prueba con semilla reproducible
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42, stratify=y
    )

    print(f"Muestras de entrenamiento: {X_train.shape[0]}")
    print(f"Muestras de prueba       : {X_test.shape[0]}")

    # Escalado de características (Estandarización Z-score: media=0, varianza=1)
    escalador = StandardScaler()
    X_train_escalado = escalador.fit_transform(X_train)
    X_test_escalado = escalador.transform(X_test)

    print(f"\nMedia antes del escalado (Train)  : {X_train.mean(axis=0).round(2)}")
    print(f"Media después del escalado (Train): {X_train_escalado.mean(axis=0).round(2)}")

    return X_train_escalado, X_test_escalado, y_train, y_test, escalador


def demo_entrenamiento_y_evaluacion(X_train, X_test, y_train, y_test, nombres_clases):
    encabezado("3. Entrenamiento del Modelo (Random Forest)")
    # Inicialización del estimador
    modelo = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)

    # Entrenamiento
    modelo.fit(X_train, y_train)
    print("Modelo entrenado con éxito.")

    # Predicción sobre el conjunto de test
    y_pred = modelo.predict(X_test)

    # Evaluación
    exactitud = accuracy_score(y_test, y_pred)
    matriz_conf = confusion_matrix(y_test, y_pred)

    print(f"\nExactitud global (Accuracy): {exactitud * 100:.2f}%")
    print("\nMatriz de Confusión:")
    print(matriz_conf)

    print("\nReporte Detallado de Clasificación:")
    print(classification_report(y_test, y_pred, target_names=nombres_clases))

    # Importancia de las características
    print("Importancia relativa de características:")
    importancias = modelo.feature_importances_
    for i, imp in enumerate(importancias):
        print(f"  - Característica #{i}: {imp * 100:.2f}%")

    return modelo


def demo_prediccion_nuevo_caso(modelo, escalador, nombres_clases):
    encabezado("4. Inferencia con Muestra No Vista")
    # Ejemplo de medidas de una flor: [sepal length, sepal width, petal length, petal width]
    nueva_flor = np.array([[5.1, 3.5, 1.4, 0.2]])
    print(f"Medidas de la flor a clasificar: {nueva_flor[0]}")

    # Escalar usando la misma transformación de entrenamiento
    nueva_flor_escalada = escalador.transform(nueva_flor)

    # Predicción de clase y probabilidades
    clase_predicha_idx = modelo.predict(nueva_flor_escalada)[0]
    probabilidades = modelo.predict_proba(nueva_flor_escalada)[0]

    nombre_predicho = nombres_clases[clase_predicha_idx]
    print(f"\nEspecie predicha por el modelo: '{nombre_predicho.upper()}'")
    print("Probabilidades por especie:")
    for clase, prob in zip(nombres_clases, probabilidades):
        print(f"  - {clase:<12}: {prob * 100:6.2f}%")


def main():
    print("============================================================")
    print("   DEMOSTRACIÓN DE LA LIBRERÍA: scikit-learn               ")
    print("============================================================")
    X, y, features, classes = demo_carga_y_exploracion()
    X_train, X_test, y_train, y_test, escalador = demo_division_y_escalado(X, y)
    modelo = demo_entrenamiento_y_evaluacion(X_train, X_test, y_train, y_test, classes)
    demo_prediccion_nuevo_caso(modelo, escalador, classes)
    print("\n[OK] Script de 'scikit-learn' ejecutado correctamente.\n")


if __name__ == "__main__":
    main()

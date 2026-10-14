"""
08_pandas_example.py
Demostración práctica de la librería de análisis de datos 'pandas'.
Instalación: pip install pandas

Cubre:
- Creación de Series y DataFrames a partir de estructuras de datos
- Inspección de datos (info, describe, head, tail)
- Filtrado y consultas avanzadas con operadores lógicos y .loc/.iloc
- Creación de columnas calculadas y transformaciones con apply/lambda
- Detección e imputación de valores faltantes (NaN)
- Agrupación y agregación multidimensional (groupby + agg)
- Ordenamiento de datos
"""

import pandas as pd
import numpy as np


def encabezado(titulo: str):
    print("\n" + "=" * 60)
    print(f" {titulo.upper()} ")
    print("=" * 60)


def crear_dataframe_ejemplo() -> pd.DataFrame:
    datos = {
        "id_empleado": [101, 102, 103, 104, 105, 106, 107, 108],
        "nombre": ["Elena", "Carlos", "Sofía", "Martín", "Lucía", "Diego", "Valeria", "Andrés"],
        "departamento": ["Ventas", "TI", "Ventas", "Marketing", "TI", "Marketing", "TI", "Ventas"],
        "ciudad": ["Madrid", "Barcelona", "Madrid", "Valencia", "Madrid", "Barcelona", "Valencia", "Sevilla"],
        "salario": [3200, 4100, 3450, 2900, 4300, 3100, 3950, np.nan],  # Andrés tiene salario faltante
        "antiguedad_anios": [2, 5, 3, 1, 6, 2, 4, 1],
        "evaluacion_desempeno": [8.8, 9.4, 7.9, 8.1, 9.7, 7.5, 8.9, 8.0],
    }
    return pd.DataFrame(datos)


def demo_inspeccion_basica(df: pd.DataFrame):
    encabezado("1. Estructura e Inspección Básica del DataFrame")
    print(f"Dimensiones del DataFrame: {df.shape[0]} filas x {df.shape[1]} columnas\n")
    print("Primeras 3 filas (.head):")
    print(df.head(3))

    print("\nResumen estadístico de variables numéricas (.describe):")
    print(df[["salario", "antiguedad_anios", "evaluacion_desempeno"]].describe().round(2))


def demo_limpieza_valores_nulos(df: pd.DataFrame) -> pd.DataFrame:
    encabezado("2. Detección y Tratamiento de Valores Faltantes (NaN)")
    print(f"Conteo de valores nulos por columna:\n{df.isna().sum()}")

    # Imputamos el salario faltante usando el promedio salarial de su respectivo departamento
    salario_medio_ventas = df[df["departamento"] == "Ventas"]["salario"].mean()
    print(f"\nImputando salario faltante con el promedio de Ventas (${salario_medio_ventas:.2f})...")
    df["salario"] = df["salario"].fillna(salario_medio_ventas)
    print("Valores nulos restantes tras imputación:", df["salario"].isna().sum())
    return df


def demo_filtrado_y_seleccion(df: pd.DataFrame):
    encabezado("3. Filtrado y Consultas Condicionales")
    # Filtrar empleados de TI con salario >= 4000
    condicion_ti = (df["departamento"] == "TI") & (df["salario"] >= 4000)
    filtro_ti = df[condicion_ti][["nombre", "departamento", "salario", "ciudad"]]
    print("Personal de TI con salario >= 4,000:")
    print(filtro_ti.to_string(index=False))

    # Filtrar empleados con excelente desempeño (evaluacion >= 9.0) o alta antigüedad (>= 5 años)
    condicion_destacados = (df["evaluacion_desempeno"] >= 9.0) | (df["antiguedad_anios"] >= 5)
    destacados = df.loc[condicion_destacados, ["nombre", "antiguedad_anios", "evaluacion_desempeno"]]
    print("\nEmpleados destacados (evaluación >= 9.0 o antigüedad >= 5 años):")
    print(destacados.to_string(index=False))


def demo_columnas_calculadas(df: pd.DataFrame) -> pd.DataFrame:
    encabezado("4. Creación de Columnas Calculadas y Transformaciones")
    # 1. Cálculo vectorizado: Bono anual del 10% del salario
    df["bono_anual"] = df["salario"] * 0.10

    # 2. Transformación con apply/lambda: Clasificación de nivel de experiencia
    def clasificar_nivel(anios):
        if anios >= 5:
            return "Senior"
        elif anios >= 3:
            return "Semi-Senior"
        return "Junior"

    df["nivel"] = df["antiguedad_anios"].apply(clasificar_nivel)

    print("Columnas añadidas ('bono_anual' y 'nivel'):")
    print(df[["nombre", "salario", "bono_anual", "antiguedad_anios", "nivel"]].head(5).to_string(index=False))
    return df


def demo_agrupaciones_groupby(df: pd.DataFrame):
    encabezado("5. Agrupaciones y Métricas Agregadas (GroupBy)")
    resumen_depto = df.groupby("departamento").agg(
        num_empleados=("id_empleado", "count"),
        salario_promedio=("salario", "mean"),
        salario_maximo=("salario", "max"),
        desempeno_promedio=("evaluacion_desempeno", "mean"),
    ).round(2)

    print("Métricas consolidadas por departamento:")
    print(resumen_depto)

    # Ordenamiento por salario promedio descendente
    print("\nDepartamentos ordenados por salario promedio:")
    print(resumen_depto.sort_values(by="salario_promedio", ascending=False)[["salario_promedio"]])


def main():
    print("============================================================")
    print("   DEMOSTRACIÓN DE LA LIBRERÍA: pandas                     ")
    print("============================================================")
    df = crear_dataframe_ejemplo()
    demo_inspeccion_basica(df)
    df = demo_limpieza_valores_nulos(df)
    demo_filtrado_y_seleccion(df)
    df = demo_columnas_calculadas(df)
    demo_agrupaciones_groupby(df)
    print("\n[OK] Script de 'pandas' ejecutado correctamente.\n")


if __name__ == "__main__":
    main()

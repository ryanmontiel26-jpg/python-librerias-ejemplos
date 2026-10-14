"""
04_csv_example.py
Demostración práctica de la librería estándar 'csv' de Python.
No requiere instalación externa.

Cubre:
- Escritura de datos tabulares con csv.writer
- Lectura secuencial con csv.reader
- Escritura orientada a diccionarios con csv.DictWriter
- Lectura estructurada con csv.DictReader
- Delimitadores personalizados (comas y punto y coma)
- Procesamiento y agregación de datos extraídos de un CSV
"""

import csv
from pathlib import Path


def encabezado(titulo: str):
    print("\n" + "=" * 60)
    print(f" {titulo.upper()} ")
    print("=" * 60)


ARCHIVO_BASICO = Path("datos_basicos.csv")
ARCHIVO_VENTAS = Path("ventas_demo.csv")


def demo_writer_y_reader_basico():
    encabezado("1. Uso de csv.writer y csv.reader (Listas)")

    filas = [
        ["ID", "Nombre", "Departamento", "Salario"],
        [101, "Ana Morales", "Ingeniería", 4200.50],
        [102, "Carlos Ruiz", "Marketing", 3100.00],
        [103, "Elena Soto", "Ventas", 3800.75],
        [104, "David Vega", "Ingeniería", 4600.00],
    ]

    # Escritura
    with open(ARCHIVO_BASICO, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerows(filas)
    print(f"-> Archivo '{ARCHIVO_BASICO}' generado exitosamente.")

    # Lectura
    print("\nContenido leído con csv.reader:")
    with open(ARCHIVO_BASICO, mode="r", newline="", encoding="utf-8") as f:
        lector = csv.reader(f)
        encabezados = next(lector)
        print(f"Encabezados: {encabezados}")
        for fila in lector:
            print(f"  ID: {fila[0]} | Empleado: {fila[1]:<15} | Depto: {fila[2]:<12} | Salario: ${float(fila[3]):.2f}")


def demo_dictwriter_y_dictreader():
    encabezado("2. Uso de csv.DictWriter y csv.DictReader (Diccionarios)")

    transacciones = [
        {"id_transaccion": "TX-001", "categoria": "Laptops", "unidades": 3, "precio_unitario": 850.0},
        {"id_transaccion": "TX-002", "categoria": "Monitores", "unidades": 5, "precio_unitario": 210.0},
        {"id_transaccion": "TX-003", "categoria": "Accesorios", "unidades": 12, "precio_unitario": 25.5},
        {"id_transaccion": "TX-004", "categoria": "Laptops", "unidades": 2, "precio_unitario": 920.0},
        {"id_transaccion": "TX-005", "categoria": "Monitores", "unidades": 4, "precio_unitario": 195.0},
    ]

    campos = ["id_transaccion", "categoria", "unidades", "precio_unitario"]

    # Escritura con DictWriter
    with open(ARCHIVO_VENTAS, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(transacciones)
    print(f"-> Archivo '{ARCHIVO_VENTAS}' generado con DictWriter.")

    # Lectura con DictReader y cálculo de totales
    print("\nLectura y análisis de transacciones con DictReader:")
    ingreso_total = 0.0
    ventas_por_categoria = {}

    with open(ARCHIVO_VENTAS, mode="r", newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            unidades = int(fila["unidades"])
            precio = float(fila["precio_unitario"])
            subtotal = unidades * precio
            categoria = fila["categoria"]

            ingreso_total += subtotal
            ventas_por_categoria[categoria] = ventas_por_categoria.get(categoria, 0.0) + subtotal

            print(f"  {fila['id_transaccion']} -> {categoria:<12} | {unidades:2d} un. @ ${precio:6.2f} = ${subtotal:8.2f}")

    print("\nResumen financiero extraído:")
    print(f"  Ingreso total general : ${ingreso_total:,.2f}")
    for cat, total in ventas_por_categoria.items():
        print(f"  - Total {cat:<11}: ${total:,.2f}")


def demo_delimitador_personalizado():
    encabezado("3. Delimitadores Personalizados (Punto y Coma ';')")
    archivo_custom = Path("catalogo_delimitador_puntoycoma.csv")

    datos = [
        {"Producto": "Teclado Mecánico", "SKU": "TEC-01", "Stock": 45},
        {"Producto": "Mouse Inalámbrico", "SKU": "MOU-02", "Stock": 80},
    ]

    with open(archivo_custom, mode="w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=["Producto", "SKU", "Stock"], delimiter=";")
        escritor.writeheader()
        escritor.writerows(datos)

    # Ver el texto crudo del archivo
    contenido_crudo = archivo_custom.read_text(encoding="utf-8")
    print(f"Contenido crudo con delimitador ';':\n{contenido_crudo}")


def main():
    print("============================================================")
    print("   DEMOSTRACIÓN DE LA LIBRERÍA ESTÁNDAR: csv               ")
    print("============================================================")
    demo_writer_y_reader_basico()
    demo_dictwriter_y_dictreader()
    demo_delimitador_personalizado()
    print("\n[OK] Script de 'csv' ejecutado correctamente.\n")


if __name__ == "__main__":
    main()

"""
02_random_example.py
Demostración práctica de la librería estándar 'random' de Python.
No requiere instalación externa.

Cubre:
- Generación de números aleatorios (enteros y decimales)
- Selección aleatoria simple y ponderada
- Muestreo sin reemplazo y mezcla de colecciones (shuffle)
- Distribución normal / gaussiana
- Ejemplo aplicado: Generador de contraseñas y dados
- Reproducibilidad con semillas (seed)
"""

import random
import string


def encabezado(titulo: str):
    print("\n" + "=" * 60)
    print(f" {titulo.upper()} ")
    print("=" * 60)


def demo_numeros_aleatorios():
    encabezado("1. Generación de Números Aleatorios")
    # Float entre [0.0, 1.0)
    print(f"random.random()            : {random.random():.5f}")

    # Float uniforme entre rango [a, b]
    print(f"random.uniform(10.5, 25.0) : {random.uniform(10.5, 25.0):.2f}")

    # Entero inclusivo en [a, b]
    print(f"random.randint(1, 100)     : {random.randint(1, 100)}")

    # Entero con paso (step), ej: números pares entre 10 y 30
    print(f"random.randrange(10, 30, 2): {random.randrange(10, 30, 2)}")


def demo_seleccion_y_muestreo():
    encabezado("2. Selección y Muestreo")
    lenguajes = ["Python", "JavaScript", "Rust", "Go", "C++", "TypeScript"]
    print(f"Lista de lenguajes: {lenguajes}")

    # Elección de un elemento
    elegido = random.choice(lenguajes)
    print(f"Elección única (choice)            : {elegido}")

    # Elección con pesos / ponderada (choices) con reemplazo
    premios = ["Bronce", "Plata", "Oro", "Diamante"]
    pesos = [70, 20, 8, 2]  # El Diamante solo tiene 2% de probabilidad
    tirada_loterias = random.choices(premios, weights=pesos, k=5)
    print(f"Tiradas ponderadas k=5 (choices)  : {tirada_loterias}")

    # Muestreo sin reemplazo (sample) - único por elemento
    numeros_loteria = random.sample(range(1, 51), k=6)
    print(f"Boleto de lotería (sample 6 de 50) : {sorted(numeros_loteria)}")


def demo_mezcla_colecciones():
    encabezado("3. Mezcla de Elementos in-place (Shuffle)")
    baraja = [f"{n} de Copas" for n in range(1, 8)]
    print(f"Baraja original : {baraja}")
    random.shuffle(baraja)
    print(f"Baraja mezclada : {baraja}")


def demo_distribucion_estadistica():
    encabezado("4. Distribución Normal (Gaussiana)")
    # Media = 175 cm, Desviación estándar = 8 cm (ejemplo de estaturas)
    media = 175
    desv = 8
    muestras = [round(random.gauss(media, desv), 1) for _ in range(5)]
    print(f"Muestras de estaturas (media=175, std=8): {muestras}")


def demo_caso_practico_password():
    encabezado("5. Caso Práctico: Generador de Contraseñas Seguras")
    caracteres = string.ascii_letters + string.digits + "!@#$%&*-_"
    longitud = 14
    password = "".join(random.choice(caracteres) for _ in range(longitud))
    print(f"Contraseña aleatoria generada ({longitud} caracteres): {password}")


def demo_reproducibilidad_semilla():
    encabezado("6. Reproducibilidad mediante Semilla (Seed)")
    semilla = 42

    random.seed(semilla)
    serie_1 = [random.randint(1, 10) for _ in range(4)]

    random.seed(semilla)
    serie_2 = [random.randint(1, 10) for _ in range(4)]

    print(f"Serie 1 con semilla {semilla}: {serie_1}")
    print(f"Serie 2 con semilla {semilla}: {serie_2}")
    print(f"¿Las series son idénticas?: {serie_1 == serie_2}")


def main():
    print("============================================================")
    print("   DEMOSTRACIÓN DE LA LIBRERÍA ESTÁNDAR: random            ")
    print("============================================================")
    demo_numeros_aleatorios()
    demo_seleccion_y_muestreo()
    demo_mezcla_colecciones()
    demo_distribucion_estadistica()
    demo_caso_practico_password()
    demo_reproducibilidad_semilla()
    print("\n[OK] Script de 'random' ejecutado correctamente.\n")


if __name__ == "__main__":
    main()

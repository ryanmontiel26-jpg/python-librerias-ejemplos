"""
01_math_example.py
Demostración práctica de la librería estándar 'math' de Python.
No requiere instalación externa.

Cubre:
- Constantes matemáticas esenciales
- Redondeo y funciones numéricas básicas
- Geometría, distancias euclidianas y trigonometría
- Logaritmos y exponenciales
- Combinatoria y teoría de números (MCD, MCM, factorial)
- Comparación precisa de números de punto flotante
"""

import math


def encabezado(titulo: str):
    print("\n" + "=" * 60)
    print(f" {titulo.upper()} ")
    print("=" * 60)


def demo_constantes():
    encabezado("1. Constantes Matemáticas")
    print(f"Pi (pi)             : {math.pi}")
    print(f"Número de Euler (e) : {math.e}")
    print(f"Tau (2*pi)          : {math.tau}")
    print(f"Infinito positivo   : {math.inf}")
    print(f"No es un número(NaN): {math.nan}")


def demo_redondeo_y_aritmetica():
    encabezado("2. Funciones Numéricas y Redondeo")
    numero = 7.65
    print(f"Número original     : {numero}")
    print(f"Techo (ceil)        : {math.ceil(numero)}    (menor entero >= número)")
    print(f"Piso (floor)        : {math.floor(numero)}   (mayor entero <= número)")
    print(f"Truncado (trunc)    : {math.trunc(numero)}   (elimina la parte decimal)")
    print(f"Valor absoluto (fabs): {math.fabs(-numero)}")
    print(f"Raíz cuadrada (sqrt): {math.sqrt(64)}")


def demo_teoria_numeros_y_combinatoria():
    encabezado("3. Teoría de Números y Combinatoria")
    # Máximo común divisor y mínimo común múltiplo
    a, b = 48, 180
    print(f"Números evaluados   : {a} y {b}")
    print(f"MCD (math.gcd)      : {math.gcd(a, b)}")
    print(f"MCM (math.lcm)      : {math.lcm(a, b)}")

    # Factorial y combinatoria
    n, k = 10, 3
    print(f"\nFactorial de 5 (5!) : {math.factorial(5)}")
    print(f"Combinaciones C({n},{k}) (math.comb): {math.comb(n, k)} formas de elegir 3 elementos de 10")
    print(f"Permutaciones P({n},{k}) (math.perm): {math.perm(n, k)} formas ordenadas de elegir 3 elementos de 10")


def demo_geometria_y_trigonometria():
    encabezado("4. Geometría y Trigonometría")
    # Conversión de ángulos
    angulo_grados = 45.0
    angulo_radianes = math.radians(angulo_grados)
    print(f"Ángulo en grados    : {angulo_grados}°")
    print(f"Ángulo en radianes  : {angulo_radianes:.4f} rad")
    print(f"Seno de 45°         : {math.sin(angulo_radianes):.4f}")
    print(f"Coseno de 45°       : {math.cos(angulo_radianes):.4f}")
    print(f"Tangente de 45°     : {math.tan(angulo_radianes):.4f}")

    # Hipotenusa y distancias
    cateto1, cateto2 = 3.0, 4.0
    hipotenusa = math.hypot(cateto1, cateto2)
    print(f"\nHipotenusa triángulo rectángulo ({cateto1}, {cateto2}): {hipotenusa}")

    # Distancia euclidiana entre dos puntos (2D y 3D)
    punto_a = (1.0, 2.0, 5.0)
    punto_b = (4.0, 6.0, 5.0)
    distancia = math.dist(punto_a, punto_b)
    print(f"Distancia entre {punto_a} y {punto_b} (math.dist): {distancia}")


def demo_logaritmos_y_comparacion():
    encabezado("5. Exponenciales, Logaritmos y Comparación Flotante")
    valor = 1000
    print(f"Logaritmo natural ln({valor})  : {math.log(valor):.4f}")
    print(f"Logaritmo base 10 log10({valor}): {math.log10(valor)}")
    print(f"Logaritmo base 2 log2(256)      : {math.log2(256)}")
    print(f"Exponencial e^2 (math.exp(2))   : {math.exp(2):.4f}")

    # Comparación de flotantes (evitar problemas de redondeo IEEE 754)
    suma_flotante = 0.1 + 0.2
    esperado = 0.3
    print(f"\n¿0.1 + 0.2 == 0.3 con '=='?    : {suma_flotante == esperado} (Peligro de redondeo: {suma_flotante})")
    print(f"¿0.1 + 0.2 ~= 0.3 con math.isclose?: {math.isclose(suma_flotante, esperado)}")


def main():
    print("============================================================")
    print("   DEMOSTRACIÓN DE LA LIBRERÍA ESTÁNDAR: math              ")
    print("============================================================")
    demo_constantes()
    demo_redondeo_y_aritmetica()
    demo_teoria_numeros_y_combinatoria()
    demo_geometria_y_trigonometria()
    demo_logaritmos_y_comparacion()
    print("\n[OK] Script de 'math' ejecutado correctamente.\n")


if __name__ == "__main__":
    main()

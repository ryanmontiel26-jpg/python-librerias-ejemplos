"""
10_requests_example.py
Demostración práctica de la librería cliente HTTP 'requests'.
Instalación: pip install requests

Cubre:
- Solicitudes HTTP GET con parámetros de consulta (query params)
- Configuración de cabeceras personalizadas (Headers)
- Manejo seguro de timeouts y códigos de estado (raise_for_status)
- Parseo automático de respuestas JSON
- Solicitudes HTTP POST enviando carga útil (JSON payload)
- Captura robusta de excepciones (ConnectionError, Timeout, HTTPError)
"""

import requests


def encabezado(titulo: str):
    print("\n" + "=" * 60)
    print(f" {titulo.upper()} ")
    print("=" * 60)


BASE_URL = "https://jsonplaceholder.typicode.com"


def demo_get_con_parametros():
    encabezado("1. Solicitud GET con Parámetros de Consulta (Params)")
    url = f"{BASE_URL}/posts"
    parametros = {"userId": 1}
    cabeceras = {"User-Agent": "CursoPython/1.0", "Accept": "application/json"}

    print(f"URL de consulta : {url}")
    print(f"Parámetros      : {parametros}")

    try:
        # Siempre especificar timeout en peticiones de producción
        respuesta = requests.get(url, params=parametros, headers=cabeceras, timeout=10)

        # Lanza excepción si el código es 4xx o 5xx
        respuesta.raise_for_status()

        print(f"Código de estado: {respuesta.status_code} ({respuesta.reason})")
        print(f"Content-Type    : {respuesta.headers.get('Content-Type')}")

        publicaciones = respuesta.json()
        print(f"Publicaciones recibidas para userId=1: {len(publicaciones)}")

        # Mostrar las 2 primeras
        for i, pub in enumerate(publicaciones[:2], start=1):
            print(f"\n  [Post #{pub['id']}]")
            print(f"  Título: {pub['title']}")
            print(f"  Cuerpo: {pub['body'][:60]}...")

    except requests.exceptions.Timeout:
        print("[ERROR] El tiempo de espera de la solicitud ha expirado (Timeout).")
    except requests.exceptions.HTTPError as err:
        print(f"[ERROR] Error HTTP retornado por el servidor: {err}")
    except requests.exceptions.RequestException as err:
        print(f"[ERROR] Error en la conexión: {err}")


def demo_post_creacion_recurso():
    encabezado("2. Solicitud POST con Cuerpo JSON")
    url = f"{BASE_URL}/posts"
    nuevo_post = {
        "title": "Tutorial Avanzado de Python",
        "body": "Aprende a dominar las mejores librerías de Python paso a paso.",
        "userId": 99,
    }

    print(f"Enviando POST a : {url}")
    print(f"Payload JSON    : {nuevo_post}")

    try:
        respuesta = requests.post(url, json=nuevo_post, timeout=10)
        respuesta.raise_for_status()

        print(f"Código de estado: {respuesta.status_code} (201 = Created)")
        datos_creados = respuesta.json()
        print("Respuesta del servidor:")
        print(f"  ID Asignado   : {datos_creados.get('id')}")
        print(f"  Título recibido: {datos_creados.get('title')}")
        print(f"  Usuario       : {datos_creados.get('userId')}")

    except requests.exceptions.RequestException as err:
        print(f"[ERROR] Falló la creación del recurso: {err}")


def demo_manejo_errores_404():
    encabezado("3. Simulación y Manejo Controlado de Error 404")
    url_inexistente = f"{BASE_URL}/ruta-que-no-existe-xyz"
    print(f"Consultando ruta inexistente: {url_inexistente}")

    try:
        resp = requests.get(url_inexistente, timeout=5)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"[COMPORTAMIENTO ESPERADO] Se capturó correctamente el error HTTP: {http_err.response.status_code} Not Found")


def main():
    print("============================================================")
    print("   DEMOSTRACIÓN DE LA LIBRERÍA: requests                   ")
    print("============================================================")
    demo_get_con_parametros()
    demo_post_creacion_recurso()
    demo_manejo_errores_404()
    print("\n[OK] Script de 'requests' ejecutado correctamente.\n")


if __name__ == "__main__":
    main()

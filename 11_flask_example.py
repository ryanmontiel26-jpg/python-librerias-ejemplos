"""
11_flask_example.py
Demostración práctica del microframework web 'flask'.
Instalación: pip install flask

Cubre:
- Creación y configuración de una aplicación Flask
- Rutas GET y POST con serialización JSON (jsonify)
- Captura de parámetros dinámicos en la URL (<nombre>, <int:id>)
- Lectura y validación de payloads JSON en solicitudes POST
- Códigos de estado HTTP semánticos (200 OK, 201 Created, 400 Bad Request, 404 Not Found)
- Manejo centralizado de errores con @app.errorhandler
- Modo dual:
  1) Ejecución directa: pruebas automáticas con Flask Test Client (ideal para verificar sin bloquear la terminal).
  2) Servidor activo: ejecución con argumento '--server' para levantar http://127.0.0.1:5000.
"""

import sys
from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada en memoria
PRODUCTOS = [
    {"id": 1, "nombre": "Monitor 4K 27\"", "precio": 350.0, "stock": 15},
    {"id": 2, "nombre": "Teclado Mecánico RGB", "precio": 95.0, "stock": 30},
    {"id": 3, "nombre": "Ratón Ergonómico", "precio": 45.0, "stock": 50},
]


@app.route("/", methods=["GET"])
def inicio():
    """Ruta raíz de bienvenida con índice de endpoints disponibles."""
    return jsonify({
        "mensaje": "¡Bienvenido a la API REST de Ejemplo con Flask!",
        "version": "1.0.0",
        "endpoints": {
            "GET /": "Información de la API",
            "GET /api/saludo/<nombre>": "Saludo personalizado",
            "GET /api/productos": "Listar todos los productos",
            "GET /api/productos/<id>": "Consultar un producto por ID",
            "POST /api/productos": "Crear un nuevo producto (requiere JSON)",
        },
    })


@app.route("/api/saludo/<string:nombre>", methods=["GET"])
def saludar(nombre: str):
    """Endpoint con parámetro dinámico de ruta."""
    return jsonify({
        "saludo": f"¡Hola, {nombre}! Bienvenido a nuestro servicio API.",
        "longitud_nombre": len(nombre),
    }), 200


@app.route("/api/productos", methods=["GET"])
def listar_productos():
    """Retorna el catálogo completo de productos."""
    return jsonify({"total": len(PRODUCTOS), "productos": PRODUCTOS}), 200


@app.route("/api/productos/<int:producto_id>", methods=["GET"])
def obtener_producto(producto_id: int):
    """Obtiene un producto específico por su identificador numérico."""
    producto = next((p for p in PRODUCTOS if p["id"] == producto_id), None)
    if not producto:
        return jsonify({"error": f"Producto con ID {producto_id} no encontrado"}), 404
    return jsonify({"producto": producto}), 200


@app.route("/api/productos", methods=["POST"])
def crear_producto():
    """Crea un nuevo producto validando los datos recibidos en el cuerpo JSON."""
    datos = request.get_json(silent=True)
    if not datos:
        return jsonify({"error": "Cuerpo de solicitud inválido. Debe enviar un objeto JSON."}), 400

    nombre = datos.get("nombre")
    precio = datos.get("precio")
    stock = datos.get("stock", 0)

    # Validaciones básicas
    if not nombre or not isinstance(nombre, str):
        return jsonify({"error": "El campo 'nombre' es obligatorio y debe ser texto."}), 400

    if precio is None or not isinstance(precio, (int, float)) or precio <= 0:
        return jsonify({"error": "El campo 'precio' es obligatorio y debe ser un número positivo."}), 400

    nuevo_id = max((p["id"] for p in PRODUCTOS), default=0) + 1
    nuevo_producto = {
        "id": nuevo_id,
        "nombre": nombre.strip(),
        "precio": float(precio),
        "stock": int(stock),
    }

    PRODUCTOS.append(nuevo_producto)
    return jsonify({"mensaje": "Producto creado con éxito", "producto": nuevo_producto}), 201


@app.errorhandler(404)
def recurso_no_encontrado(error):
    return jsonify({"error": "Ruta no encontrada (404 Not Found)"}), 404


def ejecutar_pruebas_cliente():
    """Ejecuta una serie de llamadas usando el cliente de pruebas integrado de Flask."""
    print("\n" + "=" * 60)
    print("   DEMOSTRACIÓN INTERNA DE ENDPOINTS (Flask Test Client)   ")
    print("=" * 60)

    with app.test_client() as cliente:
        # 1. Probar ruta raíz
        print("\n1. GET /")
        r = cliente.get("/")
        print(f"   Status: {r.status_code}")
        print(f"   Respuesta: {r.get_json()}")

        # 2. Probar ruta con parámetro
        print("\n2. GET /api/saludo/Antigravity")
        r = cliente.get("/api/saludo/Antigravity")
        print(f"   Status: {r.status_code}")
        print(f"   Respuesta: {r.get_json()}")

        # 3. Listar productos
        print("\n3. GET /api/productos")
        r = cliente.get("/api/productos")
        print(f"   Status: {r.status_code}")
        print(f"   Total productos disponibles: {r.get_json()['total']}")

        # 4. Crear un producto vía POST
        print("\n4. POST /api/productos (Crear Auriculares Bluetooth)")
        nuevo = {"nombre": "Auriculares Inalámbricos Pro", "precio": 129.99, "stock": 25}
        r = cliente.post("/api/productos", json=nuevo)
        print(f"   Status: {r.status_code}")
        print(f"   Respuesta: {r.get_json()}")

        # 5. Consultar el producto recién creado
        print("\n5. GET /api/productos/4")
        r = cliente.get("/api/productos/4")
        print(f"   Status: {r.status_code}")
        print(f"   Respuesta: {r.get_json()}")

        # 6. Probar error 404 controlado
        print("\n6. GET /api/productos/999 (ID inexistente)")
        r = cliente.get("/api/productos/999")
        print(f"   Status: {r.status_code}")
        print(f"   Respuesta: {r.get_json()}")


def main():
    print("============================================================")
    print("   DEMOSTRACIÓN DE LA LIBRERÍA: flask                      ")
    print("============================================================")

    if "--server" in sys.argv:
        print("\nIniciando servidor web en http://127.0.0.1:5000 ...")
        print("Presiona Ctrl + C en la terminal para detener el servidor.\n")
        app.run(host="127.0.0.1", port=5000, debug=True)
    else:
        ejecutar_pruebas_cliente()
        print("\n" + "-" * 60)
        print("[TIP] Para ejecutar como servidor web interactivo real, escribe:")
        print("      python 11_flask_example.py --server")
        print("      Luego abre en tu navegador: http://127.0.0.1:5000")
        print("-" * 60)
        print("\n[OK] Script de 'flask' ejecutado correctamente.\n")


if __name__ == "__main__":
    main()

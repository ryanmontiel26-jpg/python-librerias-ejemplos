"""
09_matplotlib_example.py
Demostración práctica de la librería de visualización 'matplotlib'.
Instalación: pip install matplotlib

Cubre:
- Creación de figuras con múltiples subgráficos (Subplots 2x2) usando el enfoque orientado a objetos
- Gráfico de líneas temporales con marcadores y área sombreada
- Gráfico de barras horizontales o verticales con etiquetas numéricas
- Histograma con distribución de frecuencias
- Gráfico de dispersión (Scatter plot) con mapeo de colores y tamaños
- Personalización visual: rejillas, leyendas, paletas, títulos y márgenes
- Exportación automática a imagen PNG de alta resolución (300 DPI)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


def generar_graficos(nombre_archivo: str = "grafico_matplotlib.png"):
    print("Generando visualizaciones analíticas con Matplotlib...")

    # Semilla para datos de ejemplo reproducibles
    np.random.seed(42)

    # Configuración de lienzo: figura con 2 filas y 2 columnas
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
    fig.suptitle("Dashboard Analítico de Negocio - Métricas Trimestrales", fontsize=18, fontweight="bold", y=0.98)

    # -------------------------------------------------------------
    # 1. Gráfico de Líneas: Ingresos vs Costos a lo largo del año
    # -------------------------------------------------------------
    ax_lineas = axes[0, 0]
    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    ingresos = [12.5, 14.0, 15.2, 13.8, 16.5, 18.2, 19.0, 17.5, 21.0, 23.4, 25.0, 28.5]
    costos = [9.0, 9.8, 10.5, 10.2, 11.0, 12.1, 12.0, 11.5, 13.0, 14.2, 15.0, 16.5]

    ax_lineas.plot(meses, ingresos, label="Ingresos ($k)", color="#2E7D32", marker="o", linewidth=2.5)
    ax_lineas.plot(meses, costos, label="Costos ($k)", color="#C62828", marker="s", linestyle="--", linewidth=2.0)
    ax_lineas.fill_between(meses, ingresos, costos, color="#81C784", alpha=0.25, label="Margen Bruto")

    ax_lineas.set_title("Evolución Mensual: Ingresos vs Costos", fontsize=12, fontweight="bold")
    ax_lineas.set_xlabel("Mes")
    ax_lineas.set_ylabel("Miles de USD ($k)")
    ax_lineas.legend(loc="upper left")
    ax_lineas.grid(True, linestyle=":", alpha=0.6)

    # -------------------------------------------------------------
    # 2. Gráfico de Barras: Ventas por Línea de Producto
    # -------------------------------------------------------------
    ax_barras = axes[0, 1]
    categorias = ["Cloud / SaaS", "Servicios TI", "Hardware", "Consultoría", "Ciberseguridad"]
    ventas = [480, 310, 250, 190, 390]
    colores_barras = ["#1976D2", "#0288D1", "#0097A7", "#00796B", "#388E3C"]

    barras = ax_barras.bar(categorias, ventas, color=colores_barras, edgecolor="#37474F", width=0.6)
    ax_barras.set_title("Ventas por Línea de Producto (Q3)", fontsize=12, fontweight="bold")
    ax_barras.set_ylabel("Unidades Facturadas")
    ax_barras.tick_params(axis="x", rotation=15)
    ax_barras.grid(axis="y", linestyle=":", alpha=0.6)

    # Añadir valores sobre las barras
    for barra in barras:
        altura = barra.get_height()
        ax_barras.annotate(
            f"{altura}",
            xy=(barra.get_x() + barra.get_width() / 2, altura),
            xytext=(0, 3),  # 3 puntos de desfase vertical
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9,
            fontweight="bold",
        )

    # -------------------------------------------------------------
    # 3. Histograma: Distribución de Tiempos de Respuesta (ms)
    # -------------------------------------------------------------
    ax_hist = axes[1, 0]
    tiempos_respuesta = np.random.normal(loc=120, scale=25, size=800)  # media 120ms, desv 25ms

    n, bins, parches = ax_hist.hist(
        tiempos_respuesta, bins=25, color="#7B1FA2", edgecolor="white", alpha=0.8, density=True
    )
    ax_hist.set_title("Distribución de Tiempos de Respuesta de API", fontsize=12, fontweight="bold")
    ax_hist.set_xlabel("Latencia (milisegundos)")
    ax_hist.set_ylabel("Densidad de Frecuencia")
    ax_hist.axvline(120, color="#FFB300", linestyle="--", linewidth=2, label="Media = 120 ms")
    ax_hist.legend()
    ax_hist.grid(True, linestyle=":", alpha=0.6)

    # -------------------------------------------------------------
    # 4. Scatter Plot: Inversión en Publicidad vs Retorno (ROI)
    # -------------------------------------------------------------
    ax_scatter = axes[1, 1]
    inversion = np.random.uniform(5, 50, 45)
    retorno = inversion * 2.8 + np.random.normal(0, 10, 45)
    clientes_nuevos = np.random.randint(20, 200, 45)

    scatter = ax_scatter.scatter(
        inversion, retorno, c=clientes_nuevos, s=clientes_nuevos * 2, cmap="viridis", alpha=0.75, edgecolors="black"
    )
    cbar = fig.colorbar(scatter, ax=ax_scatter)
    cbar.set_label("Nuevos Clientes Captados")

    ax_scatter.set_title("Inversión en Marketing vs Retorno Estimado", fontsize=12, fontweight="bold")
    ax_scatter.set_xlabel("Inversión Publicitaria ($k)")
    ax_scatter.set_ylabel("Retorno Generado ($k)")
    ax_scatter.grid(True, linestyle=":", alpha=0.6)

    # Ajuste automático de espaciado y márgenes
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    # Guardar en archivo PNG con alta calidad
    plt.savefig(nombre_archivo, dpi=300)
    plt.close(fig)

    print(f"[OK] Visualizaciones guardadas con éxito en: {Path(nombre_archivo).resolve()}")


def main():
    print("============================================================")
    print("   DEMOSTRACIÓN DE LA LIBRERÍA: matplotlib                 ")
    print("============================================================")
    archivo_salida = "grafico_matplotlib.png"
    generar_graficos(archivo_salida)
    print(f"Abra el archivo '{archivo_salida}' para visualizar la imagen generada.\n")


if __name__ == "__main__":
    main()

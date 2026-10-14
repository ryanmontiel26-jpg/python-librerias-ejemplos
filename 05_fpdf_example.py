"""
05_fpdf_example.py
Demostración práctica de la librería externa 'fpdf2'.
Instalación: pip install fpdf2

Cubre:
- Creación de una clase PDF personalizada heredando de FPDF
- Encabezado (Header) y pie de página (Footer) automáticos con numeración
- Estilización de fuentes (Helvetica/Arial), tamaños y colores
- Creación de tablas de datos con formato profesional
- Cajas de texto destacadas (Callouts)
- Guardado y exportación a archivo PDF
"""

from fpdf import FPDF
from datetime import datetime
from pathlib import Path


class ReporteCorporativo(FPDF):
    def header(self):
        # Franja superior de acento
        self.set_fill_color(33, 150, 243)  # Azul primario
        self.rect(0, 0, 210, 6, "F")

        # Título del encabezado
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(50, 50, 50)
        self.cell(0, 10, "TECNOLOGÍAS DEL FUTURO S.A. - REPORTE DE VENTAS", border=0, align="L")
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, datetime.now().strftime("%d/%m/%Y"), border=0, align="R")
        self.ln(12)
        # Línea divisoria
        self.set_draw_color(220, 220, 220)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def footer(self):
        self.set_y(-18)
        self.set_draw_color(220, 220, 220)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, "Documento confidencial generado automáticamente con Python y FPDF2.", align="L")
        self.cell(0, 10, f"Página {self.page_no()}/{{nb}}", align="R")


def generar_pdf_fpdf(nombre_archivo: str = "reporte_fpdf.pdf"):
    pdf = ReporteCorporativo(orientation="P", unit="mm", format="A4")
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # Título principal
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(20, 30, 48)
    pdf.cell(0, 12, "Resumen Ejecutivo de Rendimiento Trimestral", ln=True, align="L")

    # Párrafo descriptivo
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(80, 80, 80)
    descripcion = (
        "El presente informe consolida los resultados obtenidos durante el último ciclo operativo. "
        "Se observa un crecimiento sostenido en los canales digitales y una optimización "
        "en los tiempos de entrega promedio."
    )
    pdf.multi_cell(0, 6, descripcion)
    pdf.ln(6)

    # Cuadro de Métricas Destacadas (Callout)
    pdf.set_fill_color(240, 247, 255)
    pdf.set_draw_color(144, 202, 249)
    pdf.rect(10, pdf.get_y(), 190, 24, "FD")

    pdf.set_xy(15, pdf.get_y() + 4)
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(13, 71, 161)
    pdf.cell(60, 6, "Ingresos Totales: $84,520 USD", align="L")
    pdf.cell(60, 6, "Crecimiento: +18.4%", align="C")
    pdf.cell(60, 6, "Nivel de Satisfacción: 96%", align="R")
    pdf.ln(18)

    # Sección de Tabla de Datos
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(20, 30, 48)
    pdf.cell(0, 10, "Detalle de Categorías de Producto", ln=True)

    # Cabeceras de tabla
    columnas = [("Categoría", 60), ("Unidades", 30), ("Precio Medio", 45), ("Subtotal", 55)]
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_fill_color(41, 128, 185)  # Azul encabezado
    pdf.set_text_color(255, 255, 255)

    for nombre_col, ancho in columnas:
        pdf.cell(ancho, 9, nombre_col, border=1, align="C", fill=True)
    pdf.ln()

    # Filas de la tabla
    filas = [
        ("Servidores y Nube", "145", "$ 280.00", "$ 40,600.00"),
        ("Suscripciones SaaS", "620", "$  35.00", "$ 21,700.00"),
        ("Consultoría TI", "85", "$ 150.00", "$ 12,750.00"),
        ("Hardware & Accesorios", "210", "$  45.00", "$  9,470.00"),
    ]

    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(40, 40, 40)

    for i, fila in enumerate(filas):
        # Filas alternas con sombreado sutil
        if i % 2 == 0:
            pdf.set_fill_color(250, 250, 250)
        else:
            pdf.set_fill_color(238, 242, 246)

        pdf.cell(columnas[0][1], 8, f"  {fila[0]}", border=1, align="L", fill=True)
        pdf.cell(columnas[1][1], 8, fila[1], border=1, align="C", fill=True)
        pdf.cell(columnas[2][1], 8, fila[2], border=1, align="R", fill=True)
        pdf.cell(columnas[3][1], 8, f"{fila[3]}  ", border=1, align="R", fill=True)
        pdf.ln()

    # Fila de Total
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_fill_color(220, 230, 242)
    pdf.cell(columnas[0][1] + columnas[1][1] + columnas[2][1], 9, "Total Consolidado  ", border=1, align="R", fill=True)
    pdf.cell(columnas[3][1], 9, "$ 84,520.00  ", border=1, align="R", fill=True)
    pdf.ln(12)

    # Conclusión
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 8, "* Los importes reflejan cifras netas antes de retenciones fiscales aplicables.", align="L")

    # Guardado del archivo
    pdf.output(nombre_archivo)
    print(f"[OK] Documento PDF generado exitosamente: {Path(nombre_archivo).resolve()}")


def main():
    print("============================================================")
    print("   DEMOSTRACIÓN DE LA LIBRERÍA: fpdf2                      ")
    print("============================================================")
    salida = "reporte_fpdf.pdf"
    generar_pdf_fpdf(salida)
    print(f"Abra el archivo '{salida}' para visualizar el resultado profesional.\n")


if __name__ == "__main__":
    main()

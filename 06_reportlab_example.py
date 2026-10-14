"""
06_reportlab_example.py
Demostración práctica de la librería externa 'reportlab'.
Instalación: pip install reportlab

Cubre:
- Arquitectura de documentos con Platypus (SimpleDocTemplate)
- Hojas de estilos tipográficos con getSampleStyleSheet y ParagraphStyle
- Flujo de elementos: Títulos, párrafos, separadores (Spacer)
- Tablas complejas estilizadas con Table y TableStyle
- Paleta de colores personalizada con colors.HexColor
- Creación de pie de página mediante callbacks de canvas
"""

from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


class NumberedCanvas(canvas.Canvas):
    """Canvas de dos pasadas para calcular y pintar el número total de páginas exacto."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_paginas = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_paginas)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#7F8C8D"))
        # Línea de pie de página
        self.setStrokeColor(colors.HexColor("#BDC3C7"))
        self.setLineWidth(0.5)
        self.line(54, 40, letter[0] - 54, 40)

        # Texto del pie
        texto_pie = f"Generado por ReportLab | Página {self._pageNumber} de {page_count}"
        self.drawRightString(letter[0] - 54, 25, texto_pie)
        self.drawString(54, 25, "Confidencial - Uso Interno Exclusivo")
        self.restoreState()


def generar_pdf_reportlab(nombre_archivo: str = "reporte_reportlab.pdf"):
    # Configuración del documento (márgenes de 0.75 pulgadas)
    doc = SimpleDocTemplate(
        nombre_archivo,
        pagesize=letter,
        rightMargin=54,
        leftMargin=54,
        topMargin=54,
        bottomMargin=54,
    )

    story = []
    estilos = getSampleStyleSheet()

    # Definición de estilos personalizados
    estilo_titulo = ParagraphStyle(
        "TituloPrincipal",
        parent=estilos["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=22,
        leading=26,
        textColor=colors.HexColor("#1A365D"),
        spaceAfter=6,
    )

    estilo_subtitulo = ParagraphStyle(
        "Subtitulo",
        parent=estilos["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#4A5568"),
        spaceAfter=14,
    )

    estilo_cuerpo = ParagraphStyle(
        "CuerpoTexto",
        parent=estilos["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=15,
        textColor=colors.HexColor("#2D3748"),
    )

    estilo_th = ParagraphStyle(
        "CabeceraTabla",
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=12,
        textColor=colors.white,
        alignment=1,  # Centrado
    )

    estilo_td = ParagraphStyle(
        "CeldaTabla",
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#2D3748"),
    )

    # 1. Título y encabezado
    story.append(Paragraph("Auditoría de Sistemas e Infraestructura Cloud", estilo_titulo))
    story.append(Paragraph("Informe Técnico de Conformidad y Seguridad - Q3", estilo_subtitulo))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#3182CE"), spaceBefore=0, spaceAfter=14))

    # 2. Resumen
    texto_resumen = (
        "Este informe detalla la evaluación técnica de los clústeres de servidores en producción. "
        "Las métricas confirman una disponibilidad promedio de servicio del <b>99.98%</b> y un cumplimiento "
        "estricto de las políticas de cifrado en reposo y en tránsito."
    )
    story.append(Paragraph(texto_resumen, estilo_cuerpo))
    story.append(Spacer(1, 14))

    # 3. Tabla con Platypus
    encabezados_tabla = [
        Paragraph("<b>Servicio / Recurso</b>", estilo_th),
        Paragraph("<b>Región</b>", estilo_th),
        Paragraph("<b>Estado</b>", estilo_th),
        Paragraph("<b>Latencia Media</b>", estilo_th),
        Paragraph("<b>SLA Cumplido</b>", estilo_th),
    ]

    filas_datos = [
        [Paragraph("API Gateway Principal", estilo_td), "us-east-1", "Activo", "24 ms", "100%"],
        [Paragraph("Clúster Kubernetes (EKS)", estilo_td), "us-east-1", "Activo", "42 ms", "99.99%"],
        [Paragraph("Base de Datos PostgreSQL", estilo_td), "us-east-1", "Activo", "12 ms", "99.98%"],
        [Paragraph("Caché Distribuida Redis", estilo_td), "us-east-1", "Activo", "3 ms", "100%"],
        [Paragraph("Bucket de Backups S3", estilo_td), "eu-central-1", "Activo", "85 ms", "100%"],
    ]

    data_completa = [encabezados_tabla] + filas_datos

    tabla = Table(data_completa, colWidths=[150, 75, 75, 95, 95])
    tabla.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2B6CB0")),
                ("ALIGN", (1, 1), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F7FAFC"), colors.HexColor("#EDF2F7")]),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )

    story.append(tabla)
    story.append(Spacer(1, 18))

    # 4. Sección de recomendaciones
    story.append(Paragraph("<b>Recomendaciones Técnicas Prioritarias:</b>", estilo_subtitulo))
    recomendaciones = (
        "1. Habilitar réplicas multirregión automáticas para el clúster de base de datos.<br/>"
        "2. Ajustar las políticas de ciclo de vida de los logs archivados superiores a 90 días.<br/>"
        "3. Implementar rate-limiting adicional sobre los endpoints públicos de la API."
    )
    story.append(Paragraph(recomendaciones, estilo_cuerpo))

    # Construcción final del documento
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[OK] Documento ReportLab generado exitosamente: {Path(nombre_archivo).resolve()}")


def main():
    print("============================================================")
    print("   DEMOSTRACIÓN DE LA LIBRERÍA: reportlab                  ")
    print("============================================================")
    salida = "reporte_reportlab.pdf"
    generar_pdf_reportlab(salida)
    print(f"Abra el archivo '{salida}' para visualizar el documento generado.\n")


if __name__ == "__main__":
    main()

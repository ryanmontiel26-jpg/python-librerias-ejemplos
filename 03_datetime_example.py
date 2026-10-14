"""
03_datetime_example.py
Demostración práctica de la librería estándar 'datetime' de Python.
No requiere instalación externa.

Cubre:
- Obtención de fecha y hora actual (local y UTC)
- Creación y manipulación de date, time y datetime
- Formateo de fechas a texto (strftime)
- Parseo de texto a objetos datetime (strptime)
- Aritmética con fechas (timedelta): plazos, vencimientos y cuenta regresiva
- Manejo de zonas horarias simples con timezone
- Cálculo de diferencias temporales
"""

from datetime import datetime, date, time, timedelta, timezone


def encabezado(titulo: str):
    print("\n" + "=" * 60)
    print(f" {titulo.upper()} ")
    print("=" * 60)


def demo_fechas_actuales():
    encabezado("1. Fechas y Horas Actuales")
    ahora_local = datetime.now()
    ahora_utc = datetime.now(timezone.utc)
    solo_fecha = date.today()

    print(f"Fecha y hora local      : {ahora_local}")
    print(f"Fecha y hora UTC        : {ahora_utc}")
    print(f"Solo fecha actual       : {solo_fecha}")
    print(f"Partes individuales     : Año={ahora_local.year}, Mes={ahora_local.month}, Día={ahora_local.day}")


def demo_formateo_strftime():
    encabezado("2. Formateo de Fechas a Texto (strftime)")
    momento = datetime(2026, 10, 13, 15, 30, 45)
    print(f"Objeto original         : {momento}")

    # Formatos comunes
    print(f"Formato ISO 8601        : {momento.strftime('%Y-%m-%dT%H:%M:%S')}")
    print(f"Formato Latino/Europeo  : {momento.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Formato 12 horas con AM : {momento.strftime('%I:%M:%S %p')}")
    print(f"Nombre de día y mes     : {momento.strftime('%A, %d de %B de %Y')}")


def demo_parseo_strptime():
    encabezado("3. Parseo de Cadenas a Datetime (strptime)")
    cadena_fecha = "2026-12-31 23:59:00"
    patron = "%Y-%m-%d %H:%M:%S"

    fecha_parseada = datetime.strptime(cadena_fecha, patron)
    print(f"Texto de entrada        : '{cadena_fecha}'")
    print(f"Objeto datetime obtenido: {fecha_parseada}")
    print(f"Día de la semana (0=Lun): {fecha_parseada.weekday()} (Jueves)")


def demo_aritmetica_timedelta():
    encabezado("4. Aritmética de Fechas con timedelta")
    hoy = datetime.now()

    # Vencimiento de suscripción o factura en 30 días
    en_30_dias = hoy + timedelta(days=30)
    # Hace una semana y 3 horas
    hace_semana = hoy - timedelta(weeks=1, hours=3)

    print(f"Fecha de hoy            : {hoy.strftime('%Y-%m-%d')}")
    print(f"Vencimiento (+30 días)  : {en_30_dias.strftime('%Y-%m-%d')}")
    print(f"Hace 1 semana y 3 horas : {hace_semana.strftime('%Y-%m-%d %H:%M')}")

    # Cuenta regresiva para Año Nuevo
    ano_nuevo = datetime(hoy.year + 1, 1, 1)
    diferencia = ano_nuevo - hoy
    print(f"Faltan para Año Nuevo   : {diferencia.days} días y {diferencia.seconds // 3600} horas")


def demo_zonas_horarias():
    encabezado("5. Manejo de Zonas Horarias (timezone)")
    # Zona horaria UTC
    hora_utc = datetime.now(timezone.utc)

    # Definición de desfases horarios manuales (ej: UTC-5 Colombia/Perú, UTC-6 México, UTC+1 España peninsular)
    tz_mexico = timezone(timedelta(hours=-6), name="CST")
    tz_espana = timezone(timedelta(hours=1), name="CET")

    hora_mexico = hora_utc.astimezone(tz_mexico)
    hora_espana = hora_utc.astimezone(tz_espana)

    print(f"Hora actual en UTC      : {hora_utc.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"Hora en México (UTC-6)  : {hora_mexico.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"Hora en España (UTC+1)  : {hora_espana.strftime('%Y-%m-%d %H:%M:%S %Z')}")


def main():
    print("============================================================")
    print("   DEMOSTRACIÓN DE LA LIBRERÍA ESTÁNDAR: datetime          ")
    print("============================================================")
    demo_fechas_actuales()
    demo_formateo_strftime()
    demo_parseo_strptime()
    demo_aritmetica_timedelta()
    demo_zonas_horarias()
    print("\n[OK] Script de 'datetime' ejecutado correctamente.\n")


if __name__ == "__main__":
    main()

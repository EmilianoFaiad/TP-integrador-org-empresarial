import pandas as pd
import os

ARCHIVO_EXCEL = "C:/Users/Emiliano/Documents/UNT/org empresarial/base_datos.xlsx"

# ESTADOS DEL PROCESO

ESTADO_INICIO = 0
ESTADO_PEDIR_DNI = 1
ESTADO_VALIDAR_EMPLEADO = 2
ESTADO_PEDIR_DIAS = 3
ESTADO_EVALUAR_SOLICITUD = 4
ESTADO_FINAL = 5


# FUNCIONES AUXILIARES

def mostrar_fase(texto):
    print("\n" + "=" * 50)
    print(f"FASE ACTUAL: {texto}")
    print("=" * 50)


def cargar_datos():
    empleados = pd.read_excel(
        ARCHIVO_EXCEL,
        sheet_name="Empleados"
    )

    solicitudes = pd.read_excel(
        ARCHIVO_EXCEL,
        sheet_name="Solicitudes"
    )

    return empleados, solicitudes


def guardar_solicitud(solicitudes):
    with pd.ExcelWriter(
        ARCHIVO_EXCEL,
        engine="openpyxl",
        mode="a",
        if_sheet_exists="replace"
    ) as writer:
        solicitudes.to_excel(
            writer,
            sheet_name="Solicitudes",
            index=False
        )


def buscar_empleado(dni, empleados):
    resultado = empleados[empleados["DNI"] == dni]

    if resultado.empty:
        return None

    return resultado.iloc[0]


# CHATBOT

def chatbot_vacaciones():

    estado = ESTADO_INICIO

    empleados, solicitudes = cargar_datos()

    dni = None
    nombre = None
    dias_disponibles = None

    while True:

        # INICIO

        if estado == ESTADO_INICIO:

            mostrar_fase("INICIO DEL PROCESO")

            print("Bienvenido al Sistema de Gestión de Vacaciones")
            print("1 - Solicitar vacaciones")
            print("0 - Salir")

            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                estado = ESTADO_PEDIR_DNI

            elif opcion == "0":
                print("\nGracias por utilizar el sistema.")
                break

            else:
                print("\nERROR: opción inválida.")

        # PEDIR DNI

        elif estado == ESTADO_PEDIR_DNI:

            mostrar_fase("IDENTIFICACIÓN DEL EMPLEADO")

            dni_ingresado = input(
                "Ingrese su DNI (solo números): "
            )

            if not dni_ingresado.isdigit():
                print("\nERROR:")
                print("Debe ingresar únicamente números.")
                continue

            dni = int(dni_ingresado)

            estado = ESTADO_VALIDAR_EMPLEADO

        # VALIDAR EMPLEADO

        elif estado == ESTADO_VALIDAR_EMPLEADO:

            mostrar_fase("VALIDACIÓN DE EMPLEADO")

            empleado = buscar_empleado(
                dni,
                empleados
            )

            if empleado is None:

                print("\nDNI no encontrado.")
                print("Derivación: contactar RRHH.")

                estado = ESTADO_INICIO
                continue

            nombre = empleado["Nombre"]
            dias_disponibles = int(
                empleado["DiasDisponibles"]
            )

            print(f"\nEmpleado: {nombre}")
            print(
                f"Días disponibles: {dias_disponibles}"
            )

            estado = ESTADO_PEDIR_DIAS

        # PEDIR DÍAS

        elif estado == ESTADO_PEDIR_DIAS:

            mostrar_fase(
                "INGRESO DE CANTIDAD DE DÍAS"
            )

            dias = input(
                "¿Cuántos días desea solicitar?: "
            )

            if not dias.isdigit():
                print(
                    "\nERROR: debe ingresar un número."
                )
                continue

            dias = int(dias)

            if dias <= 0:
                print(
                    "\nERROR: debe solicitar al menos 1 día."
                )
                continue

            dias_solicitados = dias

            estado = ESTADO_EVALUAR_SOLICITUD

        # GATEWAY

        elif estado == ESTADO_EVALUAR_SOLICITUD:

            mostrar_fase(
                "EVALUACIÓN DE LA SOLICITUD"
            )

            if dias_solicitados <= dias_disponibles:

                print("\nSOLICITUD APROBADA")

                nuevo_id = (
                    1
                    if solicitudes.empty
                    else solicitudes["ID"].max() + 1
                )

                nueva_solicitud = pd.DataFrame(
                    [{
                        "ID": nuevo_id,
                        "DNI": dni,
                        "Nombre": nombre,
                        "DiasSolicitados":
                        dias_solicitados,
                        "Estado": "APROBADA"
                    }]
                )

                solicitudes = pd.concat(
                    [solicitudes,
                     nueva_solicitud],
                    ignore_index=True
                )

                guardar_solicitud(
                    solicitudes
                )

                print(
                    f"\n{nombre}, su solicitud "
                    "ha sido registrada."
                )

            else:

                print(
                    "\nSOLICITUD RECHAZADA"
                )

                print(
                    f"Dispone solamente de "
                    f"{dias_disponibles} días."
                )

                nuevo_id = (
                    1
                    if solicitudes.empty
                    else solicitudes["ID"].max() + 1
                )

                nueva_solicitud = pd.DataFrame(
                    [{
                        "ID": nuevo_id,
                        "DNI": dni,
                        "Nombre": nombre,
                        "DiasSolicitados":
                        dias_solicitados,
                        "Estado": "RECHAZADA"
                    }]
                )

                solicitudes = pd.concat(
                    [solicitudes,
                     nueva_solicitud],
                    ignore_index=True
                )

                guardar_solicitud(
                    solicitudes
                )

            estado = ESTADO_FINAL

        # FIN

        elif estado == ESTADO_FINAL:

            mostrar_fase(
                "FIN DEL PROCESO"
            )

            print(
                "El proceso ha finalizado."
            )

            volver = input(
                "\n¿Desea realizar otra solicitud? (S/N): "
            ).upper()

            if volver == "S":
                estado = ESTADO_INICIO

            elif volver == "N":
                print(
                    "\nGracias por utilizar el sistema."
                )
                break

            else:
                print(
                    "\nEntrada inválida."
                )


# PROGRAMA PRINCIPAL

chatbot_vacaciones()
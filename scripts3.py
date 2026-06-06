# ============================================================
# ACTIVIDAD 3 - INTERFAZ DE CONSOLA JUSTIA
# Proyecto: JustIA
# ============================================================

from scripts2  import clasificar_texto

def mostrar_menu():
    print("\n========== SISTEMA JUSTIA ==========")
    print("1. Ingresar una pregunta legal")
    print("2. Seleccionar documento de entrada")
    print("3. Ejecutar clasificación simulada")
    print("4. Salir")
    print("====================================")

def responder_pregunta():
    pregunta = input("\nIngrese su pregunta legal: ")

    categoria, puntajes = clasificar_texto(pregunta)

    print("\nRespuesta preliminar del sistema JustIA:")
    print("----------------------------------------")

    if categoria == "sin clasificar":
        print("No fue posible identificar una categoría jurídica clara.")
        print("Se recomienda revisión por parte de un estudiante o asesor jurídico.")
    else:
        print(f"La consulta parece estar relacionada con el área de: {categoria}.")
        print("Esta respuesta es solo una orientación preliminar.")
        print("Debe ser revisada por un estudiante o asesor jurídico autorizado.")

def seleccionar_documento():
    ruta = input("\nIngrese la ruta o nombre del documento PDF/TXT: ")

    print("\nDocumento registrado correctamente.")
    print(f"Archivo seleccionado: {ruta}")

    print("\nNota:")
    print("En esta versión prototipo no se extrae el texto real del documento.")
    print("La funcionalidad queda simulada para una futura integración con OCR o lectura de PDF.")

def ejecutar_clasificacion():
    texto = input("\nDescriba brevemente el caso jurídico: ")

    categoria, puntajes = clasificar_texto(texto)

    print("\nResultado de clasificación simulada")
    print("-----------------------------------")
    print(f"Categoría sugerida: {categoria}")

    print("\nDetalle de puntajes:")
    for nombre_categoria, puntaje in puntajes.items():
        print(f"- {nombre_categoria}: {puntaje}")

    print("\nAdvertencia:")
    print("La clasificación no constituye asesoría jurídica definitiva.")
    print("Debe ser validada por el equipo del consultorio jurídico.")

def iniciar_sistema():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            responder_pregunta()

        elif opcion == "2":
            seleccionar_documento()

        elif opcion == "3":
            ejecutar_clasificacion()

        elif opcion == "4":
            print("\nGracias por usar JustIA.")
            print("Sistema finalizado.")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")

if __name__ == "__main__":
    iniciar_sistema()
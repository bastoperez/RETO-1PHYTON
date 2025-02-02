import os
registros = []
from datetime import datetime

registros = []

def ingresar_fecha():
    while True:
        fecha_str = input("Ingrese una fecha (DD/MM/AAAA): ")
        limpiar_terminal
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")  # Convertir la cadena en fecha
            if 1950 <= fecha.year <= 2025:
                return fecha
                
            else:
                print("El año debe estar entre 1950 y 2025. Intente nuevamente.")
        except ValueError:
            
            print("❌Formato inválido. Asegúrese de usar DD/MM/AAAA.")
            
def categoria():
    while True:
        print("Seleccione una categoría:")
        print("1. Física")
        print("2. Matemáticas")
        print("3. Estadística")
        opcion = input("Ingrese el número de la categoría: ")
        
        if opcion == "1":
            return "Física"
        elif opcion == "2":
            return "Matemáticas"
        elif opcion == "3":
            return "Estadística"
        else:
            print("❌Opción no válida, intente nuevamente.")

def ingresar_experimento():
    nombre = input("Ingrese el nombre: ")
    fecha = ingresar_fecha()  # Llamamos a la función para obtener la fecha validada
    experimento = categoria()
     # Se obtiene la categoría elegida
    registro = {"nombre": nombre, "fecha": fecha.strftime('%d/%m/%Y'), "experimento": experimento,}
    registros.append(registro)


def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_resultados():
    print("\nRegistros almacenados:")
    for r in registros:
        print(f"Nombre: {r['nombre']}, fecha: {r['fecha']}, Experimento: {r['experimento']}")

def realizar_analisis():
    print("Análisis de datos en proceso...")

def eliminar_experimento():
    nombre = input("Ingrese el nombre del experimento a eliminar: ")
    global registros
    registros = [r for r in registros if r['nombre'] != nombre]
    print("✅ Experimento eliminado con exito")

def modificar_experimento():
    nombre = input("Ingrese el nombre del experimento a modificar: ")
    for r in registros:
        if r['nombre'] == nombre:
            r['fecha'] = int(input("Ingrese la nueva fecha: "))
            r['experimento'] = input("Ingrese el nuevo experimento: ")
            print("✅Experimento modificado.")
            return
    print("Experimento no encontrado.")

def generar_informe():
    print("Generando informe...")

while True:
    print("\nMenú de Opciones:")
    print("1. Ingresar nuevo experimento")
    print("2. Mostrar resultados")
    print("3. Realizar análisis de datos")
    print("4. Eliminar experimentos")
    print("5. Modificar experimentos")
    print("6. Generar informe")# formato texto averiguar
    print("7. Salir")
    opcion = input("Seleccione una opción: ")
    limpiar_terminal()
    
    if opcion == "1":
        ingresar_experimento()
    elif opcion == "2":
        mostrar_resultados()
    elif opcion == "3":
        realizar_analisis()
    elif opcion == "4":
        eliminar_experimento()
    elif opcion == "5":
        modificar_experimento()
    elif opcion == "6":
        generar_informe()
    elif opcion == "7":
        print("👋🏻Saliendo del programa...")
        break

    else:
        print("✅Opción no válida, intente de nuevo.")
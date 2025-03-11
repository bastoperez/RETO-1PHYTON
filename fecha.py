from datetime import datetime

registros = []

def ingresar_fecha():
    while True:
        fecha_str = input("Ingrese una fecha (DD/MM/AAAA): ")
        try:
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")  # Convertir la cadena en fecha
            if 1950 <= fecha.year <= 2025:
                return fecha
            else:
                print("El año debe estar entre 1950 y 2025. Intente nuevamente.")
        except ValueError:
            print("Formato inválido. Asegúrese de usar DD/MM/AAAA.")

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
            print("Opción no válida, intente nuevamente.")

def ingresar_experimento():
    nombre = input("Ingrese el nombre: ")
    fecha = ingresar_fecha()  # Llamamos a la función para obtener la fecha validada
    experimento = categoria()
     # Se obtiene la categoría elegida
    registro = {"nombre": nombre, "fecha": fecha.strftime('%d/%m/%Y'), "experimento": experimento,}
    registros.append(registro)

def mostrar_resultados():
    print("\nRegistros almacenados:")
    for r in registros:
        print(f"Nombre: {r['nombre']}, Fecha: {r['fecha']}, Experimento: {r['experimento']}")

# Prueba la función
ingresar_experimento()
mostrar_resultados()

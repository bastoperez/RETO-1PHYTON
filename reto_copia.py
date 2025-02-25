import os
from datetime import datetime

# Lista para almacenar los experimentos registrados
registros = []
# Diccionario para almacenar los resultados del análisis de datos
resultados_analisis = {} 

# Función para ingresar y validar una fecha
def ingresar_fecha():
    while True:
        fecha_str = input("Ingrese una fecha (DD/MM/AAAA): ")
        limpiar_terminal()
        try:
            # Convertimos la cadena a un objeto datetime
            fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
            if 1950 <= fecha.year <= 2025:
                return fecha.strftime('%d/%m/%Y')  # Devolvemos la fecha formateada
            else:
                print("El año debe estar entre 1950 y 2025. Intente nuevamente.")
        except ValueError:
            print("❌ Formato inválido. Asegúrese de usar DD/MM/AAAA.")

# Función para seleccionar una categoría de experimento
def categoria():
    while True:
        print("Seleccione una categoría:")
        print("1. Física")
        print("2. Matemáticas")
        print("3. Estadística")
        opcion = input("Ingrese el número de la categoría: ")

        categorias = {"1": "Física", "2": "Matemáticas", "3": "Estadística"}
        if opcion in categorias:
            return categorias[opcion]
        else:
            print("❌ Opción no válida, intente nuevamente.")

# Función para ingresar un nuevo experimento
def ingresar_experimento():
    nombre = input("Ingrese el nombre del experimento: ")
    fecha = ingresar_fecha()
    tipo = categoria()
    # Se almacena el experimento en la lista
    registros.append({"nombre": nombre, "fecha": fecha, "tipo": tipo})
    print("✅ Experimento registrado con éxito.")

# Función para limpiar la terminal
def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar los experimentos registrados
def mostrar_resultados():
    if not registros:
        print("\n📌 No hay registros almacenados.")
        return
    print("\n📋 Registros almacenados:")
    for r in registros:
        print(f"\n Nombre: {r['nombre']}, Fecha: {r['fecha']}, Tipo: {r['tipo']}")
    
        if resultados_analisis:
                print("\n📊 RESULTADOS DEL ANÁLISIS DE DATOS\n")
                if "promedio" in resultados_analisis:
                    print(f"Promedio 📊: {resultados_analisis['promedio']:.2f}")
                if "maximo" in resultados_analisis:
                    print(f"Valor máximo 📈: {resultados_analisis['maximo']}")
                if "minimo" in resultados_analisis:
                    print(f"Valor mínimo 📉: {resultados_analisis['minimo']}")
                print("-" * 30)  # Separador entre registros
    

# Función para realizar análisis de datos
def realizar_analisis():
    global resultados_analisis  # Usamos la variable global

    while True:
        print("\n¿Qué análisis desea hacer al experimento?")
        print("1. Calcular promedio")
        print("2. Valor máximo")
        print("3. Valor mínimo")
        print("4. Realizar todos los análisis")  # Nueva opción para hacer todo
        opcion = input("Ingrese una opción: ")

        if opcion in ["1", "2", "3", "4"]:
            cantidad = int(input("Ingrese la cantidad de números: "))
            numeros = [float(input(f"Ingrese el número {i + 1}: ")) for i in range(cantidad)]

            if opcion in ["1", "4"]:  # Calcular promedio
                promedio = sum(numeros) / cantidad
                resultados_analisis["promedio"] = promedio
                print(f"📊 El promedio es: {promedio:.2f}")

            if opcion in ["2", "4"]:  # Calcular máximo
                maximo = max(numeros)
                resultados_analisis["maximo"] = maximo
                print(f"📈 El valor máximo es: {maximo}")

            if opcion in ["3", "4"]:  # Calcular mínimo
                minimo = min(numeros)
                resultados_analisis["minimo"] = minimo
                print(f"📉 El valor mínimo es: {minimo}")

            return  # Salir de la función después de completar el análisis
        else:
            print("❌ Opción no válida, intente nuevamente.")

# Función para eliminar un experimento
def eliminar_experimento():
    nombre = input("Ingrese el nombre del experimento a eliminar: ")
    global registros
    registros_filtrados = [r for r in registros if r['nombre'] != nombre]
    if len(registros_filtrados) < len(registros):
        registros = registros_filtrados
        print("✅ Experimento eliminado con éxito.")
    else:
        print("⚠️ Experimento no encontrado.")

# Función para modificar un experimento
def modificar_experimento():
    nombre = input("Ingrese el nombre del experimento a modificar: ")
    for r in registros:
        if r['nombre'] == nombre:
            print("Ingrese los nuevos datos (presione Enter para mantener los actuales):")
            nueva_fecha = input(f"Fecha actual ({r['fecha']}): ")
            nuevo_tipo = input(f"Tipo actual ({r['tipo']}): ")

            if nueva_fecha:
                try:
                    datetime.strptime(nueva_fecha, "%d/%m/%Y")
                    r['fecha'] = nueva_fecha
                except ValueError:
                    print("⚠️ Fecha inválida. No se realizaron cambios.")

            if nuevo_tipo:
                r['tipo'] = nuevo_tipo
            print("✅ Experimento modificado.")
            return
    print("⚠️ Experimento no encontrado.")

# Función para generar un informe en formato de texto
def generar_informe():
    if not registros:
        print("⚠️ No hay datos para generar un informe.")
        return

    nombre_archivo = "informe_experimentos.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("📋 INFORME DE EXPERIMENTOS\n\n")
        for r in registros:
            archivo.write(f"Nombre: {r['nombre']}\nFecha: {r['fecha']}\nTipo: {r['tipo']}\n{'-'*30}\n")

        # Agregar los resultados del análisis si existen
        if resultados_analisis:
            archivo.write("\n📊 RESULTADOS DEL ANÁLISIS DE DATOS\n")
            if "promedio" in resultados_analisis:
                archivo.write(f"Promedio: {resultados_analisis['promedio']:.2f}\n")
            if "maximo" in resultados_analisis:
                archivo.write(f"Valor máximo: {resultados_analisis['maximo']}\n")
            if "minimo" in resultados_analisis:
                archivo.write(f"Valor mínimo: {resultados_analisis['minimo']}\n")

    print(f"✅ Informe generado exitosamente en '{nombre_archivo}'.\n")

    # Mostrar el contenido del archivo en la terminal
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        print(archivo.read())

# Menú principal del programa
while True:
    print("\n📌 Menú de Opciones:")
    print("1. Ingresar nuevo experimento")
    print("2. Mostrar resultados")
    print("3. Realizar análisis de datos")
    print("4. Eliminar experimentos")
    print("5. Modificar experimentos")
    print("6. Generar informe")
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
        print("👋🏻 Saliendo del programa...")
        break
    else:
        print("❌ Opción no válida, intente de nuevo.")

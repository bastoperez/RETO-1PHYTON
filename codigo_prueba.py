import os
from datetime import datetime
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import scrolledtext, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Lista para almacenar los experimentos registrados
registros = []

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
    registros.append({"nombre": nombre, "fecha": fecha, "tipo": tipo, "analisis": {}})
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
        print(f"Nombre: {r['nombre']}, Fecha: {r['fecha']}, Tipo: {r['tipo']}")

        if r["analisis"]:
            if "promedio" in r["analisis"]:
                print(f"📊 Promedio: {r['analisis']['promedio']:.2f}")
            if "maximo" in r["analisis"]:
                print(f"📈 Valor máximo: {r['analisis']['maximo']}")
            if "minimo" in r["analisis"]:
                print(f"📉 Valor mínimo: {r['analisis']['minimo']}")

            print("-" * 30)  # Separador entre registros
        return

# Función para realizar análisis de datos
def realizar_analisis():
    if not registros:
        print("⚠️ No hay experimentos registrados.")
        return

    nombre = input("Ingrese el nombre del experimento a analizar: ")

    # Buscar el experimento correspondiente
    experimento = next((r for r in registros if r["nombre"] == nombre), None)

    if not experimento:
        print("⚠️ Experimento no encontrado.")
        return

    while True:
        print("\n¿Qué análisis desea hacer al experimento?")
        print("1. Calcular promedio")
        print("2. Valor máximo")
        print("3. Valor mínimo")
        print("4. Realizar todos los análisis")  # Nueva opción para hacer todo
        print("5. Comparar experimentos")  # Nueva opción para comparar
        print("6. Graficas de los experimentos")  # Nueva opción para graficar

        opcion = input("Ingrese una opción: ")

        if opcion in ["1", "2", "3", "4"]:
            cantidad = int(input("Ingrese la cantidad de números: "))
            numeros = [float(input(f"Ingrese el número {i + 1}: ")) for i in range(cantidad)]

            if opcion in ["1", "4"]:  # Calcular promedio
                 experimento["analisis"]["promedio"] = sum(numeros) / cantidad
                 print(f"📊 El promedio es: {experimento['analisis']['promedio']:.2f}")

            if opcion in ["2", "4"]:  # Calcular máximo
                 experimento["analisis"]["maximo"] = max(numeros)
                 print(f"📈 El valor máximo es: {experimento['analisis']['maximo']}")

            if opcion in ["3", "4"]:  # Calcular mínimo
                experimento["analisis"]["minimo"] = min(numeros)
                print(f"📉 El valor mínimo es: {experimento['analisis']['minimo']}")
                        
            return  # Salir de la función después de completar el análisis

        if opcion == "5":
            comparar_resultados()
            return  # Salir de la función después de la comparación
        
        if opcion == "6":
            graficar_resultados()
            return  # Salir de la función después de la comparación
        
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
    """Genera un informe con los datos analizados y muestra gráficas en una ventana."""
    if not registros:
        print("⚠️ No hay datos para generar un informe.")
        return

    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Informe de Experimentos")
    ventana.geometry("800x600")

    # Área de texto
    texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=80, height=15)
    texto.pack(pady=10)
    texto.insert(tk.END, "📋 INFORME DE EXPERIMENTOS\n\n")

    nombres, promedios, maximos, minimos = [], [], [], []

    for r in registros:
        texto.insert(tk.END, f"Nombre: {r['nombre']}\nFecha: {r['fecha']}\nTipo: {r['tipo']}\n")
        if r["analisis"]:
            texto.insert(tk.END, "📊 RESULTADOS DEL ANÁLISIS\n")
            texto.insert(tk.END, f"  - Promedio: {r['analisis']['promedio']:.2f}\n")
            texto.insert(tk.END, f"  - Máximo: {r['analisis']['maximo']}\n")
            texto.insert(tk.END, f"  - Mínimo: {r['analisis']['minimo']}\n")
        texto.insert(tk.END, "-" * 30 + "\n")

        # Agregar datos para graficar
        nombres.append(r["nombre"])
        promedios.append(r["analisis"].get("promedio", 0))
        maximos.append(r["analisis"].get("maximo", 0))
        minimos.append(r["analisis"].get("minimo", 0))

    # Crear la gráfica
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(nombres, promedios, marker='o', label="Promedio", linestyle="--", color="blue")
    ax.plot(nombres, maximos, marker='s', label="Máximo", linestyle="-", color="red")
    ax.plot(nombres, minimos, marker='d', label="Mínimo", linestyle=":", color="green")

    ax.set_xlabel("Experimentos")
    ax.set_ylabel("Valores")
    ax.set_title("Resultados de los Experimentos")
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45)

    # Incrustar la gráfica en la ventana
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()

    # Botón para cerrar la ventana
    btn_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
    btn_cerrar.pack(pady=10)

    ventana.mainloop()


# Función para comparar resultados actuales con los anteriores
def comparar_resultados():
    if len(registros) < 2:
        print("\n⚠️ No hay suficientes análisis previos para comparar.")
        return

    print("\nExperimentos disponibles para comparar:")
    for r in registros:
        print(f"- {r['nombre']}")

    nombre1 = input("Ingrese el nombre del primer experimento: ")
    nombre2 = input("Ingrese el nombre del segundo experimento: ")

    exp1 = next((r for r in registros if r["nombre"] == nombre1), None)
    exp2 = next((r for r in registros if r["nombre"] == nombre2), None)   
    
    if not exp1 or not exp2:
        print("⚠️ Uno o ambos experimentos no existen.")
        return

    print("\n🔍 Comparación de resultados:")
    
    for key in ["promedio", "maximo", "minimo"]:
        # Primero, revisamos si el valor existe en cada experimento
        if key in exp1["analisis"]:
            val1 = exp1["analisis"][key]  # Si existe, lo tomamos
        else:
            val1 = "No calculado"  # Si no existe, ponemos este mensaje

        if key in exp2["analisis"]:
            val2 = exp2["analisis"][key]
        else:
            val2 = "No calculado"

        # Mostramos el resultado de cada experimento
        print(f"{key.capitalize()}: {nombre1} -> {val1} | {nombre2} -> {val2}")

        # Si ambos valores existen, los comparamos
        if val1 != "No calculado" and val2 != "No calculado":
            if val1 > val2:
                print(f"🔹 {nombre1} tiene un {key} mayor que {nombre2}.")
            elif val1 < val2:
                print(f"🔹 {nombre1} tiene un {key} menor que {nombre2}.")
            else:
                print(f"🔹 Ambos experimentos tienen el mismo {key}.")
        
        print("-" * 40)  # Línea separadora

def graficar_resultados():
    if not registros:
        print("\n⚠️ No hay registros para graficar.")
        return

    nombres = []
    promedios = []
    maximos = []
    minimos = []

    for r in registros:
        nombres.append(r["nombre"])
        analisis = r.get("analisis", {})

        # Obtener valores o asignar None si no existen
        promedios.append(analisis.get("promedio", None))
        maximos.append(analisis.get("maximo", None))
        minimos.append(analisis.get("minimo", None))

    # Crear la gráfica
    plt.figure(figsize=(10, 5))
    plt.plot(nombres, promedios, marker='o', label="Promedio", linestyle="--", color="blue")
    plt.plot(nombres, maximos, marker='s', label="Máximo", linestyle="-", color="red")
    plt.plot(nombres, minimos, marker='d', label="Mínimo", linestyle=":", color="green")

    # Personalización
    plt.xlabel("Experimentos")
    plt.ylabel("Valores")
    plt.title("Resultados de los Experimentos")
    plt.legend()
    plt.xticks(rotation=45)  # Girar nombres si hay muchos
    plt.grid(True)

    # Mostrar la gráfica
    plt.show()
    return
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
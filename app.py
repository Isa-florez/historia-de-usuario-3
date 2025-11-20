"""
Archivo principal con el menú del sistema.
"""

from servicios import *
from archivos import guardar_csv, cargar_csv

inventario = []

def menu():
    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        try:
            opcion = int(input("Elige opción: "))
        except ValueError:
            print("Debes ingresar un número del 1 al 9.")
            continue

        if opcion == 1:
            nombre = input("Nombre: ")
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
                if precio < 0 or cantidad < 0:
                    print("No se permiten valores negativos.")
                    continue
            except ValueError:
                print("Datos inválidos.")
                continue

            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == 2:
            mostrar_inventario(inventario)

        elif opcion == 3:
            nombre = input("Nombre a buscar: ")
            print(buscar_producto(inventario, nombre))

        elif opcion == 4:
            nombre = input("Producto a actualizar: ")
            try:
                np = input("Nuevo precio (o Enter): ")
                nc = input("Nueva cantidad (o Enter): ")

                nuevo_precio = float(np) if np else None
                nueva_cantidad = int(nc) if nc else None
            except:
                print("Valores inválidos.")
                continue

            actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)

        elif opcion == 5:
            eliminar_producto(inventario, input("Producto a eliminar: "))

        elif opcion == 6:
            est = calcular_estadisticas(inventario)
            if est:
                print("\n--- ESTADÍSTICAS ---")
                print("Unidades totales:", est["unidades_totales"])
                print("Valor total:", est["valor_total"])
                print("Producto más caro:", est["producto_mas_caro"])
                print("Mayor stock:", est["producto_mayor_stock"])

        elif opcion == 7:
            ruta = input("Ruta CSV a guardar: ")
            guardar_csv(inventario, ruta)

        elif opcion == 8:
            ruta = input("Ruta CSV a cargar: ")
            nuevos, errores = cargar_csv(ruta)

            if nuevos:
                print("¿Sobrescribir inventario actual? (S/N)")
                resp = input().upper()

                if resp == "S":
                    inventario.clear()
                    inventario.extend(nuevos)
                    print("Inventario reemplazado.")

                else:  # FUSIÓN
                    print("Fusión: si existe un nombre, suma cantidades y actualiza precio.")
                    for p in nuevos:
                        existe = buscar_producto(inventario, p["nombre"])
                        if existe:
                            existe["cantidad"] += p["cantidad"]
                            existe["precio"] = p["precio"]
                        else:
                            inventario.append(p)

            print(f"Filas inválidas omitidas: {errores}")

        elif opcion == 9:
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")

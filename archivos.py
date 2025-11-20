"""
Módulo: archivos.py
Funciones para guardar y cargar inventarios en CSV.
"""

import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    """
    if not inventario:
        print("No se puede guardar: el inventario está vacío.")
        return

    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"Inventario guardado en: {ruta}")

    except PermissionError:
        print("Error: no tienes permisos para escribir en esa ruta.")
    except Exception as e:
        print("Error inesperado al guardar:", e)


def cargar_csv(ruta):
    """
    Carga un inventario desde un archivo CSV con validaciones.
    Retorna:
        lista de productos cargados
        contador de filas inválidas
    """

    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            encabezado = next(reader, None)

            # Validar encabezado
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Error: encabezado inválido.")
                return [], 0

            for fila in reader:
                if len(fila) != 3:
                    errores += 1
                    continue

                nombre, precio, cantidad = fila

                try:
                    precio = float(precio)
                    cantidad = int(cantidad)

                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

                except ValueError:
                    errores += 1
                    continue

        return inventario, errores

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except UnicodeDecodeError:
        print("Error de codificación.")
    except Exception as e:
        print("Error inesperado al cargar:", e)

    return [], 0

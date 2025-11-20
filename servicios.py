"""
Modulo: servicios.py
contiene funciones para gestionar el inventario en memoria"""

def agregar_producto(inventario,nombre,precio,cantidad):
    """
    Agg un nuevoproducto al inventario
    parametros: 
    inventario (list), nombre (str), precio (float), cantidad (int)
    Retorno: none
    """

    #se crea el diccionario y se agrega
    producto ={"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)

def mostrar_inventario(inventario):
    """
    Muestra todos los rpoductos del inventario
    parametro:
    inventario (list): lista de productos
    """
    if not inventario:
        print("inventario vacio")
        return
    for p in inventario:
        print(f"-{p ['nombre']} | $ {p['precio']} |{p ['cantidad']} unidades")

def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre
    Retorna: el diccionario del producto o none si no se encuentra
    """
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None
def actualizar_producto(inventario, nombre, nuevo_precio = None, nueva_cantidad = None):
    """
    actualiza precio y la cantidad de un producto existente
    """
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        print("producto no encontrado")
        return
    
    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio
    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    print("actualizado correctamente")

def eliminar_producto(inventario, nombre):
    """
    Elimina un producto por nombre
    """
    producto = buscar_producto(inventario,nombre)

    if producto:
        inventario.remove(producto)
        print("producto eliminado")
    else:
        print("producto no encontrado")

def calcular_estadisticas(inventario):
    """
    Retorna estadisticas del inventario:
        unidades_totales
        valor_total
        producto_caro
        protucto_mayor_stock
    """
    if len(inventario) == 0:
        return None
    unidades_totales = 0
    valor_total = 0
    producto_caro = inventario[0]
    producto_mayor_stock = inventario[0]

    for producto in inventario:
        unidades_totales += producto["cantidad"]
        if producto["precio"] > producto_caro["precio"]: 
            producto_caro = producto
        if producto["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = producto
    return{

        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_caro": producto_caro,
        "producto_mayor_stock": producto_mayor_stock
        
    }

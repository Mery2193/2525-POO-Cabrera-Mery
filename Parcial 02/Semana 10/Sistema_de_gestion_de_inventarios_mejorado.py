# ==============================
# SISTEMA DE GESTIÓN DE INVENTARIOS MEJORADO
# ==============================

import os
import json

class Producto:
    """Clase que representa un producto del inventario."""

    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    @staticmethod
    def from_dict(data):
        return Producto(data["id"], data["nombre"], int(data["cantidad"]), float(data["precio"]))

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    """Clase que representa el inventario de la tienda."""

    ARCHIVO = "inventario.JSON"  # <- cambio aplicado aquí

    def __init__(self):
        self.productos = {}  # Diccionario con ID como clave
        self.cargar_desde_archivo()  # Recuperación automática al iniciar

    # ----------------------------
    # Almacenamiento en archivo
    # ----------------------------
    def guardar_en_archivo(self):
        try:
            with open(self.ARCHIVO, "w", encoding="utf-8") as f:
                productos_dict = {id: p.to_dict() for id, p in self.productos.items()}
                json.dump(productos_dict, f, indent=4)
        except PermissionError:
            print("❌ Error: no se tienen permisos para escribir en el archivo.")

    # ----------------------------
    # Recuperación desde archivo
    # ----------------------------
    def cargar_desde_archivo(self):
        """Carga el inventario desde el archivo inventario.JSON"""
        if not os.path.exists(self.ARCHIVO):
            try:
                with open(self.ARCHIVO, "w", encoding="utf-8") as f:
                    json.dump({}, f)
                print("📭 Inventario vacío al iniciar el programa.")
            except PermissionError:
                print("❌ Error: no se tienen permisos para crear el archivo de inventario.")
            return

        try:
            with open(self.ARCHIVO, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.productos = {id: Producto.from_dict(p) for id, p in data.items()}

            if self.productos:
                print("📂 Inventario cargado correctamente desde archivo.")
            else:
                print("📭 Inventario vacío al iniciar el programa.")

        except json.JSONDecodeError:
            print("⚠ Archivo corrupto. Se inicializa inventario vacío.")
            self.productos = {}
        except PermissionError:
            print("❌ Error: no se tienen permisos para leer el archivo.")

    # ----------------------------
    # Operaciones de inventario
    # ----------------------------
    def agregar_producto(self, producto):
        if producto.id in self.productos:
            return False
        self.productos[producto.id] = producto
        self.guardar_en_archivo()
        return True

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_en_archivo()
            return True
        return False

    def actualizar_cantidad(self, id, cantidad):
        if id in self.productos:
            self.productos[id].cantidad = cantidad
            self.guardar_en_archivo()
            return True
        return False

    def actualizar_precio(self, id, precio):
        if id in self.productos:
            self.productos[id].precio = precio
            self.guardar_en_archivo()
            return True
        return False

    def buscar_producto(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def mostrar_productos(self):
        return list(self.productos.values())


# ----------------------------
# Interfaz de usuario en consola
# ----------------------------
def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE GESTIÓN DE INVENTARIOS =====")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad de producto")
        print("4. Actualizar precio de producto")
        print("5. Buscar producto por nombre")
        print("6. Mostrar todos los productos")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            try:
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
            except ValueError:
                print("❌ Error: cantidad o precio inválidos.")
                continue
            producto = Producto(id, nombre, cantidad, precio)
            if inventario.agregar_producto(producto):
                print("✅ Producto añadido correctamente al inventario y archivo.")
            else:
                print("❌ Error: el ID ya existe.")

        elif opcion == "2":
            id = input("Ingrese ID del producto a eliminar: ")
            if inventario.eliminar_producto(id):
                print("✅ Producto eliminado correctamente del inventario y archivo.")
            else:
                print("❌ Producto no encontrado.")

        elif opcion == "3":
            id = input("Ingrese ID del producto: ")
            try:
                cantidad = int(input("Ingrese nueva cantidad: "))
            except ValueError:
                print("❌ Cantidad inválida.")
                continue
            if inventario.actualizar_cantidad(id, cantidad):
                print("✅ Cantidad actualizada en inventario y archivo.")
            else:
                print("❌ Producto no encontrado.")

        elif opcion == "4":
            id = input("Ingrese ID del producto: ")
            try:
                precio = float(input("Ingrese nuevo precio: "))
            except ValueError:
                print("❌ Precio inválido.")
                continue
            if inventario.actualizar_precio(id, precio):
                print("✅ Precio actualizado en inventario y archivo.")
            else:
                print("❌ Producto no encontrado.")

        elif opcion == "5":
            nombre = input("Ingrese nombre a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                print("📦 Resultados de búsqueda:")
                for p in resultados:
                    print(p)
            else:
                print("❌ No se encontraron productos.")

        elif opcion == "6":
            productos = inventario.mostrar_productos()
            if productos:
                print("📋 Inventario actual:")
                for p in productos:
                    print(p)
            else:
                print("📭 Inventario vacío.")

        elif opcion == "7":
            print("👋 Saliendo del sistema... Hasta pronto!")
            break

        else:
            print("⚠️ Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()

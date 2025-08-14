# SISTEMA DE GESTIÓN DE INVENTARIOS

class Producto:
    """Clase que representa un producto del inventario."""

    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y setters
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    """Clase que representa el inventario de la tienda."""

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        """Añade un nuevo producto si el ID es único."""
        if any(p.get_id() == producto.get_id() for p in self.productos):
            return False
        self.productos.append(producto)
        return True

    def eliminar_producto(self, id):
        """Elimina un producto por ID."""
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                return True
        return False

    def actualizar_cantidad(self, id, cantidad):
        """Actualiza la cantidad de un producto."""
        for p in self.productos:
            if p.get_id() == id:
                p.set_cantidad(cantidad)
                return True
        return False

    def actualizar_precio(self, id, precio):
        """Actualiza el precio de un producto."""
        for p in self.productos:
            if p.get_id() == id:
                p.set_precio(precio)
                return True
        return False

    def buscar_producto(self, nombre):
        """Busca productos cuyo nombre contenga la palabra clave."""
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_productos(self):
        """Devuelve todos los productos del inventario."""
        return self.productos


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
                print("Error: cantidad o precio inválidos.")
                continue
            producto = Producto(id, nombre, cantidad, precio)
            if inventario.agregar_producto(producto):
                print("✅ Producto añadido correctamente.")
            else:
                print("❌ Error: el ID ya existe.")

        elif opcion == "2":
            id = input("Ingrese ID del producto a eliminar: ")
            if inventario.eliminar_producto(id):
                print("✅ Producto eliminado correctamente.")
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
                print("✅ Cantidad actualizada.")
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
                print("✅ Precio actualizado.")
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

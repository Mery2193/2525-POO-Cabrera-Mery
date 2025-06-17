# Programa que modela una tienda virtual usando POO en Python

class Producto:
    """
    Representa un producto en la tienda.
    Atributos:
        codigo (str): Identificador único del producto.
        nombre (str): Nombre del producto.
        precio (float): Precio unitario.
        stock (int): Cantidad disponible.
    """
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        """
        Muestra la información del producto.
        """
        print(f"Código: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}")

    def actualizar_stock(self, cantidad):
        """
        Actualiza el stock restando la cantidad vendida.
        """
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        else:
            print(f"Stock insuficiente para el producto {self.nombre}.")
            return False

class Cliente:
    """
    Representa un cliente que realiza compras.
    Atributos:
        nombre (str): Nombre del cliente.
        carrito (dict): Diccionario con productos y cantidades.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = {}

    def agregar_al_carrito(self, producto, cantidad):
        """
        Agrega productos al carrito de compra.
        """
        if producto.actualizar_stock(cantidad):
            if producto.codigo in self.carrito:
                self.carrito[producto.codigo]['cantidad'] += cantidad
            else:
                self.carrito[producto.codigo] = {'producto': producto, 'cantidad': cantidad}
            print(f"{cantidad} unidad(es) de {producto.nombre} agregada(s) al carrito de {self.nombre}.")
        else:
            print(f"No se pudo agregar {producto.nombre} al carrito de {self.nombre}.")

    def mostrar_carrito(self):
        """
        Muestra los productos en el carrito con cantidades y total.
        """
        print(f"Carrito de {self.nombre}:")
        total = 0
        for item in self.carrito.values():
            producto = item['producto']
            cantidad = item['cantidad']
            subtotal = producto.precio * cantidad
            total += subtotal
            print(f"- {producto.nombre}: {cantidad} x ${producto.precio:.2f} = ${subtotal:.2f}")
        print(f"Total a pagar: ${total:.2f}")

class Tienda:
    """
    Representa la tienda con su catálogo y clientes.
    """
    def __init__(self):
        self.catalogo = []
        self.clientes = []

    def agregar_producto(self, producto):
        """
        Agrega un producto al catálogo de la tienda.
        """
        self.catalogo.append(producto)

    def mostrar_catalogo(self):
        """
        Muestra todos los productos disponibles en la tienda.
        """
        print("Catálogo de productos:")
        for producto in self.catalogo:
            producto.mostrar_info()

    def registrar_cliente(self, cliente):
        """
        Agrega un cliente a la tienda.
        """
        self.clientes.append(cliente)

# Programa principal
if __name__ == "__main__":
    tienda = Tienda()

    # Crear productos y agregarlos al catálogo
    producto1 = Producto("P001", "Camiseta", 15.99, 50)
    producto2 = Producto("P002", "Jeans", 39.99, 30)
    producto3 = Producto("P003", "Zapatillas", 59.99, 20)

    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)
    tienda.agregar_producto(producto3)

    tienda.mostrar_catalogo()

    # Crear clientes
    cliente1 = Cliente("Mery")
    cliente2 = Cliente("Pedro")

    tienda.registrar_cliente(cliente1)
    tienda.registrar_cliente(cliente2)

    # Clientes agregan productos al carrito
    cliente1.agregar_al_carrito(producto1, 2)
    cliente1.agregar_al_carrito(producto3, 1)

    cliente2.agregar_al_carrito(producto2, 1)
    cliente2.agregar_al_carrito(producto3, 3)

    # Mostrar carritos
    cliente1.mostrar_carrito()
    cliente2.mostrar_carrito()

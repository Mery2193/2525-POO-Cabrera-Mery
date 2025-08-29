# Tema: Sistema Avanzado de Gestión de Inventario

from dataclasses import dataclass
from collections import defaultdict
from typing import Dict, List, Set
import json
import os

# Clase Producto: representa un producto del inventario
@dataclass
class Producto:
    _id: str
    _nombre: str
    _cantidad: int
    _precio: float

    @property
    def id(self) -> str:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if not value.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value.strip()

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value: int) -> None:
        if value < 0:
            raise ValueError("La cantidad debe ser >= 0.")
        self._cantidad = value

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, value: float) -> None:
        if value < 0:
            raise ValueError("El precio debe ser >= 0.")
        self._precio = round(value, 2)

    def to_dict(self) -> Dict:
        return {"id": self.id, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    @staticmethod
    def from_dict(data: Dict) -> "Producto":
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])

# Clase Inventario: gestiona los productos usando un diccionario
class Inventario:
    def __init__(self) -> None:
        self._productos: Dict[str, Producto] = {}
        self._indice_nombre: defaultdict[str, Set[str]] = defaultdict(set)  # búsqueda rápida por nombre

    # Añadir nuevo producto
    def anadir_producto(self, producto: Producto) -> None:
        if producto.id in self._productos:
            raise KeyError(f"ID '{producto.id}' ya existe.")
        self._productos[producto.id] = producto
        self._indice_nombre[producto.nombre.lower()].add(producto.id)

    # Eliminar producto por ID
    def eliminar_producto(self, pid: str) -> None:
        if pid not in self._productos:
            raise KeyError(f"No existe el producto con ID '{pid}'.")
        prod = self._productos.pop(pid)
        self._indice_nombre[prod.nombre.lower()].remove(pid)
        if not self._indice_nombre[prod.nombre.lower()]:
            del self._indice_nombre[prod.nombre.lower()]

    # Actualizar cantidad
    def actualizar_cantidad(self, pid: str, cantidad: int) -> None:
        self._productos[pid].cantidad = cantidad

    # Actualizar precio
    def actualizar_precio(self, pid: str, precio: float) -> None:
        self._productos[pid].precio = precio

    # Buscar productos por nombre
    def buscar_por_nombre(self, nombre: str) -> List[Producto]:
        nombre = nombre.lower()
        ids = set()
        for clave, pid_set in self._indice_nombre.items():
            if nombre in clave:
                ids |= pid_set
        return [self._productos[pid] for pid in ids]

    # Mostrar todos los productos
    def mostrar_todos(self) -> List[Producto]:
        return list(self._productos.values())

    # Guardar inventario en archivo
    def guardar_en_archivo(self, ruta: str) -> None:
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self._productos.values()], f, indent=2, ensure_ascii=False)

    # Cargar inventario desde archivo
    def cargar_desde_archivo(self, ruta: str) -> None:
        if not os.path.exists(ruta):
            return
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
            for d in datos:
                prod = Producto.from_dict(d)
                self.anadir_producto(prod)

# Funciones auxiliares para entrada de datos
def input_no_vacio(msg: str) -> str:
    valor = input(msg).strip()
    if not valor:
        raise ValueError("Entrada vacía no permitida.")
    return valor

def input_entero(msg: str) -> int:
    return int(input_no_vacio(msg))

def input_float(msg: str) -> float:
    return float(input_no_vacio(msg))

# Mostrar productos en tabla simple
def imprimir_tabla(productos: List[Producto]) -> None:
    if not productos:
        print("(sin resultados)")
        return
    print(f"{'ID':<8} {'Nombre':<20} {'Cant':<6} {'Precio':<8}")
    print("-"*44)
    for p in productos:
        print(f"{p.id:<8} {p.nombre:<20} {p.cantidad:<6} {p.precio:<8.2f}")

# Menú principal
def menu():
    inventario = Inventario()
    ARCHIVO = "inventario.json"
    inventario.cargar_desde_archivo(ARCHIVO)

    while True:
        print("\n=== MENÚ INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad")
        print("4. Actualizar precio")
        print("5. Buscar por nombre")
        print("6. Mostrar todos")
        print("7. Guardar inventario")
        print("0. Salir")

        opcion = input_no_vacio("Seleccione opción: ")

        try:
            if opcion == "1":
                pid = input_no_vacio("ID: ")
                nombre = input_no_vacio("Nombre: ")
                cantidad = input_entero("Cantidad: ")
                precio = input_float("Precio: ")
                inventario.anadir_producto(Producto(pid, nombre, cantidad, precio))
                print("Producto añadido ✅")

            elif opcion == "2":
                pid = input_no_vacio("ID a eliminar: ")
                inventario.eliminar_producto(pid)
                print("Producto eliminado ✅")

            elif opcion == "3":
                pid = input_no_vacio("ID a actualizar cantidad: ")
                cantidad = input_entero("Nueva cantidad: ")
                inventario.actualizar_cantidad(pid, cantidad)
                print("Cantidad actualizada ✅")

            elif opcion == "4":
                pid = input_no_vacio("ID a actualizar precio: ")
                precio = input_float("Nuevo precio: ")
                inventario.actualizar_precio(pid, precio)
                print("Precio actualizado ✅")

            elif opcion == "5":
                nombre = input_no_vacio("Nombre a buscar: ")
                resultados = inventario.buscar_por_nombre(nombre)
                if resultados:
                    imprimir_tabla(resultados)
                else:
                    print("❌ No se encontró ningún producto.")

            elif opcion == "6":
                imprimir_tabla(inventario.mostrar_todos())

            elif opcion == "7":
                inventario.guardar_en_archivo(ARCHIVO)
                print("Inventario guardado 💾")

            elif opcion == "0":
                inventario.guardar_en_archivo(ARCHIVO)
                print("Saliendo... Inventario guardado 👋")
                break
            else:
                print("⚠ Opción inválida.")

        except Exception as e:
            print(f"❌ Error: {e}")

#  Ejecutar el programa
if __name__ == "__main__":
    menu()

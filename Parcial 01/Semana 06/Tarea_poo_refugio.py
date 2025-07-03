# tarea_poo_refugio.py

# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Encapsulación
        self._edad = edad      # Encapsulación

    def describir(self):
        return f"{self._nombre} tiene {self._edad} años."

    def hacer_sonido(self):  # Método que será sobrescrito (polimorfismo)
        return "Sonido genérico de animal."

    def get_nombre(self):  # Getter
        return self._nombre

    def set_nombre(self, nuevo_nombre):  # Setter
        self._nombre = nuevo_nombre


# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self._raza = raza

    def hacer_sonido(self):  # Polimorfismo (método sobrescrito)
        return f"{self._nombre} dice: ¡Guau!"

    def obtener_raza(self):
        return self._raza


# Otra clase derivada
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self._color = color

    def hacer_sonido(self):  # Polimorfismo (método sobrescrito)
        return f"{self._nombre} dice: ¡Miau!"

    def obtener_color(self):
        return self._color


# Función polimórfica
def hacer_hablar(animal):
    print(animal.hacer_sonido())


# Instancias
animal1 = Animal("Tigre", 4)
perro1 = Perro("Max", 3, "Labrador")
gato1 = Gato("Luna", 2, "Gris")

# Uso de métodos
print(animal1.describir())
print(perro1.describir())
print(perro1.obtener_raza())

print(perro1.get_nombre())
perro1.set_nombre("Rocky")
print(perro1.get_nombre())

hacer_hablar(animal1)
hacer_hablar(perro1)
hacer_hablar(gato1)

# Clase que simula un sistema con inicio y cierre de sesión
class Sistema:
    def __init__(self, nombre):
        # Constructor: inicializa el sistema con un nombre
        self.nombre = nombre
        print(f"Sistema '{self.nombre}' iniciado.")

    def estado(self):
        # Método para mostrar que el sistema está activo
        print(f"El sistema '{self.nombre}' está funcionando.")

    def __del__(self):
        # Destructor: indica que el sistema se cerró
        print(f"Sistema '{self.nombre}' cerrado.")


# Clase que simula una persona que inicia y cierra sesión
class Persona:
    def __init__(self, nombre, edad):
        # Constructor: inicializa el nombre y edad de la persona
        self.nombre = nombre
        self.edad = edad
        print(f"Persona creada: {self.nombre}, {self.edad} años.")

    def saludar(self):
        # Método para que la persona se presente
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

    def __del__(self):
        # Destructor: indica que la persona fue eliminada
        print(f"Persona '{self.nombre}' eliminada de la memoria.")


# Bloque principal de ejecución
if __name__ == "__main__":
    print("Inicio del programa\n")

    sistema = Sistema("Contabilidad")
    sistema.estado()

    persona = Persona("Mery", 18)
    persona.saludar()

    print("\nFin del programa")


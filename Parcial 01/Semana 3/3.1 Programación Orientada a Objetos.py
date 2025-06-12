# Programa: Promedio Semanal del Clima
# Enfoque: Programación Orientada a Objetos (POO)
# Objetivo: Desarrollar habilidades prácticas en POO mediante la implementación de un programa en Python para determinar el promedio semanal del clima.

# Clase que representa la información diaria del clima
class ClimaDiario:
    def __init__(self, temperatura):
        # Encapsulamos la temperatura como un atributo privado
        self.__temperatura = temperatura

    # Método para obtener la temperatura (getter)
    def obtener_temperatura(self):
        return self.__temperatura

    # Método para cambiar la temperatura (setter)
    def establecer_temperatura(self, nueva_temp):
        self.__temperatura = nueva_temp

# Clase que representa el clima semanal
class ClimaSemanal:
    def __init__(self):
        # Lista para almacenar objetos de tipo ClimaDiario
        self.temperaturas_diarias = []

    # Método para agregar un día de clima
    def agregar_dia(self, temperatura):
        clima = ClimaDiario(temperatura)
        self.temperaturas_diarias.append(clima)

    # Método para calcular el promedio semanal de temperatura
    def calcular_promedio(self):
        suma = 0
        for clima in self.temperaturas_diarias:
            suma += clima.obtener_temperatura()
        promedio = suma / len(self.temperaturas_diarias)
        return promedio

# Función principal
def main():
    print("=== Promedio Semanal del Clima (Programación Orientada a Objetos) ===")

    # Lista de temperaturas simuladas para evitar el uso de input()
    datos_simulados = [25.0, 26.5, 24.8, 27.1, 23.9, 26.0, 25.5]

    # Creamos el objeto que manejará la semana completa
    semana = ClimaSemanal()

    # Agregamos las temperaturas a la semana usando el método agregar_dia
    for temp in datos_simulados:
        semana.agregar_dia(temp)

    # Calculamos el promedio
    promedio = semana.calcular_promedio()
    print(f"Temperaturas: {datos_simulados}")
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

main()

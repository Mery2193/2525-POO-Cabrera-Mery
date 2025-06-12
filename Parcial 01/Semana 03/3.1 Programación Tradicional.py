# Programa: Promedio Semanal del Clima
# Enfoque: Programación Tradicional
# Objetivo: Desarrollar habilidades prácticas en la Programación Tradicional mediante la implementación de un programa en Python para determinar el promedio semanal del clima.

# Función para obtener temperaturas simuladas (sin entrada manual)
def ingresar_temperaturas():
    # Lista fija para evitar errores por input() en entornos con fallos
    temperaturas = [25.0, 26.5, 24.8, 27.1, 23.9, 26.0, 25.5]
    return temperaturas

# Función que calcula el promedio semanal de temperaturas
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

# Función principal
def main():
    print("=== Promedio Semanal del Clima (Programación Tradicional) ===")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"Temperaturas: {temperaturas}")
    print(f"El promedio semanal de temperatura es: {promedio:.2f}°C")

main()

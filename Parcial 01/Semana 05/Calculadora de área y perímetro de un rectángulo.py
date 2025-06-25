# Calculadora de área y perímetro de un rectángulo
# Este programa solicita al usuario la base y la altura de un rectángulo,
# calcula el área y el perímetro, y muestra los resultados.
# Se utilizan tipos de datos integer, float, string y boolean.
# Los identificadores siguen la convención snake_case.
# Comentarios explicativos están incluidos para claridad.

def calcular_area(base: float, altura: float) -> float:
    return base * altura

def calcular_perimetro(base: float, altura: float) -> float:
    return 2 * (base + altura)

print("Calculadora de área y perímetro de un rectángulo")

nombre_usuario = input("Ingrese su nombre: ")
base_input = input("Ingrese la base del rectángulo en cm: ")
altura_input = input("Ingrese la altura del rectángulo en cm: ")

base = float(base_input)
altura = float(altura_input)

area = calcular_area(base, altura)
perimetro = calcular_perimetro(base, altura)

print(f"\nHola, {nombre_usuario}.")
print(f"El área del rectángulo es: {area} cm²")
print(f"El perímetro del rectángulo es: {perimetro} cm")

programa_funciono_correctamente = True
print(f"¿El programa se ejecutó correctamente? {programa_funciono_correctamente}")

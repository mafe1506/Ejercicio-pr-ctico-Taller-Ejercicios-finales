def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero"


def mostrar_menu():
    print("Seleccione una operación:")
    print("1. saludo")
    print("2. suma y resta")
    print("3. edad")
    print("4. imc")
    print("5. #par e impar")
    print("6. area cuadrado")
    print("7. area triangulo")
    print("8. salario")
    print("9. horas extras")

while True:
    mostrar_menu()
    opcion = input("Ingrese el número correspondiente a la operación deseada: ")

    if opcion == '1':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = sumar(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == '2':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = restar(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == '3':
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        resultado = multiplicar(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == '4':
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador (distinto de cero): "))
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")
    elif opcion == '5':
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador (distinto de cero): "))
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")

    elif opcion == '6':
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador (distinto de cero): "))
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")

    elif opcion == '7':
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador (distinto de cero): "))
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")

    elif opcion == '8':
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador (distinto de cero): "))
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")

    elif opcion == '9':
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador (distinto de cero): "))
        resultado = dividir(a, b)
        print(f"Resultado: {resultado}")


    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
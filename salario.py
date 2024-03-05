
salario_minimo = 1300000  # Este valor puede variar, asegúrate de usar el valor actual

# Solicitar al usuario que ingrese su salario
salario = float(input("Ingresa tu salario: "))


if salario >= salario_minimo:
    print("El salario ingresado es mayor.")
else:
    print("El salario ingresado es menor que el salario mínimo.")
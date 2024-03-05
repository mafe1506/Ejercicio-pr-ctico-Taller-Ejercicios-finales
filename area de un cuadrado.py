def cuadrado(numero):
    """Esta función devuelve el cuadrado de un número."""
    return numero ** 2
# Llamada a la función y uso del valor devuelto
resultado_cuadrado = cuadrado(4)
print(resultado_cuadrado)


def cuadrado(numero):
    return numero ** 2

# Solicitar al usuario que ingrese un número
numero_usuario = int(input("Por favor, ingresa un número para calcular su cuadrado: "))

resultado_cuadrado = cuadrado(numero_usuario)
print("El cuadrado de", numero_usuario, "es:", resultado_cuadrado)
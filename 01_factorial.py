# ==================================================================
# 01_factorial.py
# EJERCICIO: Factorial de un número
# ==================================================================
# QUÉ HACE:
#   Define factorial(n), que recibe un entero positivo y retorna n!
#   (n! = 1 * 2 * 3 * ... * n). Ejemplo: factorial(5) = 120.
#
# LO MÁS IMPORTANTE:
#   - Se parte de resultado = 1 (elemento neutro de la multiplicación).
#   - Se multiplica por 2, 3, ..., n con un for. Multiplicar por 1 no cambia nada.
#   - 0! y 1! valen 1: el for no se ejecuta y se retorna 1.
# ==================================================================

def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


# ------ EJEMPLO FIJO (descomenta para probar sin escribir datos) ------
# print(factorial(5))   # Salida esperada: 120

# ------ VERSIÓN CON input() ------
n = int(input("Ingrese un entero positivo: "))
if n < 0:
    print("El factorial no está definido para negativos")
else:
    print(f"{n}! = {factorial(n)}")

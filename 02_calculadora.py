# ==================================================================
# 02_calculadora.py
# EJERCICIO: Calculadora con funciones independientes
# ==================================================================
# QUÉ HACE:
#   Cuatro funciones independientes (sumar, restar, multiplicar, dividir)
#   y una función calculadora() que pide los datos y llama a la correcta.
#
# LO MÁS IMPORTANTE:
#   - Cada operación vive en su propia función: reutilizable y fácil de probar.
#   - calculadora() solo decide cuál llamar según el símbolo ingresado.
#   - dividir() debe controlar b == 0 para no caer en ZeroDivisionError.
# ==================================================================

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b


def calculadora():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    op = input("Operación (+, -, *, /): ")
    if op == "+":
        print("Resultado:", sumar(a, b))
    elif op == "-":
        print("Resultado:", restar(a, b))
    elif op == "*":
        print("Resultado:", multiplicar(a, b))
    elif op == "/":
        print("Resultado:", dividir(a, b))
    else:
        print("Operación inválida")


# ------ EJEMPLO FIJO (descomenta para probar) ------
# print(sumar(8, 2))        # 10
# print(restar(8, 2))       # 6
# print(multiplicar(8, 2))  # 16
# print(dividir(8, 2))      # 4.0
# print(dividir(8, 0))      # Error: división por cero

# ------ VERSIÓN CON input() ------
calculadora()

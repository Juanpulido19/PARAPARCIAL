# ==================================================================
# 05_maximo_de_tres.py
# EJERCICIO: Máximo de tres números
# ==================================================================
# QUÉ HACE:
#   Define maximo_de_tres(a, b, c) sin usar listas ni la función max().
#
# LO MÁS IMPORTANTE:
#   - Patrón 'mayor hasta ahora': se asume que a es el mayor.
#   - Si b o c lo superan, se reemplaza. Al final queda el mayor de los tres.
# ==================================================================

def maximo_de_tres(a, b, c):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor


# ------ EJEMPLO FIJO (descomenta para probar) ------
# print(maximo_de_tres(3, 9, 5))   # 9

# ------ VERSIÓN CON input() ------
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))
print("El máximo es:", maximo_de_tres(a, b, c))

# ==================================================================
# 07_invertir_cadena_recursiva.py
# EJERCICIO: Invertir una cadena con recursión
# ==================================================================
# QUÉ HACE:
#   Define invertir(cadena), que retorna la cadena al revés usando RECURSIÓN,
#   sin slicing [::-1] ni estructuras avanzadas.
#
# LO MÁS IMPORTANTE:
#   - CASO BASE: cuando el índice i llega al final, se retorna cadena vacía.
#   - CASO RECURSIVO: primero se invierte el resto (desde i+1) y luego se pone
#   - el carácter actual AL FINAL. Así el primer carácter queda de último.
#   - Seguimiento: invertir('hola') -> invertir('ola') + 'h' -> ... -> 'aloh'.
#   - Esta versión no usa slicing de ningún tipo (el parámetro i es opcional).
# ==================================================================

def invertir(cadena, i=0):
    if i == len(cadena):                       # caso base
        return ""
    return invertir(cadena, i + 1) + cadena[i]  # caso recursivo


# Versión alternativa con slicing de recorte (por si el profesor la permite):
# def invertir(cadena):
#     if cadena == "":
#         return ""
#     return invertir(cadena[1:]) + cadena[0]


# ------ EJEMPLO FIJO (descomenta para probar) ------
# print(invertir("hola"))   # aloh

# ------ VERSIÓN CON input() ------
texto = input("Ingrese una cadena: ")
print("Invertida:", invertir(texto))

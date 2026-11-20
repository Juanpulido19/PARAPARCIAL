# ==================================================================
# 08_es_palindromo.py
# EJERCICIO: Determinar si una cadena es palíndroma
# ==================================================================
# QUÉ HACE:
#   Define es_palindromo(cadena), que retorna True si se lee igual al derecho
#   y al revés. Compara carácter por carácter usando la función invertir.
#
# LO MÁS IMPORTANTE:
#   - Se invierte la cadena y se compara posición por posición con la original.
#   - Si encuentra una diferencia retorna False; si termina el for, es palíndroma.
#   - Esta comparación distingue mayúsculas y espacios. Para ignorarlos:
#   - cadena = cadena.replace(' ', '').lower() al inicio de la función.
# ==================================================================

def invertir(cadena, i=0):
    if i == len(cadena):
        return ""
    return invertir(cadena, i + 1) + cadena[i]


def es_palindromo(cadena):
    inversa = invertir(cadena)
    for i in range(len(cadena)):
        if cadena[i] != inversa[i]:
            return False
    return True


# ------ EJEMPLO FIJO (descomenta para probar) ------
# print(es_palindromo("reconocer"))   # True
# print(es_palindromo("python"))      # False

# ------ VERSIÓN CON input() ------
texto = input("Ingrese una cadena: ")
if es_palindromo(texto):
    print("Es palíndroma")
else:
    print("No es palíndroma")

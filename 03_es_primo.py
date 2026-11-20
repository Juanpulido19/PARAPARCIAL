# ==================================================================
# 03_es_primo.py
# EJERCICIO: Determinar si un número es primo
# ==================================================================
# QUÉ HACE:
#   Define es_primo(n), que retorna True si n es primo y False si no.
#
# LO MÁS IMPORTANTE:
#   - Un primo solo es divisible por 1 y por sí mismo. Los menores que 2 NO son primos.
#   - Basta probar divisores desde 2 hasta la raíz cuadrada de n.
#   - i * i <= n equivale a i <= raíz(n) sin necesidad de importar math.
#   - Si algún i divide a n (n % i == 0), se retorna False de inmediato.
# ==================================================================

def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# ------ EJEMPLO FIJO (descomenta para probar) ------
# print(es_primo(17))   # True
# print(es_primo(18))   # False
# print(es_primo(1))    # False

# ------ VERSIÓN CON input() ------
n = int(input("Ingrese un entero: "))
if es_primo(n):
    print(f"{n} es primo")
else:
    print(f"{n} no es primo")

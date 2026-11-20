# ==================================================================
# 10_mcd_y_mcm.py
# EJERCICIO: Máximo común divisor (MCD) y mínimo común múltiplo (MCM)
# ==================================================================
# QUÉ HACE:
#   mcd(a, b) usa el algoritmo de Euclides.
#   mcm(a, b) usa la fórmula mcm = |a * b| / mcd(a, b).
#
# LO MÁS IMPORTANTE:
#   - Euclides: se reemplaza (a, b) por (b, a % b) hasta que b sea 0; el MCD queda en a.
#   - Ejemplo: mcd(12, 18) -> (18, 12) -> (12, 6) -> (6, 0) => MCD = 6.
#   - mcm(12, 18) = 12 * 18 / 6 = 36.
#   - Se usa // (división entera) para que el MCM sea entero.
# ==================================================================

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


def mcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // mcd(a, b)


# ------ EJEMPLO FIJO (descomenta para probar) ------
# print(mcd(12, 18))   # 6
# print(mcm(12, 18))   # 36

# ------ VERSIÓN CON input() ------
a = int(input("Primer entero: "))
b = int(input("Segundo entero: "))
print("MCD:", mcd(a, b))
print("MCM:", mcm(a, b))

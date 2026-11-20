# ==================================================================
# 04_celsius_a_fahrenheit.py
# EJERCICIO: Convertir grados Celsius a Fahrenheit
# ==================================================================
# QUÉ HACE:
#   Define celsius_fahrenheit(c) aplicando la fórmula F = (C * 9/5) + 32.
#
# LO MÁS IMPORTANTE:
#   - Es solo aplicar la fórmula y retornar el resultado.
#   - Referencias para verificar: 0 C = 32 F, 100 C = 212 F.
# ==================================================================

def celsius_fahrenheit(c):
    return (c * 9 / 5) + 32


# ------ EJEMPLO FIJO (descomenta para probar) ------
# print(celsius_fahrenheit(100))   # 212.0
# print(celsius_fahrenheit(0))     # 32.0

# ------ VERSIÓN CON input() ------
c = float(input("Grados Celsius: "))
print(f"{c} °C = {celsius_fahrenheit(c)} °F")

# ==================================================================
# 06_contar_digitos.py
# EJERCICIO: Contar los dígitos de un número entero
# ==================================================================
# QUÉ HACE:
#   Define contar_digitos(n), que retorna cuántos dígitos tiene n.
#
# LO MÁS IMPORTANTE:
#   - n // 10 elimina el último dígito; se cuenta una vez por cada dígito eliminado.
#   - abs(n) permite manejar negativos.
#   - El 0 es un caso especial: tiene 1 dígito (el while no se ejecutaría).
# ==================================================================

def contar_digitos(n):
    n = abs(n)
    if n == 0:
        return 1
    cantidad = 0
    while n > 0:
        n //= 10
        cantidad += 1
    return cantidad


# ------ EJEMPLO FIJO (descomenta para probar) ------
# print(contar_digitos(12345))   # 5
# print(contar_digitos(0))       # 1
# print(contar_digitos(-907))    # 3

# ------ VERSIÓN CON input() ------
n = int(input("Ingrese un entero: "))
print("Cantidad de dígitos:", contar_digitos(n))

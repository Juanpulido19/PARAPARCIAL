# ==================================================================
# 09_potencia_sin_operador.py
# EJERCICIO: Potencia sin usar el operador **
# ==================================================================
# QUÉ HACE:
#   Define potencia(base, exponente) con multiplicaciones repetidas
#   (y una versión recursiva de apoyo).
#
# LO MÁS IMPORTANTE:
#   - base ** exponente = base multiplicada por sí misma 'exponente' veces.
#   - Se parte de resultado = 1 (cualquier número ^ 0 = 1).
#   - Exponente negativo: se calcula con abs(exponente) y al final se invierte 1/resultado.
#   - Versión recursiva: potencia(b, e) = b * potencia(b, e - 1), caso base e == 0.
# ==================================================================

def potencia(base, exponente):
    resultado = 1
    for _ in range(abs(exponente)):
        resultado *= base
    if exponente < 0:
        return 1 / resultado
    return resultado


def potencia_recursiva(base, exponente):
    # Solo para exponentes enteros >= 0
    if exponente == 0:                                   # caso base
        return 1
    return base * potencia_recursiva(base, exponente - 1)  # caso recursivo


# ------ EJEMPLO FIJO (descomenta para probar) ------
# print(potencia(2, 10))             # 1024
# print(potencia(2, -2))             # 0.25
# print(potencia_recursiva(3, 4))    # 81

# ------ VERSIÓN CON input() ------
base = float(input("Base: "))
exponente = int(input("Exponente (entero): "))
print("Resultado:", potencia(base, exponente))

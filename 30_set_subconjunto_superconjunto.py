# ==================================================================
# 30_set_subconjunto_superconjunto.py
# EJERCICIO: Subconjunto y superconjunto
# ==================================================================
# QUÉ HACE:
#   Determina si A está contenido en B (subconjunto) y/o si B contiene a A
#   (superconjunto).
#
# LO MÁS IMPORTANTE:
#   - A.issubset(B): todos los elementos de A están en B (también A <= B).
#   - B.issuperset(A): B contiene todos los elementos de A (también B >= A).
#   - Si no se cumple ninguna, se avisa.
# ==================================================================

# ---------- DATOS ----------
# EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
# A = {1, 2}
# B = {1, 2, 3, 4}

# VERSIÓN CON input():
A = set(int(v) for v in input("Conjunto A (ej: 1 2): ").split())
B = set(int(v) for v in input("Conjunto B (ej: 1 2 3 4): ").split())

# ---------- LÓGICA ----------
if A.issubset(B):
    print("A es subconjunto de B")
if B.issuperset(A):
    print("B es superconjunto de A")
if not A.issubset(B) and not B.issubset(A):
    print("Ninguno es subconjunto del otro")
elif B.issubset(A) and not A.issubset(B):
    print("B es subconjunto de A")

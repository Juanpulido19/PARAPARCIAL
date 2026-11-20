# ======================================================================
# ejercicios_python_completo.py
# TODOS los ejercicios (funciones, matrices y colecciones) en UN solo archivo.
# ======================================================================
# CÓMO USARLO
#   1) Menú interactivo:        python ejercicios_python_completo.py
#   2) Directo por número:      python ejercicios_python_completo.py 16
#   3) Buscar por palabra:      python ejercicios_python_completo.py primo
#   4) Ver qué hace uno:        python ejercicios_python_completo.py ?16
#   5) Lista de todos:          python ejercicios_python_completo.py lista
#   6) Desde otro archivo:      from ejercicios_python_completo import *
#                               ejercicio_16()
#
# DENTRO DEL MENÚ puedes escribir:
#   un número (ej: 16)  |  una palabra (ej: primo, matriz, diccionario)
#   ?número (ej: ?16) para ver qué hace  |  lista  |  salir
#
# EN CADA EJERCICIO: lo que está activo usa input(). El EJEMPLO FIJO está
# comentado dentro de cada función (descoméntalo y comenta las líneas de input).
#
# IMPORTANTE (examen): los ejercicios de MATRICES (11-15) piden NO usar
# funciones propias. Aquí van dentro de una función solo para poder llamarlos;
# si el examen lo exige, copia el contenido SIN la línea "def ejercicio_XX():"
# y quita la sangría (indentación) de 4 espacios.
# ======================================================================

import ast
import unicodedata


# ======================================================================
# BLOQUE 1: FUNCIONES REUTILIZABLES (ejercicios 01 a 10)
# Son las funciones 'de verdad' que piden esos enunciados.
# ======================================================================


# ----- Funciones del ejercicio 01: Factorial de un número -----
def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


# ----- Funciones del ejercicio 02: Calculadora con funciones independientes -----
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


# ----- Funciones del ejercicio 03: Determinar si un número es primo -----
def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# ----- Funciones del ejercicio 04: Convertir grados Celsius a Fahrenheit -----
def celsius_fahrenheit(c):
    return (c * 9 / 5) + 32


# ----- Funciones del ejercicio 05: Máximo de tres números -----
def maximo_de_tres(a, b, c):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor


# ----- Funciones del ejercicio 06: Contar los dígitos de un número entero -----
def contar_digitos(n):
    n = abs(n)
    if n == 0:
        return 1
    cantidad = 0
    while n > 0:
        n //= 10
        cantidad += 1
    return cantidad


# ----- Funciones del ejercicio 07: Invertir una cadena con recursión -----
def invertir(cadena, i=0):
    if i == len(cadena):                       # caso base
        return ""
    return invertir(cadena, i + 1) + cadena[i]  # caso recursivo


# Versión alternativa con slicing de recorte (por si el profesor la permite):
# def invertir(cadena):
#     if cadena == "":
#         return ""
#     return invertir(cadena[1:]) + cadena[0]


# ----- Funciones del ejercicio 08: Determinar si una cadena es palíndroma -----
def es_palindromo(cadena):
    inversa = invertir(cadena)
    for i in range(len(cadena)):
        if cadena[i] != inversa[i]:
            return False
    return True


# ----- Funciones del ejercicio 09: Potencia sin usar el operador ** -----
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


# ----- Funciones del ejercicio 10: Máximo común divisor (MCD) y mínimo común múltiplo (MCM) -----
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


def mcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // mcd(a, b)


# ======================================================================
# BLOQUE 2: UNA FUNCIÓN ejercicio_XX() POR CADA EJERCICIO
# ======================================================================


# ######################################################################
# SECCIÓN: FUNCIONES
# ######################################################################

# ==================================================================
# Se llama con: ejercicio_01()
# EJERCICIO: Factorial de un número
# ==================================================================
# QUÉ HACE:
#   Define factorial(n), que recibe un entero positivo y retorna n!
#   (n! = 1 * 2 * 3 * ... * n). Ejemplo: factorial(5) = 120.
#
# LO MÁS IMPORTANTE:
#   - Se parte de resultado = 1 (elemento neutro de la multiplicación).
#   - Se multiplica por 2, 3, ..., n con un for. Multiplicar por 1 no cambia nada.
#   - 0! y 1! valen 1: el for no se ejecuta y se retorna 1.
# ==================================================================

def ejercicio_01():
    # ------ EJEMPLO FIJO (descomenta para probar sin escribir datos) ------
    # print(factorial(5))   # Salida esperada: 120

    # ------ VERSIÓN CON input() ------
    n = int(input("Ingrese un entero positivo: "))
    if n < 0:
        print("El factorial no está definido para negativos")
    else:
        print(f"{n}! = {factorial(n)}")


# ==================================================================
# Se llama con: ejercicio_02()
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

def ejercicio_02():
    # ------ EJEMPLO FIJO (descomenta para probar) ------
    # print(sumar(8, 2))        # 10
    # print(restar(8, 2))       # 6
    # print(multiplicar(8, 2))  # 16
    # print(dividir(8, 2))      # 4.0
    # print(dividir(8, 0))      # Error: división por cero

    # ------ VERSIÓN CON input() ------
    calculadora()


# ==================================================================
# Se llama con: ejercicio_03()
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

def ejercicio_03():
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


# ==================================================================
# Se llama con: ejercicio_04()
# EJERCICIO: Convertir grados Celsius a Fahrenheit
# ==================================================================
# QUÉ HACE:
#   Define celsius_fahrenheit(c) aplicando la fórmula F = (C * 9/5) + 32.
#
# LO MÁS IMPORTANTE:
#   - Es solo aplicar la fórmula y retornar el resultado.
#   - Referencias para verificar: 0 C = 32 F, 100 C = 212 F.
# ==================================================================

def ejercicio_04():
    # ------ EJEMPLO FIJO (descomenta para probar) ------
    # print(celsius_fahrenheit(100))   # 212.0
    # print(celsius_fahrenheit(0))     # 32.0

    # ------ VERSIÓN CON input() ------
    c = float(input("Grados Celsius: "))
    print(f"{c} °C = {celsius_fahrenheit(c)} °F")


# ==================================================================
# Se llama con: ejercicio_05()
# EJERCICIO: Máximo de tres números
# ==================================================================
# QUÉ HACE:
#   Define maximo_de_tres(a, b, c) sin usar listas ni la función max().
#
# LO MÁS IMPORTANTE:
#   - Patrón 'mayor hasta ahora': se asume que a es el mayor.
#   - Si b o c lo superan, se reemplaza. Al final queda el mayor de los tres.
# ==================================================================

def ejercicio_05():
    # ------ EJEMPLO FIJO (descomenta para probar) ------
    # print(maximo_de_tres(3, 9, 5))   # 9

    # ------ VERSIÓN CON input() ------
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    c = float(input("Tercer número: "))
    print("El máximo es:", maximo_de_tres(a, b, c))


# ==================================================================
# Se llama con: ejercicio_06()
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

def ejercicio_06():
    # ------ EJEMPLO FIJO (descomenta para probar) ------
    # print(contar_digitos(12345))   # 5
    # print(contar_digitos(0))       # 1
    # print(contar_digitos(-907))    # 3

    # ------ VERSIÓN CON input() ------
    n = int(input("Ingrese un entero: "))
    print("Cantidad de dígitos:", contar_digitos(n))


# ==================================================================
# Se llama con: ejercicio_07()
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

def ejercicio_07():
    # ------ EJEMPLO FIJO (descomenta para probar) ------
    # print(invertir("hola"))   # aloh

    # ------ VERSIÓN CON input() ------
    texto = input("Ingrese una cadena: ")
    print("Invertida:", invertir(texto))


# ==================================================================
# Se llama con: ejercicio_08()
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

def ejercicio_08():
    # ------ EJEMPLO FIJO (descomenta para probar) ------
    # print(es_palindromo("reconocer"))   # True
    # print(es_palindromo("python"))      # False

    # ------ VERSIÓN CON input() ------
    texto = input("Ingrese una cadena: ")
    if es_palindromo(texto):
        print("Es palíndroma")
    else:
        print("No es palíndroma")


# ==================================================================
# Se llama con: ejercicio_09()
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

def ejercicio_09():
    # ------ EJEMPLO FIJO (descomenta para probar) ------
    # print(potencia(2, 10))             # 1024
    # print(potencia(2, -2))             # 0.25
    # print(potencia_recursiva(3, 4))    # 81

    # ------ VERSIÓN CON input() ------
    base = float(input("Base: "))
    exponente = int(input("Exponente (entero): "))
    print("Resultado:", potencia(base, exponente))


# ==================================================================
# Se llama con: ejercicio_10()
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

def ejercicio_10():
    # ------ EJEMPLO FIJO (descomenta para probar) ------
    # print(mcd(12, 18))   # 6
    # print(mcm(12, 18))   # 36

    # ------ VERSIÓN CON input() ------
    a = int(input("Primer entero: "))
    b = int(input("Segundo entero: "))
    print("MCD:", mcd(a, b))
    print("MCM:", mcm(a, b))



# ######################################################################
# SECCIÓN: MATRICES (sin funciones propias)
# ######################################################################

# ==================================================================
# Se llama con: ejercicio_11()
# EJERCICIO: Suma de dos matrices (valida dimensiones)
# ==================================================================
# QUÉ HACE:
#   Lee dos matrices, verifica que tengan las mismas dimensiones y,
#   si coinciden, imprime la suma elemento a elemento (A[i][j] + B[i][j]).
#   Sin funciones propias ni numpy (regla del enunciado).
#
# LO MÁS IMPORTANTE:
#   - Una matriz es una lista de listas: matriz[fila][columna].
#   - Para leer: un for externo crea cada fila y uno interno llena sus columnas.
#   - Validación: len(A) = filas, len(A[0]) = columnas. Si difieren, mensaje de error.
#   - f'{x:8.2f}' reserva 8 espacios por número: las columnas quedan alineadas.
# ==================================================================

def ejercicio_11():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta estas 2 líneas y comenta TODO el bloque con input):
    # A = [[1, 2], [3, 4]]
    # B = [[5, 6], [7, 8]]

    # VERSIÓN CON input():
    print("Matriz A")
    filas_a = int(input("Número de filas de A: "))
    columnas_a = int(input("Número de columnas de A: "))
    A = []
    for i in range(filas_a):
        fila = []
        for j in range(columnas_a):
            fila.append(float(input(f"A[{i}][{j}]: ")))
        A.append(fila)

    print("Matriz B")
    filas_b = int(input("Número de filas de B: "))
    columnas_b = int(input("Número de columnas de B: "))
    B = []
    for i in range(filas_b):
        fila = []
        for j in range(columnas_b):
            fila.append(float(input(f"B[{i}][{j}]: ")))
        B.append(fila)

    # ---------- LÓGICA ----------
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Error: las dimensiones no coinciden")
    else:
        C = []
        for i in range(len(A)):
            fila = []
            for j in range(len(A[0])):
                fila.append(A[i][j] + B[i][j])
            C.append(fila)

        print("Matriz resultante A + B:")
        for fila in C:
            for x in fila:
                print(f"{x:8.2f}", end="")
            print()


# ==================================================================
# Se llama con: ejercicio_12()
# EJERCICIO: Matriz transpuesta (n x m)
# ==================================================================
# QUÉ HACE:
#   Lee una matriz n x m (no tiene que ser cuadrada) e imprime la original
#   y su transpuesta (m x n).
#
# LO MÁS IMPORTANTE:
#   - Transponer = intercambiar filas por columnas: T[j][i] = M[i][j].
#   - Los bucles van 'invertidos': el externo recorre las COLUMNAS (j) y el
#   - interno las FILAS (i), tomando M[i][j].
# ==================================================================

def ejercicio_12():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta esta línea y comenta TODO el bloque con input):
    # M = [[1, 2, 3], [4, 5, 6]]

    # VERSIÓN CON input():
    filas = int(input("Número de filas: "))
    columnas = int(input("Número de columnas: "))
    M = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(float(input(f"M[{i}][{j}]: ")))
        M.append(fila)

    # ---------- LÓGICA ----------
    n = len(M)        # filas de la original
    m = len(M[0])     # columnas de la original

    T = []
    for j in range(m):          # la transpuesta tiene m filas
        fila = []
        for i in range(n):      # y n columnas
            fila.append(M[i][j])
        T.append(fila)

    print("Matriz original:")
    for fila in M:
        for x in fila:
            print(f"{x:8.2f}", end="")
        print()

    print("Matriz transpuesta:")
    for fila in T:
        for x in fila:
            print(f"{x:8.2f}", end="")
        print()


# ==================================================================
# Se llama con: ejercicio_13()
# EJERCICIO: Suma de la diagonal principal
# ==================================================================
# QUÉ HACE:
#   Lee una matriz cuadrada, la imprime y calcula la suma de su diagonal principal.
#   Si no es cuadrada, muestra un mensaje de error.
#
# LO MÁS IMPORTANTE:
#   - La diagonal principal son los elementos donde fila == columna: M[i][i].
#   - Por eso basta UN solo for (no hace falta doble for).
#   - Validación: número de filas == número de columnas.
# ==================================================================

def ejercicio_13():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta esta línea y comenta TODO el bloque con input):
    # M = [[1, 2], [3, 4]]

    # VERSIÓN CON input():
    filas = int(input("Número de filas: "))
    columnas = int(input("Número de columnas: "))
    M = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(float(input(f"M[{i}][{j}]: ")))
        M.append(fila)

    # ---------- LÓGICA ----------
    if len(M) != len(M[0]):
        print("Error: la matriz no es cuadrada")
    else:
        suma = 0
        for i in range(len(M)):
            suma += M[i][i]

        print("Matriz:")
        for fila in M:
            for x in fila:
                print(f"{x:8.2f}", end="")
            print()
        print("Suma de la diagonal principal:", suma)


# ==================================================================
# Se llama con: ejercicio_14()
# EJERCICIO: Mayor valor de una matriz y su posición
# ==================================================================
# QUÉ HACE:
#   Lee una matriz n x m, imprime la matriz, el valor máximo y la posición
#   (fila X, columna Y) donde aparece por primera vez.
#
# LO MÁS IMPORTANTE:
#   - Patrón 'mayor hasta ahora': se parte de M[0][0] y se recorre todo con doble for.
#   - Se usa > ESTRICTO (no >=): así, si el máximo se repite, se conserva la PRIMERA posición.
#   - Las posiciones se cuentan desde 0 (fila 0, columna 0 es la esquina superior izquierda).
# ==================================================================

def ejercicio_14():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta esta línea y comenta TODO el bloque con input):
    # M = [[1, 9, 3], [9, 2, 4]]

    # VERSIÓN CON input():
    filas = int(input("Número de filas: "))
    columnas = int(input("Número de columnas: "))
    M = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(float(input(f"M[{i}][{j}]: ")))
        M.append(fila)

    # ---------- LÓGICA ----------
    mayor = M[0][0]
    pos_fila = 0
    pos_columna = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] > mayor:
                mayor = M[i][j]
                pos_fila = i
                pos_columna = j

    print("Matriz:")
    for fila in M:
        for x in fila:
            print(f"{x:8.2f}", end="")
        print()
    print("Valor máximo:", mayor)
    print(f"Posición: fila {pos_fila}, columna {pos_columna}")


# ==================================================================
# Se llama con: ejercicio_15()
# EJERCICIO: Multiplicar una matriz por un escalar
# ==================================================================
# QUÉ HACE:
#   Lee una matriz n x m (validando que cada valor sea numérico) y un escalar,
#   e imprime la matriz original y el resultado de multiplicar cada elemento.
#
# LO MÁS IMPORTANTE:
#   - Cada elemento se multiplica por el escalar y se guarda en una matriz NUEVA.
#   - El escalar puede ser positivo, negativo, cero o decimal.
#   - try/except ValueError + while True: si float() falla, se vuelve a pedir el dato.
# ==================================================================

def ejercicio_15():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta estas 2 líneas y comenta TODO el bloque con input):
    # M = [[1, 2], [3, 4]]
    # escalar = 2

    # VERSIÓN CON input():
    filas = int(input("Número de filas: "))
    columnas = int(input("Número de columnas: "))
    M = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    valor = float(input(f"M[{i}][{j}]: "))
                    break
                except ValueError:
                    print("Debe ser un número, intente de nuevo")
            fila.append(valor)
        M.append(fila)

    while True:
        try:
            escalar = float(input("Escalar: "))
            break
        except ValueError:
            print("Debe ser un número, intente de nuevo")

    # ---------- LÓGICA ----------
    R = []
    for i in range(len(M)):
        fila = []
        for j in range(len(M[0])):
            fila.append(M[i][j] * escalar)
        R.append(fila)

    print("Matriz original:")
    for fila in M:
        for x in fila:
            print(f"{x:8.2f}", end="")
        print()

    print("Matriz resultante:")
    for fila in R:
        for x in fila:
            print(f"{x:8.2f}", end="")
        print()



# ######################################################################
# SECCIÓN: COLECCIONES: LISTAS Y MATRICES
# ######################################################################

# ==================================================================
# Se llama con: ejercicio_16()
# EJERCICIO: Números mayores que el promedio
# ==================================================================
# QUÉ HACE:
#   Lee una lista de números y muestra el promedio y los que lo superan.
#
# LO MÁS IMPORTANTE:
#   - promedio = sum(lista) / len(lista).
#   - Comprensión de listas: [x for x in lista if x > promedio] filtra.
#   - ast.literal_eval convierte '10' en int y '2.5' en float según corresponda.
#   - sorted() solo sirve para igualar la salida del enunciado; si no piden orden, quítalo.
# ==================================================================

def ejercicio_16():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta esta línea y comenta la de input):
    # numeros = [10, 5, 8, 3, 9]

    # VERSIÓN CON input():
    numeros = [ast.literal_eval(x) for x in input("Números separados por espacio: ").split()]

    # ---------- LÓGICA ----------
    promedio = sum(numeros) / len(numeros)
    mayores = sorted([x for x in numeros if x > promedio])
    print("Promedio:", promedio)
    print("Mayores que el promedio:", mayores)


# ==================================================================
# Se llama con: ejercicio_17()
# EJERCICIO: Producto escalar de dos listas
# ==================================================================
# QUÉ HACE:
#   Dadas dos listas del mismo tamaño, calcula su producto escalar.
#
# LO MÁS IMPORTANTE:
#   - Se multiplica posición por posición y se acumulan los resultados.
#   - Ejemplo: [1,2,3] . [4,5,6] = 1*4 + 2*5 + 3*6 = 32.
#   - Validar que tengan la misma longitud antes de calcular.
# ==================================================================

def ejercicio_17():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
    # A = [1, 2, 3]
    # B = [4, 5, 6]

    # VERSIÓN CON input():
    A = [ast.literal_eval(x) for x in input("Lista A: ").split()]
    B = [ast.literal_eval(x) for x in input("Lista B: ").split()]

    # ---------- LÓGICA ----------
    if len(A) != len(B):
        print("Error: las listas deben tener el mismo tamaño")
    else:
        total = 0
        for i in range(len(A)):
            total += A[i] * B[i]
        print("Producto escalar =", total)


# ==================================================================
# Se llama con: ejercicio_18()
# EJERCICIO: Matriz identidad de tamaño n x n
# ==================================================================
# QUÉ HACE:
#   Dado n, construye la matriz identidad: 1 en la diagonal y 0 en el resto.
#
# LO MÁS IMPORTANTE:
#   - La diagonal es donde fila == columna (i == j).
#   - Expresión condicional: 1 if i == j else 0.
# ==================================================================

def ejercicio_18():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta esta línea y comenta la de input):
    # n = 3

    # VERSIÓN CON input():
    n = int(input("n = "))

    # ---------- LÓGICA ----------
    identidad = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(1 if i == j else 0)
        identidad.append(fila)

    for fila in identidad:
        print(fila)


# ==================================================================
# Se llama con: ejercicio_19()
# EJERCICIO: Suma de dos matrices (listas de listas)
# ==================================================================
# QUÉ HACE:
#   Dadas dos matrices del mismo tamaño, calcula su suma elemento a elemento.
#
# LO MÁS IMPORTANTE:
#   - Cada posición (i, j) de la resultante es A[i][j] + B[i][j].
#   - Las matrices se ingresan escritas como en Python: [[1, 2], [3, 4]]
#   - (ast.literal_eval las convierte de texto a lista de listas).
# ==================================================================

def ejercicio_19():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
    # A = [[1, 2], [3, 4]]
    # B = [[5, 6], [7, 8]]

    # VERSIÓN CON input():
    A = ast.literal_eval(input("Matriz A (ej: [[1, 2], [3, 4]]): "))
    B = ast.literal_eval(input("Matriz B (ej: [[5, 6], [7, 8]]): "))

    # ---------- LÓGICA ----------
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Error: las dimensiones no coinciden")
    else:
        C = []
        for i in range(len(A)):
            fila = []
            for j in range(len(A[0])):
                fila.append(A[i][j] + B[i][j])
            C.append(fila)
        print(C)


# ==================================================================
# Se llama con: ejercicio_20()
# EJERCICIO: Transposición de una matriz (listas de listas)
# ==================================================================
# QUÉ HACE:
#   Genera la matriz transpuesta de una matriz ingresada por el usuario.
#
# LO MÁS IMPORTANTE:
#   - A[i][j] pasa a T[j][i]: las columnas de A son las filas de T.
#   - Bucle externo sobre columnas (j), interno sobre filas (i).
#   - Se ingresa como texto de Python: [[1, 2, 3], [4, 5, 6]].
# ==================================================================

def ejercicio_20():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta esta línea y comenta la de input):
    # A = [[1, 2, 3], [4, 5, 6]]

    # VERSIÓN CON input():
    A = ast.literal_eval(input("Matriz (ej: [[1, 2, 3], [4, 5, 6]]): "))

    # ---------- LÓGICA ----------
    T = []
    for j in range(len(A[0])):
        fila = []
        for i in range(len(A)):
            fila.append(A[i][j])
        T.append(fila)
    print(T)



# ######################################################################
# SECCIÓN: COLECCIONES: TUPLAS
# ######################################################################

# ==================================================================
# Se llama con: ejercicio_21()
# EJERCICIO: Lista a tupla sin duplicados
# ==================================================================
# QUÉ HACE:
#   Convierte una lista de elementos en una tupla sin repetidos.
#
# LO MÁS IMPORTANTE:
#   - set() elimina duplicados y tuple() lo vuelve tupla.
#   - CUIDADO: un set NO conserva el orden. Si piden mantener el orden usa
#   - tuple(dict.fromkeys(lista)).
# ==================================================================

def ejercicio_21():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta esta línea y comenta la de input):
    # lista = ["rojo", "azul", "rojo", "verde"]

    # VERSIÓN CON input():
    lista = input("Elementos separados por espacio: ").split()

    # ---------- LÓGICA ----------
    sin_duplicados = tuple(set(lista))
    print(sin_duplicados)

    # Versión que conserva el orden original:
    # print(tuple(dict.fromkeys(lista)))


# ==================================================================
# Se llama con: ejercicio_22()
# EJERCICIO: Coordenadas dentro de un rango
# ==================================================================
# QUÉ HACE:
#   Dada una coordenada (x, y) en una tupla, verifica si está dentro de un rango.
#
# LO MÁS IMPORTANTE:
#   - Se desempaqueta la tupla: x, y = coordenada.
#   - Comparación encadenada: minimo <= x <= maximo (válida en Python).
#   - Ambas coordenadas deben cumplir el rango (and).
# ==================================================================

def ejercicio_22():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
    # coordenada = (4, 6)
    # minimo, maximo = 0, 10

    # VERSIÓN CON input():
    coordenada = tuple(int(v) for v in input("Coordenada x y (ej: 4 6): ").split())
    minimo, maximo = (int(v) for v in input("Rango mínimo y máximo (ej: 0 10): ").split())

    # ---------- LÓGICA ----------
    x, y = coordenada
    if minimo <= x <= maximo and minimo <= y <= maximo:
        print("Dentro del rango")
    else:
        print("Fuera del rango")


# ==================================================================
# Se llama con: ejercicio_23()
# EJERCICIO: Empaquetar y desempaquetar datos en una tupla
# ==================================================================
# QUÉ HACE:
#   Guarda (nombre, edad, país) en una tupla y muestra cada dato por separado.
#
# LO MÁS IMPORTANTE:
#   - Empaquetar: datos = (a, b, c).
#   - Desempaquetar: nombre, edad, pais = datos (el orden importa y la cantidad
#   - de variables debe coincidir con la de elementos).
# ==================================================================

def ejercicio_23():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta esta línea y comenta TODO el bloque con input):
    # datos = ("Ana", 23, "Colombia")

    # VERSIÓN CON input():
    nombre_in = input("Nombre: ")
    edad_in = int(input("Edad: "))
    pais_in = input("País: ")
    datos = (nombre_in, edad_in, pais_in)      # empaquetar

    # ---------- LÓGICA ----------
    nombre, edad, pais = datos                 # desempaquetar
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("País:", pais)


# ==================================================================
# Se llama con: ejercicio_24()
# EJERCICIO: Comparación de tuplas
# ==================================================================
# QUÉ HACE:
#   Dadas dos tuplas numéricas, determina cuál es mayor.
#
# LO MÁS IMPORTANTE:
#   - Python compara tuplas elemento a elemento (orden lexicográfico) y se detiene
#   - en el primer elemento distinto. (3,4,5) vs (3,4,2): 3=3, 4=4, 5>2 -> gana la primera.
#   - Se pueden usar directamente los operadores >, < e ==.
# ==================================================================

def ejercicio_24():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
    # t1 = (3, 4, 5)
    # t2 = (3, 4, 2)

    # VERSIÓN CON input():
    t1 = tuple(int(v) for v in input("Primera tupla (ej: 3 4 5): ").split())
    t2 = tuple(int(v) for v in input("Segunda tupla (ej: 3 4 2): ").split())

    # ---------- LÓGICA ----------
    if t1 > t2:
        print("La primera tupla es mayor.")
    elif t1 < t2:
        print("La segunda tupla es mayor.")
    else:
        print("Las tuplas son iguales.")


# ==================================================================
# Se llama con: ejercicio_25()
# EJERCICIO: Suma y promedio de una tupla
# ==================================================================
# QUÉ HACE:
#   Dada una tupla de números, calcula su suma y su promedio.
#
# LO MÁS IMPORTANTE:
#   - sum(tupla) suma todos los elementos y len(tupla) los cuenta.
#   - promedio = sum / len.
# ==================================================================

def ejercicio_25():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta esta línea y comenta la de input):
    # t = (10, 20, 30, 40)

    # VERSIÓN CON input():
    t = tuple(ast.literal_eval(v) for v in input("Números separados por espacio: ").split())

    # ---------- LÓGICA ----------
    print("Suma =", sum(t))
    print("Promedio =", sum(t) / len(t))



# ######################################################################
# SECCIÓN: COLECCIONES: SETS
# ######################################################################

# ==================================================================
# Se llama con: ejercicio_26()
# EJERCICIO: Unión y diferencia entre conjuntos
# ==================================================================
# QUÉ HACE:
#   Dados dos conjuntos A y B, muestra su unión y la diferencia A - B.
#
# LO MÁS IMPORTANTE:
#   - Unión: A | B (todos los elementos, sin repetir).
#   - Diferencia: A - B (lo que está en A pero NO en B). Importa el orden: A-B != B-A.
# ==================================================================

def ejercicio_26():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
    # A = {1, 2, 3}
    # B = {3, 4, 5}

    # VERSIÓN CON input():
    A = set(int(v) for v in input("Conjunto A (ej: 1 2 3): ").split())
    B = set(int(v) for v in input("Conjunto B (ej: 3 4 5): ").split())

    # ---------- LÓGICA ----------
    print("Unión:", A | B)
    print("Diferencia:", A - B)


# ==================================================================
# Se llama con: ejercicio_27()
# EJERCICIO: Palabras únicas de una frase
# ==================================================================
# QUÉ HACE:
#   Dada una frase, muestra sus palabras sin repetir.
#
# LO MÁS IMPORTANTE:
#   - split() separa la frase en palabras y set() elimina las repetidas.
#   - El set no garantiza orden.
# ==================================================================

def ejercicio_27():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta esta línea y comenta la de input):
    # frase = "hola mundo hola python"

    # VERSIÓN CON input():
    frase = input("Frase: ")

    # ---------- LÓGICA ----------
    print(set(frase.split()))


# ==================================================================
# Se llama con: ejercicio_28()
# EJERCICIO: Intersección de números pares
# ==================================================================
# QUÉ HACE:
#   Dadas dos listas de números, muestra los pares que están en ambas.
#
# LO MÁS IMPORTANTE:
#   - Se convierten a set y se usa & (intersección) para los comunes.
#   - Luego se filtran los pares con x % 2 == 0.
# ==================================================================

def ejercicio_28():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
    # A = [2, 4, 6, 8]
    # B = [4, 5, 6, 9]

    # VERSIÓN CON input():
    A = [ast.literal_eval(v) for v in input("Lista A (ej: 2 4 6 8): ").split()]
    B = [ast.literal_eval(v) for v in input("Lista B (ej: 4 5 6 9): ").split()]

    # ---------- LÓGICA ----------
    comunes = set(A) & set(B)
    pares_comunes = {x for x in comunes if x % 2 == 0}
    print(pares_comunes)


# ==================================================================
# Se llama con: ejercicio_29()
# EJERCICIO: Diferencia simétrica de dos conjuntos
# ==================================================================
# QUÉ HACE:
#   Muestra los elementos que están en uno de los conjuntos pero no en ambos.
#
# LO MÁS IMPORTANTE:
#   - Operador ^ o método A.symmetric_difference(B).
#   - Equivale a (A | B) - (A & B).
# ==================================================================

def ejercicio_29():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
    # A = {1, 2, 3}
    # B = {3, 4, 5}

    # VERSIÓN CON input():
    A = set(int(v) for v in input("Conjunto A (ej: 1 2 3): ").split())
    B = set(int(v) for v in input("Conjunto B (ej: 3 4 5): ").split())

    # ---------- LÓGICA ----------
    print(A ^ B)


# ==================================================================
# Se llama con: ejercicio_30()
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

def ejercicio_30():
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



# ######################################################################
# SECCIÓN: COLECCIONES: DICCIONARIOS
# ######################################################################

# ==================================================================
# Se llama con: ejercicio_31()
# EJERCICIO: Agenda telefónica
# ==================================================================
# QUÉ HACE:
#   Pide nombres y teléfonos y los guarda en un diccionario hasta escribir 'fin'.
#
# LO MÁS IMPORTANTE:
#   - Clave = nombre, valor = teléfono.
#   - while True + break cuando el usuario escribe 'fin'.
#   - partition('-') separa 'Juan - 123' en nombre y teléfono; strip() quita espacios.
# ==================================================================

def ejercicio_31():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta esta línea, comenta TODO el bloque con input y salta a LÓGICA):
    # agenda = {"Juan": "123", "Ana": "456"}

    # VERSIÓN CON input():
    agenda = {}
    while True:
        entrada = input("Nombre - teléfono (o 'fin'): ")
        if entrada.strip().lower() == "fin":
            break
        nombre, _, telefono = entrada.partition("-")
        agenda[nombre.strip()] = telefono.strip()

    # ---------- LÓGICA ----------
    print(agenda)


# ==================================================================
# Se llama con: ejercicio_32()
# EJERCICIO: Contador de palabras
# ==================================================================
# QUÉ HACE:
#   Cuenta cuántas veces aparece cada palabra de una frase.
#
# LO MÁS IMPORTANTE:
#   - Diccionario donde clave = palabra y valor = frecuencia.
#   - Si la palabra ya existe se suma 1; si no, se crea con valor 1.
#   - Atajo: conteo[p] = conteo.get(p, 0) + 1 (get devuelve 0 si no existe).
# ==================================================================

def ejercicio_32():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta esta línea y comenta la de input):
    # frase = "hola mundo hola"

    # VERSIÓN CON input():
    frase = input("Frase: ")

    # ---------- LÓGICA ----------
    conteo = {}
    for palabra in frase.split():
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    print(conteo)


# ==================================================================
# Se llama con: ejercicio_33()
# EJERCICIO: Promedio de calificaciones
# ==================================================================
# QUÉ HACE:
#   Guarda nombre -> nota y calcula el promedio general.
#
# LO MÁS IMPORTANTE:
#   - notas.values() da solo las notas; promedio = sum(...) / len(...).
#   - Se guarda float(nota) para poder calcular.
#   - Se controla el caso de diccionario vacío para evitar división por cero.
# ==================================================================

def ejercicio_33():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta esta línea, comenta TODO el bloque con input y salta a LÓGICA):
    # notas = {"Ana": 4.0, "Luis": 3.5, "Sofía": 4.5}

    # VERSIÓN CON input():
    notas = {}
    while True:
        entrada = input("Nombre: nota (o 'fin'): ")
        if entrada.strip().lower() == "fin":
            break
        nombre, _, nota = entrada.partition(":")
        notas[nombre.strip()] = float(nota)

    # ---------- LÓGICA ----------
    if len(notas) == 0:
        print("No se ingresaron notas")
    else:
        print("Promedio general:", sum(notas.values()) / len(notas))


# ==================================================================
# Se llama con: ejercicio_34()
# EJERCICIO: Diccionario invertido (valor -> clave)
# ==================================================================
# QUÉ HACE:
#   Invierte un diccionario clave -> valor a valor -> clave.
#
# LO MÁS IMPORTANTE:
#   - Comprensión de diccionarios: {v: k for k, v in dic.items()}.
#   - items() entrega pares (clave, valor).
#   - CUIDADO: si hay valores repetidos se pierden claves (las claves no se duplican).
# ==================================================================

def ejercicio_34():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta esta línea y comenta la de input):
    # dic = {"a": 1, "b": 2, "c": 3}

    # VERSIÓN CON input():
    dic = ast.literal_eval(input("Diccionario (ej: {'a': 1, 'b': 2}): "))

    # ---------- LÓGICA ----------
    invertido = {v: k for k, v in dic.items()}
    print(invertido)


# ==================================================================
# Se llama con: ejercicio_35()
# EJERCICIO: Fusionar dos diccionarios
# ==================================================================
# QUÉ HACE:
#   Combina dos diccionarios en uno. Si hay claves repetidas, el segundo
#   sobrescribe al primero.
#
# LO MÁS IMPORTANTE:
#   - Operador A | B (Python 3.9+) crea uno NUEVO; el de la derecha gana en repetidas.
#   - A.update(B) hace lo mismo pero MODIFICA A (no crea uno nuevo).
#   - Alternativa para versiones viejas: {**A, **B}.
# ==================================================================

def ejercicio_35():
    # ---------- DATOS ----------
    # EJEMPLO FIJO (descomenta estas 2 líneas y comenta las de input):
    # A = {"x": 1, "y": 2}
    # B = {"y": 10, "z": 3}

    # VERSIÓN CON input():
    A = ast.literal_eval(input("Diccionario A (ej: {'x': 1, 'y': 2}): "))
    B = ast.literal_eval(input("Diccionario B (ej: {'y': 10, 'z': 3}): "))

    # ---------- LÓGICA ----------
    fusion = A | B          # alternativa: {**A, **B}
    print(fusion)


# ======================================================================
# BLOQUE 3: REGISTRO, BUSCADOR Y MENÚ
# ======================================================================

REGISTRO = {
    1: {'titulo': 'Factorial de un número', 'func': ejercicio_01, 'ayuda': 'QUÉ HACE:\n  Define factorial(n), que recibe un entero positivo y retorna n!\n  (n! = 1 * 2 * 3 * ... * n). Ejemplo: factorial(5) = 120.\n\nLO MÁS IMPORTANTE:\n  - Se parte de resultado = 1 (elemento neutro de la multiplicación).\n  - Se multiplica por 2, 3, ..., n con un for. Multiplicar por 1 no cambia nada.\n  - 0! y 1! valen 1: el for no se ejecuta y se retorna 1.'},
    2: {'titulo': 'Calculadora con funciones independientes', 'func': ejercicio_02, 'ayuda': 'QUÉ HACE:\n  Cuatro funciones independientes (sumar, restar, multiplicar, dividir)\n  y una función calculadora() que pide los datos y llama a la correcta.\n\nLO MÁS IMPORTANTE:\n  - Cada operación vive en su propia función: reutilizable y fácil de probar.\n  - calculadora() solo decide cuál llamar según el símbolo ingresado.\n  - dividir() debe controlar b == 0 para no caer en ZeroDivisionError.'},
    3: {'titulo': 'Determinar si un número es primo', 'func': ejercicio_03, 'ayuda': 'QUÉ HACE:\n  Define es_primo(n), que retorna True si n es primo y False si no.\n\nLO MÁS IMPORTANTE:\n  - Un primo solo es divisible por 1 y por sí mismo. Los menores que 2 NO son primos.\n  - Basta probar divisores desde 2 hasta la raíz cuadrada de n.\n  - i * i <= n equivale a i <= raíz(n) sin necesidad de importar math.\n  - Si algún i divide a n (n % i == 0), se retorna False de inmediato.'},
    4: {'titulo': 'Convertir grados Celsius a Fahrenheit', 'func': ejercicio_04, 'ayuda': 'QUÉ HACE:\n  Define celsius_fahrenheit(c) aplicando la fórmula F = (C * 9/5) + 32.\n\nLO MÁS IMPORTANTE:\n  - Es solo aplicar la fórmula y retornar el resultado.\n  - Referencias para verificar: 0 C = 32 F, 100 C = 212 F.'},
    5: {'titulo': 'Máximo de tres números', 'func': ejercicio_05, 'ayuda': "QUÉ HACE:\n  Define maximo_de_tres(a, b, c) sin usar listas ni la función max().\n\nLO MÁS IMPORTANTE:\n  - Patrón 'mayor hasta ahora': se asume que a es el mayor.\n  - Si b o c lo superan, se reemplaza. Al final queda el mayor de los tres."},
    6: {'titulo': 'Contar los dígitos de un número entero', 'func': ejercicio_06, 'ayuda': 'QUÉ HACE:\n  Define contar_digitos(n), que retorna cuántos dígitos tiene n.\n\nLO MÁS IMPORTANTE:\n  - n // 10 elimina el último dígito; se cuenta una vez por cada dígito eliminado.\n  - abs(n) permite manejar negativos.\n  - El 0 es un caso especial: tiene 1 dígito (el while no se ejecutaría).'},
    7: {'titulo': 'Invertir una cadena con recursión', 'func': ejercicio_07, 'ayuda': "QUÉ HACE:\n  Define invertir(cadena), que retorna la cadena al revés usando RECURSIÓN,\n  sin slicing [::-1] ni estructuras avanzadas.\n\nLO MÁS IMPORTANTE:\n  - CASO BASE: cuando el índice i llega al final, se retorna cadena vacía.\n  - CASO RECURSIVO: primero se invierte el resto (desde i+1) y luego se pone\n  - el carácter actual AL FINAL. Así el primer carácter queda de último.\n  - Seguimiento: invertir('hola') -> invertir('ola') + 'h' -> ... -> 'aloh'.\n  - Esta versión no usa slicing de ningún tipo (el parámetro i es opcional)."},
    8: {'titulo': 'Determinar si una cadena es palíndroma', 'func': ejercicio_08, 'ayuda': "QUÉ HACE:\n  Define es_palindromo(cadena), que retorna True si se lee igual al derecho\n  y al revés. Compara carácter por carácter usando la función invertir.\n\nLO MÁS IMPORTANTE:\n  - Se invierte la cadena y se compara posición por posición con la original.\n  - Si encuentra una diferencia retorna False; si termina el for, es palíndroma.\n  - Esta comparación distingue mayúsculas y espacios. Para ignorarlos:\n  - cadena = cadena.replace(' ', '').lower() al inicio de la función."},
    9: {'titulo': 'Potencia sin usar el operador **', 'func': ejercicio_09, 'ayuda': "QUÉ HACE:\n  Define potencia(base, exponente) con multiplicaciones repetidas\n  (y una versión recursiva de apoyo).\n\nLO MÁS IMPORTANTE:\n  - base ** exponente = base multiplicada por sí misma 'exponente' veces.\n  - Se parte de resultado = 1 (cualquier número ^ 0 = 1).\n  - Exponente negativo: se calcula con abs(exponente) y al final se invierte 1/resultado.\n  - Versión recursiva: potencia(b, e) = b * potencia(b, e - 1), caso base e == 0."},
    10: {'titulo': 'Máximo común divisor (MCD) y mínimo común múltiplo (MCM)', 'func': ejercicio_10, 'ayuda': 'QUÉ HACE:\n  mcd(a, b) usa el algoritmo de Euclides.\n  mcm(a, b) usa la fórmula mcm = |a * b| / mcd(a, b).\n\nLO MÁS IMPORTANTE:\n  - Euclides: se reemplaza (a, b) por (b, a % b) hasta que b sea 0; el MCD queda en a.\n  - Ejemplo: mcd(12, 18) -> (18, 12) -> (12, 6) -> (6, 0) => MCD = 6.\n  - mcm(12, 18) = 12 * 18 / 6 = 36.\n  - Se usa // (división entera) para que el MCM sea entero.'},
    11: {'titulo': 'Suma de dos matrices (valida dimensiones)', 'func': ejercicio_11, 'ayuda': "QUÉ HACE:\n  Lee dos matrices, verifica que tengan las mismas dimensiones y,\n  si coinciden, imprime la suma elemento a elemento (A[i][j] + B[i][j]).\n  Sin funciones propias ni numpy (regla del enunciado).\n\nLO MÁS IMPORTANTE:\n  - Una matriz es una lista de listas: matriz[fila][columna].\n  - Para leer: un for externo crea cada fila y uno interno llena sus columnas.\n  - Validación: len(A) = filas, len(A[0]) = columnas. Si difieren, mensaje de error.\n  - f'{x:8.2f}' reserva 8 espacios por número: las columnas quedan alineadas."},
    12: {'titulo': 'Matriz transpuesta (n x m)', 'func': ejercicio_12, 'ayuda': "QUÉ HACE:\n  Lee una matriz n x m (no tiene que ser cuadrada) e imprime la original\n  y su transpuesta (m x n).\n\nLO MÁS IMPORTANTE:\n  - Transponer = intercambiar filas por columnas: T[j][i] = M[i][j].\n  - Los bucles van 'invertidos': el externo recorre las COLUMNAS (j) y el\n  - interno las FILAS (i), tomando M[i][j]."},
    13: {'titulo': 'Suma de la diagonal principal', 'func': ejercicio_13, 'ayuda': 'QUÉ HACE:\n  Lee una matriz cuadrada, la imprime y calcula la suma de su diagonal principal.\n  Si no es cuadrada, muestra un mensaje de error.\n\nLO MÁS IMPORTANTE:\n  - La diagonal principal son los elementos donde fila == columna: M[i][i].\n  - Por eso basta UN solo for (no hace falta doble for).\n  - Validación: número de filas == número de columnas.'},
    14: {'titulo': 'Mayor valor de una matriz y su posición', 'func': ejercicio_14, 'ayuda': "QUÉ HACE:\n  Lee una matriz n x m, imprime la matriz, el valor máximo y la posición\n  (fila X, columna Y) donde aparece por primera vez.\n\nLO MÁS IMPORTANTE:\n  - Patrón 'mayor hasta ahora': se parte de M[0][0] y se recorre todo con doble for.\n  - Se usa > ESTRICTO (no >=): así, si el máximo se repite, se conserva la PRIMERA posición.\n  - Las posiciones se cuentan desde 0 (fila 0, columna 0 es la esquina superior izquierda)."},
    15: {'titulo': 'Multiplicar una matriz por un escalar', 'func': ejercicio_15, 'ayuda': 'QUÉ HACE:\n  Lee una matriz n x m (validando que cada valor sea numérico) y un escalar,\n  e imprime la matriz original y el resultado de multiplicar cada elemento.\n\nLO MÁS IMPORTANTE:\n  - Cada elemento se multiplica por el escalar y se guarda en una matriz NUEVA.\n  - El escalar puede ser positivo, negativo, cero o decimal.\n  - try/except ValueError + while True: si float() falla, se vuelve a pedir el dato.'},
    16: {'titulo': 'Números mayores que el promedio', 'func': ejercicio_16, 'ayuda': "QUÉ HACE:\n  Lee una lista de números y muestra el promedio y los que lo superan.\n\nLO MÁS IMPORTANTE:\n  - promedio = sum(lista) / len(lista).\n  - Comprensión de listas: [x for x in lista if x > promedio] filtra.\n  - ast.literal_eval convierte '10' en int y '2.5' en float según corresponda.\n  - sorted() solo sirve para igualar la salida del enunciado; si no piden orden, quítalo."},
    17: {'titulo': 'Producto escalar de dos listas', 'func': ejercicio_17, 'ayuda': 'QUÉ HACE:\n  Dadas dos listas del mismo tamaño, calcula su producto escalar.\n\nLO MÁS IMPORTANTE:\n  - Se multiplica posición por posición y se acumulan los resultados.\n  - Ejemplo: [1,2,3] . [4,5,6] = 1*4 + 2*5 + 3*6 = 32.\n  - Validar que tengan la misma longitud antes de calcular.'},
    18: {'titulo': 'Matriz identidad de tamaño n x n', 'func': ejercicio_18, 'ayuda': 'QUÉ HACE:\n  Dado n, construye la matriz identidad: 1 en la diagonal y 0 en el resto.\n\nLO MÁS IMPORTANTE:\n  - La diagonal es donde fila == columna (i == j).\n  - Expresión condicional: 1 if i == j else 0.'},
    19: {'titulo': 'Suma de dos matrices (listas de listas)', 'func': ejercicio_19, 'ayuda': 'QUÉ HACE:\n  Dadas dos matrices del mismo tamaño, calcula su suma elemento a elemento.\n\nLO MÁS IMPORTANTE:\n  - Cada posición (i, j) de la resultante es A[i][j] + B[i][j].\n  - Las matrices se ingresan escritas como en Python: [[1, 2], [3, 4]]\n  - (ast.literal_eval las convierte de texto a lista de listas).'},
    20: {'titulo': 'Transposición de una matriz (listas de listas)', 'func': ejercicio_20, 'ayuda': 'QUÉ HACE:\n  Genera la matriz transpuesta de una matriz ingresada por el usuario.\n\nLO MÁS IMPORTANTE:\n  - A[i][j] pasa a T[j][i]: las columnas de A son las filas de T.\n  - Bucle externo sobre columnas (j), interno sobre filas (i).\n  - Se ingresa como texto de Python: [[1, 2, 3], [4, 5, 6]].'},
    21: {'titulo': 'Lista a tupla sin duplicados', 'func': ejercicio_21, 'ayuda': 'QUÉ HACE:\n  Convierte una lista de elementos en una tupla sin repetidos.\n\nLO MÁS IMPORTANTE:\n  - set() elimina duplicados y tuple() lo vuelve tupla.\n  - CUIDADO: un set NO conserva el orden. Si piden mantener el orden usa\n  - tuple(dict.fromkeys(lista)).'},
    22: {'titulo': 'Coordenadas dentro de un rango', 'func': ejercicio_22, 'ayuda': 'QUÉ HACE:\n  Dada una coordenada (x, y) en una tupla, verifica si está dentro de un rango.\n\nLO MÁS IMPORTANTE:\n  - Se desempaqueta la tupla: x, y = coordenada.\n  - Comparación encadenada: minimo <= x <= maximo (válida en Python).\n  - Ambas coordenadas deben cumplir el rango (and).'},
    23: {'titulo': 'Empaquetar y desempaquetar datos en una tupla', 'func': ejercicio_23, 'ayuda': 'QUÉ HACE:\n  Guarda (nombre, edad, país) en una tupla y muestra cada dato por separado.\n\nLO MÁS IMPORTANTE:\n  - Empaquetar: datos = (a, b, c).\n  - Desempaquetar: nombre, edad, pais = datos (el orden importa y la cantidad\n  - de variables debe coincidir con la de elementos).'},
    24: {'titulo': 'Comparación de tuplas', 'func': ejercicio_24, 'ayuda': 'QUÉ HACE:\n  Dadas dos tuplas numéricas, determina cuál es mayor.\n\nLO MÁS IMPORTANTE:\n  - Python compara tuplas elemento a elemento (orden lexicográfico) y se detiene\n  - en el primer elemento distinto. (3,4,5) vs (3,4,2): 3=3, 4=4, 5>2 -> gana la primera.\n  - Se pueden usar directamente los operadores >, < e ==.'},
    25: {'titulo': 'Suma y promedio de una tupla', 'func': ejercicio_25, 'ayuda': 'QUÉ HACE:\n  Dada una tupla de números, calcula su suma y su promedio.\n\nLO MÁS IMPORTANTE:\n  - sum(tupla) suma todos los elementos y len(tupla) los cuenta.\n  - promedio = sum / len.'},
    26: {'titulo': 'Unión y diferencia entre conjuntos', 'func': ejercicio_26, 'ayuda': 'QUÉ HACE:\n  Dados dos conjuntos A y B, muestra su unión y la diferencia A - B.\n\nLO MÁS IMPORTANTE:\n  - Unión: A | B (todos los elementos, sin repetir).\n  - Diferencia: A - B (lo que está en A pero NO en B). Importa el orden: A-B != B-A.'},
    27: {'titulo': 'Palabras únicas de una frase', 'func': ejercicio_27, 'ayuda': 'QUÉ HACE:\n  Dada una frase, muestra sus palabras sin repetir.\n\nLO MÁS IMPORTANTE:\n  - split() separa la frase en palabras y set() elimina las repetidas.\n  - El set no garantiza orden.'},
    28: {'titulo': 'Intersección de números pares', 'func': ejercicio_28, 'ayuda': 'QUÉ HACE:\n  Dadas dos listas de números, muestra los pares que están en ambas.\n\nLO MÁS IMPORTANTE:\n  - Se convierten a set y se usa & (intersección) para los comunes.\n  - Luego se filtran los pares con x % 2 == 0.'},
    29: {'titulo': 'Diferencia simétrica de dos conjuntos', 'func': ejercicio_29, 'ayuda': 'QUÉ HACE:\n  Muestra los elementos que están en uno de los conjuntos pero no en ambos.\n\nLO MÁS IMPORTANTE:\n  - Operador ^ o método A.symmetric_difference(B).\n  - Equivale a (A | B) - (A & B).'},
    30: {'titulo': 'Subconjunto y superconjunto', 'func': ejercicio_30, 'ayuda': 'QUÉ HACE:\n  Determina si A está contenido en B (subconjunto) y/o si B contiene a A\n  (superconjunto).\n\nLO MÁS IMPORTANTE:\n  - A.issubset(B): todos los elementos de A están en B (también A <= B).\n  - B.issuperset(A): B contiene todos los elementos de A (también B >= A).\n  - Si no se cumple ninguna, se avisa.'},
    31: {'titulo': 'Agenda telefónica', 'func': ejercicio_31, 'ayuda': "QUÉ HACE:\n  Pide nombres y teléfonos y los guarda en un diccionario hasta escribir 'fin'.\n\nLO MÁS IMPORTANTE:\n  - Clave = nombre, valor = teléfono.\n  - while True + break cuando el usuario escribe 'fin'.\n  - partition('-') separa 'Juan - 123' en nombre y teléfono; strip() quita espacios."},
    32: {'titulo': 'Contador de palabras', 'func': ejercicio_32, 'ayuda': 'QUÉ HACE:\n  Cuenta cuántas veces aparece cada palabra de una frase.\n\nLO MÁS IMPORTANTE:\n  - Diccionario donde clave = palabra y valor = frecuencia.\n  - Si la palabra ya existe se suma 1; si no, se crea con valor 1.\n  - Atajo: conteo[p] = conteo.get(p, 0) + 1 (get devuelve 0 si no existe).'},
    33: {'titulo': 'Promedio de calificaciones', 'func': ejercicio_33, 'ayuda': 'QUÉ HACE:\n  Guarda nombre -> nota y calcula el promedio general.\n\nLO MÁS IMPORTANTE:\n  - notas.values() da solo las notas; promedio = sum(...) / len(...).\n  - Se guarda float(nota) para poder calcular.\n  - Se controla el caso de diccionario vacío para evitar división por cero.'},
    34: {'titulo': 'Diccionario invertido (valor -> clave)', 'func': ejercicio_34, 'ayuda': 'QUÉ HACE:\n  Invierte un diccionario clave -> valor a valor -> clave.\n\nLO MÁS IMPORTANTE:\n  - Comprensión de diccionarios: {v: k for k, v in dic.items()}.\n  - items() entrega pares (clave, valor).\n  - CUIDADO: si hay valores repetidos se pierden claves (las claves no se duplican).'},
    35: {'titulo': 'Fusionar dos diccionarios', 'func': ejercicio_35, 'ayuda': 'QUÉ HACE:\n  Combina dos diccionarios en uno. Si hay claves repetidas, el segundo\n  sobrescribe al primero.\n\nLO MÁS IMPORTANTE:\n  - Operador A | B (Python 3.9+) crea uno NUEVO; el de la derecha gana en repetidas.\n  - A.update(B) hace lo mismo pero MODIFICA A (no crea uno nuevo).\n  - Alternativa para versiones viejas: {**A, **B}.'},
}


def _normalizar(texto):
    """Minúsculas y sin tildes, para buscar sin preocuparse por acentos."""
    texto = unicodedata.normalize("NFD", texto.lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")


for _d in REGISTRO.values():
    _d["titulo_norm"] = _normalizar(_d["titulo"])
    _d["indice"] = _normalizar(_d["titulo"] + " " + _d["ayuda"])


def listar():
    """Muestra todos los ejercicios con su número."""
    for n, d in REGISTRO.items():
        print(f"  {n:02d}  {d['titulo']}")


def ejecutar(n):
    """Ejecuta el ejercicio número n."""
    print(f"\n=== Ejercicio {n:02d}: {REGISTRO[n]['titulo']} ===\n")
    REGISTRO[n]["func"]()


def buscar(texto):
    """Devuelve los números de ejercicios que contienen TODAS las palabras.
    Primero busca en el título; si no hay resultados, en toda la descripción."""
    palabras = _normalizar(texto).split()
    en_titulo = [n for n, d in REGISTRO.items()
                 if all(p in d["titulo_norm"] for p in palabras)]
    if en_titulo:
        return en_titulo
    return [n for n, d in REGISTRO.items() if all(p in d["indice"] for p in palabras)]


def _procesar(entrada):
    """Interpreta lo que escribió el usuario. Retorna False para salir."""
    entrada = entrada.strip()
    bajo = entrada.lower()
    if bajo in ("salir", "exit", "q"):
        return False
    if bajo in ("", "lista", "ls"):
        listar()
        return True
    if entrada.startswith("?"):
        resto = entrada[1:].strip()
        if resto.isdigit() and int(resto) in REGISTRO:
            print(f"\n--- Ejercicio {int(resto):02d}: {REGISTRO[int(resto)]['titulo']} ---")
            print(REGISTRO[int(resto)]["ayuda"])
        else:
            print("Escribe ? seguido del número, por ejemplo: ?16")
        return True
    if entrada.isdigit():
        n = int(entrada)
        if n in REGISTRO:
            ejecutar(n)
        else:
            print("Ese número no existe (hay del 1 al 35). Escribe 'lista' para verlos.")
        return True
    encontrados = buscar(entrada)
    if not encontrados:
        print("No encontré nada con eso. Prueba otra palabra o escribe 'lista'.")
    elif len(encontrados) == 1:
        ejecutar(encontrados[0])
    else:
        print("Encontré varios, escribe el número del que quieras:")
        for n in encontrados:
            print(f"  {n:02d}  {REGISTRO[n]['titulo']}")
    return True


def menu():
    print("EJERCICIOS DE PYTHON")
    print("Escribe un número, una palabra para buscar (ej: primo, matriz),")
    print("?número para ver qué hace, 'lista' para ver todos o 'salir'.\n")
    listar()
    while True:
        try:
            entrada = input("\n> ")
        except EOFError:
            break
        if not _procesar(entrada):
            break


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        _procesar(" ".join(sys.argv[1:]))
    else:
        menu()

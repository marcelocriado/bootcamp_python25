# ===============================
#  CICLOS EN PYTHON
# ===============================

# Dos tipos principales:
#   for -> recorre elementos de una secuencia (lista, tupla, cadena, etc.)
#   while -> repite mientras una condición sea Verdadera

# Palabras clave que controlan el ciclo:
#   break -> detiene el ciclo por completo
#   continue -> salta a la siguiente iteración
#   pass -> no hace nada (marcador de posición)

# 'else' en ciclos:
#  El bloque 'else' de un for/while se ejecuta SOLO si el ciclo terminó sin usar 'break'.


# --- for sobre lista ---
numeros = [10, 20, 30]
for n in numeros:
    print(n)
# Salida:
# 10
# 20
# 30

# --- for sobre tupla (desempaquetado) ---
pares = [(1, 2), (3, 4)]
for a, b in pares:
    print(a, b)
# Salida:
# 1 2
# 3 4

# --- for sobre cadena (caracter por caracter) ---
for ch in "PY":
    print(ch)
# Salida:
# P
# Y

# --- for sobre set ---
# Atención: los conjuntos (set) no garantizan orden.
colores = {"rojo", "verde", "azul", "rojo"}
for c in colores:
    print(c)
# Salida (puede variar el orden):
# rojo
# verde
# azul
# (solo una vez cada color)

# --- for sobre diccionario: keys / values / items ---
persona = {"nombre": "Ana", "edad": 29}

print(list(persona.keys()))    # -> ['nombre', 'edad']
print(list(persona.values()))  # -> ['Ana', 29]
print(list(persona.items()))   # -> [('nombre','Ana'), ('edad',29)]

for clave, valor in persona.items():
    print(clave, "->", valor)
# Salida:
# nombre -> Ana
# edad -> 29

# --- range(inicio, fin, paso) ---
# 'fin' es EXCLUSIVO (llega hasta fin-1)
for i in range(5):  # 0,1,2,3,4
    print(i, end=" ")
print()  # -> 0 1 2 3 4

for i in range(1, 6):  # 1,2,3,4,5
    print(i, end=" ")
print()  # -> 1 2 3 4 5

for i in range(10, 0, -2):  # 10,8,6,4,2
    print(i, end=" ")
print()  # -> 10 8 6 4 2

# --- enumerate(iterable, start=1) ---
frutas = ["manzana", "pera", "uva"]
for indice, fruta in enumerate(frutas):
    print(indice, fruta)
# Salida:
# 1 manzana
# 2 pera
# 3 uva

# --- zip(lista1, lista2, ...) ---
# Recorre en paralelo varios iterables (se detiene en el más corto)
precios = [1000, 1200, 900]
for fruta, precio in zip(frutas, precios):
    print(fruta, "->", precio)
# Salida:
# manzana -> 1000
# pera -> 1200
# uva -> 900

# --- while (repite mientras la condición sea Verdadera) ---
contador = 1
while contador <= 3:
    print("contador:", contador)
    contador += 1
# Salida:
# contador: 1
# contador: 2
# contador: 3

# --- break / continue / pass ---
# break: detiene el ciclo
for i in range(1, 6):
    if i == 3:
        break
    print("i:", i)
# Salida:
# i: 1
# i: 2

# continue: salta el resto de la vuelta y sigue con la siguiente
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print("impar:", i)
# Salida:
# impar: 1
# impar: 3
# impar: 5

# pass: no hace nada (sirve como “bloque vacío”)
for i in range(3):
    pass  # no imprime nada

# --- for ... else (se ejecuta SOLO si NO hubo break) ---
valores = [2, 4, 6, 8]
objetivo = 5
for v in valores:
    if v == objetivo:
        print("Encontré", objetivo)
        break
else:
    print("No lo encontré (no hubo break)")  # -> esta línea

# --- Patrones útiles sin usar funciones ---
# 1) Suma de 1..N
N = 5
suma = 0
for i in range(1, N + 1):
    suma += i
print("Suma 1..N =", suma)  # -> 15

# 2) Filtrar pares de una lista
lista = [1, 2, 3, 4, 5, 6]
pares = []
for num in lista:
    if num % 2 == 0:
        pares.append(num)
print("Pares ->", pares)  # -> [2, 4, 6]

# 3) Bucle con “palabra de corte”
entradas = ["10", "20", "fin", "100"]  # '100' ya no se procesa
total = 0
for dato in entradas:
    if dato.lower() == "fin":
        break
    total += int(dato)
print("Total acumulado ->", total)  # -> 30

# ===============================
#  CONDICIONALES EN PYTHON
# ===============================

# En Python las decisiones se toman con:
#   if  (si)
#   elif (si no, entonces si...)
#   else (en cualquier otro caso)


# Operadores de comparación: ==  !=  <  <=  >  >=
# Operadores lógicos:        and   or   not
#   - En otros lenguajes (C/JS):  &&  ||  !
#   - En Python se escribe:       and or not


# Nota sobre "valores considerados FALSOS" en condiciones:
#   0, 0.0, "", [], {}, set(), None y False.
# #   Todo lo demás se considera VERDADERO.
#   (No hace falta memorizar la lista: es para entender por qué a veces
#    una cadena vacía "" se toma como Falso, por ejemplo.)


# --- if simple ---
# Si la condición es Verdadera, ejecuta el bloque.
numero = 10
if numero > 0:
    print("El número es positivo")  # -> El número es positivo

# --- if - else ---
# Si la condición NO se cumple, ejecuta el bloque de else.
x = 7
if (x % 2 == 0):
    print("x es par")
else:
    print("x es impar")  # -> x es impar


# --- if - elif - else (varios casos) ---
edad = 30
if edad < 0:
    print("Edad inválida")
elif edad < 18:
    print("Menor de edad")
elif edad < 65:
    print("Adulto")  # -> Adulto
else:
    print("Adulto mayor")

# --- Comparaciones encadenadas ---
# Se puede escribir 0 < n < 10 (equivale a (0 < n) and (n < 10))
n = 5
print(0 < n < 10)  # -> True

# --- Operadores lógicos: and / or / not ---
# Ejemplo típico en otros lenguajes:
#   (a > 0 && b < 10) || !bloqueado
# En Python se escribe:
a = 5
b = 7
bloqueado = False # por tanto lo no bloqueado es True (!bloqueado => no bloqueado)
resultado = (a > 0 and b < 10) or not bloqueado
print(resultado)  # -> True

# evaluar si un numero es menor que 15, par y divisble por 3
numero = int(input("ingrese un numero: "))

if (numero > 15) and (numero%2 == 0) and (numero%3 == 0):
    print("el numero es mayor que 15, par y divisble por 3")
elif numero > 15 and numero%2 == 0 and numero%3 != 0:
    print("el numero es mayor que 15, par y no divisble por 3")

if numero > 15:
    if numero%2 == 0:
        if numero%3 == 0:
            print("el numero es mayor que 15, par y divisble por 3")
        else:
            print("el numero es mayor que 15, par y no divisble por 3")
    
    else: # el numero es impar
        if numero%3 == 0:
            print("el numero es mayor que 15, impar y divisble por 3")
        else:
            print("el numero es mayor que 15, impar y no divisble por 3")


else: # el numero es menor a 15
    if numero%2 == 0:
        if numero%3 == 0:
            print("el numero es menor que 15, par y divisble por 3")
        else:
            print("el numero es menor que 15, par y no divisble por 3")
    
    else: # el numero es impar
        if numero%3 == 0:
            print("el numero es menor que 15, impar y divisble por 3")
        else:
            print("el numero es menor que 15, impar y no divisble por 3")
            

# --- Prioridad de evaluación (importante) ---
# not tiene mayor prioridad que and, y and mayor que or.
# Es decir: not > and > or
print(True or False and False)    # -> True  (se evalúa primero False and False)
print((True or False) and False)  # -> False (por los paréntesis)

# --- "Se detiene" cuando ya sabe el resultado (and / or) ---
# and: si la primera parte es FALSA, NO evalúa la segunda.
num = 0
condicion_inicial = (num != 0)      # -> False
# En la línea siguiente NO se hace 10/num porque 'and' se detiene al ver False
if condicion_inicial and (10 / num > 1):
    print("Esto no se ejecuta")
else:
    print("Con and, si la primera parte es Falsa, se detiene")  # -> esta línea

# or: si la primera parte es VERDADERA, NO evalúa la segunda.
tiene_nombre = "Ana"  # cadena no vacía se considera Verdadera
if tiene_nombre or (3 > 10):
    print("Con or, si la primera parte es Verdadera, se detiene y no evalua, no lo necesita")  # -> esta línea

# --- Textos en condiciones (cadenas vacías) ---
nombre = ""
if nombre == "":
    print("Nombre vacío (comparación directa)")  # -> esta línea
# Otra forma muy usada en Python (leer: “si nombre NO está vacío”):
if nombre:  # cadena vacía se considera Falsa
    # es lo mismo que if True:
    print("Hay nombre")
else:
    print("No hay nombre (cadena vacía)")  # -> esta línea

# --- None en Python (no existe null ni undefined) ---
# None representa “no hay valor”. Se compara con 'is' / 'is not'.
nada = None
print(nada is None)      # -> True  (forma recomendada)
print(nada == None)      # -> True  (posible, pero NO recomendado)

# --- Pertenencia: in / not in ---
texto = "python"
print("py" in texto)       # -> True
print("z" not in texto)    # -> True

# --- Expresión condicional (forma corta) ---
# Se lee: "aprobado" si nota >= 60, en caso contrario "reprobado".
nota = 59
estado = "aprobado" if nota >= 60 else "reprobado"
print(estado)  # -> reprobado

# =========================
# DICCIONARIOS EN PYTHON
# =========================

# --- Crear diccionarios ---
# Un diccionario es una colección NO ORDENADA, MUTABLE e INDEXADA de pares clave-valor.
# Las claves deben ser únicas e inmutables (strings, números o tuplas).
# Sintaxis: {clave1: valor1, clave2: valor2, ...}
# se puede declarar así:

alumno = {
    "nombre": "Ana", 
    "edad": 16, 
    "curso": "Python Básico", 
    "notas":[6, 5.5, 4.6]
    }

# o así que es lo normal ya que almarcenen muchos pares clave valor:
diccionario = {
    "nombre": "Ana",
    "edad": 16,
    "curso": "Python Básico"
}
print(diccionario)

# --- Acceder a valores por clave ---
print(diccionario["nombre"])  # Ana
print(diccionario.get("edad")) # 16 -> get() evita error si la clave no existe, pero es poco común ocuparlo

# --- Modificar valores ---
diccionario["edad"] = 17
print(diccionario["edad"])  # 17

# --- Agregar nuevas claves ---
diccionario["ciudad"] = "Santiago"
print(diccionario)

# --- Eliminar elementos ---
del diccionario["curso"]
print(diccionario)

valor_eliminado = diccionario.pop("ciudad")  # elimina y devuelve el valor
print(valor_eliminado)  # Santiago
print(diccionario)

# --- Verificar si una clave existe ---
print("nombre" in diccionario)  # True
print("curso" in diccionario)   # False

# --- Iterar sobre diccionarios --- 
# como ayuda memoria, lo veremos más adelante
# a) Claves
for clave in diccionario:
    print(clave)

# b) Valores
for valor in diccionario.values():
    print(valor)

# c) Claves y valores
for clave, valor in diccionario.items():
    print(f"{clave} → {valor}")

# --- Métodos útiles de diccionarios ---
# Devuelven vistas (views) que reflejan los cambios en el diccionario
print(diccionario.keys())    # dict_keys(['nombre', 'edad'])
print(diccionario.values())  # dict_values(['Ana', 17])
print(diccionario.items())   # dict_items([('nombre', 'Ana'), ('edad', 17)])

# ---  Diccionarios anidados (diccionario dentro de diccionario) --- 
estudiante = {
    "nombre": "Ana",
    "edad": 16,
    "notas": {"matematicas": 5, "python": 6}
}

print(estudiante["notas"]) # {'matematicas': 5, 'python': 6}
print(estudiante["notas"]["python"]) # 6

# --- Copiar diccionarios ---
# Usar copy() para evitar referencias al mismo objeto
copia = diccionario.copy()
print(copia)

# --- Vaciar diccionario --- 
diccionario.clear()
print(diccionario)  # {}

# =========================
# LISTAS EN PYTHON
# =========================

# Una lista es una colección ORDENADA y MUTABLE de elementos.
# Puede contener cualquier tipo de dato (incluso mezclados).

# --- Crear listas ---
vacia = []                 # lista vacía
numeros = [1, 2, 3, 4, 5]  # lista de enteros
mixta = [1, "hola", 3.14]  # lista con distintos tipos

print(numeros)
print(mixta)

# --- Acceso a elementos (índices) ---
print(numeros[0])   # 1 -> primer elemento
print(numeros[-1])  # 5 -> último elemento

# --- Modificar elementos (son mutables) ---
numeros[0] = 10
print(numeros)  # [10, 2, 3, 4, 5]

# --- Agregar elementos ---
numeros.append(6)      # agrega al final
print(numeros)         # [10, 2, 3, 4, 5, 6]

numeros.insert(1, 20)  # inserta en posición 1
print(numeros)         # [10, 20, 2, 3, 4, 5, 6]

# --- Eliminar elementos ---
numeros.remove(20)     # elimina primera coincidencia, el primer 20
print(numeros)

ultimo = numeros.pop() # elimina el último y lo devuelve el indice
print("Se eliminó:", ultimo)
print(numeros)

del numeros[0]         # elimina por índice
print(numeros)

# --- Otras operaciones útiles ---
print(len(numeros))         # longitud de la lista
print(3 in numeros)         # True si 3 está en la lista
print(numeros.count(3))     # cuántas veces aparece el 3
print(numeros.index(3))     # posición del primer 3

# --- Ordenar listas ---
numeros.sort()              # ordena la lista (menor a mayor)
print(numeros)

numeros.sort(reverse=True)  # ordena de mayor a menor
print(numeros)

# --- Copiar listas ---
copia = numeros.copy()
print("Copia:", copia)

# --- Listas dentro de listas (anidadas) ---
matriz = [[1, 2], [3, 4], [5, 6]]
print(matriz[0])       # [1, 2]
print(matriz[0][1])    # 2 -> fila 0, columna 1


# =========================
# NÚMEROS EN PYTHON
# =========================

# --- Enteros (int) ---
entero = 10   # número sin decimales
print(entero, type(entero))  # 10 <class 'int'>

# --- Flotantes (float) ---
decimal = 3.14   # número con decimales
print(decimal, type(decimal))  # 3.14 <class 'float'>

# =========================
# OPERACIONES BÁSICAS
# =========================

a = 10
b = 3

# Suma
print(a + b)        # 13 -> int + int = int
print(a + 2.5)      # 12.5 -> int + float = float

# Resta
print(a - b)        # 7 -> int
print(5.5 - 2)      # 3.5 -> float

# Multiplicación
print(a * b)        # 30 -> int
print(a * 2.5)      # 25.0 -> float

# División normal (/)
print(a / b)        # 3.333... -> SIEMPRE devuelve float, aunque ambos sean int
print(10 / 2)       # 5.0 -> noten que devuelve float, no int

# División entera (//)
print(a // b)       # 3 -> devuelve el cociente entero, sin decimales
print(10 // 2)      # 5 -> aquí sí devuelve un int

# Módulo (%)
print(a % b)        # 1 -> el "resto" de la división 10 ÷ 3
print(10 % 2)       # 0 -> porque es divisible exacto

# Potencia (**)
print(a ** b)       # 1000 -> 10^3
print(2 ** 0.5)     # 1.414... -> raíz cuadrada (devuelve float)

# =========================
# DIFERENCIA DE TIPOS
# =========================

# int con int -> devuelve int (excepto división normal, que da float)
print(7 + 2)        # 9 (int)
# int con float -> convierte todo a float
print(7 + 2.0)      # 9.0 (float)

# =========================
# OPERADORES DE COMPARACIÓN
# =========================

x = 5
y = 2

print(x > y)    # True -> 5 es mayor que 2
print(x < y)    # False -> 5 no es menor que 2
print(x == y)   # False -> no son iguales
print(x != y)   # True -> son distintos
print(x >= 5)   # True -> 5 es mayor o igual a 5
print(y <= 2)   # True -> 2 es menor o igual a 2

# =========================
# VALORES GRANDES Y LÍMITES
# =========================

# En Python, los enteros (int) pueden crecer sin límite
# Solo dependen de la memoria del computador.
entero_grande = 10**100   # un 1 seguido de 100 ceros
print(entero_grande)

# Los floats tienen límite, se basan en el estándar IEEE 754 (64 bits).
import sys
print("Máximo float:", sys.float_info.max)   # valor más grande representable
print("Mínimo float positivo:", sys.float_info.min)  # más pequeño positivo
print("Precisión de decimales:", sys.float_info.dig, "dígitos")

# Nota: si un float sobrepasa el máximo permitido → devuelve "inf" (infinito)
print(1e308 * 1000)   # inf

# =========================
# SETS EN PYTHON
# =========================

# --- Crear sets ---
# Un set es una colección NO ORDENADA y NO INDEXADA de elementos únicos (sin duplicados).
# Se definen con llaves {} o con la función set()
conjunto1 = {1, 2, 3, 4, 5}       # set de números
conjunto2 = {"a", "b", "c", "a"}  # los elementos repetidos se eliminan automáticamente

print(conjunto1)  # {1, 2, 3, 4, 5}
print(conjunto2)  # {'a', 'b', 'c'} -> 'a' no se repite

# --- Crear un set vacío ---
vacio = set()    # NOTA: {} crea un diccionario vacío, no un set
print(vacio)     # set()

# --- Acceder a elementos ---
# Los sets NO tienen índice, por lo que NO se puede hacer conjunto1[0]
# Podemos recorrerlos con un bucle, entender que no se puede acceder por le índice, el ciclo lo vemos más adelante
for elem in conjunto1:
    print(elem)

# --- Agregar y eliminar elementos ---
conjunto1.add(6)     # agregar un elemento
print(conjunto1)     # {1, 2, 3, 4, 5, 6}

conjunto1.remove(3)  # eliminar un elemento (error si no existe)
print(conjunto1)

conjunto1.discard(10) # eliminar si existe, no da error si no existe
print(conjunto1)

# --- Operaciones entre sets (similares a teoría de conjuntos) ---
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

print(setA.union(setB))        # {1, 2, 3, 4, 5, 6} -> unión
print(setA.intersection(setB)) # {3, 4} -> intersección
print(setA.difference(setB))   # {1, 2} -> elementos en A pero no en B
print(setB.difference(setA))   # {5, 6} -> elementos en B pero no en A

# --- Comprobación de pertenencia ---
print(2 in setA)   # True -> 2 está en A
print(5 in setA)   # False -> 5 no está en A

# --- Operaciones con operadores simbólicos ---
print(setA | setB)   # unión -> {1,2,3,4,5,6}
print(setA & setB)   # intersección -> {3,4}
print(setA - setB)   # diferencia -> {1,2}
print(setA ^ setB)   # diferencia simétrica -> {1,2,5,6}

# --- Conversión entre tipos ---
# Convertir lista a set (elimina duplicados)    
lista = [1, 2, 2, 3, 4, 4, 5]
conjunto_desde_lista = set(lista)  # elimina duplicados
print(conjunto_desde_lista)  # {1, 2, 3, 4, 5}

# --- Vaciar un set ---
conjunto1.clear()
print(conjunto1)  # set()

# =========================
# STRINGS EN PYTHON
# =========================

# Un string es una cadena de texto
# Se pueden usar comillas simples, dobles o triples

# --- Declaración básica ---
texto1 = 'Hola'
texto2 = "Mundo"
print(texto1)  # Imprime: Hola
print(texto2)  # Imprime: Mundo
print(type(texto1))  # <class 'str'>
print(type(texto2))  # <class 'str'>

# --- Se puede imprimir ambos string en un print ---
print(texto1, texto2)  # Hola Mundo

# --- Triple comillas (multilínea) ---
texto3 = '''Este es un texto
que puede ocupar
varias líneas'''
print(texto3)

# =========================
# CONCATENACIÓN
# =========================

# Unir dos o más strings con +
saludo = texto1 + " " + texto2
print(saludo)  # Hola Mundo

# =========================
# REPETICIÓN
# =========================

# Se puede repetir un string con el operador *
eco = "repito! " * 3
print(eco)  # repito! repito! repito!

# =========================
# ACCEDER A CARACTERES
# =========================

# Los strings son secuencias, es decir listas de caracteres (char), cada letra tiene una posición (índice)
palabra = "Python"
print(palabra[0])   # P (primer carácter, índice 0)
print(palabra[-1])  # n (último carácter) -> lo veremos más adelante en las listas

# =========================
# FORMATO DE STRINGS
# =========================

nombre = "Ana"
edad = 16

# f-strings 
print(f"Hola {nombre}, el próximo año tendrás {edad + 1} años")


# =========================
# FUNCIONES/MÉTODOS ÚTILES DE STRING, SE DEJA COMO AYUDA MEMORIA, LO VEREMOS MÁS ADELANTE
# =========================

print(len(palabra))       # longitud: 6
print(palabra.upper())    # PYTHON (mayúsculas)
print(palabra.lower())    # python (minúsculas)
print(palabra.capitalize()) # Python Es El Mejor Lenguaje (cada nueva palabra empieza con mayúscula)
print(palabra.title())    # Python (cada palabra capitalizada)
print(palabra.replace("Py", "My"))  # Mython
print("   hola   ".strip())  # quita espacios al inicio y al final

# Muchos métodos de los strings en Python devuelven un valor booleano
# (True o False) dependiendo de si se cumple cierta condición.

# --- isdigit() --- ¿Este texto es solo números?
# Revisa si TODOS los caracteres del string son dígitos (números del 0 al 9).
print("123".isdigit())     # True → porque todos los caracteres son números.
print("123a".isdigit())    # False → porque contiene la letra "a".

# --- isalpha() --- ¿Este texto es solo letras?
# Revisa si TODOS los caracteres son letras (a-z o A-Z, sin espacios ni números).
print("abc".isalpha())     # True → solo letras.
print("abc123".isalpha())  # False → porque hay números.
print("hola mundo".isalpha()) # False → porque contiene un espacio.

# --- isalnum() --- ¿Este texto es solo letras o números (sin símbolos)?
# Revisa si TODOS los caracteres son alfanuméricos (letras o números, sin símbolos).
print("abc123".isalnum())  # True → contiene letras y números, permitido.
print("abc!".isalnum())    # False → porque tiene un símbolo (!).
print("12345".isalnum())   # True → solo números también es válido.

# --- startswith() --- ¿El texto empieza con esto?
# Revisa si el string EMPIEZA con cierta subcadena.
print("hola".startswith("ho"))   # True → comienza con "ho".
print("hola".startswith("la"))   # False → no comienza con "la".

# --- endswith() --- ¿El texto termina con esto?
# Revisa si el string TERMINA con cierta subcadena.
print("hola".endswith("la"))     # True → termina con "la".
print("hola".endswith("ho"))     # False → no termina con "ho".

# ===============================
#  TUPLAS EN PYTHON
# ===============================

# --- Crear una tupla ---
tupla1 = (1, 2, 3, 4, 5)          # Tupla de números enteros
tupla2 = ("hola", "mundo", 2025)  # Tupla con distintos tipos de datos
tupla3 = (True, False, True)      # Tupla de valores booleanos
print(tupla1)
print(tupla2)
print(tupla3)

# --- Tupla con un solo elemento (importante) ---
entero = (5 )  # Esto NO es una tupla, es un int
print(type(entero))  # <class 'int'>
tupla_uno = (5,)   # Para que Python lo reconozca como tupla, lleva coma
print(type(tupla_uno))  # <class 'tuple'>

# --- Acceder a los elementos de una tupla ---
print(tupla1[0])   # Primer elemento (posición 0) -> 1
print(tupla2[1])   # Segundo elemento -> "mundo"
print(tupla2[-1])  # Último elemento -> 2025

# --- Slicing (cortar secciones de la tupla), creo que no lo puse en las listas, funciona igual ---
print(tupla1[1:4])  # Elementos desde posición 1 hasta 3 -> (2, 3, 4) - va desde el indice 1 hasta el n-1
print(tupla1[:3])   # Desde el inicio hasta posición 2 -> (1, 2, 3)
print(tupla1[::2])  # Saltando de 2 en 2 -> (1, 3, 5)

# --- Inmutabilidad de las tuplas ---
# A diferencia de las listas, las tuplas NO se pueden modificar (son inmutables)
# tupla1[0] = 99 -> ERROR: las tuplas no permiten reasignación
# tampoco se pueden agregar o eliminar elementos
# Pero sí se pueden crear nuevas tuplas a partir de otras
nueva_tupla = tupla1 + (6, 7, 8)
print(nueva_tupla)  # (1, 2, 3, 4, 5, 6, 7, 8)

# --- Métodos útiles de las tuplas ---
# Aunque las tuplas son inmutables, tienen algunos métodos útiles
print(tupla1.count(3))  # Cuenta cuántas veces aparece el valor 3 -> 1
print(tupla1.index(4))  # Devuelve la posición donde está el 4 -> 3


# --- Tuplas anidadas (tupla dentro de otra) ---
tupla_anidada = ((1, 2), (3, 4), (5, 6))
print(tupla_anidada[0])     # (1, 2)
print(tupla_anidada[0][1])  # 2

# --- Desempaquetado de tuplas, funciona tambien para lista, creo no lo puse ---
# Asignar los valores de una tupla a varias variables
a, b, c = (10, 20, 30)  
print(a, b, c)  # 10 20 30

# Si se desconoce el número exacto de elementos, usar "*"
x, *y = (1, 2, 3, 4, 5)
print(x)  # 1
print(y)  # [2, 3, 4, 5]

# --- Uso común: retorno múltiple en funciones ---
# DEJARLOS COMO AYUDA MEMORIA, LO ACLARAREMOS MÁS ADELANTE
def coordenadas():
    return (10.5, 20.8)  # Una función puede devolver una tupla

lat, lon = coordenadas()
print(f"Latitud: {lat}, Longitud: {lon}")

# --- Conversión entre lista y tupla
lista = [1, 2, 3]
tupla_convertida = tuple(lista)
print(tupla_convertida)  # (1, 2, 3)

lista_nueva = list(tupla1)
print(lista_nueva)  # [1, 2, 3, 4, 5]
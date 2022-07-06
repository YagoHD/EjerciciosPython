# 1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python
# tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def max(numero1, numero2):
    if numero1>numero2:
        return numero1
    elif numero2>numero1:
        return numero2
    else:
        return "Son iguales"

print(max(3,3))

# 2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max_de_tres(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        return numero1
    elif numero2 > numero1 and numero2 > numero3:
        return numero2
    elif numero3> numero1 and numero3 > numero2:
        return numero3
    else:
        return "Algunos o tooos son iguales"

print(max_de_tres(10,10,7))

# 3 - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función
# len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio

def longitud(cadena):
    contador = 0
    for letra in cadena:
        contador = contador +1
    return contador

cadena = (1,2,3,4,5,6,"sg",23,"sgdg")
print(longitud(cadena))

# 4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def vocalConsonante(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return True
    elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        return True
    else:
        return False

print(vocalConsonante("j"))

# 5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(lista):
    total = 0
    for numero in lista:
       total += numero
    return total

print(sum([5,3,7]))

def mult(lista):
    total=1
    for numero in lista:
        total*= numero
    return total

print(mult([5,3,7]))

# 6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando"
# debería devolver la cadena "odnaborp yotse"

def inversa(palabra):
    logitud=len(palabra)
    invertida = palabra[logitud::-1]
    return invertida

print(inversa("Hola"))

# 7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto
# escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(palabra):
    palabraGirada = palabra[::-1]
    if palabraGirada ==palabra:
        return True
    else:
        return False

print(es_palindromo("hooh"))

# 8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o
# devuelva False de lo contrario. Escribir la función usando el bucle for anidado.


print("Ejercicio 8")
def superposicion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
            else:
                return False



print(superposicion([9,9,7],[2,9,1]))

# 9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n.
# Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(numero, letra):
    print(numero * letra)

print(generar_n_caracteres(7,"Y"))

# 10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.
# Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

def procedimiento(lista):
    for i in lista:
        print(i*"*")

print(procedimiento([5,7,2]))
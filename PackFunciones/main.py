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


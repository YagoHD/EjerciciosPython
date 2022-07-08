# Ejercicio 1
# La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a
# funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una
# función max_in_list() que tome una lista de números y devuelva el mas grande.

def max_in_list(lista):
    max = 0
    for i in lista:
        if i > max:
            max = i
    return max

print(max_in_list([5,36,25]))


# Ejercicio 2
# Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

def mas_larga(lista):
    mas_larga = ""
    for i in lista:
        if len(i) > len(mas_larga):
            mas_larga = i
    return mas_larga

print( mas_larga(["pepe","manolo","raul"]))

# Ejercicio 3
# Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n,
# y devuelva las palabras que tengan mas de n caracteres.

def filrar_palabras(lista, numero):
    nuevalista = []
    for i in lista:
        if len(i) > numero:
            nuevalista.append(i)
    return nuevalista

print(filrar_palabras(["pan","huevos","leche","malvadisco","mayonesa","arroz"],5))

# Ejercicio 4
# Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena
# y decir cuantas letras mayúsculas tiene.

def c_mayusculas (cadena):
    contador = 0
    for i in cadena:
        if i != i.lower():
            contador += 1
    return f"La cadena tiene {contador} mayuscula/s"

print(c_mayusculas("Hola Buenos Dias"))

# Ejercicio 5
# Construir un pequeño programa que convierta números binarios en enteros.

def binarioAentero(binario):
    decimal = 0
    exp = len(binario)-1
    for i in binario:
        decimal+=(int(i)*2**(exp))
        exp = exp-1
    return decimal

print(binarioAentero("1001"))

# Ejercicio 6
# Escribir un pequeño programa donde:
# - Se ingresa el año en curso.
# - Se ingresa el nombre y el año de nacimiento de tres personas.
# - Se calcula cuántos años cumplirán durante el año en curso.
# - Se imprime en pantalla.

def edades():
    añoactual = int(input("Introduce el año actual: "))
    for i in range (3):
        nombre = input("Nombre de la persona: ")
        nacimiento = int(input("Año de nacimiento: "))
        print(f"{nombre} tiene {añoactual- nacimiento} años")

#edades()

# Ejercicio 7
# Definir una tupla con 10 edades de personas.
# Imprimir la cantidad de personas con edades superiores a 20.
# Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.

def superiora20(tupla):
    contador = 0
    for i in tupla:
        if i > 20:
            contador = contador +1
    return f"Hay {contador} numeors mayores a 20"

print(superiora20((20,15,33,54,10,2,1,52,70,23)))

# Ejercicio 8
# Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
# También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)

def nombresporX(lista, letra = 0):
    letra = input("Que letra de inicio hay que buscar?: ")
    contador = 0
    for nombre in lista:
        if nombre[0]== letra.lower() or nombre[0] == letra.upper():
            contador = contador +1
    return f"Hay {contador} nombres que empiezan con {letra}"

print(nombresporX(["Yago", "Yaiza", "Manola"]),)

# Ejercicio 9
# Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
# Se puede hacer que el usuario sea quien elija la palabra.

def contar_vocales(palabra):
    a, e, i, o, u = 0,0,0,0,0
    for letra in palabra:
        if letra == "a":
            a = a+1
        elif letra == "e":
            e = e+1
        elif letra == "i":
            i = i+1
        elif letra == "o":
            o = o+1
        elif letra == "u":
            u = u+1
    return f"La palabra {palabra} tiene {a} a, {e} e, {i} i, {o} o, {u} u"

print(contar_vocales("murcielaaago"))


# Ejercicio 10
# Escriba una función es_bisiesto() que determine si un año determinado es un año
# bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400

def es_bisiesto(año):
    if año %4 == 0 and año %100 != 0:
        return f"El año {año}, es un año bisiesto"
    elif año % 400 == 0:
        return f"El año {año}, es un año bisiesto"
    else:
        return f"El año {año}, no es un año bisiesto"

print(es_bisiesto(2000))
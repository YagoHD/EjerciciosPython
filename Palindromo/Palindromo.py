def convertidorInputStringLista():
    palabraEntrada = input("\nIntroduce una palabra o frase, se comprobara si es palindormo: ")
    palabraString = palabraEntrada.lower()
    palabraLista = list(palabraString)
    return palabraLista

def eliminarSimbolos(palabra):
    suprimidos = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""]
    for caracter in suprimidos:
        if caracter in palabra:
            palabra.remove(caracter)
            return eliminarSimbolos(palabra)
    return palabra

def comprobadorPalindromo(lista):
    listaGirada = lista[::-1]
    if listaGirada == lista:
        return "Es un palindromo!!"
    else:
        return "No es un palindromo."


print("¿Es un palindromo?".center(26,"-"))
entrada = convertidorInputStringLista()
entrada = eliminarSimbolos(entrada)
resultado = comprobadorPalindromo(entrada)
print(resultado)


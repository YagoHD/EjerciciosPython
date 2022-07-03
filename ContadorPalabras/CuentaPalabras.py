texto = open("textoParaContar").read() #Abrimos el documento al que le queremos contar la palabras
contador = 0 #Iniciamos un contador a 0
palabras = texto.split() #Dividimos el texto en un array de palabras

for palabra in palabras: #Por cada palabra en el array le sumamos uno al contador
    contador = contador +1

print(f"El texto, tiene: {contador} palabras")

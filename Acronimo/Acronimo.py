def acronimo(texto):
    salida = texto[0]

    for i in range(1, len(texto)):
        if texto[i-1]==" ":
            salida += texto[i]

    salida = salida.upper()
    return salida
while True:
    texto = input("Introduce un texto, se devolvera el acronimo (Hello World -> HW)(0 para salir): ")

    if texto == "0":
        exit()
    print(f"El acronimo de {texto} es: {acronimo(texto)}")

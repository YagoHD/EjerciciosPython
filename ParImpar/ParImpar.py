print("Bienvenido a Par o Impar".center(150," "))
while True:
    print("Introduce un numero para saber si se trata de un numero par, o impar: ".center(150,"-"))
    print("Para salir introduce (0)")
    numero = int(input("Nº:"))
    if numero == 00:
        exit()
    if numero %2==0:
        print(f"El numero {numero}, es un numero PAR")
    else:
        print(f"El numero {numero}, es un numero IMPAR")
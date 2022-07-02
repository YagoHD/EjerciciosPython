#EN ESTE JUEGO LA IA TENDRA QUE ADIVINAR EL NUMERO QUE TENEMOS EN MENTE
import random

while True:
    print("Piensa en un numero del 0 al 100, tendre que adivinarlo!!".center(100,"-"))
    numeroIA = random.randint(0,100)
    entrada = ""
    mayor = 100
    menor = 0
    print("Para salir introduce: Adios")
    entrada = input(f"El numero {numeroIA} es mas Grande (G)? O es mas pequeño (P)? Si he acertado introduce: (C)").lower()

    if entrada == "adios":
        print("¡¡Adios!!".center(100,"-"))
        exit()
    while entrada != "c":

        if entrada == "g":
            mayor=numeroIA-1
            numeroIA = random.randint(menor, mayor)
            entrada = input(f"El numero {numeroIA} es mas Grande (G)? O es mas pequeño (P)? Si he acertado introduce: (C)").lower()

        elif entrada == "p":
            menor =numeroIA+1
            numeroIA = random.randint(menor,mayor)
            entrada = input(f"El numero {numeroIA} es mas Grande (G)? O es mas pequeño (P)? Si he acertado introduce: (C)").lower()
    print(f"He acertado!!! El numero correcto era: {numeroIA}")
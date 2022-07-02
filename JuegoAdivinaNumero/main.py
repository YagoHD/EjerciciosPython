#EN ESTE JUEGO TENDREMOS QUE ADIVINAR EL NUMERO QUE LA IA TIENE EN MENTE
import random

while True:
    print("La IA escogera un numero del 0 al 100 ¡¡Intenta adivinarlo!!".center(100,"-"))
    print("Introduce: 00 para salir")
    numeroIA = random.randint(0,100)
    numeroIntroducido = int(input("Introduce el numero: "))
    if numeroIntroducido == 00:
        print("¡¡Adios!!".center(100,"-"))
        exit()
    while numeroIntroducido != numeroIA:
        if numeroIntroducido<numeroIA:
            numeroIntroducido=int(input("Demasiado pequeño, prueba de nuevo: "))
        elif numeroIntroducido>numeroIA:
            numeroIntroducido=int(input("Te pasaste! Prueba de nuevo: "))
    print(f"Enhorabuena!! El numero era el {numeroIA}")
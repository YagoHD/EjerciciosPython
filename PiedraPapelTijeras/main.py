import random

while True:
    aleatorio = random.randrange(0, 3)
    jugadaIA = None
    jugadaPlayer = None
    print("1. Piedra/  2. Papel/  3. Tijeras")
    opcion = int(input("Elije una opcion (1,2,3): "))

    if opcion == 1:
        jugadaPlayer = "Piedra"
    elif opcion == 2:
        jugadaPlayer = "Papel"
    elif opcion == 3:
        jugadaPlayer = "Tijeras"
    print(f"Eres {jugadaPlayer}")

    if aleatorio == 0:
        jugadaIA = "Piedra"
    elif aleatorio == 1:
        jugadaIA = "Papel"
    elif aleatorio == 2:
        jugadaIA = "Tijeras"
    print(f"La IA elije:  {jugadaIA}")

    if jugadaPlayer == jugadaIA:
        print(f"{jugadaPlayer} y {jugadaIA} -> EMPATE!!")
    elif jugadaIA == "Piedra" and jugadaPlayer == "Papel":
        print(f"{jugadaPlayer} y {jugadaIA} El papel envuelve la piedra -> GANASTE!!")
    elif jugadaIA == "Papel" and jugadaPlayer == "Tijeras":
        print(f"{jugadaPlayer} y {jugadaIA} Las tijeras cortan el papel -> GANASTE!!")
    elif jugadaIA == "Tijeras" and jugadaPlayer == "Piedra":
        print(f"{jugadaPlayer} y {jugadaIA} La piedra rompe las tijeras -> GANASTE!!")
    elif jugadaIA == "Piedra" and jugadaPlayer == "Tijeras":
        print(f"{jugadaPlayer} y {jugadaIA} La piedra rompe las tijeras -> PERDISTE!!")
    elif jugadaIA == "Papel" and jugadaPlayer == "Piedra":
        print(f"{jugadaPlayer} y {jugadaIA} El papel envuelve la piedra -> PERDISTE!!")
    elif jugadaIA == "Tijeras" and jugadaPlayer == "Papel":
        print(f"{jugadaPlayer} y {jugadaIA} Las tijeras cortan el papel -> PERDISTE!!")



    jugarDeNuevo = input("¿Quieres jugar otra vez? (s/n): ")
    if jugarDeNuevo.lower() != "s":
        break
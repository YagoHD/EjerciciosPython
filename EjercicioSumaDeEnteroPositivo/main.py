#Escribir un programa que lea un entero positivo,x , introducido por el usuario
# y después muestre en pantalla la suma de todos los enteros desde 1 hasta x.

x = int(input("Introduce un numero entero positivo: "))
while x>=0:
    suma = x * (x+1)/2
    print(f"La suma de {x} y los numeros que le preceden es de: {suma}")
    break
else:
    print("Numero no valido")
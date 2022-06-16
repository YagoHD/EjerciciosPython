peso = float(input("Introduce tu peso en Kg: "))
estatura = float(input("Introduce tu altura en m (1.85): "))

imc = round(peso/estatura**2,2)
print(f"Tu indice de masa corporal es de: {imc}")
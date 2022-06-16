# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora
# Después debe mostrar por pantalla la paga que le corresponde.

horasTrabajadas = float(input("¿Cuantas horas trabajas?: "))
sueldoHora = float(input("¿Cuanto cobras a la hora?: "))

print(f"Trabajando {horasTrabajadas} horas, y a {sueldoHora}€ la hora, cobras {horasTrabajadas * sueldoHora}€")
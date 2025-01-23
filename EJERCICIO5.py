#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.

hours_work = float(input('Coloca las horas trabajadas: '))
cost_hours = float(input('Coloca el costo por hora trabajada: '))

pay = hours_work * cost_hours

print('La paga correnpondiente a las horas trabajadas y costo por hora es:', pay)
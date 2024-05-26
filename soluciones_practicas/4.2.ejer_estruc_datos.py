# Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo

nombres = []

for i in range(10):
    nombre = input('Ingresa un nombre: ')
    nombres.append(nombre)

elemento_tres = nombres.pop(2)
ultimo_elemento = nombres.pop(8)

print(elemento_tres, ultimo_elemento)
# Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 

nombres = []

for i in range(10):
    nombre = input('Ingresa un nombre: ')
    nombres.append(nombre)

print(nombres)
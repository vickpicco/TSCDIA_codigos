ganados = int(input('Ingresa la cantidad de partidos ganados: '))
empatados = int(input('Ingresa la cantidad de partido empatados: '))
perdidos = int(input('Ingresa la cantidad de partidos perdidos: '))
total = ganados * 3 + empatados * 1 + perdidos * 0
print('El total de puntos de su equipo es: ', total)
# Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”

while True:
    nombre = input('Ingresa un nombre: ').upper()
    if nombre == 'FIN':
        print('Fin del programa.')
        break
    else:
        print(nombre)
    
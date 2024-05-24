# Mostrar sólo los números pares desde 0 hasta el número ingresado (input). 
# Nota: para saber si un número es par hacer i % 2 == 0)

num = int(input('Ingresa un número: '))

for i in range(0, num + 1):
    if i % 2 == 0:
        print (i)
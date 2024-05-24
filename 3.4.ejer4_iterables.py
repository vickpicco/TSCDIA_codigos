# En una escuela, luego de tomar un determinado examen, es necesario calcular el promedio de notas (las notas van de 0 a 10) 
# de los alumnos de un curso. Se necesita saber si el rendimiento ha sido elevado (el promedio es mayor a 8),
# aceptable (el promedio está comprendido entre 6 y 8) o bajo (promedio es inferior a 6). 
# Desarrollar un algoritmo que resuelva este problema. Para tener en cuenta: las autoridades del colegio saben cuántos 
# estudiantes del curso han rendido el examen.

cantidad = 30
acumulador = 0

for i in range(1, cantidad + 1):
    nota = int(input('Ingresa la nota: '))
    acumulador = acumulador + nota

promedio = acumulador / 30
if promedio > 8: 
    print('Rendimiento elevado.')
elif promedio > 6 and promedio < 8:
    print('Rendimiento aceptable.')
else: 
    print('Rendimiento bajo.')
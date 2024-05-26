// Condicional parcial (solo el if) con expresión lógica simple

Algoritmo solo_if
	Definir num, resto Como Entero
	Escribir 'Ingresa un número: '
	Leer num
	resto = num MOD 2
	Si resto = 0 Entonces
		Escribir 'El número es par'
	FinSi
FinAlgoritmo

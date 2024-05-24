// EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente.
// Lo que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. 
// El cliente le indica que necesita conocer el costo de mano de obra para pintar una
// pared rectangular de un galpón. El pintor cobra un monto fijo por cada metro cuadrado.
// Puedes hacer un algoritmo para calcular el costo de mano de obra para pintar la pared.

Algoritmo pintor
	Definir monto_fijo, total Como Real
	Definir metros Como Entero
	Escribir 'Ingresa el monto fijo por metro cuadrado:' 
	Leer monto_fijo
	Escribir 'Ingresa los metros cuadrados que debe pintar: '
	Leer metros
	total = monto_fijo * metros
	Escribir 'El costo de la mano de obra es: $', total
FinAlgoritmo

// Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad. 
// Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento del 10%. 
// Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción a los jubilados. 
// La promoción de jubilados es sumarle un 10% de descuento (si posee otros descuentos, se suma los descuentos). 
// Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.

Algoritmo despensa
	Definir precio_leche, cant_leches, total, total_descuento, total_jubilado Como Entero
	Definir jubilado Como Caracter
	precio_leche = 1000
	Escribir 'Ingresa la cantidad de leches compradas: '
	Leer cant_leches
	Escribir 'Es jubiliado? (S/N)'
	Leer jubilado
	Si cant_leches >= 12 Y cant_leches <= 24 Entonces
		total = precio_leche * cant_leches
			Si jubilado = 'S' Entonces
				total_jubilado = total - total * 0.2
				Escribir 'El total es: $', total_jubilado
			SiNo
				total_descuento = total - total * 0.1 
				Escribir 'El total es: $', total_descuento
			FinSi
	SiNo
		total = precio_leche * cant_leches	
		Si cant_leches > 24 Entonces
			Si jubilado = 'S' Entonces
				total_jubilado = total - total * 0.25
				Escribir 'El total es: $', total_jubilado
			SiNo
				total_descuento = total - total * 0.15
				Escribir 'El total es: $', total_descuento
			FinSi
			FinSi
		FinSi
FinAlgoritmo
Algoritmo sin_titulo
	definir x como caracter
	Escribir "Convertir de Hexadecimal a Decimal"
	leer x
	letras="0123456789abcdef"
	Para i<-0 Hasta Longitud(x)-1 Con Paso 1 Hacer
		Para l<-0 Hasta longitud(letras)-1 Con Paso 1 Hacer
			Si Subcadena(x,i,i)=Subcadena(letras,l,l) Entonces
				acum=acum+l*16^(longitud(x)-i-1)
				l=longitud(letras)-1
				cont=cont+1
			finsi
		Fin Para
	Fin Para
	si cont=Longitud(x) entonces
		escribir hex," Hexadecimal = ",acum," en Decimal"
	sino
		escribir "El numero ",x," no es numero Hexadecimal"
	FinSi

FinAlgoritmo

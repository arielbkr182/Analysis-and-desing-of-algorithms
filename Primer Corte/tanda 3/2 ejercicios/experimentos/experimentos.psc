Algoritmo Experimetos
	Definir c,s,r,sum,i Como Real
	c <- 0
	s <- 0
	r <- 0
	sum <- 0
	Definir conj,sapp,ratn,ch Como Caracter
	Definir n Como Entero
	Escribir 'ingrese el numero de casos'
	Leer n
	Escribir 'ingrese la cantidad de animales no mayores a 15 seguido de la letra del tipo de animal'
	Para j<-0 Hasta n Hacer
		Leer i,ch
		sum <- sum+i
		Si (ch=='C') Entonces
			c <- c+i
		SiNo
			Si (ch=='R') Entonces
				r <- r+i
			SiNo
				Si (ch=='S') Entonces
					s <- s+i
				FinSi
			FinSi
		FinSi
	FinPara
	CON <- (c*100)/sum
	rat <- (r*100)/sum
	sap <- (s*100)/sum
	Escribir 'total animales son',sum
	Escribir 'total conejos son',c
	Escribir 'total ratones son',r
	Escribir 'total sapos son',s
	Escribir 'porcentaje de conejos',CON
	Escribir 'porcentaje de conejos',rat
	Escribir 'porcentaje de conejos',sap
FinAlgoritmo

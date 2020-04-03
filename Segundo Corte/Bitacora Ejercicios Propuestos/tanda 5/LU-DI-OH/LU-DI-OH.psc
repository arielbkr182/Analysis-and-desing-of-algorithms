Algoritmo LU_DI_OH
	Definir atrib, i, j, sort, Mcartas, Lcartas, e1, e2, vm, vl Como Entero
	w=sort-1
	w1=e2-1
	Escribir "Ingresa la  cantidad de atributos que contienen las cartas de Marcos y Leonardo"
	leer atrib
	para i=1 hasta atrib con paso 1 Hacer
		Escribir "Ingresa el numero de cartas en el mazo de Marcos."
		leer Mcartas
		Escribir "Ingresa el numero de cartas en el mazo de Leonardo."
		leer Lcartas
		Dimension vm(Mcartas,atrib)
		Dimension vl(Lcartas,atrib)
		para i=0 hasta Mcartas con paso 1 hacer
			Escribir "¡Es el turno de Marcos para lanzar!."
			
			para j=0 hasta atrib Con Paso 1 Hacer
				Escribir "Digita el valor de cada atributo de cada carta."
				leer vm(Mcartas,atrib)
				Escribir "Digita el valor de cada atributo de cada carta."
				leer vm(Lcartas,atrib)
			FinPara
		FinPara
		para i=0 hasta Lcartas con paso 1 Hacer
			Escribir "Es el turno de Leonardo para lanzar!"
			para j=0 hasta atrib con paso 1 hacer
				
				Escribir "Digita el valor de cada atributo de cada carta."
				leer vl(Lcartas,atrib)
				
				Escribir "Digita el valor de cada atributo de cada carta."
				leer vl(Lcartas,atrib)
			FinPara
		FinPara
		Escribir "Digita el numero carta elegida por Marcos y Leonardo:"
		leer e1
		leer e2
		Escribir "Digita el atributo elegido para atacar."
		leer sort
		si sm=e1-1 entonces
			
			si w > w1 entonces
			Escribir "gana marcos"
					
			SiNo
				si sm=e1-1 Entonces
					si w < w1 entonces
						Escribir "gana leonardo"
					FinSi
				SiNo
					Escribir "empate"
				FinSi
			FinSi
			
		FinSi
	FinPara
FinAlgoritmo

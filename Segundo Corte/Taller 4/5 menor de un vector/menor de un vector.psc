Proceso mayorymenor 
	Dimension V[20]
	para i=1 hasta 20 hacer 
		V[i] = azar(20)+1
	FinPara
	
	mayor=V[1]
	menor=V[1]
	para x=1 hasta 20 hacer
		si V[x] > mayor entonces
			mayor = V[x]
		FinSi
		si V[x] < menor Entonces
			menor= V[x]
		FinSi
	FinPara
	para i=1 hasta 20 con paso 1 hacer
		Escribir "El vector en su posicion ",i," Es igual a ", V[i] 
	FinPara
	Escribir "El numero mayor es: ", mayor
	Escribir "El numero menor es: ", menor
FinProceso
	
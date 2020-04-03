Algoritmo suma_numeros_consecutivos_impares
	Definir n,x,z,min,max,k Como Entero
	Escribir 'ingrese la cantidad de casos de prueba: '
	Leer n
	Escribir 'Ingrese los numeros X ^ Y tal como se ve en las variales: '
	Para i<-0 Hasta n Hacer
		k <- 0
		Leer x
		Leer z
		Escribir 'Valor total de la suma de los valores impares entre x y sin incluir los valores digitados es: '
		Si (x<z) Entonces
			min <- x
			max <- z
		SiNo
			min <- x
			max <- z
		FinSi
		Para i<-min+1 Hasta i Hacer
			Si (i MOD 2=1 O i MOD 2=-1) Entonces
				k <- k+i
			FinSi
		FinPara
		Escribir '',k
	FinPara
FinAlgoritmo

Algoritmo Intenado
	definir casos, numerador, denominador, nota, carga Como Entero
	numerador=0
	denominador=0
	definir media Como real
	Escribir "digite la cantidad de materias"
	Leer casos
	para j=1 Hasta casos con paso 1 Hacer
		
		Escribir "digite la nota"
		leer nota
		Escribir "digite la carga"
		leer carga
		numerador<-numerador+nota*carga
		denominador=denominador+carga
		media<-numerador/(denominador*100.0)
	FinPara
	
	Escribir "su API fue:" (media)
	
FinAlgoritmo

Algoritmo Prueba_de_Seleccion
	Escribir "ingresar el numero A"
	Leer a
	Escribir "ingresar el numero B"
	Leer b
	Escribir "ingresar el numero C"
	Leer c
	Escribir "ingresar el numero D"
	Leer d
	s<-c+d;
	r<-a+b;
	si (b>c) Entonces
		si (d>a)Entonces
			si(s>r) Entonces
				si(c>0) Entonces
					si(d>0) Entonces
						si a es Par Entonces
							Escribir "valores Aceptados";
						SiNo
							Escribir "valores NO 6 Aceptados";
						FinSi
					SiNo
						Escribir "valores no 5 aceptados";
					FinSi
				SiNo
					Escribir "valores no 4 aceptados";
				FinSi
			SiNo
				Escribir "valores no 3 aceptados";
			FinSi
		SiNo
			Escribir "valores no 2 aceptados";
		FinSi
	SiNo
		Escribir "valores no 1 aceptados"		
	FinSi
FinAlgoritmo

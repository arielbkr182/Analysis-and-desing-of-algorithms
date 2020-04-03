Algoritmo sin_titulo
	Escribir "Escribir el numero a convertir"
	Leer dec
	hex <- ''
	Repetir
		r <- dec MOD 16
		dec <- trunc(dec/16)
		Si r=10 Entonces
			hex <- 'A'+hex
		SiNo
			Si r=11 Entonces
				hex <- 'B'+hex
			SiNo
				Si r=12 Entonces
					hex <- 'C'+hex
				SiNo
					Si r=13 Entonces
						hex <- 'D'+hex
					SiNo
						Si r=14 Entonces
							hex <- 'E'+hex
						SiNo
							Si r=15 Entonces
								hex <- 'F'+hex
							SiNo
								Si r<10 O r>16 Entonces
									re <- ConvertirATexto(r)
									hex <- re+hex
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	Hasta Que dec<10
	Si dec<>0 Entonces
		d <- ConvertirATexto(dec)
		res <- d+hex
		Escribir 'El resultado es: ',res
	SiNo
		res <- d+hex
		Escribir 'El resultado es: ',res
	FinSi
FinAlgoritmo

SubProceso fun 
	Definir  n Como Entero
	leer n
	Escribir n
FinSubProceso

Proceso uno
	Definir num como entero;
	Dimension num[14];
	num[1]=1000;
	num[2]=900;
	num[3]=500;
	num[4]=400;
	num[5]=100;
	num[6]=90;
	num[7]=60;
	num[8]=50;
	num[9]=40;
	num[10]=10;
	num[11]=9;
	num[12]=5;
	num[13]=4;
	num[14]=1;
	para i=0 hasta 14 con paso 1 hacer
		mientras n>num[i]
			n=n-num[i]
			si num[i]==1000
				escribir"M"
			SiNo
				si num[i]==900
					Escribir "CM"
				FinSi
				si num[i]==500
					escribir"D"
				SiNo
					si num[i]==400
						Escribir "CD"
					FinSi
				FinSi
				si num[i]==100
					escribir"C"
				SiNo
					si num[i]==90
						Escribir "XC"
					FinSi
				FinSi
				si num[i]==60
					escribir"LX"
				SiNo
					si num[i]==50
						Escribir "L"
					FinSi
				FinSi
				si num[i]==40
					escribir"XL"
				SiNo
					si num[i]==10
						Escribir "X"
					FinSi
				FinSi
			FinSi
			si num[i]==9
				escribir"IX"
			SiNo
				si num[i]==5
					Escribir "V"
				FinSi
			FinSi
			si num[i]==4
				escribir"IV"
			SiNo
				si num[i]==1
					Escribir "I"
				FinSi
			FinSi
		FinMientras
	FinPara

FinProceso
	
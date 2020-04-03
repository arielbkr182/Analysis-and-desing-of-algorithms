Proceso sin_titulo
	Definir a como numerico;
	Escribir "Ingrese un numero entre 1 y 1000";
	Leer a;
	
	Definir b Como Logico;
	b<-Verdadero;
	si a=0 Entonces
		escribir "El cero no puede ser representado";
		b<-Falso;
		
	FinSi
	si a<>trunc(a) entonces
		Escribir "El numero debe ser entero";
		b<-falso;
		
	FinSi
	si a>1000 Entonces
		Escribir "Muy alto";
		b<-Falso;
		
	FinSi
	si a<0 entonces
		Escribir "El numero tiene que ser positivo";
		b<-falso;
		
	FinSi
	si b Entonces
		si a=1000 entonces
			escribir "M";
		Sino
			Dimension nu(10), nd(10), nc(10);
			Definir nu,nd,nc como caracter;
			nu(0)<-" "; nu(1)<-"I"; nu(2)<-"II";nu(3)<-"III";nu(4)<-"IV";nu(5)<-"V";nu(6)<-"VI";nu(7)<-"VII";nu(8)<-"VIII";nu(9)<-"IX";
			nd(0)<-" "; nd(1)<-"X"; nd(2)<-"XX";nd(3)<-"XXX";nd(4)<-"XL";nd(5)<-"L";nd(6)<-"LX";nd(7)<-"LXX";nu(8)<-"LXXX";nu(9)<-"XC";
			nc(0)<-" "; nc(1)<-"C"; nc(2)<-"CC";nc(3)<-"CCC";nc(4)<-"CD";nc(5)<-"D";nc(6)<-"DC";nc(7)<-"DCC";nc(8)<-"DCCC";nu(9)<-"CM";
		FinSi
	finsi
	Definir cent,dec,uni como entero;
	cent<-trunc(a/100)%10;
	dec<-trunc(a/10)%10;
	uni<- a%10;
	Escribir nc(cent),nd(dec),nu(uni);
FinProceso
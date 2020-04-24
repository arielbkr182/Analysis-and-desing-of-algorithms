Algoritmo sin_titulo
	Escribir "Ingrese una palabra "
	leer palabra
	para i=longitud(palabra) hasta 0 con paso -1 hacer
		palabrainv=palabrainv+subcadena(palabra,i,i)
	FinPara
	si palabrainv = palabra entonces
		Escribir "Palabra palindome"
	SiNo
		Escribir "No es palindrome"
	FinSi
	Escribir "Palabra inicial: ",palabra;
	Escribir "Palabra invertida: ",palabrainv;
	
FinAlgoritmo

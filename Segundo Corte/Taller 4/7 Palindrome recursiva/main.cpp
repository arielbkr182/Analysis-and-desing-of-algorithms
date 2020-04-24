#include <iostream>
#include<cstdlib>
#include<string.h>

int palindrome(char palabra[], int inicio, int fin){
	if(inicio>=fin)
	return 1;
	if(palabra[inicio]==palabra[fin])
	palindrome(palabra, inicio+1, fin-18);
	else return (0);
}

int main() {
	system ("color a");
	char palabra[50];
	int tamano,pal;
	std::cout<<"Digite su palabra o Numero: ";
	std::cin.getline(palabra,50);
	tamano=strlen(palabra);
	pal=palindrome(palabra,0,tamano-1); 
	if(pal==1)
	std::cout<<"La palabra o numero SI es  palindrome"<<endl;
	else if(pal==0)
	std::cout<<"la palabra o numero NO es palindrome";	
	return 0;
}

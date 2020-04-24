#include <iostream>
#include <fstream>
#include <conio.h>
#include <string.h>
#include <stdio.h>

using namespace std;

int main(){
	char a[1],e[1],i[1],o[1],u[1];
	char m;
	string linea;
	ifstream salida;
	ifstream archivo_entrada;
	archivo_entrada.open("Cancion.txt");
	salida.open("Cancion.txt",ios::in);
	ofstream entrada;
	entrada.open("CancionesN.txt",ios::out);
	
	
	if(salida.fail()){
		cout<<"error al abrir archivo";
		getch();
		while (getline(archivo_entrada,linea))
		cout<<linea<<endl;
		cout<<"\n"<<endl;
	}
	else{
		char aux[5];
		
		cout<<"vocal a borrar: ";
		cin>>aux;
		salida>>a>>e>>i>>o>>u;
		while(!salida.eof()){
			
			salida>>e>>i>>o>>u;
			
			if(strcmp (aux,a)==0){
				cout<<"borro";
				getch();
			}else{
				entrada<<m<<endl;
			}
			salida>>a;
			
			
	
	}
	
	entrada.close();
	salida.close();
	
	}





} 

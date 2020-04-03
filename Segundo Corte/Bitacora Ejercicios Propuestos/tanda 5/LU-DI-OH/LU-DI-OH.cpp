#include <stdio.h>
#include<iostream>
#include <stdlib.h>
using namespace std;
int main(){
	
	int atrib, i, j, sort;
	int Mcartas,Lcartas;
	int e1, e2;
	cout << "Ingresa la  cantidad de atributos que contienen las cartas de Marcos y Leonardo."<< endl;
	while(scanf("%d",&atrib) != EOF ){
		cout << "Ingresa el numero de cartas en el mazo de Marcos y Leonardo."<< endl;
		scanf("%d %d",&Mcartas,&Lcartas);
		

		int vm[Mcartas][atrib];
		
		int vl[Lcartas][atrib];
		
		for ( i = 0 ; i < Mcartas ; i++ ){
			cout << "¡Es el turno de Marcos para lanzar!."<< endl;
			cout << "Digita el valor de cada atributo de cada carta"<< endl;
			for ( j = 0 ; j < atrib ; j++){
				scanf("%d",&vm[i][j]);
			}
		}
		for ( i = 0 ; i < Lcartas ; i++ ){
			cout << "¡Es el turno de Leonardo para lanzar!."<< endl;
			cout << "Digita el valor de cada atributo de cada carta"<< endl;
			for ( j = 0 ; j < atrib ; j++){
				scanf("%d",&vl[i][j]);
				
			}
		}
		cout << "Digita el numero carta elegida por Marcos y Leonardo:"<< endl;
		scanf("%d %d", &e1, &e2);
		cout <<"Digita el atributo elegido para atacar." << endl;
		scanf("%d",&sort);
		
		if(vm[e1-1][sort-1] > vl[e2-1][sort-1]) printf("Gana Marcos!!");
		else if (vm[e1-1][sort-1] < vl[e2-1][sort-1]) printf("Gana Leonardo!!");
		else printf("Batalla reñida hay un Empate\n");
	}
	return 0;
}
   


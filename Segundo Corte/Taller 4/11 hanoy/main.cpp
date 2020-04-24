#include <iostream>

using namespace std;
int hanoy(int disco, int varilla1, int varilla2, int varilla3){
	if(disco==1){
		cout<<"Mueva el disco de la varilla: "<<varilla1<<" hacia la varilla: "<<varilla3<<endl;
	}
	else{
		hanoy(disco-1, varilla1, varilla3, varilla2);
		cout<<"Mueva el disco de la varilla: "<<varilla1<<" hacia la varilla: "<<varilla3<<endl;
		hanoy(disco-1, varilla2, varilla1, varilla3);
	}
	
}

int main(){
	int Varilla1 = 1, Varilla2 = 2, Varilla3 = 3, Disco = 0;
	cout<<"Digite los discos con los que quiere jugar: ";
	cin>>Disco;
	hanoy(Disco, Varilla1, Varilla2, Varilla3);

return 0;
}

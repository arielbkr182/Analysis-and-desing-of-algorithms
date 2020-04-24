#include <iostream>
#include<iomanip>

using namespace std;

int main(int) {
	int numero;
	 cout<<"Ingrese Numero a Invertir: ";
	 cin>>numero;
	 cout<<"Numero numero invertido es: ";
	 do{
	 	cout<<(numero%10);
	 	numero/=10;
	 	
	 }while( numero !=0);
	
	
	return 0;
}

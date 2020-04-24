#include <iostream>

using namespace std;

int Invertir(int n, int t)
{
return n == 0 ? t : Invertir(n / 10, t * 10 + n % 10); // OPERADOR TERNARIO
}
int main (){

     int num;
	 cout << "Ingrese un numero: ";
	 cin >> num;
	 cout << "Numero invertido: " << Invertir(num, 0) << endl;
	 system ("pause");
	 return 0;

}
 

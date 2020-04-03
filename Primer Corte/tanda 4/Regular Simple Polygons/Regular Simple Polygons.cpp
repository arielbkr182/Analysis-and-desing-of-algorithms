#include<iostream>
using namespace std;
int main() {
	float a;
	float b;
	float multiplicar;
	reinicio:
	cout << "escribir el numero de lados del poligono" << endl;
	cin >> a;
	cout << "escribir la longitud del los lados del poligono" << endl;
	cin >> b;
	multiplicar = (a*b);
	cout << "el perimetro del poligono es :" << multiplicar << endl;
	goto reinicio;	
}


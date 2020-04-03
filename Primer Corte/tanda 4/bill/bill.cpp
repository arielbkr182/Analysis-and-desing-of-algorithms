#include<iostream>
#include<stdio.h>
using namespace std;

int main() {
	int a;
	int b;
	int i;
	cout << "digita el numero de casos de prueba: " << endl;
	cin >> a;
	cout << "digita la cantidad de numeros de enteros: " << endl;
	for (i=0;i<=a;i++) {
		cin >> b;
		if (b % 2 == 0) {
			cout << "el resultado de la suma es 0" << endl;
		} else {
			cout << "el resultado de la suma es 1" << endl;
		}
	}
	return 0;
}


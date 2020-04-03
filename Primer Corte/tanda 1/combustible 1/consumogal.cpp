#include<iostream>
#include <iomanip>
using namespace std;
int main() {
	int a;
	int b;
	float divicion;
	float multiplicacion;
	cout << "Ingresa el tiempo en horas que duro el viaje\nsin letras solo los numeros Ejemplo 30 :" << endl;
	cin >> a;
	cout << "Ingresa la velocidad promedio durante el viaje\nsin letras solo los numeros Ejemplo 100 :" << endl;
	cin >> b;
	multiplicacion = (a*b);
	divicion = (multiplicacion/12);
	cout << "Los litros nesesarios de combustible o gasolina para el viaje son:\n"<<fixed<<setprecision(3)<<divicion<< "Lts"<<endl;
	return 0;
}


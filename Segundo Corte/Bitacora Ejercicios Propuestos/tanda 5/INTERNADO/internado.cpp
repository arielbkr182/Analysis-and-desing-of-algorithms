#include<iostream>
#include<iomanip>
using namespace std;

int main() {
	int carga;
	int casos;
	int denominador;
	float j;
	float media;
	int nota;
	int numerador;
	numerador = 0;
	denominador = 0;
	cout << "digite la cantidad de materias" << endl;
	cin >> casos;
	for (j=1;j<=casos;j++) {
		cout << "digite la nota" << endl;
		cin >> nota;
		cout << "digite la carga" << endl;
		cin >> carga;
		numerador = numerador+nota*carga;
		denominador = denominador+carga;
		media = numerador/(denominador*100.0);
	}
	cout<<fixed<<showpoint<<setprecision(4)<< "su API fue:" << (media) << endl;
	return 0;
}


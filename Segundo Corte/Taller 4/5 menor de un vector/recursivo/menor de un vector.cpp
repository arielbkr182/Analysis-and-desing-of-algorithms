#include<iostream>
#include<cstdlib>
using namespace std;


int main() {
	int i;
	float mayor;
	float menor;
	float v[20];
	int x;
	for (i=1;i<=20;i++) {
		v[i-1] = (rand()%20)+1;
	}
	mayor = v[0];
	menor = v[0];
	for (x=1;x<=20;x++) {
		if (v[x-1]>mayor) {
			mayor = v[x-1];
		}
		if (v[x-1]<menor) {
			menor = v[x-1];
		}
	}
	for (i=1;i<=20;i++) {
		cout << "El vector en su posicion " << i << " Es igual a " << v[i-1] << endl;
	}
	cout << "El numero mayor es: " << mayor << endl;
	cout << "El numero menor es: " << menor << endl;
	return 0;
}


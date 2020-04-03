#include <stdlib.h>
#include<iostream>
using namespace std;
int main() {
	char dato[10];
	int a,b,c,d,r,s;
	reinicio:
	do{
	cout << "ingresar el numero A" << endl;
	cin >> dato;
	a=atoi(dato);
	}while(a==0);
	do{
	cout << "ingresar el numero B" << endl;
	cin >> dato;
	b=atoi(dato);
	}while(b==0);
	do{
	cout << "ingresar el numero C" << endl;
	cin >> dato;
	c=atoi(dato);
	}while(c==0);
	do{
	cout << "ingresar el numero D" << endl;
	cin >> dato;
	d=atoi(dato);
	}while(d==0);
	s = c+d;
	r = a+b;
	if (b>c) {
		if (d>a) {
			if (s>r) {
				if (c>0) {
					if (d>0) {
						if (a % 2 == 0) {
							cout << "valores Aceptados" << endl;
						} else {
							cout << "valores NO Aceptados Condicion 6" << endl;
						}
					} else {
						cout << "valores NO aceptados Condicion 5" << endl;
					}
				} else {
					cout << "valores NO aceptados Condicion 4" << endl;
				}
			} else {
				cout << "valores NO aceptados Condicion 3" << endl;
			}
		} else {
			cout << "valores NO aceptados Condicion 2" << endl;
		}
	} else {
		cout << "valores NO aceptados Condicion 1" << endl;
	}
    goto reinicio;	
}


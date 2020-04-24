#include<iostream>
using namespace std;

int main() {
	int a, b, c, i, n;
	cout << "Ingrese el numero para hallar serie: ";
	cin >> n;
	a = 0;
	b = 1;
	for (i=1;i<=n;i++) {
		cout << a << endl;
		c = a+b;
		a = b;
		b = c;
	}
	return 0;
}


#include<iostream>
#include<cmath>
#include<sstream>
using namespace std;

string convertiratexto(float f);

int main() {
	string d;
	int dec;
	string hex;
	float r;
	string re;
	string res;
	cout << "escribir el numero a convertir" << endl;
	cin >> dec;
	hex = "";
	do {
		r = dec%16;
		dec = int(dec/16);
		if (r==10) {
			hex = "A"+hex;
		} else {
			if (r==11) {
				hex = "B"+hex;
			} else {
				if (r==12) {
					hex = "C"+hex;
				} else {
					if (r==13) {
						hex = "D"+hex;
					} else {
						if (r==14) {
							hex = "E"+hex;
						} else {
							if (r==15) {
								hex = "F"+hex;
							} else {
								if (r<10 || r>16) {
									re = convertiratexto(r);
									hex = re+hex;
								}
							}
						}
					}
				}
			}
		}
	} while (dec>=10);
	if (dec!=0) {
		d = convertiratexto(dec);
		res = d+hex;
		cout << "El resultado es: " << res << endl;
	} else {
		res = d+hex;
		cout << "El resultado es: " << res << endl;
	}
	return 0;
}

string convertiratexto(float f) {
	stringstream ss;
	ss << f;
	return ss.str();
}


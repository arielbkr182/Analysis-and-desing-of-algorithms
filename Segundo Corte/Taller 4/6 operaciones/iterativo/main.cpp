#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main() {
	float a,b,suma,resta,pot;
	float multi,div;
	cout<<"primer numero: ";
	cin>>a;
	cout<<"segundo numero: ";
	cin>>b;
	if (a&&b>=0){
		suma=a+b;
		resta=a-b;
		multi=a*b;
		div=a/b;
		pot=pow(a,b);
		cout<<"La suma es: "<<suma<<endl;
		cout<<"La resta es: "<<resta<<endl;
		cout<<"La multiplicacion es: "<<multi<<endl;
		cout<<"La division es: "<<fixed<<setprecision(3)<<div<<endl;
		cout<<"La potencia es: "<<pot<<endl;
	}else{
		cout<<"dato erroneo"<<endl;
	}	
}

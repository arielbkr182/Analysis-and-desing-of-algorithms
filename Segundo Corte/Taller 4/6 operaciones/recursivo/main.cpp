#include <iostream>
#include<cstdlib>
#include <iomanip>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;
int suma(int a, int b){
	if(b==0) return a;
	if(a==0) return b;
	
	else{
		return 1+suma(a,b-1);
	}
}
int resta(int a, int b){
	if(a>b) return 1+resta(a,b+1);
	else
		if(b>a) return -1+resta(a+1,b);
	return 0;
	}

int multi(int a, int b){
	if(b==1) return a;
	if(b>0){
		return a+multi(a,b-1);
	} 
	else
	{
	return -a+multi(a,b+1);
		}
	
	return (0);
	}
float division(float a, float b){
	if(a==b) return (1);
	if(a<b) return (0);
	if(a>b){
		return (division(a-b,b)+1);
	}
	}
float potencia(float a, float b){
	if (b==1){
		return (a);
		
	}else{
		a=a*potencia(a,b-1);
		return (a);
	}
}

int main() {
	system("color a");
	float a;
	float b;
	cout<<"Digite el primer numero: "<<endl;
	cin>>a;
	cout<<"Digite el segundo numero: "<<endl;
	cin>>b;
	cout<<"La suma es: "<<a<<"+"<<b<<"="<<suma(a,b)<<endl;
	cout<<"La resta es: "<<a<<"-"<<b<<"="<<resta(a,b)<<endl;
	cout<<"La multiplicacion es: "<<a<<"*"<<b<<"="<<multi(a,b)<<endl;
	cout<<"La division es: "<<a<<"/"<<b<<"="<<fixed<<setprecision(3)<<division(a,b)<<endl;
	cout<<"La potencia es: "<<a<<"^"<<b<<"="<<potencia(a,b)<<endl;
	system ("pause");
	return 0;
}

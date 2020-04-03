#include<iostream>
#include<iomanip>
using namespace std;

int main()
{
float c=0;
float s=0;
float r=0;
float sum=0;
float i;
// se declaran dos variables para ingresar la cantidad de animales seguido de la letra que identifica a cada animal
char conj;
char sapp;
char ratn;
char ch; // letra que identifica el animal y hace la dima de lo 
int n;
cout << "Ingrese el numero de casos: "<< endl;
cin>>n;
cout << "Ingrese la cantidad de animales no mayores a 15 seguido del tipo de animal: "<< endl;
for(int j=0;j<n;j++)
{
cin>>i>>ch;
sum=sum+i;
if(ch=='C')
{
c=c+i;
} else
	if(ch=='C'){
	c=c+i;
	}
	else
	if(ch=='R')
	{
	r=r+i;
	}
	else
	if(ch=='S')
	{
	s=s+i;
	}else{
	}
	}
float con=(c*100)/sum;
float rat=(r*100)/sum;
float sap=(s*100)/sum;

cout<<"Total Animales Son: "<<sum<<endl;
cout<<"Total de Conejos: "<<c<<endl;
cout<<"Total de Ratones: "<<r<<endl;
cout<<"Total de Sapos: "<<s<<endl;
cout<<fixed<<showpoint<<setprecision(2)<<"Porcentaje de Conejos: "<<con<<" %"<<endl;
cout<<fixed<<showpoint<<setprecision(2)<<"Porcentaje de Ratones: "<<rat<<" %"<<endl;
cout<<fixed<<showpoint<<setprecision(2)<<"Porcentaje de Sapos: "<<sap<<" %"<<endl;

return 0;
}

#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

int permutacion(string aux,string *letras,int a,int b){ //funcion que hacela permutacion 
    string resp=aux;
    if(b>0){
        for(int x=0; x<a; x++){
            permutacion(aux+letras[x],letras,a,b-1);
        }
    }else{
        cout<<""<<resp<<endl;
    }
}

int main(){
    string letras[]={"A","B","C","D"};
    int a,b;
    cout<<"Inrese el tamano de vector: ";
    cin>>a;
    cout<<"Ingrese la cantidad de letras a permutar:";
    cin>>b;
    cout<<"Lista de elementos:"<<endl;
    for(int x=0; x<a; x++){
        cout<<letras[x]<<",";
    }
	 cout<<"Numero de permutaciones con repeticion: "<<pow(a,b)<<endl;
     cout<<"Lista de permutaciones con repeticion: "<<endl;
	 permutacion("",letras,a,b);
    return 0;
}

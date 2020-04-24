#include <iostream>

using namespace std;
int sum(int num1, int num2[], int x){
	if(x==5){
		return num1;
	}
	else{
		num1=num1+num2[x];
		sum(num1, num2, x+1);
	}
}

int min(int vec[], int minn, int n){
	if (n==5){
		return minn;
	}
	else{
		if (vec[n]<minn){
			minn=vec[n];
		}
		min(vec,minn,n+1);//menos
	}
}
int main() {
	int vector[5],i,menor,suma;
	for(i=0;i<5;i++){
		cout<<"X["<<i+1<<"]= ";
		cin>>vector[i];
	}
	suma = sum(0, vector, 0);
	cout<<"La suma es: "<<suma<<endl;
	
	menor = min(vector, vector[0], 0);
	cout<<"El menor es:"<<menor;
	
	
	
	
}

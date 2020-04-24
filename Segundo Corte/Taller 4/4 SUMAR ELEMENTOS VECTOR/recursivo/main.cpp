#include<iostream>
#include<conio.h>

using namespace std;
int suma(int t[], int n) {
	int r=0;
	if(n==0){
		r+=t[0];
	}
	else{
		r = t[n]+suma(t,n-1);
	}
	return r;
}

int main() {
	int n=5;
	int t[]={1,2,3,4,5};
	cout <<"el resultado de la suma del vector es: "<<suma(t,n-1);
	getch();
	return 0;
}

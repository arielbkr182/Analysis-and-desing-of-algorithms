#include <bits/stdc++.h>

using namespace std;

char r[10],d[] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
int n,k;

int main(){
	printf("digite el numero a convertir en Hexadecimal:");
	scanf("%d",&n);
	while(n){
		r[k++] = d[n%16];
		n /= 16;
	}
	while(k--) 

	printf("El resultado es:"  "%c",r[k]);
	return 0;
}


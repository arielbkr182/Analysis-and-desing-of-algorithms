#include <iostream>

using namespace std;

int main()
{
	int n; //cantidad de datos x y 
	int x;
	int y; 
	int min;
	int max; 
	int k;
	cout << "Ingrese la cantidad de casos de prueba: "<< endl;
	cin >> n;
	cout << "Ingrese los numeros X ^ Y tal como se ve en las variales: "<< endl;
	for (int i = 0; i < n; ++i)
	{
		k = 0;
		
		cin >> x >> y;
		cout << "Valor total de la suma de los valores impares entre x y sin incluir los valores digitados es: "<< endl;

		if(x < y){
			min = x;
			max = y;
		}else{
			max = x;
			min = y;
		}

		for(int i = (min + 1); i < max; ++i)
		{
			if(i % 2 == 1 || i % 2 == -1){
				k += i;
			}
		}
	
		cout << k << endl;
	}


	return 0;
}

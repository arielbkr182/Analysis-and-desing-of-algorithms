#include <fstream>
#include <iostream>
#include <string>
using namespace std;
int main()
{
	char 
	
	
	ifstream archivo_entrada;
	string linea;
	
	archivo_entrada.open("Cancion.txt");
	if (archivo_entrada.fail())
		cout<<"el archivo se abrio correctamente"<<endl;
		
	while (getline(archivo_entrada,linea))
	cout<<linea<<endl;
	cout<<"\n"<<endl;

	archivo_entrada.close();
system ("pause");
return 0;


}

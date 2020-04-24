![](https://www.virtualpro.co/noticiasImg/1134/Universidaddesan%20buenaventura20130927.jpg)



Análisis y diseño de algoritmos es una de las materias más elementales e 

indispensables en la carrera de ingeniería de sistemas en este espacio 

veremos la aplicación de varios algoritmos en varios lenguajes de 

programación, ejemplos de la vida cotidiana.

**Tabla de Contenido**

[TOCM]

[TOC]

#Primer Corte
##Bitacora Ejercicios Propuestos
####Ejercicio Combustible
##### Codigo en C++
```
#include<iostream>
#include <iomanip>
using namespace std;
int main() {
	int a;
	int b;
	float divicion;
	float multiplicacion;
	cout << "Ingresa el tiempo en horas que duro el viaje\nsin letras 

solo los numeros Ejemplo 30 :" << endl;
	cin >> a;
	cout << "Ingresa la velocidad promedio durante el viaje\nsin 

letras solo los numeros Ejemplo 100 :" << endl;
	cin >> b;
	multiplicacion = (a*b);
	divicion = (multiplicacion/12);
	cout << "Los litros nesesarios de combustible o gasolina para el 

viaje son:\n"<<fixed<<setprecision(3)<<divicion<< "Lts"<<endl;
	return 0;
}
```
#####Diagrama de Flujo
![]( http://imgfz.com/i/yBCkFLM.png)
#####Seudocodigo
![](http://imgfz.com/i/mueCHjz.jpeg)

####Ejercicio Pruebas de Seleccion
##### Codigo en C++
```
#include <stdlib.h>
#include<iostream>
using namespace std;
int main() {
	char dato[10];
	int a,b,c,d,r,s;
	reinicio:
	do{
	cout << "ingresar el numero A" << endl;
	cin >> dato;
	a=atoi(dato);
	}while(a==0);
	do{
	cout << "ingresar el numero B" << endl;
	cin >> dato;
	b=atoi(dato);
	}while(b==0);
	do{
	cout << "ingresar el numero C" << endl;
	cin >> dato;
	c=atoi(dato);
	}while(c==0);
	do{
	cout << "ingresar el numero D" << endl;
	cin >> dato;
	d=atoi(dato);
	}while(d==0);
	s = c+d;
	r = a+b;
	if (b>c) {
		if (d>a) {
			if (s>r) {
				if (c>0) {
					if (d>0) {
						if (a % 2 == 0) {
							cout << "valores 

Aceptados" << endl;
						} else {
							cout << "valores 

NO Aceptados Condicion 6" << endl;
						}
					} else {
						cout << "valores NO 

aceptados Condicion 5" << endl;
					}
				} else {
					cout << "valores NO aceptados 

Condicion 4" << endl;
				}
			} else {
				cout << "valores NO aceptados Condicion 

3" << endl;
			}
		} else {
			cout << "valores NO aceptados Condicion 2" << 

endl;
		}
	} else {
		cout << "valores NO aceptados Condicion 1" << endl;
	}
    goto reinicio;	
}
```
#####Diagrama de Flujo
![]( http://imgfz.com/i/lVWR0h4.jpeg)
#####Seudocodigo
![](http://imgfz.com/i/lPKGIQs.jpeg)

####Ejercicio Experimentos
##### Codigo en C++
```
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
// se declaran dos variables para ingresar la cantidad de animales 

seguido de la letra que identifica a cada animal
char conj;
char sapp;
char ratn;
char ch; // letra que identifica el animal y hace la dima de lo 
int n;
cout << "Ingrese el numero de casos: "<< endl;
cin>>n;
cout << "Ingrese la cantidad de animales no mayores a 15 seguido del tipo 

de animal: "<< endl;
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
cout<<fixed<<showpoint<<setprecision(2)<<"Porcentaje de Conejos: 

"<<con<<" %"<<endl;
cout<<fixed<<showpoint<<setprecision(2)<<"Porcentaje de Ratones: 

"<<rat<<" %"<<endl;
cout<<fixed<<showpoint<<setprecision(2)<<"Porcentaje de Sapos: "<<sap<<" 

%"<<endl;

return 0;
}
```
#####Diagrama de Flujo
![]( http://imgfz.com/i/YyqPc6E.jpeg)
#####Seudocodigo
![](http://imgfz.com/i/8gBKZil.jpeg)

####Ejercicio Suma de numeros consecutivos
##### Codigo en C++
```
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
	cout << "Ingrese los numeros X ^ Y tal como se ve en las 

variales: "<< endl;
	for (int i = 0; i < n; ++i)
	{
		k = 0;
		
		cin >> x >> y;
		cout << "Valor total de la suma de los valores impares 

entre x y sin incluir los valores digitados es: "<< endl;

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
```
#####Diagrama de Flujo
![](http://imgfz.com/i/fz6bv4V.png)
#####Seudocodigo
![](http://imgfz.com/i/wUq1X6G.png)

####Ejercicio Bill
##### Codigo en C++
```
#include<iostream>
#include<stdio.h>
using namespace std;

int main() {
	int a;
	int b;
	int i;
	cout << "digita el numero de casos de prueba: " << endl;
	cin >> a;
	cout << "digita la cantidad de numeros de enteros: " << endl;
	for (i=0;i<=a;i++) {
		cin >> b;
		if (b % 2 == 0) {
			cout << "el resultado de la suma es 0" << endl;
		} else {
			cout << "el resultado de la suma es 1" << endl;
		}
	}
	return 0;
}
```
#####Diagrama de Flujo
![](http://imgfz.com/i/CAgwlfb.png)
#####Seudocodigo
![](http://imgfz.com/i/5RipgjY.png)

####Ejercicio Convercion a Hxadecimal
##### Codigo en C++
```
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
								hex = 

"F"+hex;
							} else {
								if (r<10 

|| r>16) {
									

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
```
#####Diagrama de Flujo
![](http://imgfz.com/i/Ose32dR.png)
#####Seudocodigo
![](http://imgfz.com/i/n8N6c7w.png)
![](http://imgfz.com/i/NOIUFgo.png)

####Ejercicio Poligonos Simples Regulares
##### Codigo en C++
```
#include<iostream>
using namespace std;
int main() {
	float a;
	float b;
	float multiplicar;
	reinicio:
	cout << "escribir el numero de lados del poligono" << endl;
	cin >> a;
	cout << "escribir la longitud del los lados del poligono" << 

endl;
	cin >> b;
	multiplicar = (a*b);
	cout << "el perimetro del poligono es :" << multiplicar << endl;
	goto reinicio;	
}
```
#####Diagrama de Flujo
![](http://imgfz.com/i/TqKN3GE.png)
#####Seudocodigo
![](http://imgfz.com/i/oGx8k75.png)


#Segundo Corte
##Ejercicios Propuestos Segundo corte
####Ejercicio DIJKSTRA
##### Codigo en Java NetBeans
```
package dijkstra;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 *
 * @author Toño
 */
public class Dijkstra {

    
    public static void main(String[] args) {
       List<String> jewel=new ArrayList<>();
       Scanner lc = new Scanner(System.in);
       String a;
       boolean flag = true;
       do {
           a=lc.next();
           if(a.contains("(") || a.contains(")")){
               if (!jewel.isEmpty()){
                   for (int i = 0; i < jewel.size();i++){
                       if(a.equals(jewel.get(i))){
                           flag=true;
                           break;
                       }
                   }
               }  else{
                   jewel.add(a);
                   
               }
               if(!flag){
                   jewel.add(a);
               }
           }else{
               break;
           }
           
         flag=false;  
       }while(!a.contains("(") || !a.contains(")"));
       System.out.println(jewel.size());
       
 }
}

```
#####Diagrama de Flujo
![]()
#####Seudocodigo
![]()

####Ejercicio internado
##### Codigo en C++
```
#include<iostream>
#include<iomanip>
using namespace std;

int main() {
	int carga;
	int casos;
	int denominador;
	float j;
	float media;
	int nota;
	int numerador;
	numerador = 0;
	denominador = 0;
	cout << "digite la cantidad de materias" << endl;
	cin >> casos;
	for (j=1;j<=casos;j++) {
		cout << "digite la nota" << endl;
		cin >> nota;
		cout << "digite la carga" << endl;
		cin >> carga;
		numerador = numerador+nota*carga;
		denominador = denominador+carga;
		media = numerador/(denominador*100.0);
	}
	cout<<fixed<<showpoint<<setprecision(4)<< "su API fue:" << (media) << endl;
	return 0;
}


```
#####Diagrama de Flujo
![](http://imgfz.com/i/XW40sCZ.png)
#####Seudocodigo
![](http://imgfz.com/i/3QCqPND.png)

####Ejercicio LU-DI -OH
##### Codigo en C++
```
#include <stdio.h>
#include<iostream>
#include <stdlib.h>
using namespace std;
int main(){
	
	int atrib, i, j, sort;
	int Mcartas,Lcartas;
	int e1, e2;
	cout << "Ingresa la  cantidad de atributos que contienen las cartas de Marcos y Leonardo."<< endl;
	while(scanf("%d",&atrib) != EOF ){
		cout << "Ingresa el numero de cartas en el mazo de Marcos y Leonardo."<< endl;
		scanf("%d %d",&Mcartas,&Lcartas);
		

		int vm[Mcartas][atrib];
		
		int vl[Lcartas][atrib];
		
		for ( i = 0 ; i < Mcartas ; i++ ){
			cout << "¡Es el turno de Marcos para lanzar!."<< endl;
			cout << "Digita el valor de cada atributo de cada carta"<< endl;
			for ( j = 0 ; j < atrib ; j++){
				scanf("%d",&vm[i][j]);
			}
		}
		for ( i = 0 ; i < Lcartas ; i++ ){
			cout << "¡Es el turno de Leonardo para lanzar!."<< endl;
			cout << "Digita el valor de cada atributo de cada carta"<< endl;
			for ( j = 0 ; j < atrib ; j++){
				scanf("%d",&vl[i][j]);
				
			}
		}
		cout << "Digita el numero carta elegida por Marcos y Leonardo:"<< endl;
		scanf("%d %d", &e1, &e2);
		cout <<"Digita el atributo elegido para atacar." << endl;
		scanf("%d",&sort);
		
		if(vm[e1-1][sort-1] > vl[e2-1][sort-1]) printf("Gana Marcos!!");
		else if (vm[e1-1][sort-1] < vl[e2-1][sort-1]) printf("Gana Leonardo!!");
		else printf("Batalla reñida hay un Empate\n");
	}
	return 0;
}
```
#####Diagrama de Flujo
![](http://imgfz.com/i/XW40sCZ.png)
#####Seudocodigo
![](http://imgfz.com/i/0R2ZmF1.png)
![](http://imgfz.com/i/pnio1mB.png)

####Ejercicio Navegador web

#####Diagrama de Flujo
#####Seudocodigo

####Algoritmos de Ordenamiento en Python
##### Algoritmo Bubuja en Python
```
# llena el  vector
def llenar(a, tamano):
	print("digite los datos para llenar el vector")
	for i in range(1,tamano+1):
		n = input()
		a[i-1] = n

# define el tamaño del vector
def esc(arreglo, tamano):
	for i in range(1,tamano+1):
		print(arreglo[i-1])

# ordena el vector
def ordenamiento(a, tam):
	for i in range(1,tam+1):
		for j in range(1,tam):
			if a[j-1]>a[j]:
				temp = a[j-1]
				a[j-1] = a[j]
				a[j] = temp

# imnprime el vector
if __name__ == '__main__':
	print("Tamaño del vector: ")
	tam = int(input())
	arreglo = [str() for ind0 in range(tam)]
	llenar(arreglo,tam)
	print("Arreglo desordenado: ")
	esc(arreglo,tam)
	ordenamiento(arreglo,tam)
	print("Arreglo ordenado Acendentemente de menor a mayor: ")
	esc(arreglo,tam)
```
####Algoritmos de Ordenamiento en Python
##### Algoritmo Bubuja Bidireccional en Python
```
miLista = [34,93,19,58,12,28,95,37,23,80,57,82,55,48,21,39,53,65,30,32,84,64,44,68,36]

def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return sort(izquierda)+centro+sort(derecha)
    else:
      return lista

print(miLista)
print(sort(miLista))
```
####Algoritmos de Ordenamiento en Python
##### Algoritmo Gnome Short en Python
```
class Sort:
    def __init__(sort, v):
        sort.v = v
    
    def get_sorted(sort):
        length = len(sort.v)
        i = 1
        while i < length:
            if i == 0:
                i = i + 1
                
            if sort.v[i] >= sort.v[i-1]:
                i += 1
            else:
                sort.v[i], sort.v[i-1] = sort.v[i-1], sort.v[i]
                i -= 1
        return sort.v

def main():
    v = list(map(int, input("Digite los datos del vector a ordenar: ").split(' ')))
    obj = Sort(v)
    sorted_v = obj.get_sorted()
    print("Sorted Array:", end = ' ')
    print(*sorted_v)

if __name__ == "__main__":
    main()
```
####Algoritmos de Ordenamiento en Python
##### Algoritmo Insercion en Python
```
if __name__ == '__main__':
	print("ingrese el tamaño del vector")
	n = int(input())
	vector = [str() for ind0 in range(n)]
	print("ingrese los valores para llenar el vector")
	for i in range(1,n+1):
		vector[i-1] = input()
	k = 1
	for i in range(1,n+1):
			for j in range(1,k+1):
				if vector[k-1]<vector[j-1]:
					auxiliar = vector[k-1]
					vector[k-1] = vector[j-1]
					vector[j-1] = auxiliar
				else:
					vector[k-1] = vector[k-1]
					vector[j-1] = vector[j-1]
			k = k+1
	
	print("vector ordenadon es: ")
	for i in range(1,n+1):
		print(vector[i-1])
```
####Algoritmos de Ordenamiento en Python
##### Algoritmo Peine o Comb Short en Python
```
def comb_sort(nums):
    shrink_fact = 1.3
    gap = len(nums)
    swapped = True
    i = 0

    while gap > 1 or swapped:
        gap = int(float(gap) / shrink_fact)

        swapped = False
        i = 0

        while gap + i < len(nums):
            if nums[i] > nums[i+gap]:
                nums[i], nums[i+gap] = nums[i+gap], nums[i]
                swapped = True
            i += 1
    return nums

num1 = input('Digite los numeros a ordenar separados por una coma:\n').strip()
nums = [int(item) for item in num1.split(',')]
print(comb_sort(nums))
```
####Algoritmos de Ordenamiento en Python
##### Algoritmo QuickShort en Python
```
miLista = [34,93,19,58,12,28,95,37,23,80,57,82,55,48,21,39,53,65,30,32,84,64,44,68,36]

def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return sort(izquierda)+centro+sort(derecha)
    else:
      return lista

print(miLista)
print(sort(miLista))
```
####Algoritmos de Ordenamiento en Python
##### Algoritmo Seleccion en Python
```
if __name__ == '__main__':
	print("ingrese el tamaño del vector")
	n = int(input())
	v = [str() for ind0 in range(n)]
	print("ingrese los valores para llenar el vector")
	for i in range(1,n+1):
		v[i-1] = input()
		for i in range(1,n+1):
			min = i
			for j in range(i+1,n+1):
				if v[min-1]>v[j-1]:
					min = j
			temp = v[min-1]
			v[min-1] = v[i-1]
			v[i-1] = temp

	
	print("vector ordenadon es: ")
	for i in range(1,n+1):
		print(v[i-1])
```
####Algoritmos de Ordenamiento en Python
##### Algoritmo Sell en Python
```
if __name__ == '__main__':
	print("Ingrese el tamaño del vector: ")
	n = int(input())
	v = [str() for ind0 in range(n)]
	print("Ingrese los valores para llenar el vector: ")
	for i in range(1,n+1):
		v[i-1] = input()
	interno = int(n/2)
	while interno!=0:
		for i in range(interno,n+1):
			j = i-interno
			while j>=1:
				k = j+interno
				if v[j-1]<=v[k-1]:
					j = j-1
				else:
					aux = v[j-1]
					v[j-1] = v[k-1]
					v[k-1] = aux
					j = j-interno
		interno = int(interno/2)
	print("El vector ordenado es: ")
	for i in range(1,n+1):
		print(v[i-1]," ")
```
####Caso Covid En NetBeans Java M-V-C
##### Clase Modelo
```
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package co.edu.usbbog.model;

import co.edu.usbbog.controller.Covid;
import java.util.LinkedList;

/**
 *
 * @author hp
 */
public class Pais {

    public LinkedList<Covid> pais = new LinkedList<>();
    
    Covid co = new Covid();
    
    public void coronavirus(){
        
    }

    public void agregar(String nombrePais, int numeroContagiados, int numeroMuertos) {
        Covid c = new Covid(nombrePais, numeroContagiados, numeroMuertos);
        pais.add(c);
    }
    
    public String modificar(String nombrePais, int numeroContagiados, int numeroMuertos){
        Covid c = new Covid(nombrePais, numeroContagiados, numeroMuertos);
        String salida = "";
        for (int i = 0; i < pais.size(); i++) {
            if (nombrePais.equalsIgnoreCase(pais.get(i).getNombrePais())) {
                pais.set(i, c);
            } else {
                salida = "No existe el Pais";
            }            
        }
        return salida;
    }
       
    public String eliminar(String nombrePais){
        String salida = "";
        for (int i = 0; i < pais.size(); i++) {
            if (nombrePais.equalsIgnoreCase(pais.get(i).getNombrePais())) {                
                pais.remove(i);
            } else {
                salida = "No existe el Pais";
            }            
        }
        return salida;
    }

    public String mostrar() {
        String salida = "";
        for (Object listaPais : pais) {
            salida = salida + listaPais
                    + "\n-------------------------------------\n";
        }
        return salida;
    }
    
    public String mostrarTxt(){
        String salida = "";
        
        return salida;
    }
    
    public String mostrarPorContagiados() {
        for (int i = 0; i < pais.size() - 1; i++) {
            for (int j = 0; j < pais.size() - 1; j++) {
                if (pais.get(j).getNumeroContagiados() < pais.get(j + 1).getNumeroContagiados()) {                    
                    Covid aux = pais.get(j + 1);
                    Covid aux2 = pais.get(j);
                    pais.set(j, aux);
                    pais.set(j + 1, aux2);
                }
            }
        }
        return mostrar();
    }
    
    public String mostrarPorMuertes() {
        for (int i = 0; i < pais.size() - 1; i++) {
            for (int j = 0; j < pais.size() - 1; j++) {
                if (pais.get(j).getNumeroMuertos() < pais.get(j + 1).getNumeroMuertos()) {
                    Covid aux = pais.get(j + 1);
                    Covid aux2 = pais.get(j);
                    pais.set(j, aux);
                    pais.set(j + 1, aux2);
                }
            }
        }
        return mostrar();
    }
}
```
##### Clase Vista
```
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package co.edu.usbbog.view;

import co.edu.usbbog.model.Pais;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.LinkedList;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;
import javax.swing.filechooser.FileNameExtensionFilter;

/**
 *
 * @author hp
 */
public class Interfaz extends javax.swing.JFrame {
    
    Pais p = new Pais();
    private File fichero; 
    
    String sep = File.separator;
    Path path = Paths.get("C:"+sep+"Users"+sep+"hp"+sep+"Desktop"+sep+"prueba.txt");

    /**
     * Creates new form Principal
     */
    public Interfaz() {
        initComponents();
        this.setLocationRelativeTo(null);
        this.setVisible(true);

    }
    
    public void cargarExportar(File fich){
        this.fichero = fich;
    }
    
    public void añadirExportar(File fich){
        String nuevoItem;
        this.fichero = fich;
        if (jTextFieldNombrePais.getText().equals("") || jTextFieldNoContagiados.getText().equals("") || jTextFieldNoMuertes.getText().equals("")) {
            JOptionPane.showMessageDialog(this, "ERROR: Faltan datos", "Mensaje de Error", JOptionPane.WARNING_MESSAGE);
            //return;
        }
//        Covid c = new Covid(jTextFieldNombrePais.getText(), Integer.parseInt(jTextFieldNoContagiados.getText()), Integer.parseInt(jTextFieldNoMuertes.getText()));
//        nuevoItem = jTextFieldNombrePais.getText() + " " + jTextFieldNoContagiados.getText() + " " + jTextFieldNoMuertes.getText() + " \n";
//        p.pais.add(c);
//        jTextAreaListaPaises.setText(jTextAreaListaPaises.getText() + nuevoItem);
    }
    
    public void mostrar(){
        jTextAreaListaPaises.setText(p.mostrar());
        jTextAreaListaNoContagiados.setText(p.mostrarPorContagiados());
        jTextAreaListaNoMuertes.setText(p.mostrarPorMuertes());
        
    }
    
    public void agregar(){
        p.agregar(jTextFieldNombrePais.getText(), Integer.parseInt(jTextFieldNoContagiados.getText()), Integer.parseInt(jTextFieldNoMuertes.getText()));
        añadirExportar(fichero);
        JOptionPane.showMessageDialog(null,"Se agrego un elemento a la lista");
        jTextFieldNombrePais.setText(null);
        jTextFieldNoContagiados.setText(null);
        jTextFieldNoMuertes.setText(null);
        mostrar();
    }
    
    public void modificar(){
        p.modificar(jTextFieldNombrePais.getText(), Integer.parseInt(jTextFieldNoContagiados.getText()), Integer.parseInt(jTextFieldNoMuertes.getText()));
        JOptionPane.showMessageDialog(null,"Se modifico un elemento a la lista");
        jTextFieldNombrePais.setText(null);
        jTextFieldNoContagiados.setText(null);
        jTextFieldNoMuertes.setText(null);
        mostrar();
    }   
    
    public void eliminar(){
        String limite = " ";// Elemento que separa el nombre, el usuario y la contraseña dentro del fichero
        String[] trozos; // Dividimos la linea del dichero en unidades independientes
        String nombre; // Nombre del sitio que el usuario ha introducido en el cuadro de texto
        String nombreTrozo; // Nombre del sitio dentro del string trozos
        Boolean encontrado = false;
        LinkedList<String> clonLista = new LinkedList(); // Almacenamos todas las lineas que no son las que queremos borrar, para despues volverlas a guardar
        
        if (jTextFieldNombrePais.getText().equals("")) {
            JOptionPane.showMessageDialog(this, "El campo del nombre del sitio está vacío", "Campo vacío", JOptionPane.INFORMATION_MESSAGE);
        } else {
            try {

                BufferedReader reader = new BufferedReader(new FileReader(fichero));  // Cargamos el fichero para lectura
                String linea = reader.readLine(); // Leemos la primera linea

                if (linea == null) {
                    JOptionPane.showMessageDialog(this, "El fichero está vacío", "Fichero vacío", JOptionPane.INFORMATION_MESSAGE);
                    reader.close();// Cerramos el fichero para lectura
                } else {
                    do {
                        p.eliminar(jTextFieldNombrePais.getText());
                        trozos = linea.split(limite, 3); //Dividimos la linea leida en tres parte

                        nombre = jTextFieldNombrePais.getText().toUpperCase();
                        nombreTrozo = trozos[0].toUpperCase();

                        if (!nombreTrozo.equals(nombre)) {
                            //Comprobamos que la linea no sea vacia. Si es vacia, no la guardamos
                            if (!nombreTrozo.equals("")) {
                                clonLista.add(linea);
                            }
                        } else {
                            encontrado = true;
                        }

                        linea = reader.readLine(); // leemos la siguiente línea

                    } while (linea != null);

                    reader.close();// Cerramos el fichero para lectura

                    if (!encontrado) {
                        JOptionPane.showMessageDialog(this, "No hay ningun sitio con ese nombre", "No está el sitio", JOptionPane.INFORMATION_MESSAGE);
                    } else {
                        BufferedWriter writer = new BufferedWriter(new FileWriter(fichero));
                        while (!clonLista.isEmpty()) {
                            writer.write(clonLista.poll().toString());
                            writer.newLine();
                        }
                        writer.flush();
                        writer.close();
                        JOptionPane.showMessageDialog(this, "Eliminado con éxito", "Eliminado", JOptionPane.INFORMATION_MESSAGE);
                    }
                }
            } catch (IOException e) {
                Logger.getLogger(Interfaz.class.getName()).log(Level.SEVERE, null, e);
            }
        }
        jTextFieldNombrePais.setText(null);
        mostrar();
    }
    
    public void guardar(){
       BufferedWriter writer; //Para escribir en el fichero     

        if (fichero == null) {
            //Activamos el filtro para que nos muestre, por defecto, los archivos de texto
            FileNameExtensionFilter filtro = new FileNameExtensionFilter("Archivos de texto", "txt");
            JFileChooser fileChooserGuardar = new JFileChooser();
            fileChooserGuardar.setFileFilter(filtro);
            fileChooserGuardar.setDialogTitle("Guardar");
            int seleccion = fileChooserGuardar.showSaveDialog(this);

            if (seleccion == JFileChooser.APPROVE_OPTION) {
                fichero = fileChooserGuardar.getSelectedFile();
                fileChooserGuardar.setFileSelectionMode(JFileChooser.FILES_ONLY);
                try {
                    writer = new BufferedWriter(new FileWriter(fichero + ".txt")); // Ponemos .txt para darle extension al archivo que creamos
                    while (!p.pais.isEmpty()) {
                        writer.write(p.pais.poll().toString());
                        writer.newLine();
                    }
                    writer.flush();
                    writer.close();
                } catch (IOException e) {
                    JOptionPane.showMessageDialog(this, "Error al guardar el archivo", "Error guardar archivo", JOptionPane.ERROR_MESSAGE);
                }

                JOptionPane.showMessageDialog(this, "El fichero de texto se ha guardado correctamente con los datos introducidos");
            }
        } else if (!(fichero == null)) // Añadimos al fichero existente
        {
            try {
                writer = new BufferedWriter(new FileWriter(fichero, true));
                while (!p.pais.isEmpty()) {
                    writer.write(p.pais.poll().toString());
                    writer.newLine();
                }
                writer.flush();
                writer.close();
            } catch (IOException e) {
                JOptionPane.showMessageDialog(this, "Error al guardar el archivo", "Error guardar archivo", JOptionPane.ERROR_MESSAGE);
            }
            JOptionPane.showMessageDialog(this, "El fichero de texto se ha guardado correctamente con los datos introducidos");
        } else {
            JOptionPane.showMessageDialog(this, "ERROR: Error al guardar", "Mensaje de Error", JOptionPane.ERROR_MESSAGE);
        }
    }
    
    public void exportar(){        
        // Creamos un filtro para que se reconozcan los archivos de texto
        FileNameExtensionFilter filtro = new FileNameExtensionFilter("Archivos de texto", "txt");
        JFileChooser fileChooserCargar = new JFileChooser();
        fileChooserCargar.setFileFilter(filtro);
        fileChooserCargar.setDialogTitle("Abrir");

        int seleccion = fileChooserCargar.showOpenDialog(this);

        if (seleccion == JFileChooser.APPROVE_OPTION) {
            File file = fileChooserCargar.getSelectedFile();
            cargarExportar(file);               
        }
        String info_archivo = leerArchivo(path.toString());
		if(info_archivo != null){
			//System.out.println("Texto archivo: "+info_archivo);
                        jTextAreaListaPaises.setText(info_archivo);
                }        

        
        
        
        //guardar();
        //mostrar();
        //añadirExportar(fichero);
    }
    
    public static String leerArchivo(String path){
		try{
			FileReader reader = new FileReader(path);
			BufferedReader buffer = new BufferedReader(reader);
			
			String linea = buffer.readLine();
			String texto = linea;
			while(linea != null){
				//System.out.println(linea);
				linea = buffer.readLine();
				if(linea!= null)
					texto = texto + linea+"\n";
			}			
			return texto;
		}catch(Exception e){
			System.out.println("Hubo un error leyendo el archivo." +e.getMessage());
		}
		return null;
	}
    
    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">                          
    private void initComponents() {

        jScrollPaneListaNoMuertes = new javax.swing.JScrollPane();
        jTextAreaListaNoMuertes = new javax.swing.JTextArea();
        jScrollPaneListaNoContagiados = new javax.swing.JScrollPane();
        jTextAreaListaNoContagiados = new javax.swing.JTextArea();
        jLabelListaNoMuertes = new javax.swing.JLabel();
        jLabelListaNoContagiados = new javax.swing.JLabel();
        jLabelNoMuertes = new javax.swing.JLabel();
        jTextFieldNoMuertes = new javax.swing.JTextField();
        jLabelNombrePais = new javax.swing.JLabel();
        jTextFieldNombrePais = new javax.swing.JTextField();
        jLabelNoContagiados = new javax.swing.JLabel();
        jTextFieldNoContagiados = new javax.swing.JTextField();
        jButtonAgregar = new javax.swing.JButton();
        jButtonEliminar = new javax.swing.JButton();
        jButtonModificar = new javax.swing.JButton();
        jPanel1 = new javax.swing.JPanel();
        jButtonMostrar = new javax.swing.JButton();
        jButtonGuardar = new javax.swing.JButton();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTextAreaListaPaises = new javax.swing.JTextArea();
        jButtonExportar = new javax.swing.JButton();
        jLabelTituloProyecto = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jTextAreaListaNoMuertes.setColumns(20);
        jTextAreaListaNoMuertes.setRows(5);
        jScrollPaneListaNoMuertes.setViewportView(jTextAreaListaNoMuertes);

        getContentPane().add(jScrollPaneListaNoMuertes, new org.netbeans.lib.awtextra.AbsoluteConstraints(600, 110, 210, 540));

        jTextAreaListaNoContagiados.setColumns(20);
        jTextAreaListaNoContagiados.setRows(5);
        jScrollPaneListaNoContagiados.setViewportView(jTextAreaListaNoContagiados);

        getContentPane().add(jScrollPaneListaNoContagiados, new org.netbeans.lib.awtextra.AbsoluteConstraints(60, 110, 210, 540));

        jLabelListaNoMuertes.setFont(new java.awt.Font("Dialog", 1, 18)); // NOI18N
        jLabelListaNoMuertes.setText("Lista Paises Con No.Muertes");
        getContentPane().add(jLabelListaNoMuertes, new org.netbeans.lib.awtextra.AbsoluteConstraints(580, 70, -1, -1));

        jLabelListaNoContagiados.setFont(new java.awt.Font("Dialog", 1, 18)); // NOI18N
        jLabelListaNoContagiados.setText("Lista Paises Con No.Contagiados");
        getContentPane().add(jLabelListaNoContagiados, new org.netbeans.lib.awtextra.AbsoluteConstraints(30, 70, -1, -1));

        jLabelNoMuertes.setFont(new java.awt.Font("Dialog", 0, 14)); // NOI18N
        jLabelNoMuertes.setText("Número De Muertes:");
        getContentPane().add(jLabelNoMuertes, new org.netbeans.lib.awtextra.AbsoluteConstraints(380, 230, -1, -1));
        getContentPane().add(jTextFieldNoMuertes, new org.netbeans.lib.awtextra.AbsoluteConstraints(340, 260, 200, 30));

        jLabelNombrePais.setFont(new java.awt.Font("Dialog", 0, 14)); // NOI18N
        jLabelNombrePais.setText("Nombre País:");
        getContentPane().add(jLabelNombrePais, new org.netbeans.lib.awtextra.AbsoluteConstraints(400, 90, -1, -1));
        getContentPane().add(jTextFieldNombrePais, new org.netbeans.lib.awtextra.AbsoluteConstraints(340, 120, 200, 30));

        jLabelNoContagiados.setFont(new java.awt.Font("Dialog", 0, 14)); // NOI18N
        jLabelNoContagiados.setText("Número De Contagiados:");
        getContentPane().add(jLabelNoContagiados, new org.netbeans.lib.awtextra.AbsoluteConstraints(360, 160, -1, -1));
        getContentPane().add(jTextFieldNoContagiados, new org.netbeans.lib.awtextra.AbsoluteConstraints(340, 190, 200, 30));

        jButtonAgregar.setText("Agregar");
        jButtonAgregar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonAgregarActionPerformed(evt);
            }
        });
        getContentPane().add(jButtonAgregar, new org.netbeans.lib.awtextra.AbsoluteConstraints(300, 300, -1, -1));

        jButtonEliminar.setText("Eliminar");
        jButtonEliminar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonEliminarActionPerformed(evt);
            }
        });
        getContentPane().add(jButtonEliminar, new org.netbeans.lib.awtextra.AbsoluteConstraints(510, 300, -1, -1));

        jButtonModificar.setText("Modificar");
        jButtonModificar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonModificarActionPerformed(evt);
            }
        });
        getContentPane().add(jButtonModificar, new org.netbeans.lib.awtextra.AbsoluteConstraints(405, 300, -1, -1));

        jPanel1.setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        jButtonMostrar.setText("Mostrar");
        jButtonMostrar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonMostrarActionPerformed(evt);
            }
        });
        jPanel1.add(jButtonMostrar, new org.netbeans.lib.awtextra.AbsoluteConstraints(310, 620, -1, -1));

        jButtonGuardar.setText("Guardar");
        jButtonGuardar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonGuardarActionPerformed(evt);
            }
        });
        jPanel1.add(jButtonGuardar, new org.netbeans.lib.awtextra.AbsoluteConstraints(400, 620, -1, -1));

        jTextAreaListaPaises.setColumns(20);
        jTextAreaListaPaises.setRows(5);
        jScrollPane1.setViewportView(jTextAreaListaPaises);

        jPanel1.add(jScrollPane1, new org.netbeans.lib.awtextra.AbsoluteConstraints(330, 340, 220, 260));

        jButtonExportar.setText("Exportar");
        jButtonExportar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButtonExportarActionPerformed(evt);
            }
        });
        jPanel1.add(jButtonExportar, new org.netbeans.lib.awtextra.AbsoluteConstraints(500, 620, -1, -1));

        jLabelTituloProyecto.setFont(new java.awt.Font("Dubai", 1, 48)); // NOI18N
        jLabelTituloProyecto.setText("EL CORONAVIRUS ALIAS COVID-19");
        jPanel1.add(jLabelTituloProyecto, new org.netbeans.lib.awtextra.AbsoluteConstraints(60, 10, 760, 60));

        getContentPane().add(jPanel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 870, 680));

        pack();
    }// </editor-fold>                        

    private void jButtonAgregarActionPerformed(java.awt.event.ActionEvent evt) {                                               
        agregar();
    }                                              

    private void jButtonModificarActionPerformed(java.awt.event.ActionEvent evt) {                                                 
        modificar();
    }                                                

    private void jButtonEliminarActionPerformed(java.awt.event.ActionEvent evt) {                                                
        eliminar();      
    }                                               

    private void jButtonMostrarActionPerformed(java.awt.event.ActionEvent evt) {                                               
        mostrar();
    }                                              

    private void jButtonGuardarActionPerformed(java.awt.event.ActionEvent evt) {                                               
        guardar();
    }                                              

    private void jButtonExportarActionPerformed(java.awt.event.ActionEvent evt) {                                                
        exportar();
    }                                               

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Interfaz.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Interfaz.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Interfaz.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Interfaz.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Interfaz().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify                     
    private javax.swing.JButton jButtonAgregar;
    private javax.swing.JButton jButtonEliminar;
    private javax.swing.JButton jButtonExportar;
    private javax.swing.JButton jButtonGuardar;
    private javax.swing.JButton jButtonModificar;
    private javax.swing.JButton jButtonMostrar;
    private javax.swing.JLabel jLabelListaNoContagiados;
    private javax.swing.JLabel jLabelListaNoMuertes;
    private javax.swing.JLabel jLabelNoContagiados;
    private javax.swing.JLabel jLabelNoMuertes;
    private javax.swing.JLabel jLabelNombrePais;
    private javax.swing.JLabel jLabelTituloProyecto;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPaneListaNoContagiados;
    private javax.swing.JScrollPane jScrollPaneListaNoMuertes;
    private javax.swing.JTextArea jTextAreaListaNoContagiados;
    private javax.swing.JTextArea jTextAreaListaNoMuertes;
    private javax.swing.JTextArea jTextAreaListaPaises;
    private javax.swing.JTextField jTextFieldNoContagiados;
    private javax.swing.JTextField jTextFieldNoMuertes;
    private javax.swing.JTextField jTextFieldNombrePais;
    // End of variables declaration                   

}
```
##### Clase Controlador
```
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package co.edu.usbbog.controller;

/**
 *
 * @author hp
 */
public class Covid {

    String nombrePais;
    int numeroContagiados;
    int numeroMuertos;

    public Covid() {
    }

    public Covid(String nombrePais, int numeroContagiados, int numeroMuertos) {
        this.nombrePais = nombrePais;
        this.numeroContagiados = numeroContagiados;
        this.numeroMuertos = numeroMuertos;
    }

    public String getNombrePais() {
        return nombrePais;
    }

    public void setNombrePais(String nombrePais) {
        this.nombrePais = nombrePais;
    }

    public int getNumeroContagiados() {
        return numeroContagiados;
    }

    public void setNumeroContagiados(int numeroContagiados) {
        this.numeroContagiados = numeroContagiados;
    }

    public int getNumeroMuertos() {
        return numeroMuertos;
    }

    public void setNumeroMuertos(int numeroMuertos) {
        this.numeroMuertos = numeroMuertos;
    }

 
    @Override
    public String toString() {
        return "País: " + nombrePais + 
                "\nNumero Contagiados: " + numeroContagiados +
                "\nNumero Muertes: " + numeroMuertos;        
    }

}

```
####Ejemplo  recursivo
##### Codigo en C++

```
int factorial(int n){
if(n==0){
return 1; //Caso Base
}
else {
return n * factorial(n-1);  //Fórmula Recursiva
}
}
```
####Ejemplo  iterativo
##### Codigo en C++
```
f = 0; i = 1;
while(i <= N)
{
f = f + i;
i = i + 1;
}
```
####Parte 2 
#####Algoritmo que calcule el factorial de un número.
###### Codigo en C++
```
Recursivo:
#include <iostream>
using namespace std;
long double factorial(int);
int main()
{   int n;
    cout << "Introduzca numero: ";
    cin >> n;
    cout << "factorial: " << factorial(n) << endl;
    system("pause");
}
long double factorial(int n)
{
    long double fact;
    if (n==0)
        return 1;
    else
         return n*factorial(n-1);
}
```
```
Interativo:
#include <iostream>
using namespace std;
int main(){
    int i,fact=1,num;
         cout<<"Ingresa un numero"<<endl;
        cin>>num;
        for(i=1;i<num+1;i++){
            fact=fact*i;
        }
         cout<<fact;
      return 0;
}
```
#####Algoritmo que calcule un número de la serie Fibonacci.
###### Codigo en C++
```
Recursivo:
#include <iostream>

using namespace std;

int fibonacci(int n);

int main(int argc, char *argv[]) {
 int n;
 cout<<"ingrese numero"<<endl;
 cin>>n;
 
 cout<<"el resultado es:"<<fibonacci(n)<<endl;
 return 0;
}

int fibonacci(int a){
 if((a==1 || a==2)){
  return 1;
 }
 else{
  return(fibonacci(a-1)+fibonacci(a-2));
 }
 
}
```
```
Interativo:
#include<iostream>
using namespace std;

int main() {
	int a, b, c, i, n;
	cout << "Ingrese el numero para hallai serie: ";
	cin >> n;
	a = 0;
	b = 1;
	for (i=1;i<=n;i++) {
		cout << a << endl;
		c = a+b;
		a = b;
		b = c;
	}
	return 0;
}
```
#####Algoritmo que permita invertir un número. Ejemplo: Entrada: 56789 
###### Codigo en C++
```
Recursivo:
#include <iostream>

using namespace std;

int Invertir(int n, int t)
{
return n == 0 ? t : Invertir(n / 10, t * 10 + n % 10); //OPERADORTERNARIO
}
int main (){

     int num;
	 cout << "Ingrese un numero: ";
	 cin >> num;
	 cout << "Numero invertido: " << Invertir(num, 0) << endl;
	 system ("pause");
	 return 0;

}

Iterativo:
#include <iostream>
#include<iomanip>

using namespace std;

int main(int) {
	int numero;
	 cout<<"Ingrese Numero a Invertir: ";
	 cin>>numero;
	 cout<<"Numero numero invertido es: ";
	 do{
	 	cout<<(numero%10);
	 	numero/=10;
	 	
	 }while( numero !=0);
	
	
	return 0;
}
```
#####Algoritmo que permita sumar los elementos de un vector.
###### Codigo en C++
```
Recursivo:
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
Iterativo:
#include <iostream>
#include "conio.h"

using namespace std;

int main(){
	int numeros[] = {1,2,3,4,5};
	int suma=0;
	
	for(int i=0; i<5; i++){
		suma += numeros[i];
	}
	cout << "La suma de los numeros del  vector es: "<<suma;
	getch();
	return 0;
}
```
##### Algoritmo que muestre el número menor de un vector. 
###### Codigo en C++
```
Recursivo:
#include <iostream>
using namespace std;
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
	int vector[5],i,menor;
	for(i=0;i<5;i++){
		cout<<"X["<<i+1<<"]= ";
		cin>>vector[i];
	}
	menor = min(vector, vector[0], 0);
	
	
	cout<<"El menor es:"<<menor;
		return 0;
}
Iterativo:
#include<iostream>
#include<cstdlib>
using namespace std;
int main() {
	int i;
	float mayor;
	float menor;
	float v[20];
	int x;
	for (i=1;i<=20;i++) {
		v[i-1] = (rand()%20)+1;
	}
	mayor = v[0];
	menor = v[0];
	for (x=1;x<=20;x++) {
		if (v[x-1]>mayor) {
			mayor = v[x-1];
		}
		if (v[x-1]<menor) {
			menor = v[x-1];
		}
	}
	for (i=1;i<=20;i++) {
cout << "El vector en su posicion " << i << " Es igual a " << v[i-1] << endl;
	}
	cout << "El numero mayor es: " << mayor << endl;
	cout << "El numero menor es: " << menor << endl;
	return 0;
}
```
#####Algoritmo que permita sumar, restar, multiplicar, dividir y calcular la potencia dos números naturales
###### Codigo en C++
```
Recursivo:
#include <iostream>
#include<cstdlib>
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
int potencia(int a, int b){
	if (b==1){
		return (a);
		
	}else{
		a=a*potencia(a,b-1);
		return (a);
	}
}

int main() {
	system("color a");
	int a;
	int b;
	cout<<"Digite el primer numero: "<<endl;
	cin>>a;
	cout<<"Digite el segundo numero: "<<endl;
	cin>>b;
	cout<<"La suma es: "<<a<<"+"<<b<<"="<<suma(a,b)<<endl;
	cout<<"La resta es: "<<a<<"-"<<b<<"="<<resta(a,b)<<endl;
	cout<<"La multiplicacion es: "<<a<<"*"<<b<<"="<<multi(a,b)<<endl;
	cout<<"La division es: "<<a<<"/"<<b<<"="<<division(a,b)<<endl;
	cout<<"La potencia es: "<<a<<"^"<<b<<"="<<potencia(a,b)<<endl;
	system ("pause");
	return 0;
}

Iterativo:
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
```
#####g.	Algoritmo que permita buscar un elemento tipo String en una matriz de N*N 
###### Codigo en Java
```
package string;


import java.util.Arrays;
import java.util.Scanner;



public class string {

    static Scanner s = new Scanner(System.in);


    public static void main(String[] args) {
        System.out.println("BUSCAR ELEMENTO ITERATIVO = " + buscarElemento(llenarMatriz(s.nextInt()), s.next().toUpperCase()));
        System.out.println("BUSCAR ELEMENTO RECURSIVO = " + buscarelementoRecursivo(llenarMatrizR(0, 0, s.nextInt(), null), s.next().toUpperCase(), 0, 0));
    }

    private static String[][] llenarMatriz(int n) {
        String[][] matriz = new String[n][n];
        for (String[] matriz1 : matriz) {
            for (int j = 0; j < matriz[0].length; j++) {
                matriz1[j] = s.next().toUpperCase();
            }
        }
        return matriz;
    }

    private static String[][] llenarMatrizR(int i, int j, int ext, String[][] matriz) {
        if (i == 0 && j == 0) {
            String[][] m = new String[ext][ext];
            m[i][j] = s.next().toUpperCase();
            return llenarMatrizR(i, j + 1, ext, m);
        } else if (i != ext) {
            matriz[i][j] = s.next().toUpperCase();
            if (j == ext - 1) {
                return llenarMatrizR(i + 1, 0, ext, matriz);
            } else {
                return llenarMatrizR(i, j + 1, ext, matriz);
            }
        } else {
            return matriz;
        }
    }


    private static String buscarElemento(String[][] matriz, String elemento) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[0].length; j++) {
                if (matriz[i][j].equals(elemento)) {
                    return elemento + " SE ENCUENTRA EN LA POSICIÃ“N [" + (i + 1) + "]-[" + (j + 1) + "]";
                }
            }
        }
        return "NO SE ENCONTRO A " + elemento + " EN LA MATRIZ";
    }

    private static String buscarelementoRecursivo(String[][] matriz, String elemento, int i, int j) {
        if (matriz[i][j].equals(elemento)) {
            return elemento + " SE ENCUENTRA EN LA POSICIÃ“N [" + (i + 1) + "]-[" + (j + 1) + "]";
        } else if (i == matriz.length - 1 && j == matriz.length - 1) {
            return "NO SE ENCONTRO A " + elemento + " EN LA MATRIZ";
        } else {
            if (j == matriz.length - 1) {
                return buscarelementoRecursivo(matriz, elemento, i + 1, 0);
            } else {
                return buscarelementoRecursivo(matriz, elemento, i, j + 1);
            }
        }
    }
}
```
####Parte 3
#####PARTE 3 RESOLVER DE MANERA RECURSIVA
Ejercicio 1 - Palíndromo: 
Escriba un algoritmo recursivo que verifique si dado un String es palíndromo o no (Un Palíndromo es una palabra, frase, número y otra secuencia de caracteres los cuales se leen de la misma manera de derecha a izquierda o de izquierda a derecha. Como por ejemplo madam o racecar.

###### Codigo en C++
```
Recursivo:
#include <iostream>
#include<cstdlib>
#include<string.h>

int palindrome(char palabra[], int inicio, int fin){
	if(inicio>=fin)
	return 1;
	if(palabra[inicio]==palabra[fin])
	palindrome(palabra, inicio+1, fin-18);
	else return (0);
}

int main(void) {
	system ("color a");
	char palabra[50];
	int tamano,pal;
	std::cout<<"Digite su palabra o Numero: ";
	std::cin.getline(palabra,50);
	tamano=strlen(palabra);
	pal=palindrome(palabra,0,tamano-1); 
	if(pal==1)
	std::cout<<"La palabra o numero SI es  palindrome";
	else if(pal==0)
	std::cout<<"la palabra o numero NO es palindrome";	
	return 0;
}
```
#####Ejercicio 2 - Permutaciones: 
Desarrollar un algoritmo que muestre por consola todas las permutaciones que se pueden realizar con los caracteres de una cadena de cualquier longitud. La cadena la ingresa el usuario por consola o por línea de comandos y no tendrá caracteres repetidos. 
Por ejemplo, si la cadena ingresada fuese “ABC” entonces el programa debería arrojar las siguientes 6 líneas, en cualquier orden: 
ABC 
ACB 
BAC 
BCA 
CAB 
CBA 
Y si la cadena fuese “ABCD ” entonces la salida debería ser: 
ABCD 
ABDC 
ACBD 
ACDB 
ADBC 
ADCB 
BACD 
BADC

###### Codigo en C++
```
Recursivo:
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
```
#####Ejercicio 3 - Canción sin vocales: 
Hacer la lectura de un archivo plano en donde este un texto de una canción, usted debe leer la canción, eliminar con una función recursiva todas las vocales que tenga este texto y volver a escribir un archivo plano con la misma canción, pero sin ninguna vocal. Al final tendrá dos archivos planos, uno con la canción con vocales y otro con la canción sin vocales.

###### Codigo en C++
```
#include <iostream>
#include <fstream>
#include <conio.h>
#include <string.h>
#include <stdio.h>

using namespace std;

int main(){
	char a[1],e[1],i[1],o[1],u[1];
	char m;
	string linea;
	ifstream salida;
	ifstream archivo_entrada;
	archivo_entrada.open("Cancion.txt");
	salida.open("Cancion.txt",ios::in);
	ofstream entrada;
	entrada.open("CancionesN.txt",ios::out);
	
	
	if(salida.fail()){
		cout<<"error al abrir archivo";
		getch();
		while (getline(archivo_entrada,linea))
		cout<<linea<<endl;
		cout<<"\n"<<endl;
	}
	else{
		char aux[5];
		
		cout<<"vocal a borrar: ";
		cin>>aux;
		salida>>a>>e>>i>>o>>u;
		while(!salida.eof()){
			
			salida>>e>>i>>o>>u;
			
			if(strcmp (aux,a)==0){
				cout<<"borro";
				getch();
			}else{
				entrada<<m<<endl;
			}
			salida>>a;
			
			
	
	}
	
	entrada.close();
	salida.close();
	
	}
```
#####Ejercicio 4 - Palabras repetidas en un poema
Hacer la lectura de un archivo plano en donde este un texto de un poema (mínimo de 4 párrafos), usted debe leer el poema, recorrer el texto e identificar cuantas palabras repetidas hay de cada tipo, cuantos espacios tiene el texto, cuantas consonantes tiene el texto, cuantas vocales tiene el texto y cuantas letras en total. 
Ejemplo: 
Cantidad de vocales: 53 
Cantidad de consonantes: 45 
Cantidad de espacio: 15 
Cantidad de letras: 98 
Palabras repetidas: 
Hola: 4 veces 
De: 19 veces 
Para: 22 veces 
Semáforo: 1 vez 
Casa: 3 veces 
Historia:1 vez 
Siempre: 18 veces

###### Codigo en Java
```
package poema;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class poema {
    
    static int v = 0, l = 0, e = 0;
    static ArrayList<Palabra> palabrasEncontradas = new ArrayList<>();
    static String aeiou = "aeiouÃ¡Ã©Ã­Ã³Ãº", sign = ",.Â¿?!Â¡':;'";

    public static void main(String[] args) throws IOException {
        // Revisar Ruta del Archivo
        leerArchivo("D:/Documents/NetBeansProjects/iterativosRecursivos/poema.txt", true, null, null);
        System.out.println("-----LISTA-----");
        contadorMuestra();
        System.out.println("Palabra repetidas:");
        listarPalabras(0);
    }

    public static void leerArchivo(String archivo, boolean flag, FileReader f, BufferedReader b) throws FileNotFoundException, IOException {
        String verso = "";
        if (flag) {
            FileReader file = new FileReader(archivo);
            BufferedReader buffer = new BufferedReader(file);
            verso = buffer.readLine();
            System.out.println("      Y TE BUSQUE POR PUEBLOS");
            System.out.println(verso);
            contarVocalesConsonantesEspacioa(verso, 0, verso.length() - 1);
            palabras(verso, 0, verso.length() - 1, "");
            leerArchivo(archivo, false, file, buffer);
        } else {
            verso = b.readLine();
            if (verso != null) {
                System.out.println(verso);
                contarVocalesConsonantesEspacioa(verso, 0, verso.length() - 1);
                palabras(verso, 0, verso.length() - 1, "");
                leerArchivo(archivo, false, f, b);
            } else {
                System.out.println("                       POR: Jose Marti");
                b.close();
            }
        }
    }

    private static void palabras(String verso, int i, int exts, String palabra) {
        if (i == exts) {
            addLista(palabra);
        } else {
            String letra = String.valueOf(verso.charAt(i)).toLowerCase();
            if (palabra.length() == 1){
                palabra = palabra.toUpperCase();
            }
            if (vocales(letra, aeiou, 0, aeiou.length() - 1) || letras(letra) && !espacios(letra)) {
                palabra += letra;
                palabras(verso, i + 1, exts, palabra);
            } else if (!palabra.equals("")) {
                addLista(palabra);
                palabras(verso, i + 1, exts, "");
            }
        }
    }

    public static void addLista(String palabra) {
        if (palabrasEncontradas.isEmpty()) {
            Palabra cl1 = new Palabra(palabra, 1);
            palabrasEncontradas.add(cl1);
        }else if (existsPalabra(0, palabra)) {
            int pos = ubicacionPalabra(0, palabra);
            Palabra cl = new Palabra(palabra, palabrasEncontradas.get(pos).getNum() + 1);
            palabrasEncontradas.set(pos, cl);
        } else {
            Palabra cl1 = new Palabra(palabra, 1);
            palabrasEncontradas.add(cl1);
        }
    }
    
    private static void contarVocalesConsonantesEspacioa(String verso, int i, int exts) {
        if (i == exts) {
            String letra = String.valueOf(verso.charAt(i)).toLowerCase();
            if (vocales(letra, aeiou, 0, aeiou.length() - 1)) {
                v++;
            } else if (espacios(letra)) {
                e++;
            } else if (letras(letra)) {
                l++;
            }            
        } else {
            String letra = String.valueOf(verso.charAt(i)).toLowerCase();
            if (vocales(letra, aeiou, 0, aeiou.length() - 1)) {
                v++;
                contarVocalesConsonantesEspacioa(verso, i + 1, exts);
            } else if (espacios(letra)) {
                e++;
                contarVocalesConsonantesEspacioa(verso, i + 1, exts);
            } else if (letras(letra)) {
                l++;
                contarVocalesConsonantesEspacioa(verso, i + 1, exts);
            } else {
                contarVocalesConsonantesEspacioa(verso, i + 1, exts);
            }
        }
    }
    
    private static boolean vocales(String letra, String aeiou, int i, int exts) {
        if (String.valueOf(aeiou.charAt(i)).equals(letra)) {
            return true;
        } else if (i == exts && !String.valueOf(aeiou.charAt(i)).equals(letra)) {
            return false;
        } else if (i == exts && String.valueOf(aeiou.charAt(i)).equals(letra)) {
            return true;
        } else {
            return vocales(letra, aeiou, i + 1, exts);
        }
    }
    
    private static boolean espacios(String letra) {
        return letra.equals(" ");
    }
    
    private static boolean letras(String letra) {
        return !signos(letra, sign, 0, sign.length() - 1);
    }
    
    private static boolean signos(String letra, String sign, int i, int exts) {
        if (String.valueOf(sign.charAt(i)).equals(letra)) {
            return true;
        } else if (i == exts && !String.valueOf(sign.charAt(i)).equals(letra)) {
            return false;
        } else if (i == exts && String.valueOf(sign.charAt(i)).equals(letra)) {
            return true;
        } else {
            return signos(letra, sign, i + 1, exts);
        }
    }
    
    private static void contadorMuestra() {
        System.out.println("-VOCALES: " + v + "\n"
                + "-CONSONANTES: " + l + "\n"
                + "-ESPACIOS: " + e + "\n"
                + "-LETRAS: " + (v + l));
    }
    
    private static void listarPalabras(int i) {
        if (i == 0){
           Collections.sort(palabrasEncontradas);
        }
        if (i == palabrasEncontradas.size() - 1) {
            System.out.println(" - " + palabrasEncontradas.get(i).toString());
        } else {
            System.out.println(" - " + palabrasEncontradas.get(i).toString());
            listarPalabras(i + 1);
        }
    }
    
    private static boolean existsPalabra(int i, String palabra) {
        if (palabrasEncontradas.isEmpty()){
            return false;
        } else if (i == palabrasEncontradas.size() - 1 && palabrasEncontradas.get(i).getPalabra().equals(palabra)) {
            return true;
        } else if (i == palabrasEncontradas.size() - 1 && !palabrasEncontradas.get(i).getPalabra().equals(palabra)) {
            return false;
        } else if (palabrasEncontradas.get(i).getPalabra().equals(palabra)) {
            return true;
        } else {
            return existsPalabra(i + 1, palabra);
        }
    }
    
    private static int ubicacionPalabra(int i, String palabra) {
        if (palabrasEncontradas.isEmpty()){
            return -2;
        }else if (i == palabrasEncontradas.size() - 1 && palabrasEncontradas.get(i).getPalabra().equals(palabra)) {
            return i;
        } else if (i == palabrasEncontradas.size() - 1 && !palabrasEncontradas.get(i).getPalabra().equals(palabra)) {
            return -1;
        } else if (palabrasEncontradas.get(i).getPalabra().equals(palabra)) {
            return i;
        } else {
            return ubicacionPalabra(i + 1, palabra);
        }
    }
    
    public static class Palabra implements Comparable<Palabra>{
        String palabra;
        int num;
        public Palabra(String palabra, int num) {
            this.palabra = palabra;
            this.num = num;
        }
        
        public String getPalabra() {
            return palabra;
        }
        
        public int getNum() {
            return num;
        }

        public void setNum(int num) {
            this.num = num;
        }

        @Override
        public String toString() {
            if (num == 1) {
                return palabra + ": " + num + " vez";
            } else {
                return palabra + ": " + num + " veces";
            }
        }
        @Override
        public int compareTo(Palabra t) {
            if (num > t.num) {
                return -1;
            } else if (num < t.num) {
                return 1;
            } else {
                return 0;
            }
        }
    }
}
```
#####Ejercicio 5 - El juego de los discos: La Torre de Hanoi: 
El juego, en su forma más tradicional, consiste en tres varillas verticales. En una de las varillas se apila un número indeterminado de discos (elaborados de madera) que determinará la complejidad de la solución, por regla general se consideran ocho discos. Los discos se apilan sobre una varilla en tamaño decreciente. No hay dos discos iguales, y todos ellos están apilados de mayor a menor radio en una de las varillas, quedando las otras dos varillas vacantes. El juego consiste en pasar todos los discos de la varilla ocupada (es decir la que posee la torre) a una de las otras varillas vacantes. Para realizar este objetivo, es necesario seguir tres simples reglas: 
-Sólo se puede mover un disco cada vez. 
-Un disco de mayor tamaño no puede descansar sobre uno más pequeño que él mismo. 
-Sólo puedes desplazar el disco que se encuentre arriba en cada varilla.
Usted debe realizar: 
• Usando interfaz grafica o por consola realizar la dinámica del juego para hacerlo con 3 varillas verticales o torres y 4 discos. 
• Usted gana si pasa todos los discos cumpliendo con las reglas mencionadas de la torre 1 a la torre 3 
• En la siguiente grafica se ve el juego pero con 3 discos (recuerde que su algoritmo debe ser con 4).

###### Codigo en C++
```
#include <iostream>

using namespace std;
int hanoy(int disco, int varilla1, int varilla2, int varilla3){
	if(disco==1){
		cout<<"Mueva el disco de la varilla: "<<varilla1<<" hacia la varilla: "<<varilla3<<endl;
	}
	else{
		hanoy(disco-1, varilla1, varilla3, varilla2);
		cout<<"Mueva el disco de la varilla: "<<varilla1<<" hacia la varilla: "<<varilla3<<endl;
		hanoy(disco-1, varilla2, varilla1, varilla3);
	}
	
}

int main(){
	int Varilla1 = 1, Varilla2 = 2, Varilla3 = 3, Disco = 0;
	cout<<"Digite los discos con los que quiere jugar: ";
	cin>>Disco;
	hanoy(Disco, Varilla1, Varilla2, Varilla3);

return 0;
}
```

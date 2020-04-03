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



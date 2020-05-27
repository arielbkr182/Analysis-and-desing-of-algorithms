#sintaxis de while
import math as m

i=1
while i<=10:
    print("ejecucion" + str(i))
    i=i+1
print("fin programa")

#
edad=int(input("introduce la edad: "))

while edad<0:
    print("edad negativa")
    edad=int(input("introduce la edad: "))
print("gracias pase")
print("edad: " + str(edad))

#ciclo while con or
edad=int(input("introduce la edad: "))

while edad<5 or edad>100:
    print("edad negativa")
    edad=int(input("introduce la edad: "))
print("gracias pase")
print("edad: " + str(edad))



#solucion matematica con while 
print("programa de calculo de raiz")
numero=int(input("instroduce un numeropor favor: "))
intentos=0
while numero<0:
    print("no se puede hallar la raiz de un negativo")
    if intentos==2:
        print("intentos maximos permitios fin fel programa")
        break;
    numero=int(input("introduceun nuemro por favor: "))
    if numero<0:
        intentos=intentos+1
if intentos<2:
    solucion=m.sqrt(numero)
    print("la raiz es " + str(numero) + " es " + str(solucion))
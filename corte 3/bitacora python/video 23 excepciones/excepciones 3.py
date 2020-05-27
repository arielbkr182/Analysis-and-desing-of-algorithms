import math
def Raiz(num1):
    if num1<0:
        raise ValueError ("el numero no pude ser negativo")
    else:
        return math.sqrt(num1)
op1=(int(input("introduce un numero: ")))
try:
    print(Raiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
print("fin del programa")

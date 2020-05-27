#Excepciones
def suma(num1, num2):
    return num1+num2
def resta(num1, num2):
    return num1-num2
def multi(num1, num2):
    return num1*num2
def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("no existe la diviciion por cero")
        return "operacion erronea"
while True:
            try:     
                op1=(int(input("intrudusca el primer numero: ")))
                op2=(int(input("intrusca el segundo numero: ")))
                break
            except ValueError:
                print("los valores introducidos no son correctos")

operacion=input("introdusca la operacion a realizar(suma,resta,multi,divide): ")

if operacion=="suma":
    print(suma(op1,op2))
elif operacion=="resta":
    print(resta(op1,op2))
elif operacion=="multi":
    print(multi(op1,op2))
elif operacion=="divide":
    print(divide(op1,op2))
else:
    print("operacion no contemplada")

print("operacion ejecutada")


#Ejemplo 2
def divide():
    try:
        op1=(float(input("primer numero")))
        op2=(float(input("segundo numero")))
        print("la divion es: " + str(op1/op2))
    finally:
        print("calculo finalizado")

divide()
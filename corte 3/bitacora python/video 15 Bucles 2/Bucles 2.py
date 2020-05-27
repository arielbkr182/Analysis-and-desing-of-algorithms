#imprecion vertical con bucles
for i in ["pildoras", "informaticas", 3]:
    print (i, end="   ")

# true false con  bucles
email=False
for i in "ariel@gmail.com":
    if(i=="@"):
        email=True
if email==True:
    print("email correcto")
else:
    print("email incorrecto")


# true false con con entrada por teclado
email=False
miemail=input("ingrese correo: ")
for i in miemail:
    if(i=="@"):
        email=True
if email==True:
    print("email correcto")
else:
    print("email incorrecto")


# true false con con entrada por teclado y contador con or 
contador=0
miemail=input("ingrese correo: ")
for i in miemail:
    if(i=="@" or i=="."):
        contador=contador+1
if contador==2:
    print("email correcto")
else:
    print("email incorrecto")


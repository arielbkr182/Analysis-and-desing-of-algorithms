#condicional if-else
print("verificacion de acceso")

edad_usuario=int(input("introucior edad: "))
if edad_usuario<18:
    print("menor de edad")
else:
    print("mayor de edad")
print("fin del sistema")

#condicional if-else anidados 
print("verificacion de acceso")
nota_alumno=int(input("introucior edad: "))

if nota_alumno<5:
    print("insufisiente")
elif nota_alumno<6:
    print("sufisiente")
elif nota_alumno<7:
    print("notable")
elif nota_alumno<9:
    print("notable")
else:
    print("sobresaliente")

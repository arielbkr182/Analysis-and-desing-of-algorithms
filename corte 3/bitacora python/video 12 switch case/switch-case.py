#ciclo normal 
edad=7
if edad<100:
    print("edad correcta")
else:
    print("edad incorrecta")

#concatenacion dentro de una condicion 
edad=7
if 0<edad<100:
    print("edad correcta")
else:
    print("edad incorrecta")

#ciclos concatenados con IFELSE(ELIF)
salario_presidente=int(input("digite el salario del presidente: "))
print("salario presidente: " + str(salario_presidente))

salario_director=int(input("digite el salario director: "))
print("salario director: " + str(salario_director))

salario_jefe_area=int(input("digite el salario jefe area: "))
print("salario jefe_area: " + str(salario_jefe_area))

salario_administrativo=int(input("digite el salario adminitrativo: "))
print("salario administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("todo corecto")
else:
    print("fallas economicas")

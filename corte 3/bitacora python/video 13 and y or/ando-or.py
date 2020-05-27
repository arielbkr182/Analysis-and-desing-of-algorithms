#funciones solo con and
print("becas colombia")
disttancia_escuela=int(input("introduce la distancia a la escuela: "))
print(disttancia_escuela)

numero_hermanos=int(input("cuantos hermanos tiene: "))
print(numero_hermanos)

salario_familiar=int(input("cuanto es el salario familiar: "))
print(salario_familiar)

if disttancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
    print("tienes derecho a beca")
else:
    print("no tienes derecho a beca")


#funciones con and y or

print("becas colombia")
disttancia_escuela=int(input("introduce la distancia a la escuela: "))
print(disttancia_escuela)

numero_hermanos=int(input("cuantos hermanos tiene: "))
print(numero_hermanos)

salario_familiar=int(input("cuanto es el salario familiar: "))
print(salario_familiar)

if disttancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
    print("tienes derecho a beca")
else:
    print("no tienes derecho a beca")


#fucnoines con strings
print("becas colombia")
print("Tecnicas de ataque - software - bases de datos")
asignatura=input("escriba la materia: ")
if asignatura in ("Tecnicas de ataque", "software", "bases de datos"):
    print("materia elejida" + asignatura)
else:
    print("no existe materia") 


#fucnoines con strings mayusculas y minisculas
print("becas colombia")
print("Tecnicas de ataque - Software - Bases de datos")
opcion=input("escriba la materia: ")
asignatura=opcion.lower()
if asignatura in ("Tecnicas de ataque", "software", "bases de datos"):
    print("materia elejida" + asignatura)
else:
    print("no existe materia")





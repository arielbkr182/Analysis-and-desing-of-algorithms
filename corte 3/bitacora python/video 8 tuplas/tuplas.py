# creacion de una tupla
mitupla=("Juan", 13,1,1995)
print(mitupla[1])

# como inprmir una tupla a una lista
mitupla=("Juan", 13,1,1995)
milista=list(mitupla)
print(milista)

#como pasar de una lista a una tupla
milista=["Juan", 13,1,1995]
mitupla=tuple(milista)
print(mitupla)

# buscar datos en una tupla
mitupla=["Juan", 13,1,1995]
mitupla=tuple(milista)
print("Juan" in mitupla)

#contar elementos de una tupla
mitupla=["Juan", 13,1,1995]
mitupla=tuple(milista)
print(mitupla.count(13))

# hallar el tamaño de una tupla
milista=["Juan", 13,1,1995,13]
mitupla=tuple(milista)
print(len(mitupla))

#Desempaquetao de tupla
mitupla=("Juan", 13,1,1995)
nombre, dia, mes, agno=mitupla
print(nombre)
print(dia)
print(agno)
print(mes)

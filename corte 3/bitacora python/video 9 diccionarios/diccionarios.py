#crear un diccionario
midiccionario={"Alemania":"berlin","francia":"paris","UK":"londres"} # concepto clave valor
print(midiccionario["francia"])

#imprimir todo el diccionario
midiccionario={"Alemania":"berlin","francia":"paris","UK":"londres"} # concepto clave valor
print(midiccionario)

#agragar palabras a un diccionario ya creado
midiccionario={"Alemania":"berlin","francia":"paris","UK":"londres"} # concepto clave valor
midiccionario["italia"]="roma"
print(midiccionario)

#como cambiar el valor de una palabra al diccionario
midiccionario={"Alemania":"berlin","francia":"paris","UK":"londres"} # concepto clave valor
midiccionario["italia"]="lisboa"
print(midiccionario)
midiccionario["italia"]="roma"
print(midiccionario)

#como borrar una clave del diccionario
midiccionario={"Alemania":"berlin","francia":"paris","UK":"londres"} # concepto clave valor
midiccionario["italia"]="lisboa"
print(midiccionario)
midiccionario["italia"]="roma"
print(midiccionario)
del midiccionario["UK"]
print(midiccionario)

#crear un diccionario string  y enteros
midiccionario={1:"berlin","francia":4,2:"londres"} # concepto clave valor
print(midiccionario)

#como impormir la longitud de un diccionario
midiccionario={1:"berlin","francia":4,2:"londres"} # concepto clave valor
print(len(midiccionario))
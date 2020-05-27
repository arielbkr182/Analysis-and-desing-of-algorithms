#condicional IF
def evaluacion(nota): #crear la funcion
    valoracion="aprovo" #crear variable que guradara el resultado
    if nota<5:
        valoracion="perdio"
        return valoracion
print(evaluacion(4))


#ingresar valores por teclado y que el ciclo if la evalue
print("programa de evaluacion")

nota_alumno=input("instroducir la nota del alumno: ")
def evaluacion(nota): #crear la funcion
    valoracion="aprovo" #crear variable que guradara el resultado
    if nota<5:
        valoracion="perdio"
    return valoracion

print(evaluacion(int(nota_alumno)))
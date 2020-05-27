def busqueda_binaria(lista,elem):
    pi = 0
    pf = len(lista)-1
    while (pi<pf):
        pm=int((pi+pf)/2)
        if (lista[pm]==elem):
            return pm
        elif (lista[pm]<elem):
            pi = pm + 1
        else:
            pf = pm - 1
    return -1

def main():
    lista = []
    elem = input("Elemento: ")
    while elem != "":
        lista.append(elem)
        elem = input("Elemento siguiente: ")
    lista.sort()
    print(lista)
    lista.sort()
    elem = input("Ingrese el numero a buscar: ")
    elem = elem
    pos = busqueda_binaria(lista,elem)
    
    if (pos>-1):
        print("el elemento se encuentra en la pocicion: ",pos+1, "con el numero:", elem)
    else:
        print("el elemento no se encuetra en la lista")
main()

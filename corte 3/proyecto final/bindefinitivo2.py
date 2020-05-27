def binary_search_it(array, x):#se crea la funcion con las variables del vector y el dato de entrada
    left = 0#se inicia el vector en cero
    right = len(array) - 1#se espeifica hasta donde va el vector
    while left <= right:# Se ejecuta la búsqueda mientras que el límite izquierdo sea menor o igual al derecho
        mid = (left+right)//2#En cada iteración del bucle calculamos un puntomedio y recalculamos..... 
        if array[mid] == x:#los límites dependiendo si hemos encontrado el elemento o no
            return mid#
        elif array[mid] > x:#Si el elemento que buscamos esta en el array el algoritmo lo va a encontrar en alguna posición que calcule como mitad,
            right = mid-1#ya que vamos acotando la búsqueda en cada iteración
        else:
            left = mid+1# 
    return -1

def main():#metodo para interactuar con el usuario
    array = []#se declara el vector
    array.sort()#se ordena el vector de menor a mayor
    x= input("Elemento: ")#se pide el dato de entrada para llenar el vector
    while x != "":# se crea un bucle para definir el limite de llenado del vector con un doble enter
        array.append(x)#se llena el vector
        x = input("Elemento siguiente: ")#se pide el numeero siguiente para llenar el vector
    array.sort()#se ordena el vector
    print(array)#se imprime el vector lleno de numeros
    x = input("Ingrese el numero a buscar: ")#se pide el numero a buscar
    x = x#se iguala el numero a buscar con el numero dentro del vector para saver si esta
    pos = binary_search_it(array,x)#se busca el numero dentro del vector 
    
    if (pos>-1):# por medio de un avariable pos que contiene el numero a buscar se verifica si el numero ingresado es menor a 1 y se hace la compracion
        print("el elemento se encuentra en la pocicion: ",pos+1, "con el numero:", x) # si es igual se sele suma 1 ya que el vector empiesa en la pocicion cero y se muestra en consola junto con el nuemero que se pide
    else:
        print("el elemento no se encuetra en la lista")# si no que muestre el mensaje...  no se encuentra 
main()#fin del main


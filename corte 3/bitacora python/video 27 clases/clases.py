#creacion de clases
class Coche():

    def __init__(self):

        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            return " el coche esta en marcha"
        else:
            return "el coche esta parado"

    def estado(self):
        print("el coche tiene ", self.__ruedas, " ruedas. un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)


miCoche=Coche() #instamciando la clase
print(miCoche.arrancar(True))

miCoche.estado()

print("-------------------creacion del segundo objeto--------------------------")
miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.ruedas=2
miCoche2.estado()



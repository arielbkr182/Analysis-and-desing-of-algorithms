#creacion de clases
class Coche():

    def __init__(self): #contrsuctor 

        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            chequeo=self.__chequeo()
        if(self.__enmarcha and chequeo):
            return "en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "algo salio mal"
        else:
            return " esta quieto el carro"
            
    def estado(self):
        print("el coche tiene ", self.__ruedas, " ruedas. un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

    def chequeo(self):
        print("relizando chequeo")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="ok"
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="ok"):
            return True
        else:
            return False
miCoche=Coche() #instamciando la clase
print(miCoche.arrancar(True))

miCoche.estado()

print("-------------------creacion del segundo objeto--------------------------")
miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.ruedas=2
miCoche2.estado()



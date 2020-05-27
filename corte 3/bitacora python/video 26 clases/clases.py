#creacion de clases
class coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    def arrancar(self):
        self.enmarcha=True
    def estado(self):
        if(self.enmarcha):
            return "el coche esta en marcha"
        else:
            return"el coche esta parado"


micoche=coche() #instamciando la clase
print("el largo del carro es: ",micoche.largoChasis)
print("El conche tiene ", micoche.ruedas, "ruedas")
micoche.arrancar()
print(micoche.estado())





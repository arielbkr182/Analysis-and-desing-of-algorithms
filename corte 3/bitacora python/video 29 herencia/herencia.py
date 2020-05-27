class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=modelo
        self.acelera=False
        self.frena=False
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        print("marca: ", self.marca, "\nmodelo: ", self.modelo, "\nen marcha: ", self.enmarcha, "\nacelerando: "
        , self.acelera, "\nfrenando", self.frena )

class moto(Vehiculos):
    pass
mimoto=moto("homnda", "CBR")
mimoto.estado()
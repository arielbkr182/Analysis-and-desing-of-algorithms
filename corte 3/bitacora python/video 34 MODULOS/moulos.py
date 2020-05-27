class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.acelera=True

    def estado(self):
        print("marca: ", self.marca, "\nmodelo: ", self.modelo, "\nen marcha: ", self.enmarcha, "\nacelerando: "
        , self.acelera, "\nfrenando", self.frena )

class furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargando=cargar
        if(self.cargando):
            return "furgoneta cragada"
        else:
            return "la furgoneta no esta cargada"
class moto(Vehiculos):
    hcaballito=""
    def caballito(self):
       self.hcaballito="voy en caballo"

    def estado(self):
        print("marca: ", self.marca, "\nmodelo: ", self.modelo, "\nen marcha: ", self.enmarcha, "\nacelerando: "
        , self.acelera, "\nfrenando", self.frena, "\n", self.hcaballito)

class VElectricos():
    def __init__(self, marca, modelo):
        super().__init__(marca, marca)
        self.automatiza=100

    def cargaEnergia(self):
        self.cargando=True
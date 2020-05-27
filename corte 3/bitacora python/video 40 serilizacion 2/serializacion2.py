import pickle
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

coche1=Vehiculos("mazda","mx5")
coche2=Vehiculos("mseat","leon")
coche3=Vehiculos("audi","ooo")

coches=[coche1, coche2, coche3]
fichero=open("los coches", "wb")

pickle.dump(coches, fichero)
fichero.close()
del (fichero)

#apertura fichero
ficheroapertura=open("los coches", "rb")
miscoches=pickle.load(ficheroapertura)
ficheroapertura.close()
for c in miscoches:
    print(c.estado())

class coche():
    def desplazamiento(self):
        print("me desplazo utiizando cuatro ruedas")

class moto():
    def desplazamiento(self):
        print("me desplazo utilizando dos ruedas")

class camion():
    def desplazamiento(self):
        print("me desplazo en seis ruedas")

def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()

mivehiculo=moto()

desplazamientovehiculo(mivehiculo)
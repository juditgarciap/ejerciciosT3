class Nave():
    def __init__ (self , nombre, largo, tripulacion, cantidad_pasajeros):
        self. nombre = nombre
        self.largo  = largo
        self.tripulacion = tripulacion 
        self.cantidad_pasajeros = cantidad_pasajeros
    def __str__ (self):
#la f es lo mismpo que .format pero hay que pasarle las variables con el self
        print(f 'Nombre: {self.nombre} - Largo: {self.largo}')
        print(f 'tripulacion: {self.tripulacion} - cantidad pasajeros: {self.cantidad_pasajeros}')
        
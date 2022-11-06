class Nave():
    def __init__ (self , nombre, largo, tripulacion, cantidad_pasajeros):
        self. nombre = nombre
        self.largo  = largo
        self.tripulacion = tripulacion 
        self.cantidad_pasajeros = cantidad_pasajeros
    def __str__ (self):
#la f es lo mismpo que .format pero hay que pasarle las variables con el self
        return f'Nombre: {self.nombre} - Largo: {self.largo}'
        return f'tripulacion: {self.tripulacion} - cantidad pasajeros: {self.cantidad_pasajeros}')
        
def ordenar(lista_naves):
#ordenar por letras
    lista_ordenada = sorted(lista_naves, key= lambda x: x.nombre)
    lista_nombres = [nave.nombre for nave in lista_ordenada]
#ordenar por largo
    letras_iniciales = [nave.nombre[0] for nave in lista_ordenada]

#esta no es la manera más eficiente de hacerlo pero no se me ocurría otra forma
for letra in set(letras_iniciales):
    posiciones = []
    for pos, nombre_nave in enumerate (lista_nombres):
        if nombre_nave [0] == letra:
            posiciones.append(pos)
    if len (posiciones) > 1:

    
        print 



return lista_ordenada













#crear naves 

nave1 = Nave('Halcón Milenario', 800, 3, 6)
nave2 = Nave('Estrella de la Muerte', 750, 2, 5)
nave3 = Nave('HalaX', 600, 1, 4)
nave4 = Nave('Destructor Estelar', 10000, 4, 7)
nave5 = Nave('Lanzadera Imperial', 11000, 2, 6)
nave6 = Nave('Nave real nubian 327', 9000, 5, 20)
nave7 = Nave('AT real X', 6000, 4, 2)
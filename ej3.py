

class Nave():

    def __init__ (self , nombre, largo, tripulacion, cantidad_pasajeros):
        self. nombre = nombre
        self.largo  = largo
        self.tripulacion = tripulacion 
        self.cantidad_pasajeros = cantidad_pasajeros
    def __str__ (self):
#la f es lo mismpo que .format pero hay que pasarle las variables con el self
        return f'Nombre: {self.nombre} - Largo: {self.largo}'
        return f'tripulacion: {self.tripulacion} - cantidad pasajeros: {self.cantidad_pasajeros}'

#crear naves 
nave1 = Nave('Halcón Milenario', 800, 3, 6)
nave2 = Nave('Estrella de la Muerte', 750, 2, 5)
nave3 = Nave('HalaX', 600, 1, 4)
nave4 = Nave('Destructor Estelar', 10000, 4, 7)
nave5 = Nave('Lanzadera Imperial', 11000, 2, 6)
nave6 = Nave('Nave real nubian 327', 9000, 5, 20)
nave7 = Nave('AT real X', 6000, 4, 2)





def ordenar(lista_naves):
#ordenar por letras
    lista_ordenada = sorted(lista_naves, key= lambda x: x.nombre)
    lista_nombres = [nave.nombre for nave in lista_ordenada]
#ordenar por largo
    letras_iniciales = [nave.nombre[0] for nave in lista_ordenada]

#esta no es la manera más eficiente de hacerlo pero no se de otra forma
naves = [nave1, nave2, nave3, nave4, nave5, nave6, nave7]

naves

def ordenar(lista_naves):
    # ordenar por letras
    lista_ordenada = sorted(lista_naves, key = lambda x: x.nombre.lower())
    lista_naves_copia = lista_ordenada.copy()
    lista_nombres = [nave.nombre for nave in lista_ordenada]
    lista_tamanio = [nave.largo for nave in lista_ordenada]
    # ordenar por largo
    letras_iniciales = [nave.nombre[0] for nave in lista_ordenada]


#zip() toma como argumento dos o más objetos iterables (idealmente cada uno de ellos con la misma cantidad de elementos) 
#y retorna un nuevo iterable cuyos elementos son tuplas que contienen un elemento de cada uno de los iteradores originales.
#función dict asocia claves a valores 
    for letra in set(letras_iniciales):
        posiciones = []
        for pos, nombre_nave in enumerate(lista_nombres):
            if nombre_nave[0] == letra:
                posiciones.append(pos)
        if len(posiciones) > 1:
            tamanios = []
            for posicion in posiciones:
                tamanios.append(lista_tamanio[posicion])
            tabla_tamanios = dict(zip(tamanios, posiciones))
            posiciones_ordenadas = []
            for k in sorted(tabla_tamanios.keys(), reverse=True):
                posiciones_ordenadas.append(tabla_tamanios[k])
            orden = dict(zip(posiciones[:len(posiciones)//2], posiciones_ordenadas[:len(posiciones)//2]))

            for pos_no_ordenada, pos_ordenada in orden.items():
                elemento_pivote = lista_ordenada[pos_no_ordenada]
                lista_naves_copia[pos_no_ordenada] = lista_naves_copia[pos_ordenada]
                lista_naves_copia[pos_ordenada] = elemento_pivote

    return lista_naves_copia


# apartado2 
#mostrar por pantalla el nombre y el tamaño de la nave
[(nave.nombre, nave.largo) for nave in ordenar(naves)]

#apartado3
def mayor_pasajeros(naves):
    naves_ordenadas = sorted(naves, key = lambda x: x.cantidad_pasajeros, reverse = True)
    for i in range(5):
        print(i+1, naves_ordenadas[i])

mayor_pasajeros(naves)

#apartado4
def buscar_at(naves):
    flag = False
    for nave in naves:
        if nave.nombre.lower()[:2] == 'at':
            flag = True
            print(nave)

    if flag == False:
        print('No hay naves que inicien por at')
buscar_at(naves)

#Apartado5


#apartado6
    
















#crear naves 

nave1 = Nave('Halcón Milenario', 800, 3, 6)
nave2 = Nave('Estrella de la Muerte', 750, 2, 5)
nave3 = Nave('HalaX', 600, 1, 4)
nave4 = Nave('Destructor Estelar', 10000, 4, 7)
nave5 = Nave('Lanzadera Imperial', 11000, 2, 6)
nave6 = Nave('Nave real nubian 327', 9000, 5, 20)
nave7 = Nave('AT real X', 6000, 4, 2)
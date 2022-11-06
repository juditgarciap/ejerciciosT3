# ¿cómo funciona la torre de Torre de Hanói?
# Resolver 
# 3 agujas en una plataforma
# La primera aguja contiene n discos apilados,
# cada disco es ligeramente menor que el disco que está debajo
# Se deben pasar los discos desde la primera aguja a la tercera aguja
# Solo puede moverse un disco a la vez
# Ningún disco podrá ponerse encima de otro disco más pequeño

def TorreDeHanoi(nDisco, agujaFuente, agujaDestino, agujaAuxiliar):
    
    if nDisco == 0: 
 # Caso base de la recursión cuando no hay discos para mover,
        # por lo tanto se termina la llamada de la función
        return None
 # Llamada para mover disco n-1, desde la aguja fuente hasta la aguja auxiliar,para otorgar libertad de movimiento al disco n
    elif nDisco > 0: 
         TorreDeHanoi(nDisco-1, agujaFuente, agujaAuxiliar, agujaDestino)                  
# Imprimir movimiento del disco n, desde la aguja fuente hasta la aguja destino.
    print("Mover disco", 
              nDisco, 
              "desde la aguja", 
              agujaFuente, 
              "hasta la aguja",
              agujaDestino)   
        
# Llamada para mover disco n-1,
# desde la aguja auxiliar hasta la aguja destino.
    TorreDeHanoi(nDisco-1, agujaAuxiliar, agujaDestino, agujaFuente)



TorreDeHanoi(1, 'A', 'C', 'B')

TorreDeHanoi(2, 'A', 'C', 'B')

TorreDeHanoi(3, 'A', 'C', 'B')

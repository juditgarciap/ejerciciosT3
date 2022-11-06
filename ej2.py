# ejercicio 2a forma iterativa
def det_iterativa(matriz): 
    tamanio = len(matriz)
    matriz = matriz + matriz 
    matriz = matriz[:-1]

    determinante = 0 
    for i in range(0,tamanio): 
        termino_pos = matriz[i][0] * matriz[i+1][1] * matriz[i+2][2]
        termino_neg = matriz[i][2] * matriz[i+1][1] * matriz[i+2][0]

        resta = termino_pos - termino_neg
        determinante = determinante + resta

    print(determinante)

det_iterativa(matriz=[[1,2,3],
                      [1,0,1],
                      [2,2,1]])

#forma recursiva 
def ReglaSarrus(matrix, nivel=0, det=0):
    print("Determinante acumulado:", 
          det, 
          " - Nivel de recursión:",
          nivel)


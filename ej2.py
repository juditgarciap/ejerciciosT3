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

    if nivel < 3:
        det += matrix[0][0] * matrix[1][1] * matrix[2][2]
    elif nivel >= 3 and nivel < 6:
        det += -matrix[0][2] * matrix[1][1] * matrix[2][0]
    else:
        print("\n")
        print("El determinante de la matrix es:", det)
        return None
        
#Dezplazar columna de la matriz según Regla de Sarrus.
    matrix = [ matrix[0][1:3] + [matrix[0][0]],
               matrix[1][1:3] + [matrix[1][0]],
               matrix[2][1:3] + [matrix[2][0]] ]
    
    print(matrix)    
    ReglaSarrus(matrix, nivel+1, det)



matrix = [[2, 4, 3],
          [1, 4, 6],
          [1, 6, 8]]
ReglaSarrus(matrix)    
matrix = [[3, -3, -6],
          [-9, 8, 1],
          [-3, -1, 2]]
ReglaSarrus(matrix)  


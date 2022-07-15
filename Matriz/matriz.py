from asyncio.windows_events import NULL
import numpy as np


def createMatrix():
    matrix= np.random.randint(10, size=(5, 5))
    
    return(matrix)

def findNumbers(matrix):
    print("la matriz a evaluar es:")
    print(matrix)
    position=findByRow(matrix)
    if(position!=NULL):
        print("posicion inicial/final - encontrado por fila")
        print(position)
    else:
        position=findByColumn(matrix)
        if(position!=NULL):
            print("posicion inicial/final - encontrado por columna")
            print(position)
        else:
            print("no se encontraron coincidencias de numeros consecutivos")

def findByRow(matrix):
    listNumbers=list()
    count=3
    position_i=list()
    position_j=list()
    position=list()
    for i in range(len(matrix)):
            for j in range(len(matrix)-1):
                if(matrix[i][j]==matrix[i][j+1] and count>0 ):
                    listNumbers.append(matrix[i][j])
                    position_i.append(i)
                    position_j.append(j)
                    count-=1
                    
            if(count>0):
                count=3
                listNumbers.clear()
                position_j.clear()
                position_i.clear()
    if(len(position_i)>0):
        position.append({"inicial_i": position_i[0], "inicial_j": min(position_j),"final_i": min(position_j), "final_j": max(position_j)+1})
        return position
    else:
        return NULL

def findByColumn(matrix):
    listNumbers=list()
    count=3
    position_i=list()
    position_j=list()
    position=list()
    for j in range(len(matrix)):
        for i in range(len(matrix)-1):
            if(matrix[i][j]==matrix[i+1][j] and count>0 ):
                listNumbers.append(matrix[i][j])
                position_i.append(i)
                position_j.append(j)
                count-=1
        if(count>0):
            count=3
            listNumbers.clear()
            position_j.clear()
            position_i.clear()
       

        if(len(position_i)>0):
            return position
        else:
            return NULL

        
#EJEMPLO DE PRUEBA UTILIZADO ---> reemplazar "matrix" por "mat" es decir, cambiar  "findNumbers(matrix) por finNumbers(mat)"
mat= [  
[7, 9, 6, 2, 4], 
[8, 4, 1, 3, 2],
[0, 2, 2, 2, 2],
[8, 1, 3, 6, 9], 
[8, 6, 6, 7, 0]]  

matrix=createMatrix()
findNumbers(matrix)
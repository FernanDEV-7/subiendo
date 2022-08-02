#las matrices pueden tener 2 dimensiones 
import numpy as  np 
#matriz de 1 dimension:
#matriz = np.array([1,2,3,4,5,6])
#print(matriz)

#matriz de 2 dimensiones:
#m2d= np.array([[1,2,3],[4,5,6]])
#print (m2d)
#[[1 2 3]
# [4 5 6]]
#se encierra entre corchetes la matriz total, pero las lineas de las matrices se vuelven a encerrar entre corchetes

#para usar los elementos de una lista en una matriz se hace lo siguiente:

#lista = [1,2,3,4,5]
#matriz = np.array(lista)
#print (matriz)
#[1 2 3 4 5]

#llamamos a la funcion array con el argumento lista, esto hara que los elementos de una lista se conviertan a una matriz

#lista = [[1,2,3],[4,5,6],[7,8,9]]
#matriz = np.array(lista)
#print(matriz)

#para generar matrices mas rapido, usaremos el siguiente codigo
m = np.arange(15).reshape(3,5)
print (m)
#lo que hara esta funcion es generar una matriz en el range del numero del argumento, luego con el metodo .reshape
#le daremos forma a la matriz de 2 dimensiones, primero se especifican las filas, luego con una coma las columnas
#en el caso de que la multiplicacion de filas y columnas sea inferior a los elementos del arange, saldra un error.
#si no se llama al metodo reshape, se generara una matriz de una dimension. 

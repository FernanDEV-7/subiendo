#FUNCIONES EN MATRICES:
import numpy as np
 
#con .shape podremos saber cuantas filas y columnas tiene nuestra matriz ejm:(4, 5)
#print (m.ndim)
#con .ndim podremos saber el numero de dimensiones que tiene nuestra matriz. ejm: 2
#print (m.size)
#con .size podremos saber el numero de elementos que tiene mi matriz. ejm: 20

#m = np.zeros((3,4))
#print (m.shape)
#print(m)

#con la funcion zeros se puede generar una matriz llena de ceros, en el argumento se tiene que llenar con un parentesis
#las filas y las columnas 

#para generar matrices de manera rapida usaremos la funcion linspace, y en sus argumentos especificaremos
#el INICIO, el FINAL, y el numero de elementos que tendra la matriz. ejm:

#m=np.linspace(99,88,25)
#print (m.shape)
#print(m)

#Matriz de 3 dimensiones:
m=np.arange(24).reshape(2,3,4)
print(m)
# la misma sintaxis, solo que se le añade un argumento mas que seria el del principio, 2 capas 
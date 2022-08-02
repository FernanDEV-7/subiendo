#LISTA = Coleccion de elementos que contiene multiples tipos de datos. ejm: int float str etc.
#Array = Matriz o Array es un vector que contiene elementos homogeneos, osea el mismo tipo de datos

#import array as ar
#matriz = ar.array ('i',[1,2,3,4,5])
#for ar in matriz :
#    print(ar)
#llamamos a la funcion array para denotar una clase, 'i' para denotar que seran elementos tipo int y luego de eso
#una coma y con corchetes los numeros 

import numpy as np
#lista =  [1,3,5]
#matriz = np.array([2,4,6])
#lista.append(7)
#matriz.append(8)
#matriz = matriz + np.array([8])
#AttributeError: 'numpy.ndarray' object has no attribute 'append' 

#mientras que en una lista se suma el elemento nuevo con el metodo append, en las matrices no se puede, mas bien
#cuando se llama a la funcion array se le suma ese elemento a cada elemento en la matriz [10 12 14]

#print(lista)
#print (matriz)

#Diferencia numero 2 entre listas y arrays: en las matrices se pueden manejar operaciones aritmeticas y en las listas no

#a = [1,2,3]
#b = [4,5,6]
#print (a+b)
#[1, 2, 3, 4, 5, 6]
#print (a*b) = TypeError: can't multiply sequence by non-int of type 'list'
#en listas no se puede 

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b) 
#[5 7 9] 



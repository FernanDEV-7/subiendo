import numpy as np 
#METODOS CON MATRICES:
#m = np.arange(24).reshape(4,6)
#print(m[3,4])
#print(m)
#cuando haces print con un numero especifico de fila y columna, sale el valor como
#un indice, contando desde 0

#m1 = np.array([90, 7, 9, 4, 2, 1])
#print (np.sort(m1))
#con este metodo podremos ordenar los elementos de forma ascendente dentro de una matriz
#primero se llama al modulo y luego al metodo sort con el argumento que es la matriz a ordenar

#m1 = np.array([2,3,])
#print(m1.power(m1,2))
# con el metodo power se puede elevar los elementos de una determinada matriz a la enecima
#potencia, de igual manera se puede usar el operador ** para hacer lo mismo
 

#m1 = np.array([2,3,4,5,6])
#print (np.array(m1.max())) 

# con el metodo.max() se retorna el valor mas alto dentro de una matriz y igualmente con el metodo
# .min se retorna el mas bajo 

#m1 = np.array([2,3,4,5,6])
#m2 = np.array([11,34,67,99])
#print (np.concatenate((m1,m2)))

#con este metodo podemos concatenar ambas matrices, en el argumento se especifican las matrices
#dentro de otro parentesis. resultado = [ 2  3  4  5  6 11 34 67 99] 

m1 = np.array ([[1,2],[3,4]])
m2 = np.array ([[5,6],[7,8]])
print (m1+m2)
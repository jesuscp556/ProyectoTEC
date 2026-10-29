import numpy
from numpy import *

data_list = [1,2,3,4,5]
data_array = array([1,2,3,4,5])

id_list = []

for i in range(len(data_array)):
#                 print("ID del elemento " + str(i) + " de la lista = " + str(id(data_list[i])))
                print("ID del elemento " + str(i) + " del arreglo = " + str(id(data_array[i])))
                id_list.append(id(data_array[i]))
#                 if i > 0:
#                     print("Diferencia memoria = " + str(id(data_array[i]) - id(data_array[i-1])))



print("Hola mundo")

print("Hola mundo, otra vez")


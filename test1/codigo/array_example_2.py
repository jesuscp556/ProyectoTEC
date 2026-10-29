from numpy import *

valido = False
print("Dame el length del arreglo")

while not valido:
    len_array = input()
    if(len_array.isdigit()):
        if(int(len_array) > 0):
            valido = True
        else:
            print("Entero negativo")
    else:
        print("Dato erroneo, ingrese nuevamente")

len_array_int = int(len_array)

array_length = zeros(len_array_int)
array_string = array([])
# array_string = array(["" for x in range(len_array_int)])


for i in range (len_array_int):
    print("Ingresa el String de la " + str(i) + " posicion")
    temp = input()
    array_string.append(temp)
#     array_string[i] = temp
    array_length[i] = len(array_string[i])

print(array_string)
print(array_length.astype(int))
print("El numero maximo de caracteres es " + str(int(array_length.max())) + " y esta en la posicion " + str(array_length.argmax()))





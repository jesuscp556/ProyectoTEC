

data = 412
str_data = str(data)
var_divisor = 10

# print(data)
# print(str_data)
# print(len(str_data))
# data_inv = int(str_data[::-1]);
# print(data_inv)

num_valido = 0
inverso = 0

#CHECK DATA.is_integer()

while not num_valido:
    print("Ingresa tu numero entero positivo, por favor")
    data_int = input()
    if(data_int.find('.') > -1 or data_int.isdecimal() == False):
        print("Caracter invalido, intente de nuevo")
    elif(int(data_int) > 0):
        num_valido = 1
    else:
        print("Numero mal escrito, intente de nuevo")

data_int = int(data_int)
while data_int > 10:
    temp_residuo = int(data_int % 10)
    data_int /= 10
    data_int = int(data_int)
    inverso  = 10*inverso + temp_residuo

inverso = 10*inverso + data_int
print(inverso)

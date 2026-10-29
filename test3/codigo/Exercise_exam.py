from numpy import *
import random as rd


def check_int_input(msg):
    while True:
        try:
            print(msg)
            return int(input())
            break
        except ValueError:
            print("Dato no valido, ingrese nuevamente")

def exercise_1():
    var = [1,2,3,4,5]
    print(var*3)

def exercise_2(len_max):
    var = array(["*" for i in range(len_max)])
    for i in range(len_max):
        var[i] = int(input())
    print(var)

def exercise_3(seed):
    var = zeros([5,5])
    for i in range(len(var)):
        for j in range(len(var)):
            var[i][j] = rd.randint(0,seed)
    print(var)

def exercise_4():
    var = [4,5,6,1,2,7,4,5]
    var.remove(1)
    print(var)

def exercise_5():
    var = ['a','b','c','d']
    var.append(['e','f','g'])
    print(len(var))

def exercise_6():
    var = [8,2,2024]
    print(sum(var))
    var.append("100")
    print(sum(var))

def exercise_7(refran):

    temp = ""
    lista = []
    for i in range(len(refran)):
        if (refran[i] != " "):
            temp = temp + refran[i]
        else:
            lista.append(temp)
            temp = ""
    lista.append(temp)
    print(lista)

if __name__ == '__main__':
     exercise_1()
     # exercise_2(5)
    # exercise_3(50)
     exercise_4()
    # exercise_5()
   # exercise_7("Tecnologico de Monterrey Campus GDL PrepaTEC")


    # print("EXAMEN")
    #
    # len_array = check_int_input("Ingresa tu tamaño de arreglo, por favor")
    # arreglo_numeros = zeros(len_array)
    # arreglo_suma = zeros(len_array)
    #
    # i = 0
    # while i<len_array:
    #     temp_number = check_int_input("Ingresa un numero")
    #     if(temp_number != 0 and not any(arreglo_numeros == temp_number)):
    #         arreglo_numeros[i] = temp_number
    #         arreglo_suma[i] = arreglo_numeros.sum()
    #         i+=1
    #     else:
    #         print("Numero invalido")
    # print(arreglo_numeros)
    # print(arreglo_suma)
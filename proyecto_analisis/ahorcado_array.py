from numpy import *
import random as rd



w_str = input("Ingresa palabra a descubrir ")
len_arr = len(w_str)

hint = int(input("Ingresa cuantas ayudas quieres "))
if(hint >= len_arr):
    hint = len_arr - 2


arr = array(list(w_str))
list_valid = [False]*len_arr
arr_valid = array(list_valid)
arr_ahorcado = ["_" for x in range(len_arr)]
vidas = 3
index = 0

while index < hint:
    hint_index = rd.randint(0, hint)
    if(arr_valid[hint_index] == False):
        arr_ahorcado[hint_index] = arr[hint_index]
        arr_valid[hint_index] = True
        index+=1;
        
Indice_valido = False
print(arr_ahorcado)



while vidas > 0:
    letra_check = input('Dame la letra, por favor')
    Indice_valido = False
    #Nada mas pida esto
    while not Indice_valido:
        index_check = int(input("Dame la posicion, por favor"))
        if(index_check >= len_arr):
            print("Indice fuera de rango")
        else:
            Indice_valido = True
            if(arr[index_check] == letra_check):
                arr_valid[index_check] = True
                #Funcion que imprima las letras que ya se descubrieron
                arr_ahorcado[index_check] = arr[index_check]
                print(arr_ahorcado)
            else:
                vidas = vidas - 1
                print("Dato erroneo, te quedan " + str(vidas) + " Vidas")
    if(all(arr_valid == True)):
        print("Felicidades")
        break

print("Perdiste, lo siento, la palabra era " + w_str)
from ADT_library import *
from numpy import *

instruccion = ListStack()

print("Da las instrucciones que quieras, para terminar, digita la palabra *Terminar* al final")
while True:
    temp_instr = input("Dame una instruccion a guardar ")
    if(temp_instr == "Terminar"):
        break
    else:
        instruccion.push(temp_instr)

while not instruccion.isEmpty():
        print(instruccion.pop())
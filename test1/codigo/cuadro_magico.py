#Cuadro magico, 3x3
import sys
import random



from numpy import *

cuadro_magico = zeros([3,3])

Valid = False
row_valid = False
column_valid = False

while not Valid:
    row_valid = False
    column_valid = False
    number_input = int(input("Ingresa El numero "))
    while not row_valid:
        row = int(input("Ingresa la fila "))
        if(row >= 3):
            print("Fila fuera de rango, ingresa nuevamente")
        else:
            row_valid = True
            while not column_valid:
                column = int(input("Ingresa la columna "))
                if(column >= 3):
                    print("Columna fuera de rango, ingresa nuevamente")
                else:                    
                    cuadro_magico[row][column] = number_input
                    print(cuadro_magico)
                        
                    if(not any(cuadro_magico == 0)):
                       print(cuadro_magico)
                       Valid = True
                    column_valid = True
            
suma_filas = cuadro_magico.sum(0)
suma_columnas = cuadro_magico.sum(1)
diagonales = array([diag(cuadro_magico), diag(cuadro_magico[::-1])])
suma_diagonales = diagonales.sum(1)

if(all(suma_filas == 15) and all(suma_columnas == 15) and all(suma_diagonales == 15)):
    print("Cuadro Magico")
else:
    print("Cuadro incorrecto")

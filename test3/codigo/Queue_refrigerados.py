from datetime import date

class ListQueueSimple:
    def __init__(self, LEN_MAX):
        self._L = []
        self.LEN_MAX = LEN_MAX
        
    def enqueue(self, item):
        if self.isFull():
            print("Queue lleno")
        else:
            self._L.append(item)
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue vacio")
        else:
            return self._L.pop(0)
    
    def peek(self):
        if self.isEmpty():
            print("Queue vacio")
            return "No hay"
        else:
            return self._L[0]
          
    def __len__(self):
        return len(self._L)
    
    def isEmpty(self):
        return len(self) == 0
    
    def isFull(self):
        return len(self) >= self.LEN_MAX

def check_int_input(msg):
    while True:
        try:
            print(msg)
            return int(input())
            break
        except ValueError:
            print("Dato no valido, ingrese nuevamente")
 
def ingresar_producto(frutas_refri):
    boxes = check_int_input("Cuantas cajas vas a guardar")
    for i in range(boxes):
        if frutas_refri.isFull():
            print("Producto excedente, faltan " + str(boxes - i) + "Cajas por almacenar")
            break
        else:
            temp_date = date.today()
            frutas_refri.enqueue(temp_date)
 
 
#INGRESAR EL LENGTH MAXIMO DE MI QUEUE
len_max = check_int_input("Ingresa el numero de paquetes maximo a guardar")
frutas_refri = ListQueueSimple(len_max)

while 1:
    opcion = check_int_input("Ingresa una opcion, por favor: \n1)Checar caducidad \n2)Ingresar producto \n3)Vender producto \n4)Salir")
    #MENU
    if(opcion == 1):
        fecha_vieja = frutas_refri.peek()
        print("Caja mas vieja, ingresada el " + str(fecha_vieja))
    elif(opcion == 2):
        ingresar_producto(frutas_refri)
    elif(opcion == 3):
        print("Opcion 3")
    elif(opcion == 4):
        print("Opcion 4")
        break
    else:
        print("Opcion no valida")
    
    
#     match opcion:
#         case 1:
#             print("Opcion 1")
#         case 2:
#             print("Opcion 2")
#         case 3:
#             print("Opcion 3")
#         case 4:
#             print("Opcion 4")
#             break
#         case _:
#             print("Opcion no valida")
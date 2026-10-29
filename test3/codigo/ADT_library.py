class ListStack:
    def __init__(self):
        self._L = []

    def push(self, item):
        self._L.append(item)
    
    def pop(self):
        try:
            return self._L.pop()
        except IndexError:
            raise RuntimeError("pop from empty stack")
    
    def peek(self):
        return self._L[-1]

    def __len__(self):
        return len(self._L)
    
    def isEmpty(self):
        return len(self) == 0
    
    def isFull(self):
        return len(self) >= max_len
    

class ListQueueSimple:
    def __init__(self,len_max):
        self._L = []
        self.len_max = len_max
        
    def enqueue(self, item):
        if self.isFull():
            print("Queue lleno")
        else:
            self._L.append(item)
        
    def dequeue(self):
        return self._L.pop(0)
    
    def peek(self):
        return self._L[0]
    
    def __len__(self):
        return len(self._L)
    
    def isEmpty(self):
        return len(self) == 0
    
    def isFull(self):
        return len(self) >= self.len_max

def check_int_input(msg):
    while True:
        try:
            print(msg)
            return int(input())
            break
        except ValueError:
            print("Dato no valido, ingrese nuevamente")


def print_emergency(name,level):
    print("Paciente: " + name + "\nGravedad: " + str(level))

def switch(level,name):
    if(level == 1):
        level_one.enqueue(name)
        print(str(level_one.__len__()))
    elif(level == 2):
        level_two.enqueue(name)
        print(str(level_two.__len__()))
    elif(level == 3):
        level_three.enqueue(name)
        print(str(level_three.__len__()))
    else:
        print("Opcion incorrecta")
    
    print_emergency(name,level)

if __name__ == '__main__':
    
    #Ingresar los tamaños de los queue
    len_max = check_int_input("Ingresa los tamaños de tus Queue, por favor ")
    print("Tamaño = " + str(len_max)) 
    
    #creando los Queue
    level_one 	= 	ListQueueSimple(len_max)
    level_two 	= 	ListQueueSimple(len_max)
    level_three = 	ListQueueSimple(len_max)
    
    terminar = False
    
    while not terminar:
        
        menu_option = check_int_input("Ingresa la opcion que quieres\n 1)Revisar lista \n 2)Registrar paciente \n 3)Nombre del siguiente paciente \n 4)Salir \n")

        if(menu_option == 1):
            print("Mantenimiento")
        elif(menu_option == 2):
            nombre = input("Ingresa nombre completo del paciente, por favor ")
            gravedad = check_int_input("Ingrese la gravedad del paciente, por favor \n 1)Sin Urgencia \n 2)Urgencia \n 3)Emergencia \n")
            switch(gravedad,nombre)
        elif(menu_option == 3):
            print("Proximo paciente: " + level_one.dequeue())
        elif(menu_option == 4):
            terminar = True
        else:
            print("Opcion incorrecta")
    
        input("Ingresa una tecla para continuar")
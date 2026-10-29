import logging
from ADT_library import *

class levels_queue():
    def __init__(self,len_max):
            self.level_one = ListQueueSimple(len_max)
            self.level_two = ListQueueSimple(len_max)
            self.level_three = ListQueueSimple(len_max)
            self.level_four = ListQueueSimple(len_max)
            self.level_five = ListQueueSimple(len_max)
            logging.debug("Queues de niveles creado exitosamente")

class priority_queue():
    def __init__(self,len_max):
        self.priority_name = []
        self.priority_number = []
        logging.debug("Priority creado")

    def ingreso(self,data):
        self.priority_name.append(data)
        print(self.priority_name)

    def check_priority(self):
        if(self.priority_name == []):
            print("No hay pacientes por atender")
        else:
            print(self.priority_name)

    def set_list(self,name,level):
        if(len(self.priority_number) > 1):
            self.idx = self.acomodo_queue(level)
            self.priority_name = self.priority_name[::-1]
            self.priority_name.insert(self.idx,name)
            self.priority_name = self.priority_name[::-1]

            self.priority_number = self.priority_number[::-1]
            self.priority_number.insert(self.idx,level)
            self.priority_number = self.priority_number[::-1]
            logging.debug(self.idx)
        elif(len(self.priority_number) == 1):
            logging.debug("NUMERO UNO!")
            if(level > TRIAGE.priority_number[0]):
                self.priority_name.append(name)
                self.priority_number.append(level)
            else:
                self.priority_name.insert(0,name)
                self.priority_number.insert(0,level)
        else:
            self.priority_name.append(name)
            self.priority_number.append(level)

        logging.debug(self.priority_name)
        logging.debug(self.priority_number)

    def update_queue(self):
        self.data,self.level = check_queues()
        logging.debug(self.data)
        logging.debug(self.level)
        logging.debug("Numero del dato " + str(len(self.priority_name)))
        if(len(self.priority_name) == 0):
            self.priority_name.append(self.data)
            self.priority_number.append(self.level)
            logging.debug("DATO LISTO EN QUEUE VACIA")
        else:
            match self.level:
                case 1:
                    print("Data 1")
                case 2:
                    print("Data 2")
                case 3:
                    print("Data 3")
                case 4:
                    print("Data 4")
                case 5:
                    print("Data 5")
                case _:
                    print("No hay gente")

    def acomodo_queue(self,level):
        self.temp = level
        while True:
            logging.debug("Nuevo nivel")
            logging.debug(self.temp)
            if (self.temp in TRIAGE.priority_number):
                logging.debug("SI ESTA")
                x = TRIAGE.priority_number[::-1]
                return x.index(self.temp)
            else:
                if(self.temp > TRIAGE.priority_number[0]):
                    self.temp -= 1
                elif(self.temp < TRIAGE.priority_number[0]):
                    return 0




def print_emergency(name, level):
    print("Paciente: " + name + "\nGravedad: " + str(level))

def check_queues():
    if(TRIAGE_niveles.level_one.isEmpty()):
        if (TRIAGE_niveles.level_two.isEmpty()):
            if (TRIAGE_niveles.level_three.isEmpty()):
                if (TRIAGE_niveles.level_four.isEmpty()):
                    if (TRIAGE_niveles.level_five.isEmpty()):
                        return "No hay","0"
                    else:
                        return TRIAGE_niveles.level_five.dequeue(),5
                else:
                    return TRIAGE_niveles.level_four.dequeue(),4
            else:
                return TRIAGE_niveles.level_three.dequeue(),3
        else:
            return TRIAGE_niveles.level_two.dequeue(),2
    else:
        return TRIAGE_niveles.level_one.dequeue(),1

def switch_match(level,name):
    if(len(TRIAGE.priority_name) >= len_max):
        match level:
            case 1:
                TRIAGE_niveles.level_one.enqueue(name)
                logging.debug("Enqueue en primer nivel")
            case 2:
                TRIAGE_niveles.level_two.enqueue(name)
                logging.debug("Enqueue en segundo nivel")
            case 3:
                TRIAGE_niveles.level_three.enqueue(name)
                logging.debug("Enqueue en tercer nivel")
            case 4:
                TRIAGE_niveles.level_four.enqueue(name)
                logging.debug("Enqueue en cuarto nivel")
            case 5:
                TRIAGE_niveles.level_five.enqueue(name)
                logging.debug("Enqueue en quinto nivel")
            case _:
                logging.debug("Error!")
    else:
        logging.debug("Agregando valor a lista")
        TRIAGE.set_list(name,level)
    print_emergency(name, level)



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    len_max = 5
    # len_max = check_int_input("Ingresa tu tamaño de queues")
    TRIAGE_niveles = levels_queue(len_max)
    TRIAGE = priority_queue(len_max)

    terminar = False

    while not terminar:

        menu_option = check_int_input(
            "Ingresa la opcion que quieres\n 1)Revisar lista \n 2)Registrar paciente \n 3)Nombre del siguiente paciente \n 4)Salir \n")
        if (menu_option == 1):
            TRIAGE.check_priority()
        elif (menu_option == 2):
            nombre = input("Ingresa nombre completo del paciente, por favor ")
            gravedad = check_int_input(
                "Ingrese la gravedad del paciente, por favor \n 1)Resucitacion \n 2)Emergencia \n 3)Urgencia \n 4)Urgencia menor \n 5)Sin urgencia \n")
            switch_match(gravedad, nombre)
        elif (menu_option == 3):
            TRIAGE.update_queue()
        elif (menu_option == 4):
            terminar = True
        else:
            print("Opcion incorrecta")





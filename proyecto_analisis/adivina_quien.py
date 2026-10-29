from random import *
import logging

P = [["frank", "man", "black", "no_g", "no_h", "no_v", "curly", "l"],
     ["anita", "woman", "blonde", "no_g", "no_h", "no_v", "straight", "s"],
     ["robert", "man", "brown", "no_g", "no_h", "no_v", "straight", "s"],
     ["herman", "man", "orange", "no_g", "no_h", "no_v", "straight", "l"],
     ["alfred", "man", "orange", "no_g", "no_h", "yes_v", "straight", "s"],
     ["victor", "man", "white", "no_g", "no_h", "no_v", "straight", "l"],
     ["sally", "woman", "black", "yes_g", "yes_h", "no_v", "curly", "m"],
     ["joe", "man", "white", "no_g", "yes_h", "no_v", "straight", "m"],
     ['mario', 'man', 'black', 'no_g', 'no_h', 'yes_v', 'curly', 's'],
     ["maria", "woman", "brown", "no_g", "yes_h", "no_v", "straight", "l"],
     ["charles", "man", "white", "yes_g", "no_h", "yes_v", "none", "m"],
     ['bernard', 'man', 'orange', 'no_g', 'yes_h', 'no_v', 'straight', 'm'],
     ["albert", "man", "black", "yes_g", "no_h", "no_v", "none", "s"],
     ["maximo", "man", "black", "no_g", "no_h", "yes_v", "straight", "l"],
     ["holly", "woman", "brown", "no_g", "no_h", "no_v", "straight", "s"],
     ["luke", "man", "blonde", "no_g", "no_h", "yes_v", "curly", "s"],
     ["paul", "man", "white", "yes_g", "no_h", "no_v", "straight", "s"],
     ["roger", "man", "brown", "no_g", "no_h", "yes_v", "none", "s"]]

logging.basicConfig(level=logging.DEBUG)

rd = randint(0, len(P) - 1)
persona_random = P[rd]
print(persona_random)

def check_int_input(msg):
    while True:
        try:
            print(msg)
            return int(input())
            break
        except ValueError:
            print("Invalid data, try again")

def check_person(x,caracteristic):
    global P
    new_person = []
    logging.debug("length = " + str(len(P)))
    for i in range(len(P)):
        if(caracteristic in P[i]):
            new_person.append(P[i])
            logging.debug(P[i])
    P = new_person
    logging.debug("New length = " + str(len(P)))
    return P

if __name__ == "__main__":

    while True:
        opcion = check_int_input("Questions about \n1)Sex \n2)Hair Color \n3)Glasses \n4)Headgear \n5)Facial hair \n6)Hair Type \n7)Nose size \n8)Guess \n9)Exit")
        # if(opcion >9 or opcion < 1):
        #     print("Opcion fuera de rango!")
        match opcion:
            case 1:
                sexo = check_int_input("It's : \n1)Man \n2)Woman")
                if(sexo == 1):
                    check_person(P,"man")
                elif(sexo == 2):
                    check_person(P,"woman")
                else:
                    print("Invalid data, try again")

            case 2:
                pelo = check_int_input("Does your character have : \n1)black hair \n2)brown hair \n3)orange hair \n4)white hair \n5)blonde")
                match pelo:
                    case 1:
                        check_person(P, "black")
                    case 2:
                        check_person(P, "brown")
                    case 3:
                        check_person(P, "orange")
                    case 4:
                        check_person(P, "white")
                    case 5:
                        check_person(P, "blonde")
                    case _:
                        print("Invalid data, try again")

            case 3:
                glass = check_int_input("Does your character have glasses?: \n1)yes \n2)no")
                if (glass == 1):
                    check_person(P, "yes_g")
                elif (glass == 2):
                    check_person(P, "no_g")
                else:
                    print("Invalid data, try again")

            case 4:
                glass = check_int_input("Does your character have headgear?: \n1)yes \n2)no")
                if (glass == 1):
                    check_person(P, "yes_h")
                elif (glass == 2):
                    check_person(P, "no_h")
                else:
                    print("Invalid data, try again")

            case 5:
                glass = check_int_input("Does your character have facial hair?: \n1)yes \n2)no")
                if (glass == 1):
                    check_person(P, "yes_v")
                elif (glass == 2):
                    check_person(P, "no_v")
                else:
                    print("Invalid data, try again")

            case 6:
                pelo = check_int_input(
                    "Does your character have : \n1)straight hair \n2)curly hair \n3)no hair")
                match pelo:
                    case 1:
                        check_person(P, "straight")
                    case 2:
                        check_person(P, "curly")
                    case 3:
                        check_person(P, "none")
                    case _:
                        print("Invalid data, try again")

            case 7:
                pelo = check_int_input(
                    "Does your character have : \n1)big nose \n2)medium nose \n3)small nose")
                match pelo:
                    case 1:
                        check_person(P, "l")
                    case 2:
                        check_person(P, "m")
                    case 3:
                        check_person(P, "s")
                    case _:
                        print("Invalid data, try again")

            case 8:
                persona = input("Cual persona crees que es?")
                #FUNCION PARA CHECAR SI ES LA PERSONA
                valido = False
                for i in range(len(P)):
                    if(persona in P[i]):
                        valido = True
                        break
                if(valido == True):
                    print("Si esta!")
                else:
                    print("No esta!")

            case 9:
                break
            case _:
                print(P)
                print("Opcion no valida por el momento")

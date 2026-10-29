
class Animal():
    def __init__(self,name):
        print("Te llamas ",name)


class mamifero(Animal):
    def __init__(self,mamifero_name):
        print("Eres animal, ",mamifero_name)
        super().__init__(mamifero_name)	


class perro(mamifero):   
    def __init__(self,mamifero_name):
        print("Ladra", mamifero_name)
        super().__init__(mamifero_name)

class ladra(perro):
 
    def __init__(self, name):
 
        print("Woof Woof")
        super().__init__(name)

Perrito = ladra("Rocky")

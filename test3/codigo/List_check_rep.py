from numpy import *


li = ["x","y","z","a","b","b"]


rep = li.count("b")
index = []

if rep > 1:
    print("Lista con dato repetido")
    for i in range(rep):
        index.append(li.index("b")+i)
        li.remove("b")
        print(li)
else:
    print("lista sin dato repetido")
    
for i in range(len(index)):
    li.insert(index[i], 'b')

li_array = zeros(len(li))

print(li)
for i in range(len(li)):
    print("Id de la posision " + str(i) + " = "+ str(id(li[i])))
    li_array[i] = int(ascii(li[i]))
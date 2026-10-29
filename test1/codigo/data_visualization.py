# import random
# import matplotlib.pyplot as plt
#
# p = list(range(14))
# q = [random.randint(0, 20) for _ in range(14)]
#
#
# def filtro(p, q):
#     q = [random.randint(0, 20) for _ in range(14)]
#     return p, q
#
#
# fig1 = plt.figure("Filtro")
# fig1.subplots_adjust(hspace=0.5, wspace=0.5)
#
# for i in range(1, 5):
#     p, q = filtro(p, q)
#
#     ax = fig1.add_subplot(2, 2, i)
#     ax.plot(p,q,"g--")
#     ax.set_xlabel("z")
#     ax.set_ylabel("w")
#     ax.set_title("cordenadas xy")
#     ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
#     # Pintar los ejes pasando por (0,0)
#     ax.axhline(0, color='black', linewidth=0.5)
#
#
#
# def npotencia(array, exp):
#     return [n ** exp for n in array]
#
#
# # Creamos otra figura, se mostrar
# fig2 = plt.figure("n ** i")
# fig2.subplots_adjust(hspace=0.5, wspace=0.5)
#
# x = list(range(1, 10))
# for i in range(2, 6):
#     y = npotencia(x, i)
#     ax = fig2.add_subplot(2, 2, i-1)
#     ax.plot(x, y, "r-.")
#     ax.set_xlabel("x")
#     ax.set_ylabel("y")
#     ax.set_title("n ** {}".format(i))
#     ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
#     ax.axhline(0, color='black', linewidth=0.5)
#
# plt.show()



import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from numpy import random



x = random.randint(50,100,40)
len_x = len(x)
print(type(x))
print(len_x)
print(x)

calf_50 = 0
calf_60 = 0
calf_70 = 0
calf_80 = 0
calf_90 = 0



for i in range(len_x):
    if(x[i] >= 90):
        calf_90 += 1
    elif(x[i] >= 80):
        calf_80 += 1
    elif (x[i] >= 70):
        calf_70 += 1
    elif (x[i] >= 60):
        calf_60 += 1
    else:
        calf_50 += 1

idx = []
for i in range(len_x):
    idx.append(i)
print(idx)

plt.scatter(idx,x)
plt.show()
print(calf_90)
print(calf_80)
print(calf_70)
print(calf_60)
print(calf_50)

# setting the ranges and no. of intervals
range = (50, 100)
bins = 5

# plotting a histogram
counts, bins, bars = plt.hist(x, bins, range, color='green', histtype='bar', rwidth=0.8)
print(counts)
plt.show()

print(type(bins))
print(len(counts))
plt.barh(bins[1:],counts,color = "red")

#pie-chart
cal_list = [calf_50,calf_60,calf_70,calf_80,calf_90]
cal_identifier = ["50-59","60-69","70-79","80-89","90-100"]

colors = ['r', 'y', 'g', 'b']

# plotting the pie chart
# plt.pie(cal_list, labels=cal_identifier,
#         startangle=90, shadow=True,
#         radius=1.2, autopct='%1.1f%%')

plt.show()


##
primer_periodo = 866/3
segundo_periodo = 838/5

print("Primer periodo " + str(primer_periodo))
print("Segundo periodo " + str(segundo_periodo))

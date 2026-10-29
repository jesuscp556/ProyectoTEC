import pandas as pd
import matplotlib.pyplot as plt

data_set = pd.read_csv("dataset_excel/Titanic.csv")

#Ver nombres de las columnas
columns_names = data_set.columns.values
print(columns_names)
print(type(data_set))
#

data_sex = data_set["Sex"]
print(data_sex[100])


data_survived = data_set['Survived']
range_survived = (data_survived.min(),data_survived.max())
bins_survived = 2

# # plotting a histogram
data_pclass = data_set["Pclass"]

data_set_type = set(data_pclass)
print(data_set_type)

range_pclass = (data_pclass.min(),data_pclass.max())
bins_pclass = 3

fig1 = plt.figure("Titanic")
fig1.subplots_adjust(hspace=0.5, wspace=0.5)

plot_survived = fig1.add_subplot(2, 1, 1)
plot_survived.hist(data_survived, bins_survived, range_survived, color='green', histtype='bar', rwidth=0.6)
plot_survived.set_title("Survived")
plot_survived.set_xticks([0,1], ["Die","Survive"])


plot_pclass = fig1.add_subplot(2,1,2)
plot_pclass.hist(data_pclass,bins_pclass,range_pclass, color = "blue", histtype='bar', rwidth=0.8 )
plot_pclass.set_title("Class Type")
plot_pclass.set_xticks([1, 2, 3], ["Primera","Segunda","Tercera"])

plot_pclass.set_ylabel("Data values")
plot_pclass.set_xlabel("Data sets")


data_set_age = data_set["Age"]
data_age_description = data_set_age.describe()
print(data_age_description)

set_age = set(data_sex)
print(set_age)


fig2 = plt.figure("Edad de los pasajeros")
range_age = (data_set_age.min(),data_set_age.max())
bins_age = 11
plot_age = fig2.add_subplot(1,1,1)


print(data_set_age.std())
print(data_set_age.mean())
print(data_set_age.describe())
plot_age.hist(data_set_age,bins_age,range_age, color = "blue", histtype='bar', rwidth=0.8 )
plot_age.set_title("Edades de los tripulantes")

plt.show()



# print(data_set_class)
#
# for idx in range(len(columns_names)):
#     print(columns_names[idx])
#

# data_description = data_set_class.describe()
# print(data_description)
#
# data_age = data_set["Age"]
# print(data_age.min())
# print(type(data_age.min()))
#
# range = (data_age.min(),data_age.max())
# bins = 10
#
# # # plotting a histogram
# plt.hist(data_set_class, bins, range, color='green', histtype='bar', rwidth=0.8)
# plt.show()
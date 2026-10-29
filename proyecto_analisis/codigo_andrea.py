#/Users/usuario/Downloads
import pandas as pd
import matplotlib.pyplot as plt
archivo = pd.read_csv("dataset_excel/superstore.csv",encoding='latin-1') #csv pesa 1/4 menos que el xls pero con la misma cantidad de información
columns_names = archivo.columns.values #<< retorna etiquetas de qué tienen las columnas (te lo da como un vector)
print(columns_names) #Ver nombres de la columna
print(type(columns_names)) #Ver el tipo de los nombres de la columna

ship_mode = archivo["Ship Mode"]
bin_ship_mode = 3

order_priority = archivo["Order Priority"]
bin_order_priority = 4

shipping_cost = archivo["Shipping Cost"]
print(shipping_cost.describe())
range_s = (shipping_cost.min(), shipping_cost.max())
#range_s = (0,100)
bin_shipping_cost = 500
print(shipping_cost)

fig1 = plt.figure("Ship Mode")
fig1.subplots_adjust(hspace= 0.5, wspace= 0.5)
plot_ship_mode = fig1.add_subplot(2,1,1) #fig1.add_subplot(2,2,1)(filas, columnas, posición donde va a estar la gráfica)
plot_ship_mode.hist(ship_mode, bin_ship_mode, color = "green", histtype = "bar", rwidth = 0.8)
plot_ship_mode.set_title("Ship Mode")

plot_order_priority = fig1.add_subplot(2,1,2)
plot_order_priority.hist(order_priority, bin_order_priority, color = "green", histtype = "bar", rwidth = 0.8)
plot_order_priority.set_title("Order Priority")

#a = shipping_cost.describe()

fig2 = plt.figure("Shipment")
fig2.subplots_adjust(hspace= 0.8, wspace= 0.8)

plot_shipping_cost = fig2.add_subplot(1,1,1) #fig1.add_subplot(2,2,1)(filas, columnas, posición donde va a estar la gráfica)
counts, bins, bars = plot_shipping_cost.hist(shipping_cost, bin_shipping_cost,range_s, color = "red", histtype = "bar", rwidth = 0.4)
print(counts)
print(bins)
print(bars)
plot_shipping_cost.set_title("Shipping Cost")

fig3 = plt.figure("Plot Shipment")
plot_s_c = fig3.add_subplot(1,1,1)
plot_s_c.plot(shipping_cost)
plot_s_c.set_title("Plot Shipping cost")


#plt.legend()

plt.show()


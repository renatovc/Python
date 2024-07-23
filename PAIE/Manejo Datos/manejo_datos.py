import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Datos.csv", sep=";",decimal=",")

(fil,col) = (df.shape)
print("Filas del Data Frame", fil)
print("Columnas del Data Frame", col)

print(df.sort_values("Costo kw/hora", ascending=True))

ckwh = df.iloc[:fil,2]
print("Columna con datos de consumo:")
print(ckwh)

print("Consumos Máximos y Mínimos en KW/H")
print("Máximo", ckwh.max())
print("Mínimo", ckwh.min())

dfcasas = df[df.iloc[:fil,0] == "casa"]
dfcasas = dfcasas.sort_values("Pago Promedio/Dia", ascending=True)
print(dfcasas)
print("Casa de Menor Pago por Día", dfcasas.iloc[0,0], dfcasas.iloc[0,1])
print("================================================================")

tabla = df.loc[:fil, ("Consumo kw/hora","Costo kw/hora","Pago Promedio/Dia")]
print(tabla)
print(tabla.describe())

df["PromedioDatos"] = tabla.mean(axis = 1)
df["Nivel Consumo"] = np.where(df["Consumo kw/hora"] >= 10, "Sobreconsumo", "Consumo Normal")

dfdpto = df[df.iloc[:fil,0] == "dpto"]
print(dfdpto)

x = dfdpto.iloc[:fil,1]
y = dfdpto.iloc[:fil,4]
ax = plt.subplot()

ax.bar(x,y)
ax.set_xlabel("Departamentos", fontdict = {"fontsize": 14, "fontweight": "bold", "color": "tab:blue"})
ax.set_ylabel("Pago Promedio Por Día", fontdict= {"fontsize": 14, "fontweight": "bold", "color": "tab:blue"})
plt.show()

x = dfdpto.iloc[:fil,1]
val = ["","","","","","","","","",""]
larg = len(x)
i = 0
while(i < larg):
    dato = str(x.iloc[i])
    val[i] = str(dato)
    i += 1

print(val)
ax = plt.subplot()
ax.bar(val, y)
ax.set_xlabel("Departamentos", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_ylabel("Pago Promedio por Día",fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
plt.show()
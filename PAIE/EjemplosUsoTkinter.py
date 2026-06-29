# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 23:48:31 2023

@author: 56982
"""
from tkinter import messagebox, ttk
import tkinter


# Funciones que serán invocadas al presionar un botón
def saludo(saludo):
    
    messagebox.showinfo(
        message=saludo,
        title="Saludo Inicial"
    )
    
def textoDeLaCaja():
    text20 = cajaTexto.get()
    etiqueta2["text"]="El texto ingresado es: " + text20
    
def show_selection():
    # Obtener la opción seleccionada.
    #selection = combo.current() #con esta se obtiene el indice de la opción seleccionada
    selection = combo.get()
    messagebox.showinfo(
        message=f"La opción seleccionada es: {selection}",
        title="Selección"
    )

def close():
    
   # Creando un mensaje de consulta 
   response = tkinter.messagebox.askquestion("Consulta", "Esta seguro que desea abandonar el programa?")
   
   # De acuerdo a la respuesta se muestra en un label o etiqueta de texto un mensaje
   if response == "yes":
       #cierra la ventana
       ventana.destroy()

    
    
    
   
  
### Fin funciones



# Primero se debe crear la ventana y darle una dimensión.
ventana = tkinter.Tk()
ventana.geometry("800x400")
ventana.title("Ejemplo ventana")



# Crear una etiqueta
etiqueta = tkinter.Label(ventana,text="Ingresa tu nombre:")
etiqueta.place(x=10, y=40)

# Otras formas de posicionar los elementos
#etiqueta.pack(side= tkinter.BOTTOM )
#etiqueta.pack(side= tkinter.TOP )
#etiqueta.pack()


# Crear una etiqueta
etiqueta2 = tkinter.Label(ventana,text="")
etiqueta2.place(x=10, y=60)


# Crear una Caja de Texto
cajaTexto = tkinter.Entry(ventana)
cajaTexto.place(x=120, y=40)


# Crear diversos botones, con distintas maneras de posicionarlos en la ventana
boton1 = tkinter.Button(ventana, text="Presiona",padx=40,pady=5,command =lambda: saludo("Bienvenido a la clase de TKinter"))
boton1.pack()


boton2=tkinter.Button(ventana, text="Click",padx=30,pady=10,command = textoDeLaCaja)
boton2.pack()

# Create a Button to call close()
boton3=tkinter.Button(ventana, text= "cerrar ventana", font=("Calibri",14,"bold"), command=close).pack(pady=20)
#boton1.grid(row = 1,column = 0)
#boton2.grid(row = 2,column = 0)

# Crear un combo box
combo = ttk.Combobox(state="readonly",values=["Python", "C", "C++", "Java"])
combo.place(x=50, y=150)


# Otro botón que ejecuta la funcion que muestra la seleccion hecha en el combobox
button = tkinter.Button(text="Mostrar selección", command=show_selection)
button.place(x=50, y=200)









#Esta línea siempre debe ir al final del programa. Al ejecutarlo, provoca que el programa no termine y la interfaz
#quede a la espera de que el usuario realice alguna accion.
ventana.mainloop()
















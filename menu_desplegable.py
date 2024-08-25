#Voy a trabajar con ttkinter

import tkinter as tk
import tkinter as ttk
from tkinter import messagebox


def opcion_uno():
       pass

def opcion_dos():
       pass


ventana = tk.Tk()
ventana.title("Prueba del menú como botón")
ventana.geometry("400x500")
ventana.config(bg="#000c18")
ventana.resizable(width=0, height=0)




#Imagen que va a servir para el boton menú
imagen = tk.PhotoImage(file="images/plus.png")


#Creo el botón para usarlo como menú
boton_menu = ttk.Menubutton(ventana, image=imagen)
menu = tk.Menu(boton_menu, tearoff=0)
menu.config(bg="#000c18", fg="white", font=("Calibri", 20, "bold")) #(color_fondo, color_fuente, fuente(tipo, tamaño, estilo))
boton_menu['menu'] = menu
menu.add_command(label="Nueva contraseña", command=opcion_uno)
menu.add_command(label="Historial de contraseñas", command=opcion_dos)

boton_menu.place(x=300, y=400)
boton_menu.config(bg="#000c18")




ventana.mainloop()

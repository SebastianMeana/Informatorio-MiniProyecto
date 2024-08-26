import tkinter as ttk
from tkinter import messagebox

ventana = ttk.Tk()
ventana.title("Ventana principal")
ventana.geometry("500x700")
ventana.config(bg="#121417")
ventana.resizable(width=0, height=0)

frame_header = ttk.Frame(ventana, width=500, height=70)
frame_header.config(bg="black")
frame_header.pack()

frame_hora = ttk.Frame(ventana, width=500, height=85)
frame_hora.config(bg="white")
frame_hora.pack()

frame_opc1 = ttk.Frame(ventana, width=500, height=60)
frame_opc1.config(bg="red")
frame_opc1.pack()

frame_opc2 = ttk.Frame(ventana, width=500, height=60)
frame_opc2.config(bg="yellow")
frame_opc2.pack()

lbl_titulo = ttk.Label(frame_header, text="Generador de Contraseñas", width=36, height=2)
lbl_titulo.config(bg="#121417", fg=("white"), font=("Calibri", 20, "bold"), anchor="center")
lbl_titulo.place(x=0, y=0)



ventana.mainloop()
import tkinter as tk
from tkinter import ttk
import string
import random

def main():



    ventana= tk.Tk()
    ventana.state('zoomed')
    ventana.configure(bg='gray25')
    ventana.columnconfigure(0 ,pad=5, weight=1)
    ventana.columnconfigure(1 ,pad=5, weight=2)
    ventana.columnconfigure(2 ,pad=5, weight=1)
    ventana.rowconfigure(0, weight=1)

    control_alfabetico_mayus= tk.BooleanVar(value=False)
    control_alfabetico_minus= tk.BooleanVar(value=False)
    control_numerico= tk.BooleanVar(value=False)
    control_especiales= tk.BooleanVar(value=False)
    control_longitud= tk.IntVar()
    contrasenia_generada= tk.StringVar()

    estilos= ttk.Style()
    estilos.configure('Custom.TLabel', background='gray25', font='Calibri 12 bold', foreground='white')
    estilos.configure('TScale', background='gray25', font='Calibri 12 bold')
    estilos.configure('TCheckbutton', background='gray25', font='Calibri 12 bold', foreground='white')




    def generar_frame_izq():
        frame_izquierdo= tk.Frame(ventana, bg='red')
        frame_izquierdo.grid(row=0, column=0, sticky='nsew')
        etiqueta_izquierda= ttk.Label(frame_izquierdo, text='Generador de Contraseña', font='Calibri 20 bold')
        etiqueta_izquierda.pack(pady=5)



    def generar_frame_cen():
        caracteres_numericos= string.digits
        caracteres_alfanum_minus= string.ascii_lowercase
        caracteres_alfanum_mayus= string.ascii_uppercase
        caracteres_simbolos= string.punctuation
        caracteres_permitidos= []
        


        def actualizar_label_longitud(valor):
            valor_actual= scale_longitud.get()
            valor_redondeado= round(float(valor))
            if valor_actual!=valor_redondeado:
                scale_etiqueta.config(text=valor_redondeado)
                scale_longitud.set(valor_redondeado)

        def controlador_checkbuttons():
            caracteres_permitidos.clear()
            if control_alfabetico_mayus.get():
                caracteres_permitidos.append(caracteres_alfanum_mayus)	
            if control_alfabetico_minus.get():
                caracteres_permitidos.append(caracteres_alfanum_minus)
            if control_numerico.get():
                caracteres_permitidos.append(caracteres_numericos)
            if control_especiales.get():
                caracteres_permitidos.append(caracteres_simbolos)


        def generar_contrasenia():
            contrasenia=''

            for i in range(0, control_longitud.get()):
                indice_grupo= random.randint(0, len(caracteres_permitidos))
                grupo_seleccionado= caracteres_permitidos[indice_grupo-1]
                indice_caracter= random.randint(0, len(grupo_seleccionado))
                contrasenia= contrasenia+grupo_seleccionado[indice_caracter-1]
            contrasenia_generada.set(contrasenia)
            area_texto.configure(state='normal')
            area_texto.delete('1.0', tk.END)
            area_texto.insert(tk.END, contrasenia_generada.get())
            area_texto.configure(state='disabled')
        

        frame_centro= tk.Frame(ventana, bg='gray25')
        frame_centro.grid(row=0, column=1, sticky='nsew')

        etiqueta_central= ttk.Label(frame_centro, text='Nueva Contraseña', font='Calibri 20 bold', style='Custom.TLabel')
        area_texto= tk.Text(frame_centro, height=1, width=40, font='Calibri 20 bold')

        scale_contenedor= tk.Frame(frame_centro, padx=5, pady=40, bg='Gray25')
        scale_etiqueta_2= ttk.Label(scale_contenedor, text='Longitud de Contraseña',style='Custom.TLabel')
        scale_etiqueta= ttk.Label(scale_contenedor, text='0',style='Custom.TLabel')
        scale_longitud= ttk.Scale(scale_contenedor, variable=control_longitud, from_=4, to=30,command=actualizar_label_longitud, style='TScale')

        check_contenedor= tk.Frame(frame_centro, padx=5, pady=5, bg= 'Gray25')
        check_numerico= ttk.Checkbutton(check_contenedor, text='Dígitos', variable=control_numerico, style= 'TCheckbutton', command=controlador_checkbuttons)
        check_alfabeticos_mayus= ttk.Checkbutton(check_contenedor, text='Alfabeto Mayúsculas', variable=control_alfabetico_mayus, style= 'TCheckbutton', command=controlador_checkbuttons)
        check_alfabeticos_minus= ttk.Checkbutton(check_contenedor, text='Alfabeto Minúsculas', variable=control_alfabetico_minus, style= 'TCheckbutton', command=controlador_checkbuttons)
        check_especiales= ttk.Checkbutton(check_contenedor, text='Caracteres Especiales', variable=control_especiales, style= 'TCheckbutton', command=controlador_checkbuttons)

        boton_generador= ttk.Button(frame_centro, text='Generar Contraseña', command=generar_contrasenia)

        etiqueta_central.pack(pady=5)
        area_texto.pack( pady=(150, 20))

        scale_contenedor.pack()
        scale_etiqueta_2.pack(pady=5)
        scale_etiqueta.pack(side='left', padx=5)
        scale_longitud.pack(padx=5)


        check_contenedor.pack()
        check_numerico.pack( padx=5 ,pady=5, side='left')
        check_alfabeticos_mayus.pack( padx=5 ,pady=5, side='left')
        check_alfabeticos_minus.pack( padx=5 ,pady=5, side='left')
        check_especiales.pack( padx=5 ,pady=5, side='left')

        boton_generador.pack()





    def generar_frame_der():
        frame_derecho= tk.Frame(ventana, bg='green')
        frame_derecho.grid(row=0, column=2, sticky='nsew')
        etiqueta_derecha= ttk.Label(frame_derecho, text='Historial de Contraseñas', font='Calibri 20 bold')
        etiqueta_derecha.pack(pady=5)




    #ventana.rowconfigure(0, weight=1)
    #ventana.columnconfigure(0, weight=1)

    #frame= tk.Frame(ventana, bg='gray25')
    #frame.grid(row=0, column=0, sticky='nsew')
    generar_frame_izq()
    generar_frame_cen()
    generar_frame_der()
    ventana.mainloop()


if __name__=='__main__':
    main()
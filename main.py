import tkinter as tk
from tkinter import ttk

def main():



    ventana= tk.Tk()
    ventana.state('zoomed')
    ventana.configure(bg='gray25')
    ventana.columnconfigure(0 ,pad=5, weight=1)
    ventana.columnconfigure(1 ,pad=5, weight=2)
    ventana.columnconfigure(2 ,pad=5, weight=1)
    ventana.rowconfigure(0, weight=1)

    control_alfabetico= tk.BooleanVar(value=False)
    control_numerico= tk.BooleanVar(value=False)
    control_especiales= tk.BooleanVar(value=False)
    control_longitud= tk.IntVar()

    estilos= ttk.Style()
    estilos.configure('Custom.TLabel', background='gray25', font='Calibri 12 bold')
    estilos.configure('TScale', background='gray25', font='Calibri 12 bold')
    estilos.configure('TCheckbutton', background='gray25', font='Calibri 12 bold')




    def generar_frame_izq():
        frame_izquierdo= tk.Frame(ventana, bg='red')
        frame_izquierdo.grid(row=0, column=0, sticky='nsew')
        etiqueta_izquierda= ttk.Label(frame_izquierdo, text='Generador de Contraseña', font='Calibri 20 bold')
        etiqueta_izquierda.pack(pady=5)



    def generar_frame_cen():

        def actualizar_label_longitud(valor):
            valor_actual= scale_longitud.get()
            valor_redondeado= round(float(valor))
            if valor_actual!=valor_redondeado:
                scale_etiqueta.config(text=valor_redondeado)
                scale_longitud.set(valor_redondeado)
        

        frame_centro= tk.Frame(ventana, bg='gray25')
        frame_centro.grid(row=0, column=1, sticky='nsew')

        etiqueta_central= ttk.Label(frame_centro, text='Nueva Contraseña', font='Calibri 20 bold', style='Custom.TLabel')
        area_texto= tk.Text(frame_centro, height=1, width=40, font='Calibri 20 bold', state='disabled')

        scale_contenedor= tk.Frame(frame_centro, padx=5, pady=40, bg='Gray25')
        scale_etiqueta_2= ttk.Label(scale_contenedor, text='Longitud de Contraseña',style='Custom.TLabel')
        scale_etiqueta= ttk.Label(scale_contenedor, text='0',style='Custom.TLabel')
        scale_longitud= ttk.Scale(scale_contenedor, variable=control_longitud, from_=4, to=30,command=actualizar_label_longitud, style='TScale')

        check_contenedor= tk.Frame(frame_centro, padx=5, pady=5, bg= 'Gray25')
        check_numerico= ttk.Checkbutton(check_contenedor, text='Caracteres Numéricos', variable=control_numerico, style= 'TCheckbutton')
        check_alfabeticos= ttk.Checkbutton(check_contenedor, text='Caracteres Alfabéticos', variable=control_alfabetico, style= 'TCheckbutton')
        check_especiales= ttk.Checkbutton(check_contenedor, text='Caracteres Especiales', variable=control_especiales, style= 'TCheckbutton')

        etiqueta_central.pack(pady=5)
        area_texto.pack( pady=(150, 20))

        scale_contenedor.pack()
        scale_etiqueta_2.pack(pady=5)
        scale_etiqueta.pack(side='left', padx=5)
        scale_longitud.pack(padx=5)


        check_contenedor.pack()
        check_numerico.pack( padx=5 ,pady=5, side='left')
        check_alfabeticos.pack( padx=5 ,pady=5, side='left')
        check_especiales.pack( padx=5 ,pady=5, side='left')





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
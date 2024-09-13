import tkinter as tk
from tkinter import ttk
import string
import random

def main():

    # Configuraciones de Ventana
    ventana= tk.Tk()
    ventana.state('zoomed')
    ventana.minsize(700, 500)
    ventana.configure(bg='DodgerBlue')
    ventana.columnconfigure(0 ,pad=5, weight=1)
    ventana.columnconfigure(1 ,pad=5, weight=2)
    ventana.columnconfigure(2 ,pad=5, weight=1)
    ventana.rowconfigure(0, weight=1)
    ventana.title('Generador de Contraseña')

    # Variables de Control
    control_alfabetico_mayus= tk.BooleanVar(value=False)
    control_alfabetico_minus= tk.BooleanVar(value=False)
    control_numerico= tk.BooleanVar(value=False)
    control_especiales= tk.BooleanVar(value=False)
    control_longitud= tk.IntVar(value=4)  # Establecemos el valor inicial en 4
    contrasenia_generada= tk.StringVar()

    # Estilos de Widgets
    estilos= ttk.Style()
    estilos.configure('Custom.TLabel', background='DodgerBlue', font='Calibri 12 bold', foreground='white')
    estilos.configure('TScale', background='DodgerBlue', font='Calibri 12 bold')
    estilos.configure('TCheckbutton', background='DodgerBlue', font='Calibri 12 bold', foreground='white')

    # Método para Crear Frame Central
    def generar_frame_cen():
        # Variables contenedores de Carácteres y Digitos
        caracteres_numericos= string.digits
        caracteres_alfanum_minus= string.ascii_lowercase
        caracteres_alfanum_mayus= string.ascii_uppercase
        caracteres_simbolos= '#@$'
        caracteres_permitidos= []
        caracteres_seleccionados = []  # Para almacenar al menos un carácter de cada grupo seleccionado

        # Método para Actualizar el Número del Widget de Longitud
        def actualizar_label_longitud(valor):
            valor_actual= scale_longitud.get()
            valor_redondeado= round(float(valor))
            if valor_actual!=valor_redondeado:
                scale_etiqueta.config(text=valor_redondeado)
                scale_longitud.set(valor_redondeado)

        # Método para Controlar los Checkbutttons
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

        # Método con Lógica para generar contraseña
        def generar_contrasenia():
            contrasenia = []
            caracteres_seleccionados.clear()
            
            # Ejecución si no se seleccionó ningun campo
            if control_alfabetico_mayus.get() == False and control_alfabetico_minus.get() == False and control_numerico.get() == False and control_especiales.get() == False:
                area_texto.delete('1.0', tk.END)
                area_texto.insert(tk.END , 'Debes seleccionar al menos un Tipo de Caracter')
                area_texto.configure(state='disabled')
                return
            
            # Asegurarse de seleccionar al menos un carácter de cada tipo habilitado
            if control_alfabetico_mayus.get():
                contrasenia.append(random.choice(caracteres_alfanum_mayus))
            if control_alfabetico_minus.get():
                contrasenia.append(random.choice(caracteres_alfanum_minus))
            if control_numerico.get():
                contrasenia.append(random.choice(caracteres_numericos))
            if control_especiales.get():
                contrasenia.append(random.choice(caracteres_simbolos))
            
            # Rellenar el resto de la contraseña con caracteres aleatorios de los grupos permitidos
            while len(contrasenia) < control_longitud.get():
                grupo_seleccionado = random.choice(caracteres_permitidos)
                contrasenia.append(random.choice(grupo_seleccionado))
            
            # Mezclar la contraseña para evitar patrones predecibles
            random.shuffle(contrasenia)

            # Convertir la lista en un string y actualizar el widget de texto
            contrasenia_generada.set(''.join(contrasenia))
            area_texto.configure(state='normal')
            area_texto.delete('1.0', tk.END)
            area_texto.insert(tk.END, contrasenia_generada.get())
            area_texto.configure(state='disabled')
        
        
        # Agregando Elementos a la Ventana
        frame_centro= tk.Frame(ventana, bg='DodgerBlue')
        frame_centro.grid(row=0, column=1, sticky='nsew')

        etiqueta_central= ttk.Label(frame_centro, text='Generar Contraseña', font='Calibri 20 bold', style='Custom.TLabel')
        area_texto= tk.Text(frame_centro, height=1, width=40, font='Calibri 20 bold')
        area_texto.configure(state='disabled')

        scale_contenedor= tk.Frame(frame_centro, padx=5, pady=40, bg='DodgerBlue')
        scale_etiqueta_2= ttk.Label(scale_contenedor, text='Longitud de Contraseña',style='Custom.TLabel')
        scale_etiqueta= ttk.Label(scale_contenedor, text='4',style='Custom.TLabel')  # Etiqueta inicial con valor 4
        scale_longitud= ttk.Scale(scale_contenedor, variable=control_longitud, from_=4, to=30,command=actualizar_label_longitud, style='TScale')
        scale_longitud.set(4)  # Establecemos el valor inicial de la escala en 4

        check_contenedor= tk.Frame(frame_centro, padx=5, pady=5, bg= 'DodgerBlue')
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

    generar_frame_cen()
    ventana.mainloop()

if __name__=='__main__':
    main()

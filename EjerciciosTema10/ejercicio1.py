import tkinter
from tkinter import ttk
from tkinter.ttk import Button


def reiniciar():
    seleccion.set('')
    label['text'] = 'Seleccion'


def muestraSeleccion():
    label['text'] = seleccion.get()


ventana = tkinter.Tk()
seleccion = tkinter.StringVar()

r_btn_1 = ttk.Radiobutton(ventana, text='Kotlin', value='Kotlin', variable=seleccion, command=muestraSeleccion)
r_btn_2 = ttk.Radiobutton(ventana, text='Python', value='Python', variable=seleccion, command=muestraSeleccion)
r_btn_3 = ttk.Radiobutton(ventana, text='Java', value='Java', variable=seleccion, command=muestraSeleccion)
r_btn_1.grid(column=0, row=1, sticky=tkinter.W, padx=15)
r_btn_2.grid(column=0, row=2, sticky=tkinter.W, padx=15)
r_btn_3.grid(column=0, row=3, sticky=tkinter.W, padx=15)

btn_reset = Button(ventana, text="Reiniciar", command=reiniciar)
btn_reset.grid(column=0, row=4, padx=15)

label = ttk.Label(ventana, text='Seleccion')
label.grid(column=0, row=5)

ventana.mainloop()

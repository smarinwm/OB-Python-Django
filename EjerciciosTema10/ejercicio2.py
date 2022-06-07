import tkinter
from tkinter import ttk

ventana = tkinter.Tk()
seleccion = tkinter.StringVar()

label = ttk.Label(ventana, text='Selecciona lenguaje.')
label.grid(column=0, row=1)

lista = ['Kotlin', 'Python', 'Java']
lista_items = tkinter.StringVar(value=lista)
list_caja = tkinter.Listbox(ventana, listvariable=lista_items)

list_caja.grid(column=0, row=2, sticky=tkinter.W, padx=10, pady=10)

ventana.mainloop()

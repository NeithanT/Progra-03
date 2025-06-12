"""

"""

import tkinter as tk
from tkinter import ttk

# create window
def showMenu():
    """
        Funcion principal del programa la cual
        crea la interfaz y le muestra el menu al
        usuario
    """

    app = tk.Tk()
    app.title("Progra03")
    app.geometry("700x700")

    #text_area = tk.Text(root, height=5, width=30)
    #text_area.pack()

    frm = ttk.Frame(app, padding=10)
    frm.grid()
    
    #ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="prueba", command=whenClicked).grid(column=1, row=0)

    #for x in range(3):
    #    for y in range(3):
    #        ttk.Label(frm, text="Hello World!").grid(column=x, row=y)

    """
    frame = tk.Frame(root, borderwidth=2, relief="groove")
    frame.pack()

    entry_name = tk.Entry(root)
    entry_name.grid(row=1, column=1)
    label_name = tk.Label(root, text="Name:")
    label_name.grid(row=2, column=2)
    
    """

    app.mainloop()


def whenClicked():
    print("boton clickeado")

def button(root):

     # Botones 
    button = tk.Button(root, text="Click Me", command=whenClicked)
    button.pack() # Or .grid(), or .place() to display it

def text(root):

    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack() # Or .grid(), or .place() to display it

def text_input(root):

    # Entrada de texto 
    entry = tk.Entry(root)
    entry.pack()

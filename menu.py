"""

"""

from tkinter import *

# create window
def showMenu():
    """
        Funcion principal del programa la cual
        crea la interfaz y le muestra el menu al
        usuario
    """

    app = Tk()
    #app.configure(bg="lightblue")

    #app.wm_attributes('-transparentcolor','grey')
    app.overrideredirect(True)

    #app.title("Progra03")
    app.geometry("1280x720")

    def readjust(e):
        app.geometry(f'+{e.x_root}+{e.y_root}')

    

    black_jack_image = PhotoImage(file = 'designs/blackjack.png')
    black_jack_label = Label(app,border=0,bg='lightblue',image= black_jack_image)
    black_jack_label.pack(fill=BOTH,expand=True)
    black_jack_label.bind('<B1-Motion>',readjust)
    #black_jack_button = Button(app,bg="lightblue",
    #                              image=black_jack_image,
    #                              borderwidth=0)
    
    exit_button = Button(app,command=app.quit,width=10,height=5)
    exit_button.place(x=100,y=400)

    """black_jack_button = tk.Button(text="prueba",
                                  font=("Arial",12),bg="black",
                                  fg="white",borderwidth=0,
                                  compound=tk.CENTER,
                                  image=black_jack_image,
                                  width=35,
                                  height=35)"""
    #black_jack_button.place(x=10,y=10)
    
    app.mainloop()


def whenClicked():
    print("boton clickeado")

def button(root):

    # Botones 

    def config():
        button.configure(bg="pink",fg="red")
    """
        bg = color del fondo
        fg = color del texto
        command = funcion que llama, config para hacerlo dinamico
    """
    button = Button(root, text="Click Me", command=whenClicked)

    #button.grid(row=0,column=0,padx=10,pady=10) # Or .grid(), or .place() to display it

    button.pack() # Or .grid(), or .place() to display it

def text(root):

    label = Label(root, text="Hello, Tkinter!")
    label.pack() # Or .grid(), or .place() to display it

def text_input(root):

    # Entrada de texto 
    entry = Entry(root)
    entry.pack()

def text_area(root):


    text_area = Text(root, height=5, width=30)
    text_area.pack()

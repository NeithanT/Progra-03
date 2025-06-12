"""

"""

from tkinter import Tk, Canvas, Button, PhotoImage



# create window
def showMenu():
    """
        Funcion principal del programa la cual
        crea la interfaz y le muestra el menu al
        usuario
    """
    
        
    def on_blackjack_click(event):
        """
            Maneja la funcion para el boton de blackjack
        """
        
        print("blackjack!")
        # Agregar el resto de funcionalidad


    def on_houndsandrabbits_click(event):
        """
            Maneja la funcion para el boton de 
            hounds and rabbits
        """
        
        print("hounds and rabbit!")

        # Agregar el resto de funcionalidad


    def on_exit_click(event):
        """
            Maneja la funcion para el boton de salida
        """
        
        app.quit() 

    app = Tk()
        
    app.geometry("1280x720")
    app.configure(bg = "#88E4F8")


    menu_canvas = Canvas(
        app,
        bg = "lightblue",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness= 0,
        relief = "ridge"

    )

    menu_canvas.place(x = 0, y = 0)
    menu_canvas.create_rectangle(
        0.0,
        0.0,
        1280.0,
        70.0,
        fill = "#67CDF2",
        outline=""
    )

    houndsandrabbits_image = PhotoImage(
        file = "designs/houndsandrabbit.png"
    )
    blackjack_image = PhotoImage(
        file = "designs/blackjack.png"
    )
    exit_image = PhotoImage(
        file = "designs/exit.png"
    )

    houndsandrabbits = menu_canvas.create_image(
        360.0, 340.0,
        image = houndsandrabbits_image
    )

    blackjack = menu_canvas.create_image(
        920.0, 350.0,
        image = blackjack_image
    )

    exit = menu_canvas.create_image(
        155.0, 575.0,
        image = exit_image
    )

    menu_canvas.tag_bind(blackjack, "<Button-1>", on_blackjack_click)

    menu_canvas.tag_bind(houndsandrabbits, "<Button-1>", on_houndsandrabbits_click)

    menu_canvas.tag_bind(exit, "<Button-1>", on_exit_click)

    menu_canvas.create_text(
    280.0, 80.0,
    anchor="nw",
    text="Sabuesos \ny la liebre",
    fill="#000000",
    font=("Kurale Regular", 36 * -1)
    )


    menu_canvas.create_text(
        896.0, 103.0,
        anchor="nw",
        text="21",
        fill="#000000",
        font=("Kurale Regular", 48 * -1)
    )


    menu_canvas.create_text(
        450.0, -20.0,
        anchor="nw",
        text="Minijuegos",
        fill="#000000",
        font=("InknutAntiqua Regular", 64 * -1)
    )

    app.resizable(False, False)

    app.mainloop()

from tkinter import Tk, Canvas, PhotoImage, font

from anarquistAndFacist.game import start_anarquist_vs_facist
from gameOfCards.GUI import start_black_jack


def show_anarquist_vs_facist():
    start_anarquist_vs_facist()
    print("Showing anarquist vs facist")
    pass

def show_blackjack():
    start_black_jack()
    print("Showing Blackjack")
    pass


def load_image(file_path):
    """
        Loads an image from a file path 
        with try and except for error handling

    Entradas:
        file: A string, the path to the image file

    Salidas:
        PhotoImage or None: The loaded image if successful

    """

    try:
        image  = PhotoImage(
            file = file_path
            )
        return image
    
    except Exception: 
        
        print(f"Image not found")
        return None


def showMenu():
    """
    Main function, shows the menu of the application
    """

    app = Tk()
    app.title("Progra 03")
    app.geometry("1280x720")
    app.configure(bg="#404040")
    app.resizable(False, False) 

    menu_canvas = Canvas(
        app,
        bg="#023E8A",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    menu_canvas.place(x=0, y=0)

    background_image = load_image("designs/holder.png")
    anrquistandfacist_image = load_image("designs/anarquist.png") 
    blackjack_image = load_image("designs/blackjack.png")
    exit_image = load_image("designs/exit.png")
    
    border_id = None
    border_thickness = 5 


    def on_enter(event):
        """
        """
        nonlocal border_id
        # Delete border if it exists
        if border_id:
            menu_canvas.delete(border_id)

        # Get the bounding cordinates
        x1, y1, x2, y2 = menu_canvas.bbox(exit) 

        # Calculate a slight movement
        border_x1 = x1 - border_thickness
        border_y1 = y1 - border_thickness
        border_x2 = x2 + border_thickness
        border_y2 = y2 + border_thickness

        # Create the border rectangle
        border_id = menu_canvas.create_rectangle(
            border_x1, border_y1,
            border_x2, border_y2,
            outline="#00B4D8",
            width=border_thickness
            #tags="hover_border", ill leave it here maybe for the future
        )
        
        menu_canvas.tag_lower(border_id, exit)

    def on_exit(event):
        nonlocal border_id
        # Delete the border if it exists
        if border_id:

            menu_canvas.delete(border_id)
            border_id = None 
            

    def on_blackjack_click(event):
        """
        """
        app.withdraw()
        show_blackjack()
        app.deiconify()
        
        
    def on_anarquistandfacist_click(event):
        """
        """
        app.withdraw()
        show_anarquist_vs_facist()
        app.deiconify()

        
        
    def on_exit_click(event):
        """
        """
        app.quit() 

    background = menu_canvas.create_image(
        640.0, 360.0,
        image=background_image
    )

    title_font = font.Font(family="Arial Black", size=20, weight="bold")


    # Title for the menu
    menu_canvas.create_text(
        180.0, 0.0,
        anchor="nw",
        text="ANARQUISTAS VS FACISTAS",
        fill="#B4ACAC", 
        font=("InknutAntiqua Bold", 52)
    )

    # Create text for the minigames

    text_anarquist = menu_canvas.create_text(
        470.0, 300.0,
        font=title_font,
        text="EL CAMPO DE\n   BATALLA",
        fill="#A2A2A2"
    )

    text_blackjack = menu_canvas.create_text(
        810.0, 480.0,
        font=title_font,
        text="EL MOVIMIENTO\n     SOCIAL",
        fill="#A2A2A2"
    )

    anarquistandfacist = menu_canvas.create_image(
        190.0, 300.0,
        image=anrquistandfacist_image
    )

    blackjack = menu_canvas.create_image(
        1090.0, 480.0,
        image=blackjack_image
    )

    exit = menu_canvas.create_image(
        0.0, 740.0,
        image=exit_image
    )

    # Bind the objects
    menu_canvas.tag_bind(blackjack, "<Button-1>", on_blackjack_click)
    menu_canvas.tag_bind(anarquistandfacist, "<Button-1>", on_anarquistandfacist_click)
    menu_canvas.tag_bind(exit, "<Button-1>", on_exit_click)

    # Bind hover events
    menu_canvas.tag_bind(exit, "<Enter>", on_enter)
    menu_canvas.tag_bind(exit, "<Leave>", on_exit)


    app.mainloop()

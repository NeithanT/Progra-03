"""

"""

from tkinter import Tk, Canvas, PhotoImage

from anarquistAndFacist.game import start_game
from gameOfCards.GUI import showBlackJack

# create main application and show window
def showMenu():

    """
        Main function, shows the menu
        of the application
    """
        
    def on_blackjack_click(event):
        
        menu_canvas.destroy()
        showBlackJack(app)
        print("blackjack!")
       
    def on_anarquistandfacist_click(event):
        
        menu_canvas.destroy()
        start_game(app)
        app.quit()
        print("anarquist and facist")

    def on_exit_click(event):
       
        app.quit() 


    app = Tk()
    app.title("Progra 03")
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



    anrquistandfacist_image = PhotoImage(
        file = "designs/houndsandrabbit.png"
    )
    blackjack_image = PhotoImage(
        file = "designs/blackjack.png"
    )
    exit_image = PhotoImage(
        file = "designs/exit.png"
    )

    anrquistandfacist = menu_canvas.create_image(
        360.0, 340.0,
        image = anrquistandfacist_image
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

    menu_canvas.tag_bind(anrquistandfacist, "<Button-1>", on_anarquistandfacist_click)

    menu_canvas.tag_bind(exit, "<Button-1>", on_exit_click)


    menu_canvas.create_text(
        450.0, -10.0,
        anchor="nw",
        text="Mini-juegos",
        fill="#000000",
        font=("InknutAntiqua Regular", 64 * -1)
    )

    app.resizable(False, False)


    app.mainloop()

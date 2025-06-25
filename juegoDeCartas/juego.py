# MAIN FUNCTION OF BLACKJACK
from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Label

def showBlackJack():
    """
        Main function of the program that
        creates the interface and shows the menu
        to the user
    """
    
    def menu_button(event):
        """
            Button for menu
        """
        print("Go to menu!")
        

    def stand_button(event):
        """
            Button for stand (No more cards)
        """
        print("Stand cards!")
       

    def request_button(event):
        """
            Button for request of card
        """
        print("Request a card!")
        

    def finish_button(event):
        """
            Button to finish the game
        """
        print("Finish the game!")
        

    def tutorial_button(event):
        """
            Button for the game tutorial
        """
        print("Game tutorial!")
        

    def on_exit_click(event):
        """
            Handles the exit button functionality
        """
        app.quit() 

    app = Tk()
    app.geometry("1280x720")
    app.configure(bg="#88E4F8")

    # Canvas for the interface layout
    main_canvas = Canvas(
        app,
        bg="lightblue",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    main_canvas.place(x=0, y=0)

    # Top rectangle for header area
    main_canvas.create_rectangle(
        0.0, 0.0, 1280.0, 100.0,
        fill="#67CDF2",
        outline=""
    )

    # Load all button images
    menu_image = PhotoImage(file="images/menu.png")
    stand_image = PhotoImage(file="images/stand.png")
    request_image = PhotoImage(file="images/request.png")
    finish_image = PhotoImage(file="images/finish.png")
    tutorial_image = PhotoImage(file="images/tutorial.png")
    exit_image = PhotoImage(file="images/exit.png")

    # Display buttons as images
    exit = main_canvas.create_image(183.0, 650.0, image=exit_image)
    menu = main_canvas.create_image(366.0, 650.0, image=menu_image)
    stand = main_canvas.create_image(549.0, 650.0, image=stand_image)
    request = main_canvas.create_image(732.0, 650.0, image=request_image)
    finish = main_canvas.create_image(915.0, 650.0, image=finish_image)
    tutorial = main_canvas.create_image(1098.0, 650.0, image=tutorial_image)

    # Bind events to buttons
    main_canvas.tag_bind(menu, "<Button-1>", menu_button)
    main_canvas.tag_bind(stand, "<Button-1>", stand_button)
    main_canvas.tag_bind(request, "<Button-1>", request_button)
    main_canvas.tag_bind(finish, "<Button-1>", finish_button)
    main_canvas.tag_bind(tutorial, "<Button-1>", tutorial_button)
    main_canvas.tag_bind(exit, "<Button-1>", on_exit_click)

    # Title text
    main_canvas.create_text(
        640.0, 50.0,
        anchor="center",
        text="Blackjack", 
        fill="#000000",
        font=("InknutAntiqua Regular", 60)
    )

    # Frame for the player (dealer)
    container_1 = Frame(
        app,
        bg="#1E3F66", 
        width=540, 
        height=380,   
        bd=2, 
        relief="raised"
    )
    container_1.place(
        x=50, 
        y=160   
    ) 

    # Text above player's container
    main_canvas.create_text(
        320.0, 130.0, 
        anchor="center",
        text="Jugador(Casa)",
        fill="#000000",
        font=("Arial", 24, "bold")
    )

    # Frame for the computer (opponent)
    container_2 = Frame(
        app,
        bg="#0B6623", 
        width=540, 
        height=380, 
        bd=2, 
        relief="raised"
    )
    container_2.place(
        x=690, 
        y=160
    ) 

    # Text above computer's container
    main_canvas.create_text(
        960.0, 130.0,
        anchor="center",
        text="Computadora(Juega)",  
        fill="#000000",
        font=("Arial", 24, "bold")
    )

    app.resizable(False, False)
    app.mainloop()

showBlackJack()

# MAIN FUNCTION OF BLACKJACK
from tkinter import Tk, Canvas, PhotoImage, Frame, Label

from user_game import *
import functions
import computer_game

user_card_index = 0
pc_card_index = 0
label_user_sum = None
label_pc_sum = None

def showBlackJack():
    """
    Main function of the program that
    creates the interface and shows the menu
    to the user
    """

    image_path = "cards_img/"  # Path to images

    saved_images_user = [None] * 10  # List to save user's card images
    saved_images_pc = [None] * 10    # List to save computer's card images
    
    def stand_button(event):
        """
        Button for stand (No more cards)
        """
        global pc_card_index, label_pc_sum
        print("Stand cards!")
        pc_cards_list = computer_game.computer_round()  # Get computer cards
        print(f"Computer cards: {pc_cards_list}")
        
        pc_sum = functions.sum_cards(pc_cards_list)  # Get total value of computer's cards
        print(f"Computer sum: {pc_sum}")

        # Eliminar el label anterior si existe
        if label_pc_sum != None:
           label_pc_sum.destroy()

        # Crear un nuevo label con la suma actualizada
        label_pc_sum = Label(container_2, text="Contador: " + str(pc_sum), fg="white", bg="#0B6623", font=("Arial", 12, "bold"))
        
        label_pc_sum.place(x=5, y=5)
        

        # Show each  card image
        for card in pc_cards_list:
            if pc_card_index < len(saved_images_pc):
                
                full_path = image_path + card + ".png"
                img = PhotoImage(file=full_path)
                saved_images_pc[pc_card_index] = img

                x_pos = 10 + pc_card_index * (img.width() + 10)
                label = Label(container_2, image=img, bg="#0B6623")
                label.place(x=x_pos, y=90)

                pc_card_index += 1

    def request_button(event):
        """
        Button to ask for a card
        """
        global user_card_index, label_user_sum

        cards_list = request_card()  # Get cards for the user
        print(f"Requested cards: {cards_list}")
        user_sum = functions.sum_cards(cards_list)
        print(f"User cards: {user_sum}")

        if label_user_sum != None:
            label_user_sum.destroy()

    #Crear un nuevo label con la suma actualizada
        label_user_sum = Label(container_1, text="Contador: " + str(user_sum), fg="white", bg="#0B6623", font=("Arial", 12, "bold"))
        label_user_sum.place(x=5, y=5)
        # Show the new card image for the user
        if user_card_index < len(saved_images_user):
            
            img_name = cards_list[user_card_index]  
            full_path = image_path + img_name + ".png"

            img = PhotoImage(file=full_path)
            saved_images_user[user_card_index] = img 

            x_pos = 10 + user_card_index * (img.width() + 10)
            label = Label(container_1, image=img, bg="#0B6623")
            label.place(x=x_pos, y=90)

            user_card_index += 1


        
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
    app.configure(bg="#164179")

    # Canvas for the interface layout
    main_canvas = Canvas(
        app,
        bg="#164179",
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
    menu_image = PhotoImage(file="btn_img/menu.png")
    stand_image = PhotoImage(file="btn_img/stand.png")
    request_image = PhotoImage(file="btn_img/request.png")
    finish_image = PhotoImage(file="btn_img/finish.png")
    tutorial_image = PhotoImage(file="btn_img/tutorial.png")
    exit_image = PhotoImage(file="btn_img/exit.png")

    # Display buttons as images
    exit = main_canvas.create_image(256.0, 650.0, image=exit_image)
    stand = main_canvas.create_image(512.0, 650.0, image=stand_image)
    request = main_canvas.create_image(768.0, 650.0, image=request_image)
    tutorial = main_canvas.create_image(1024.0, 650.0, image=tutorial_image)


    # Bind events to buttons
    
    main_canvas.tag_bind(stand, "<Button-1>", stand_button)
    main_canvas.tag_bind(request, "<Button-1>", request_button)
    main_canvas.tag_bind(tutorial, "<Button-1>", tutorial_button)
    main_canvas.tag_bind(exit, "<Button-1>", on_exit_click)

    # Title text


    # Frame for the player (dealer)
    container_1 = Frame(
        app,
        bg="#0B6623", 
        width=540, 
        height=380,   
        bd=2, 
        relief="raised"
    )
    container_1.place(
        x=50, 
        y=160   
    ) 

    label_user_sum = Label(
        container_1, text="Contador: 0", 
        fg="white", bg="#0B6623", 
        font=("Arial", 12, "bold")
        )
    
    label_user_sum.place(x=5, y=5)
    
    # Text above player's container
    main_canvas.create_text(
        320.0, 130.0, 
        anchor="center",
        text="Jugador(Casa)",
        fill="#FFFFFF",
        font=("Arial", 24, "bold")
    )

    # Frame for the computer
    container_2 = Frame(
        app,
        bg="#0B6623",
        width=540,
        height=380,
        bd=2,
        relief="raised"
    )
    container_2.place(x=690, y=160)

    # Text above computer's container
    main_canvas.create_text(
        960.0, 130.0,
        anchor="center",
        text="Computadora(Juega)",  
        fill="#FFFFFF",
        font=("Arial", 24, "bold")
    )
    
    label_pc_sum = Label(container_2, text="Contador: 0",
                         fg="white", bg="#0B6623",
                         font=("Arial", 12, "bold")
                         )
    
    label_pc_sum.place(x=5, y=5)
    app.resizable(False, False)
    app.mainloop()

showBlackJack()

# MAIN FUNCTION OF BLACKJACK
from tkinter import Canvas, PhotoImage, Frame, Label

from gameOfCards.functions import sum_cards, total_winner
from gameOfCards.computer_game import computer_round
from gameOfCards.user_game import request_card

def showBlackJack(app):

    """
        Main function of the program that creates the interface and shows the menu
    """

    def stand_button(event):
        """
            Button to finish the round
        """
        results=total_winner(user_deck,pc_deck)
        if results == 1:
            print("Gano la pc")
            return 
        elif results == 2:
            print("Gano la casa")
            
        elif results == 3:
            print("Es un empate")
            
        else:
            print("Ambos perdieron")
            
    def action_pc():
        """
        funcion para activar el turno de la pc solo una vez
        """

        nonlocal pc_deck
        nonlocal pc_card_render_index
        nonlocal saved_images_pc

        # Pc cards, could do this on line line but we need a copy to not mess with references, cause 
        # python is made with C and ... pointers and yeah ...
        final_pc_hand = computer_round(pc_deck)
        pc_deck = final_pc_hand
        
        pc_sum = sum_cards(final_pc_hand)
        pc_sum_real = sum_cards(final_pc_hand)
        print(f"Computer sum: {pc_sum}")

        # Update the sum label for the PC, with config instead of creating a new one
        gui_elements["label_pc_sum"].config(text=f"Contador: {pc_sum}")

        # Display the computer cards
        container = gui_elements["container_2"]
        image_path = gui_elements["image_path"]

        
        pc_card_index=pc_card_render_index
        if pc_card_index < len(final_pc_hand):
            # Could be reduced to one line
            img_name_pc = pc_deck[pc_card_index]
            full_path = image_path +img_name_pc + ".png"
            img = PhotoImage(file=full_path)
            saved_images_pc += [img] # Save reference to avoid garbage collection ...

            x_pos = 10 + pc_card_index  * (img.width() + 10)
            label = Label(container, image=img, bg="#0B6623")
            label.place(x=x_pos, y=90)
            
            pc_card_render_index += 1
            
    def request_button(event):
        """
        Handles the request button click, deals a card to the player
        
        """
        nonlocal user_deck
        nonlocal user_card_render_index
        nonlocal saved_images_user

        updated_hand = request_card(user_deck)
        user_deck = updated_hand

        user_sum = sum_cards(updated_hand)
        print(f"User sum: {user_sum}")

        # Update the sum label for the user
        gui_elements["label_user_sum"].config(text=f"Contador: {user_sum}")

        # Display the newly drawn card
        user_card_index = user_card_render_index
        if user_card_index < len(updated_hand):
            container = gui_elements["container_1"]
            image_path = gui_elements["image_path"]
            
            img_name = updated_hand[user_card_index]
            full_path = image_path + img_name + ".png"
            img = PhotoImage(file=full_path)
            saved_images_user += [img] # Save reference

            x_pos = 10 + user_card_index * (img.width() + 10)
            label = Label(container, image=img, bg="#0B6623")
            label.place(x=x_pos, y=90)

            user_card_render_index += 1
        action_pc()

    def tutorial_button(event):
        """
            Function for the game tutorial button
        """

        print("Game tutorial!")

    def on_exit_click(event):
        """
            Handles the exit button click to close the application
        """

        app.quit()

    # Data for the game
    user_deck = []
    pc_deck = []

    # This is to render the cards one by one
    user_card_render_index = 0
    pc_card_render_index = 0

    # This is to prevent Gardbage collection
    saved_images_user = []
    saved_images_pc = []

    # Create canvas
    main_canvas = Canvas(app, bg="#164179", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
    main_canvas.place(x=0, y=0)

    main_canvas.create_rectangle(0.0, 0.0, 1280.0, 100.0, fill="#67CDF2", outline="")


    # Frame for the player 
    container_1 = Frame(app, bg="#0B6623", width=540, height=380, bd=2, relief="raised")
    container_1.place(x=50, y=160)
    label_user_sum = Label(container_1, text="Contador: 0", fg="white", bg="#0B6623", font=("Arial", 12, "bold"))
    label_user_sum.place(x=5, y=5)
    main_canvas.create_text(320.0, 130.0, anchor="center", text="Jugador(Casa)", fill="#FFFFFF", font=("Arial", 24, "bold"))

    # Frame for the computer
    container_2 = Frame(app, bg="#0B6623", width=540, height=380, bd=2, relief="raised")
    container_2.place(x=690, y=160)
    label_pc_sum = Label(container_2, text="Contador: 0", fg="white", bg="#0B6623", font=("Arial", 12, "bold"))
    label_pc_sum.place(x=5, y=5)
    main_canvas.create_text(960.0, 130.0, anchor="center", text="Computadora(Juega)", fill="#FFFFFF", font=("Arial", 24, "bold"))
    
    # Load all button images
    stand_image = PhotoImage(file="gameOfCards/btn_img/stand.png")
    request_image = PhotoImage(file="gameOfCards/btn_img/request.png")
    tutorial_image = PhotoImage(file="gameOfCards/btn_img/tutorial.png")
    exit_image = PhotoImage(file="gameOfCards/btn_img/exit.png")

    # Display buttons as images
    exit_btn = main_canvas.create_image(256.0, 650.0, image=exit_image, tags="exit_btn")
    stand_btn = main_canvas.create_image(512.0, 650.0, image=stand_image, tags="stand_btn")
    request_btn = main_canvas.create_image(768.0, 650.0, image=request_image, tags="request_btn")
    tutorial_btn = main_canvas.create_image(1024.0, 650.0, image=tutorial_image, tags="tutorial_btn")
    
    # should store images on the canvas to prevent garbage collection but oh well
    
    # GUI elements to be passed
    # They can be treated differented but oh well
    gui_elements = {
        "main_canvas": main_canvas,
        "container_1": container_1,
        "container_2": container_2,
        "label_user_sum": label_user_sum,
        "label_pc_sum": label_pc_sum,
        "image_path": "gameOfCards/cards_img/",
        "btn_path": "gameOfCard/btn_img/"
    }
    print(gui_elements)
    # Binding events
    
    main_canvas.tag_bind(stand_btn, "<Button-1>", stand_button)
    main_canvas.tag_bind(request_btn, "<Button-1>", request_button)
    main_canvas.tag_bind(tutorial_btn, "<Button-1>", tutorial_button)
    main_canvas.tag_bind(exit_btn, "<Button-1>",on_exit_click)

    app.mainloop()
 
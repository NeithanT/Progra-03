# MAIN FUNCTION OF BLACKJACK
from tkinter import Canvas, PhotoImage, Frame, Label
from gameOfCards.functions import sum_cards, total_winner, check_points
from gameOfCards.computer_game import computer_round
from gameOfCards.user_game import request_card
import time

def showBlackJack(app):

    """
        Main function of the program that creates the interface and shows the menu
    """

    def stand_button(event):
        """
        Button to finish the round
        """
        nonlocal pc_deck
        nonlocal saved_images_pc
        nonlocal saved_labels_pc  # New list to store Labels

        # Destroy previous labels to reveal real card values
        for label in saved_labels_pc:
            label.destroy()

        saved_labels_pc = []
        saved_images_pc = []

        for i in range(len(pc_deck)):
            pc_sum = sum_cards(pc_deck)
            print(f"Computer sum: {pc_sum}")

            # Update the PC's sum label
            gui_elements["label_pc_sum"].config(text=f"Contador: {pc_sum}")

            container = gui_elements["container_2"]
            image_path = gui_elements["image_path"]

            img_name = pc_deck[i]
            full_path = image_path + img_name + ".png"
            img = PhotoImage(file=full_path)

            saved_images_pc += [img]

            x_pos = 10 + i * (img.width() + 10)
            label = Label(container, image=img, bg="#0B6623")
            label.place(x=x_pos, y=90)

            saved_labels_pc += [label]
            

        # Show the score table
        pc_points = check_points(pc_deck)
        user_points = check_points(user_deck)

        if user_points == None:
            user_points = 0
        if pc_points == None:
            pc_points = 0

        message_p = (
            f"Puntos por Jugada | Anarquistas: {user_points} | Fascistas: {pc_points}"
        )

        points_label = Label(
            app,
            text=message_p,
            font=("Times New Roman", 20, "bold"),
            bg="#555555",
            fg="white",
            justify="left"
        )
        points_label.place(relx=0.5, y=30, anchor="n")

        # Remove the score label after 2 seconds
        def remove_label():
            points_label.destroy()

        app.after(2000, remove_label)

        # Show final result after 3 seconds
        def show_result():
            results = total_winner(user_deck, pc_deck)

            if results == 1:
                message = "¡Victoria fascista! Su orden se impone y el caos comienza."
            elif results == 2:
                message = "¡Triunfo anarquista! La rebelión derriba el yugo del poder opresor."
            elif results == 3:
                message = "¡Empate! La lucha continúa en la historia."
            else:
                message = "¡Ambos caen! Fascistas y Anarquistas caen, devorados por su propio conflicto."


            result_label = Label(
                app,
                text=message,
                font=("Times New Roman", 20, "bold"),
                bg="#555555",
                fg="white"
            )
            result_label.place(relx=0.5, y=30, anchor="n")

            # Remove result label after 3 seconds
            def remove_result_label():
                result_label.destroy()

            app.after(3000, remove_result_label)

        app.after(3000, show_result)

    def request_user_card():
        """
        Draws a card for the user, updates the hand, sum, and GUI.
        """
        nonlocal user_deck
        nonlocal user_card_render_index
        nonlocal saved_images_user

        updated_hand = request_card(user_deck)
        user_deck = updated_hand

        user_sum = sum_cards(updated_hand)
        print(f"User sum: {user_sum}")

        gui_elements["label_user_sum"].config(text=f"Contador: {user_sum}")

        user_card_index = user_card_render_index
        if user_card_index < len(updated_hand):
            container = gui_elements["container_1"]
            image_path = gui_elements["image_path"]

            img_name = updated_hand[user_card_index]
            full_path = image_path + img_name + ".png"
            img = PhotoImage(file=full_path)
            saved_images_user += [img]

            x_pos = 10 + user_card_index * (img.width() + 10)
            label = Label(container, image=img, bg="#0B6623")
            label.place(x=x_pos, y=90)

            user_card_render_index += 1
        container.update()
        time.sleep(1)

    def request_cards_pc():
        nonlocal pc_deck
        nonlocal pc_card_render_index
        nonlocal saved_images_pc

        # Pc cards, could do this on line line but we need a copy to not mess with references, cause 
        # python is made with C and ... pointers and yeah ...
        final_pc_hand = computer_round(pc_deck)
        pc_deck = final_pc_hand

        # Display the computer cards
        container = gui_elements["container_2"]
        image_path = gui_elements["image_path"]


        # Reset to base state
        pc_card_render_index = 0
        # This is the equivalent to saying = []
        saved_images_pc = []

        for card_name in final_pc_hand:
            if pc_card_render_index == 0:
                full_path = image_path + card_name + ".png"
            else:
                full_path = image_path + "back1.png"
            
            img = PhotoImage(file=full_path)
            saved_images_pc += [img]

            x_pos = 10 + pc_card_render_index * (img.width() + 10)
            label = Label(container, image=img, bg="#0B6623")
            label.place(x=x_pos, y=90)

            pc_card_render_index += 1
            container.update()
            time.sleep(1)
        # Show final message after PC plays
        end_message = Label(
            app,
            text="Los Fascistas se plantan. El destino esta marcado, ahora responde..",
            font=("Times New Roman", 20, "bold"),
            bg="#555555",
            fg="white"
        )
        end_message.place(relx=0.5, y=30, anchor="n")
        app.after(3000, end_message.destroy)

            

    def deal_initial_cards():
        """
        funcion para activar el turno de la pc solo una vez
        """
        i=0
        while i < 2:
            nonlocal pc_deck
            nonlocal pc_card_render_index
            nonlocal saved_images_pc

            # Pc cards, could do this on line line but we need a copy to not mess with references, cause 
            # python is made with C and ... pointers and yeah ...
            final_pc_hand = request_card(pc_deck)
            pc_deck = final_pc_hand
            
            pc_sum = sum_cards([final_pc_hand[0]])
            pc_sum_real = sum_cards(final_pc_hand)
            print(f"Computer sum: {pc_sum}")

            # Update the sum label for the PC, with config instead of creating a new one
            gui_elements["label_pc_sum"].config(text=f"Contador: {pc_sum}")

            # Display the computer cards
            container = gui_elements["container_2"]
            image_path = gui_elements["image_path"]

            
            pc_card_index=pc_card_render_index
            if pc_card_index < len(final_pc_hand):
                img_name_pc = pc_deck[pc_card_index]
                
                if pc_card_index == 0:
                    full_path = image_path + img_name_pc + ".png"
                else:
                    full_path = image_path + "back1.png"

                img = PhotoImage(file=full_path)
                saved_images_pc += [img]

                x_pos = 10 + pc_card_index * (img.width() + 10)
                label = Label(container, image=img, bg="#0B6623")
                label.place(x=x_pos, y=90)

                pc_card_render_index += 1
                container.update()
                time.sleep(1)
                
            #
            request_user_card()
            i+=1
            
        request_cards_pc()
        
    

    
    def request_button(event):
        """
        Handles the request button click, deals a card to the player
        
        """
        request_user_card()
        

    def play_button(event):
        """
            Function for the game tutorial button
        """
        deal_initial_cards()


        print("Game tutorial!")
        
    def menu_button(event):
        """
            Function for the game tutorial button
        """
        app.quit()
        
    def restart_button(event):
        """
        Resets all variables and GUI elements to initial game state
        """
        nonlocal user_deck
        nonlocal pc_deck
        nonlocal user_card_render_index
        nonlocal pc_card_render_index
        nonlocal saved_images_user
        nonlocal saved_images_pc
        nonlocal saved_labels_pc

        # Clear decks
        user_deck = []
        pc_deck = []

        # Reset render indices
        user_card_render_index = 0
        pc_card_render_index = 0

        # Clear saved images and labels to free memory and remove from display
        for label in saved_labels_pc:
            label.destroy()
        saved_labels_pc = []

        for img in saved_images_user:
            del img # This might not directly remove from canvas, but helps GC
        saved_images_user = []

        for img in saved_images_pc:
            del img # This might not directly remove from canvas, but helps GC
        saved_images_pc = []

        # Clear all card labels from containers
        for widget in gui_elements["container_1"].winfo_children():
            if isinstance(widget, Label) and widget != gui_elements["label_user_sum"]:
                widget.destroy()
        for widget in gui_elements["container_2"].winfo_children():
            if isinstance(widget, Label) and widget != gui_elements["label_pc_sum"]:
                widget.destroy()

        # Reset sum labels
        gui_elements["label_user_sum"].config(text="Contador: 0")
        gui_elements["label_pc_sum"].config(text="Contador: 0")

        print("Game restarted!")


    # Data for the game
    user_deck = []
    pc_deck = []

    # This is to render the cards one by one
    user_card_render_index = 0
    pc_card_render_index = 0

    # This is to prevent Gardbage collection
    saved_images_user = []
    saved_images_pc = []
    saved_labels_pc = []


    # Create canvas
    main_canvas = Canvas(app, bg="#777676", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
    main_canvas.place(x=0, y=0)

    main_canvas.create_rectangle(0.0, 0.0, 1280.0, 100.0, fill="#555555", outline="")


    # Frame for the player 
    bg_img_a = PhotoImage(file="gameOfCards/btn_img/anarquistas.png")
    container_1 = Frame(app, bg="#0B6623", width=540, height=380, bd=2, relief="raised")
    container_1.place(x=50, y=160)
    background_label_a = Label(container_1, image=bg_img_a)
    background_label_a.place(x=0, y=0, relwidth=1, relheight=1)
    container_1.image = bg_img_a
    label_user_sum = Label(container_1, text="Contador: 0", fg="white", bg="#0B6623", font=("Times New Roman", 12, "bold"))
    label_user_sum.place(x=5, y=5)
    main_canvas.create_text(320.0, 130.0, anchor="center", text="Anarquistas", fill="#FFFFFF", font=("Times New Roman", 24, "bold"))
    
    # Frame for the computer
    bg_img_f = PhotoImage(file="gameOfCards/btn_img/fascistas.png")
    container_2 = Frame(app, bg="#0B6623", width=540, height=380, bd=2, relief="raised")
    container_2.place(x=690, y=160)
    background_label_f = Label(container_2, image=bg_img_f)
    background_label_f.place(x=0, y=0, relwidth=1, relheight=1)
    container_2.image = bg_img_f
    label_pc_sum = Label(container_2, text="Contador: 0", fg="white", bg="#0B6623", font=("Times New Roman", 12, "bold"))
    label_pc_sum.place(x=5, y=5)
    main_canvas.create_text(960.0, 130.0, anchor="center", text="Fascistas", fill="#FFFFFF", font=("Times New Roman", 24, "bold"))
    
    # Load all button images
    menu_image = PhotoImage(file="gameOfCards/btn_img/menu.png")
    restart_image = PhotoImage(file="gameOfCards/btn_img/restart.png")
    stand_image = PhotoImage(file="gameOfCards/btn_img/stand.png")
    request_image = PhotoImage(file="gameOfCards/btn_img/request.png")
    play_image = PhotoImage(file="gameOfCards/btn_img/play.png")

    # Display buttons as images
    menu_btn = main_canvas.create_image(50.0, 50.0, image=menu_image, tags="menu_btn")
    restart_btn = main_canvas.create_image(1024.0, 650.0, image=restart_image, tags="restart_btn")
    stand_btn = main_canvas.create_image(512.0, 650.0, image=stand_image, tags="stand_btn")
    request_btn = main_canvas.create_image(768.0, 650.0, image=request_image, tags="request_btn")
    play_btn = main_canvas.create_image(256.0, 650.0, image=play_image, tags="play_btn")
    
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
    
    main_canvas.tag_bind(menu_btn, "<Button-1>", menu_button)
    main_canvas.tag_bind(restart_btn, "<Button-1>", restart_button)
    main_canvas.tag_bind(stand_btn, "<Button-1>", stand_button)
    main_canvas.tag_bind(request_btn, "<Button-1>", request_button)
    main_canvas.tag_bind(play_btn, "<Button-1>", play_button)

    app.mainloop()
 
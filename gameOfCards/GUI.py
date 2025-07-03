# MAIN FUNCTION OF BLACKJACK
from tkinter import Canvas, PhotoImage, Frame, Label,Toplevel
from gameOfCards.functions import sum_cards, total_winner, check_points
from gameOfCards.computer_game import computer_round
from gameOfCards.user_game import request_card
import time

def start_black_jack():
    """
    Main function of the program that creates the Blackjack interface and game logic.

    E: game_window: a Tkinter Toplevel window where the game will be displayed
    S: None: creates and renders the full Blackjack game screen and logic
    R: game_window must be a valid Tkinter Toplevel instance
    """
    game_window = Toplevel()
    game_window.title("BlackJack")
    game_window.geometry("1780x750")
    game_window.configure(bg = "#E9E9E9")
    
    
    def deal_initial_cards():
        """
        Deals two initial cards to both the PC and the user. Shows two PC
        cards and two user cards.

        E: None
        S: This function triggers the card dealing(update of the values of the game)
        and GUI updates for the first round
        R: None: must be called after GUI and game state are properly initialized
        """
        i = 0
        while i < 2:
            nonlocal pc_deck
            nonlocal pc_card_render_index
            nonlocal saved_images_pc

            # Request card for the PC and update deck
            final_pc_hand = request_card(pc_deck)
            pc_deck = final_pc_hand

            # Calculate sum to display only first card value
            pc_sum = sum_cards([final_pc_hand[0]])
            print(f"Suma Computadora: {pc_sum}")

            # Update the PC sum label
            gui_elements["label_pc_sum"].config(text=f"Contador: {pc_sum}")

            container = gui_elements["container_2"]
            image_path = gui_elements["image_path"]

            pc_card_index = pc_card_render_index
            if pc_card_index < len(final_pc_hand):
                img_name_pc = pc_deck[pc_card_index]

                # Show first card face up, second card face down
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

            # Request one card for the user
            request_user_card()
            i += 1

        # After initial dealing, proceed to PC logic
        text_id = main_canvas.create_text(
        890, 30,
        anchor="n",
        text="Mientras los anarquistas estaban manifestándose,\nlos fascistas estaban planeando jugadas malevolas",
        font=("Times New Roman", 20, "bold"),
        fill="white",
        justify="center"
    )

        game_window.after(6000, lambda: main_canvas.delete(text_id))

        request_cards_pc()
        

    def request_user_card():
        """
        Draws a card for the user, updates the hand, and GUI.

        E: None
        S: Modifies the user hand and renders the new card
        R: None: must be called in the correct scope with nonlocal 
        variables and GUI initialized
        """
        nonlocal user_deck
        nonlocal user_card_render_index
        nonlocal saved_images_user

        # Request and update the user hand
        updated_hand = request_card(user_deck)
        user_deck = updated_hand

        # Calculate the new sum and update the label
        user_sum = sum_cards(updated_hand)
        print(f"Suma Usuario: {user_sum}")
        gui_elements["label_user_sum"].config(text=f"Contador: {user_sum}")

        # Render the latest card on the GUI
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
        """
        Requests and renders the final cards for the 
        computer after its round.

        E: None
        S: Updates the PC hand and shows the cards on screen
        R: None: must be called in the scope where nonlocal variables and GUI exist
        """
        nonlocal pc_deck
        nonlocal pc_card_render_index
        nonlocal saved_images_pc

        # Request the full hand for the computer
        final_pc_hand = computer_round(pc_deck)
        pc_deck = final_pc_hand

        # GUI container and image path setup
        container = gui_elements["container_2"]
        image_path = gui_elements["image_path"]

        # Reset state for re-rendering cards
        pc_card_render_index = 0
        saved_images_pc = []

        # Render each card in PC's hand
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
            time.sleep(3)
       
        end_message_id = main_canvas.create_text(
            890, 30,
            anchor="n",
            text="Los Fascistas se plantan. El destino está marcado, y todos sus proyectos están en marcha..",
            font=("Times New Roman", 20, "bold"),
            fill="white",
            justify="center"
        )

        
        def show_start_message():
            main_canvas.delete(end_message_id)
            start_message_id = main_canvas.create_text(
                890, 30,
                anchor="n",
                text="Es momento de que los anarquistas contra ataquen!",
                font=("Times New Roman", 20, "bold"),
                fill="white",
                justify="center"
            )
            game_window.after(3000, lambda: main_canvas.delete(start_message_id))

        
        game_window.after(4000, show_start_message)

        
    def stand_button(event):
        """
        Ends the user turn, reveals all PC cards, and shows the game result.

        E: event: event object from the button click
        S: None: reveals PC hand and displays final result
        R: None: must be called with GUI and game state already initialized
        """
        nonlocal pc_deck
        nonlocal saved_images_pc
        nonlocal saved_labels_pc  # New list to store Labels

        # Destroy previous card back labels to show real cards
        for label in saved_labels_pc:
            label.destroy()

        saved_labels_pc = []
        saved_images_pc = []

        for i in range(len(pc_deck)):
            pc_sum = sum_cards(pc_deck)
            print(f"Suma Computadora: {pc_sum}")

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

        # Show special points result
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
            game_window,
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

        game_window.after(2000, remove_label)

        # Show the final result after 3 seconds
        def display_result():
            result_code = total_winner(user_deck, pc_deck)

            if result_code == 1:
                message = "¡Victoria fascista! imponen el caos con los siguientes proyectos:"
            elif result_code == 2:
                message = "¡Triunfo anarquista! Aurelio no ordenó, inspiró. Y eso bastó para lograr:"
            elif result_code == 3:
                message = "¡Empate! La lucha continúa en la historia."
            else:
                message = "¡Ambos caen! Fascistas y Anarquistas caen, devorados por su propio conflicto."

            result_text_id = main_canvas.create_text(
                890, 30,
                anchor="n",
                text=message,
                font=("Times New Roman", 20, "bold"),
                fill="white",
                justify="center"
            )

            def clear_result_and_display_projects():
                main_canvas.delete(result_text_id)
                if result_code == 1:
                    display_projects(result_code)
                if result_code == 2:
                    display_projects(result_code)

            game_window.after(5000, clear_result_and_display_projects)


        def display_projects(result_code):
            anarchist_projects = [
                "Reuniones clandestinas en bosques y tabernas para planear la resistencia.",
                "Esparcir pergaminos con mensajes de libertad y subversión por todo el reino.",
                "Negarse en masa a pagar tributos y rentas a los señores fascistas.",
                "Levantamientos campesinos armados con hoces y palos contra las tropas opresoras.",
                "Esconder a perseguidos en aldeas y monasterios escondidos.",
                "Organizar huelgas silenciosas en los talleres y mercados de la ciudad.",
                "Destruir caminos y puentes para cortar las rutas de abastecimiento fascistas.",
                "Quemar graneros y depósitos de armas enemigos en ataques nocturnos.",
                "Crear refugios secretos en cuevas y bosques para los rebeldes heridos.",
                "Celebrar festivales paganos y rituales antiguos para fortalecer el espíritu y la unión."
            ]

            fascist_projects = [
                "Establecimiento de patrullas y guardias en aldeas y caminos.",
                "Imposición de toques de queda estrictos para controlar la población.",
                "Creación de cárceles y calabozos para castigar a los rebeldes.",
                "Construcción de murallas y torres de vigilancia en territorios clave.",
                "Quema pública de pergaminos y libros subversivos.",
                "Organización de juicios sumarios para disuadir la disidencia.",
                "Reclutamiento forzado de campesinos para ejércitos y trabajos forzados.",
                "Control estricto del comercio y aprovisionamiento de alimentos.",
                "Implementación de espías para infiltrarse en grupos rebeldes.",
                "Celebración de ceremonias y festivales para reforzar la lealtad al poder."
            ]

            if result_code == 1:
                selected_projects = fascist_projects
            else:
                selected_projects = anarchist_projects


            total_cards = len(user_deck)

            delay = 0
            for i in range(total_cards):
                project_text = selected_projects[i]

                def show(i=i, project_text=project_text):
                    text_id = main_canvas.create_text(
                        890, 30,
                        anchor="n",
                        text=project_text,
                        font=("Times New Roman", 20, "bold"),
                        fill="white",
                        justify="center"
                    )
                    game_window.after(5000, lambda: main_canvas.delete(text_id))

                game_window.after(delay, show)
                delay += 5000

        game_window.after(3000, display_result)

      #Start of buttons 
    def request_button(event):
        """
        Handles the request button click, and triggers the request_user_card

        E: event: event object from the button click
        S: None: this function triggers an action 
        R: None: the button must be cliked
        """
        request_user_card()
        
    def play_button(event):
        """
        Function to start the game when the play button is clicked

        E: event: event object from the button click
        S: None: triggers the start of the game by dealing initial cards
        R: None: the button must be clicked
        """
        deal_initial_cards()


        print("Start the Game!")
        
    def menu_button(event):
        """
        Function for going to the menu

        E: event: event object from the button click
        S: None: triggers the transition to the menu screen
        R: None: the button must be clicked
        """
        game_window.destroy()
        game_window.quit()
        
    def restart_button(event):
        """
        Resets all variables and GUI elements to initial game state.

        E: None
        S: None - resets internal variables and GUI components
        R: Must be called in the correct scope where nonlocal variables exist
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
    main_canvas = Canvas(
        game_window,
        bg="#666666",
        height=750,
        width=1780,
        bd=0,
        highlightthickness=0,
        relief="ridge",
    )
    main_canvas.place(x=0, y=0)

    main_canvas.create_rectangle(0.0, 0.0, 1780.0, 100.0, fill="#575757", outline="")

    text_id = main_canvas.create_text(
        890,
        30,
        anchor="n",
        text=(
            "Después de una batalla histórica, el bando no se rindió.\n"
            "Comenzaron otra batalla, pero esta es de estrategia."
        ),
        font=("Times New Roman", 20, "bold"),
        fill="white",
        justify="center",
    )

    game_window.after(6000, lambda: main_canvas.delete(text_id))

    # Frame for the Anarchist player
    container_1 = Frame(
        game_window,
        bg="#0B6623",
        width=750,
        height=420,
        bd=2,
        relief="raised",
    )
    container_1.place(x=95, y=160)  
    label_user_sum = Label(
        container_1,
        text="Contador: 0",
        fg="white",
        bg="#0B6623",
        font=("Times New Roman", 12, "bold"),
    )
    label_user_sum.place(x=5, y=5)
    main_canvas.create_text(
        470.0,
        130.0,
        anchor="center",
        text="Anarquistas",
        fill="#FFFFFF",
        font=("Times New Roman", 24, "bold"),
    )

    # Frame for the Fascist player
    container_2 = Frame(
        game_window,
        bg="#0B6623",
        width=750,
        height=420,
        bd=2,
        relief="raised",
    )
    container_2.place(x=935, y=160) 
    label_pc_sum = Label(
        container_2,
        text="Contador: 0",
        fg="white",
        bg="#0B6623",
        font=("Times New Roman", 12, "bold"),
    )
    label_pc_sum.place(x=5, y=5)
    main_canvas.create_text(
        1310.0,
        130.0,
        anchor="center",
        text="Fascistas",
        fill="#FFFFFF",
        font=("Times New Roman", 24, "bold"),
    )

    # Load all button images
    menu_image = PhotoImage(file="gameOfCards/btn_img/menu.png")
    restart_image = PhotoImage(file="gameOfCards/btn_img/restart.png")
    stand_image = PhotoImage(file="gameOfCards/btn_img/stand.png")
    request_image = PhotoImage(file="gameOfCards/btn_img/request.png")
    play_image = PhotoImage(file="gameOfCards/btn_img/play.png")

    # Display buttons as images (aligned and centered)
    menu_btn = main_canvas.create_image(50.0, 50.0, image=menu_image, tags="menu_btn")

    play_btn = main_canvas.create_image(515.0, 650.0, image=play_image, tags="play_btn")
    request_btn = main_canvas.create_image(765.0, 650.0, image=request_image, tags="request_btn")
    stand_btn = main_canvas.create_image(1015.0, 650.0, image=stand_image, tags="stand_btn")
    restart_btn = main_canvas.create_image(1265.0, 650.0, image=restart_image, tags="restart_btn")

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

    # Binding events
    
    main_canvas.tag_bind(menu_btn, "<Button-1>", menu_button)
    main_canvas.tag_bind(restart_btn, "<Button-1>", restart_button)
    main_canvas.tag_bind(stand_btn, "<Button-1>", stand_button)
    main_canvas.tag_bind(request_btn, "<Button-1>", request_button)
    main_canvas.tag_bind(play_btn, "<Button-1>", play_button)

    game_window.mainloop()
 
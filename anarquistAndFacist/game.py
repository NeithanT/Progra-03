from tkinter import Tk, Canvas, PhotoImage, Toplevel

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


def draw_game_lines(canvas, line_coordinates):
    """
        Draws the game lines on the canvas
    """

    for line in line_coordinates:
        canvas.create_line(line[0], line[1], fill="blue", width=10)


def draw_game_pieces(game_canvas, game_state, circles_coordinates, anarquist_img, facist_img):
    """
        Draws the game pieces (circles and images) on the canvas

    Returns:
        list: A list of canvas item ids for the drawn game pieces
    """

    # The list for the ids in the canvas
    pieces_list = []
    index = 0


    for list in game_state:
        
        for circle in list:

            if circle == 0:
                continue


            x,y = circles_coordinates[index]

            index += 1

            if circle == 1:

                circle_id = game_canvas.create_oval(
                    x, y, x+80, y+80, fill = "red"
                )

            elif circle == 2:

                circle_id = game_canvas.create_image(
                    x+40, y+40,
                    image = anarquist_img
                )

            elif circle == 3:

                circle_id = game_canvas.create_image(
                    x+40, y+40,
                    image = facist_img
                )

            pieces_list += [circle_id]


    return pieces_list


def start_anarquist_vs_facist():
    """
        Initializes and runs the game application
    """
    
    game_window = Toplevel() 
    game_window.title("Anarquistas vs Facistas Game")
    game_window.geometry("1280x720") 
    game_window.configure(bg="#404040")
    
    
    def click(event):
        """
            Handles click event
        """
        print("clicked")
    

    def on_exit_click(event):
        """
        """
        game_window.destroy() 
        game_window.quit()


    game_canvas = Canvas(
        game_window,
        bg="lightblue",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    game_canvas.place(x=0, y=0)
    

    # Load images
    frame_image = load_image("anarquistAndFacist/logos/frame.png")
    anarquist_image = load_image("anarquistAndFacist/logos/anarquist.png")
    facist_image = load_image("anarquistAndFacist/logos/facist.png")
    exit_image = load_image("designs/game_exit.png")

    if frame_image:
        
        game_canvas.create_image(640.0, 340.0, image=frame_image)

    initial_game_state = [
        [0, 2, 1, 1, 0],
        [2, 1, 1, 1, 3],
        [0, 2, 1, 1, 0]
    ]

    circles_coordinates = [
        (390.0, 90.0), (590.0, 90.0), (790.0, 90.0),
        (210.0, 290.0),
        (390.0, 290.0), (590.0, 290.0), (790.0, 290.0),
        (970.0, 290.0),
        (390.0, 490.0), (590.0, 490.0), (790.0, 490.0)
    ]

    line_coordinates = [
        [(250.0, 330.0), (430.0, 130.0)], [(250.0, 330.0), (1010.0, 330.0)],
        [(250.0, 330.0), (430.0, 530.0)], [(430.0, 130.0), (830.0, 130.0)],
        [(430.0, 130.0), (830.0, 530.0)], [(430.0, 530.0), (830.0, 130.0)],
        [(430.0, 530.0), (830.0, 530.0)], [(430.0, 130.0), (430.0, 530.0)],
        [(630.0, 130.0), (630.0, 530.0)], [(830.0, 530.0), (830.0, 130.0)],
        [(830.0, 130.0), (1010.0, 330.0)], [(830.0, 530.0), (1010.0, 330.0)]
    ]

    # Draw lines 
    draw_game_lines(game_canvas, line_coordinates)

    


    exit = game_canvas.create_image(
        70.0, 650.0,
        image=exit_image
    )

    game_canvas.tag_bind(exit, "<Button-1>", on_exit_click)
    # Draw game pieces
    drawn_circles_ids = draw_game_pieces(
        game_canvas, initial_game_state, circles_coordinates, anarquist_image, facist_image
    )

    # Bind click event to the first created circle/image, if any were drawn
    for circle in drawn_circles_ids:
        game_canvas.tag_bind(circle, "<Button-1>", click)

    game_canvas.pack()

    # Idk what does this do but it is recommended somehow

    game_window.mainloop()
    
    
"""
while not game_over:

    if current_player == "hounds":
        # Get hound move
        # Validate hound move
        # Update board
        # Check for hound win
        # Check for hound stalling
        current_player = "rabbit"
    else: # current_player == "rabbit"
        # Get rabbit move
        # Validate rabbit move
        # Update board
        # Check for rabbit win
        current_player = "hounds"
"""
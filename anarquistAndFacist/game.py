from tkinter import Tk, Canvas, PhotoImage, Toplevel, messagebox
import os

def load_image(file_path):
    """
        Loads an image from a file path with error handling
    
    Args:
        file_path: A string, the path to the image file
    
    Returns:
        PhotoImage or None: The loaded image if successful,
            None otherwise
    """

    try:
        image = PhotoImage(file=file_path)
        return image
    except:
        print("Image not found: 404 or something")
        return None


def draw_game_lines(canvas):
    """
        Draws the game lines on the canvas
    """

    line_coordinates = [
        [(250.0, 330.0), (430.0, 130.0)], [(250.0, 330.0), (1010.0, 330.0)],
        [(250.0, 330.0), (430.0, 530.0)], [(430.0, 130.0), (830.0, 130.0)],
        [(430.0, 130.0), (830.0, 530.0)], [(430.0, 530.0), (830.0, 130.0)],
        [(430.0, 530.0), (830.0, 530.0)], [(430.0, 130.0), (430.0, 530.0)],
        [(630.0, 130.0), (630.0, 530.0)], [(830.0, 530.0), (830.0, 130.0)],
        [(830.0, 130.0), (1010.0, 330.0)], [(830.0, 530.0), (1010.0, 330.0)]
    ]

    for line in line_coordinates:
        canvas.create_line(line[0], line[1], fill="blue", width=10)


def draw_game_pieces(game_canvas, game_state, circles_coordinates, anarquist_img, facist_img):
    """
        Draws the game pieces (circles and images) on the canvas
    
    Args:
        game_canvas: The canvas in which the lines are created


    Returns:
        list: A list of canvas item ids for the drawn game pieces

    """

    pieces_list = []
    coord_index = 0
    
    for row_idx, row in enumerate(game_state):
        for col_idx, cell in enumerate(row):

            if cell == 0:
                continue
                
            x, y = circles_coordinates[coord_index]
            coord_index += 1
            
            if cell == 1:

                # Red circle for empty positions
                circle_id = game_canvas.create_oval(
                    x, y, x+80, y+80, fill="red", outline="red",
                    width=10, tag = "piece"
                )
            elif cell == 2:

                # Anarchist piece
                circle_id = game_canvas.create_image(
                    x+40, y+40, image=anarquist_img, tag = "piece"
                )
            elif cell == 3:

                # Fascist piece
                circle_id = game_canvas.create_image(
                    x+40, y+40, image=facist_img, tag = "piece"
                )
            
            pieces_list += [circle_id]
    
    return pieces_list

def initial_game_state():
    """
        Returns the initial game state
    """
    return [
        [0, 2, 1, 1, 0],
        [2, 1, 1, 1, 3],
        [0, 2, 1, 1, 0]
    ]


def get_position_from_coordinates(x, y, circles_coordinates):
    """
        Get the board position from click coordinates
    
    Returns:
        int: An index (0-10), associated with the piece id() 
             or -1 if not found
    """

    for i, (cx, cy) in enumerate(circles_coordinates):
        if cx <= x <= cx + 80 and cy <= y <= cy + 80:
            return i
        
    return -1

def position_to_board_index(position):
    """
        Convert position index to board coordinates
    
    Returns:
        (x, y): the x and y in which the piece is found
                or None
    """

    position_map = {
        0: (0, 1), 1: (0, 2), 2: (0, 3),
        3: (1, 0), 4: (1, 1), 5: (1, 2), 6: (1, 3), 7: (1, 4),
        8: (2, 1), 9: (2, 2), 10: (2, 3)
    }
    for key,value in position_map.items():
        if position == key:
            return value
    return None

def board_index_to_position(x, y):
    """
        Converts board coordinates to position index
    
    Returns:
        int: Position index or -1 otherwise
    """
    index_map = {
        (0, 1): 0, (0, 2): 1, (0, 3): 2,
        (1, 0): 3, (1, 1): 4, (1, 2): 5, (1, 3): 6, (1, 4): 7,
        (2, 1): 8, (2, 2): 9, (2, 3): 10
    }

    for key,value in index_map  .items():
        if (x,y) == key:
            return value
            
    return None

def is_valid_move(game_state, from_pos, to_pos, possible_moves):
    """
        Check if a move is valid according to the game rules.

    Args:
        Too many
        
    Returns:
        bool: True if the move is valid, False otherwise.
    """
    
    # Check if it's a possible move ... no questions

    is_possible = False
    for key, moves in possible_moves.items():
        if key == from_pos and not is_possible: 
            for move in moves:
                if to_pos == move:
                    is_possible = True

    if not is_possible:
        return False
    

    # Check if the destination is empty
    to_coords = position_to_board_index(to_pos)
    # not to_coords is to check if they exist:)
    if not to_coords or not game_state[to_coords[0]][to_coords[1]] == 1:
        return False 
    

    # Check so the player can only move forward
    from_coords = position_to_board_index(from_pos)
    
    if from_coords:
        from_col = from_coords[1]
        to_col = to_coords[1]

        if to_col >= from_col:
            return True # Valid forward move for an Anarchist
        else:
            return False # Invalid backward/sideways move for an Anarchist
    
    return False # Should not be reached


def move_piece(game_canvas, game_state, from_pos, to_pos, circles_coordinates, anarquist_img, facist_img):
    """
        Move a piece from one position to another
    """
    from_coords = position_to_board_index(from_pos)
    to_coords = position_to_board_index(to_pos)
    
    if not from_coords or not to_coords:
        return False
    
    from_row, from_col = from_coords
    to_row, to_col = to_coords
    
    # Exchange the pieces in the game state
    game_state[from_row][from_col], game_state[to_row][to_col] = \
        game_state[to_row][to_col], game_state[from_row][from_col]
    
    # Redraw the board, to update
    redraw_board(game_canvas, game_state, circles_coordinates, anarquist_img, facist_img)
    return True

def redraw_board(game_canvas, game_state, circles_coordinates, anarquist_img, facist_img):
    """
    Redraw the entire board with current game state
    """

    # Clear existing pieces, not deleting lines and frame...
    game_canvas.delete("piece")
    
    
    coord_index = 0
    
    for row in game_state:
        for cell in row:
            if cell == 0:
                continue
                
            x, y = circles_coordinates[coord_index]
            coord_index += 1
            
            if cell == 1:
                
                game_canvas.create_oval(
                    x, y, x+80, y+80, fill="red", outline="red", width=10,
                    tags="piece"
                )

            elif cell == 2:

                game_canvas.create_image(
                    x+40, y+40, image=anarquist_img, tags="piece"
                )
            elif cell == 3: 
                
                game_canvas.create_image(
                    x+40, y+40, image=facist_img, tags="piece"
                )

def check_win_condition(game_state, possible_moves):
    """
    Check if a player has won the game.

    Returns:
        str: "Anarchist" if they win, "Fascist" if they win, None if game continues.
    """

    # Find the positions of all pieces
    fascist_pos_coord = None
    anarchist_pos_coords = []
    for r, row in enumerate(game_state):
        for c, piece in enumerate(row):
            if piece == 3:
                fascist_pos_coord = (r, c)
            elif piece == 2:
                anarchist_pos_coords.append((r, c))

    if not fascist_pos_coord or len(anarchist_pos_coords) < 3:
        # Should not happen in a normal game, but good for safety
        return None 

    # --- Fascist Win Condition (Escaped) ---
    # The Fascist wins if its column is to the left of ALL anarchist columns.
    fascist_col = fascist_pos_coord[1]
    anarchists_all_to_the_right = True
    for anarch_coord in anarchist_pos_coords:
        if anarch_coord[1] <= fascist_col:
            anarchists_all_to_the_right = False
            break
    if anarchists_all_to_the_right:
        return "Fascist"

    # --- Anarchist Win Condition (Trapped the Fascist) ---
    # The Anarchists win if the Fascist has no legal moves.
    fascist_board_pos = board_index_to_position(fascist_pos_coord[0], fascist_pos_coord[1])
    
    # Get all adjacent positions for the fascist
    fascist_possible_moves = possible_moves.get(fascist_board_pos, [])
    
    has_legal_move = False
    for move_pos in fascist_possible_moves:
        move_coords = position_to_board_index(move_pos)
        if move_coords:
            # Check if any adjacent spot is empty
            if game_state[move_coords[0]][move_coords[1]] == 1:
                has_legal_move = True
                break # Found a legal move, so not trapped
    
    if not has_legal_move:
        return "Anarchist"

    # If no one has won yet
    return None


def start_anarquist_vs_facist():
    """
        Initializes and runs the game application
    """
    game_window = Toplevel() 
    game_window.title("Hounds and Hare Game")
    game_window.geometry("1280x720") 
    game_window.configure(bg="#404040")
    
    # Game data, in a dictionary to be passed around
    game_data = {
        "possible_moves": {
            0: [1, 3, 4, 5], 1: [0, 2, 5], 2: [1, 5, 6, 7], 3: [0, 4, 8],
            4: [0, 3, 5, 8], 5: [0, 1, 2, 4, 6, 8, 9, 10], 6: [2, 5, 7, 10], 
            7: [2, 6, 10], 8: [3, 4, 5, 9], 9: [5, 8, 10], 10: [5, 6, 7, 9],
        },
        "game_state": initial_game_state(),
        "selected_position": -1,
        "current_player": 1,
        "winner": None,
        "game_over": False,
    }
    
    circles_coordinates = [
        (390.0, 90.0), (590.0, 90.0), (790.0, 90.0),
        (210.0, 290.0), (390.0, 290.0), (590.0, 290.0), (790.0, 290.0), (970.0, 290.0),
        (390.0, 490.0), (590.0, 490.0), (790.0, 490.0)
    ]
    
    def click(event):
        """
        Handle click events
        """
        if game_data["game_over"]:
            return
        
        clicked_position = get_position_from_coordinates(event.x, event.y, circles_coordinates)
        
        if clicked_position == -1:
            return
        
        board_coords = position_to_board_index(clicked_position)
        if not board_coords:
            return
        
        y, x = board_coords
        clicked_piece = game_data["game_state"][y][x]
        
        if game_data["selected_position"] == -1:
            # First click - select a piece
            if clicked_piece == 2 or clicked_piece == 3:  
                game_data["selected_position"] = clicked_position
                print(f"Selected piece at position {clicked_position}")
        else:
            # Second click - attempt to move
            if clicked_position == game_data["selected_position"]:
                # Clicked same piece - deselect
                game_data["selected_position"] = -1
                print("Deselected piece")
            elif clicked_piece == 2 or clicked_piece == 3:
                # Clicked another piece, selecting it instead
                game_data["selected_position"] = clicked_position
                print(f"Selected piece at position {clicked_position}")
            else:
                # Try to move to this position
                # Get the selected piece type
                selected_coords = position_to_board_index(game_data["selected_position"])
                if selected_coords:
                    
                    if is_valid_move(game_data["game_state"], game_data["selected_position"], 
                                clicked_position, game_data["possible_moves"]):
                        if move_piece(game_canvas, game_data["game_state"], 
                                    game_data["selected_position"], clicked_position, circles_coordinates,
                                    anarquist_image, facist_image):
                            print(f"Moved piece from {game_data['selected_position']} to {clicked_position}")
                            game_data["selected_position"] = -1
                            
                            # Check win condition
                            winner = check_win_condition(game_data["game_state"], game_data["possible_moves"])
                            if winner:
                                game_data["winner"] = winner
                                game_data["game_over"] = True
                                messagebox.showinfo("Game Over", f"{winner} wins!")
                        else:
                            print("Move failed")
                    else:
                        print("Invalid move")
                        game_data["selected_position"] = -1

                        
    def on_exit_click(event):
        """
            Handle exit button click
        """
        game_window.destroy()
        game_window.quit()
    
    def reset_game():
        """
        Reset the game to initial state
        """
        game_data["game_state"] = initial_game_state()
        game_data["selected_position"] = -1
        game_data["current_player"] = 1
        game_data["winner"] = None
        game_data["game_over"] = False
        redraw_board(game_canvas, game_data["game_state"], circles_coordinates
                     , anarquist_image, facist_image)
    
    # Create canvas
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
    exit_image = load_image("anarquistAndFacist/logos/menu.png")
    
    # Draw frame
    if frame_image:
        game_canvas.create_image(640.0, 340.0, image=frame_image)
    
    # Draw lines
    draw_game_lines(game_canvas)
    
    # Draw exit button
    if exit_image:
        exit_button = game_canvas.create_image(50.0, 50.0, image=exit_image)
        game_canvas.tag_bind(exit_button, "<Button-1>", on_exit_click)
    
    # Draw initial game pieces
    if anarquist_image and facist_image:
        draw_game_pieces(game_canvas, game_data["game_state"], circles_coordinates, 
                        anarquist_image, facist_image)
    
    # Bind click event to canvas
    game_canvas.bind("<Button-1>", click)
    
    game_canvas.pack()
    game_window.mainloop()


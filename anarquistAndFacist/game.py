

from tkinter import Tk, Canvas, PhotoImage

def start_game(app):
    """
    
    """

    def click(event):
        print("clicked")

    game_canvas = Canvas(
        app,
        bg = "lightblue",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness= 0,
        relief = "ridge"
    )

    game_canvas.place(x = 0, y = 0)
    
    
    frame_image = PhotoImage(
        file = "anarquistAndFacist/logos/frame.png"
    )
    game_canvas.create_image(640.0 , 340.0,image = frame_image)

    initial_game = [
        [0,2,1,1,0],
        [2,1,1,1,3],
        [0,2,1,1,0]
    ]

    circles_cordinates = [(390.0,90.0), (590.0,90.0), (790.0,90.0),
                          (210.0,290.0), 
                          (390.0,290.0), (590.0,290.0), (790.0,290.0), 
                          (970.0,290.0),
                          (390.0,490.0), (590.0,490.0), (790.0,490.0)]
    
    line_cordinates = [

                    # Start from the left to the rigth,
                    # top and bottom adjacent nodes
                    [(250.0,330.0), (430.0,130.0)],
                    [(250.0,330.0),(1010.0,330.0)],
                    [(250.0,330.0), (430.0,530.0)],

                    # From top left to top rigth and
                    # the one of the main diagonals
                    [(430.0,130.0), (830.0,130.0)],
                    [(430.0,130.0),(830.0,530.0)],

                    # The main diagonal from bottom left to
                    # top rigth and horizontal line at the bottom
                    [(430.0,530.0), (830.0,130.0)],
                    [(430.0,530.0),(830.0,530.0)],


                    [(430.0,130.0), (430.0,530.0)],
                    [(630.0,130.0),(630.0,530.0)],
                    [(830.0,530.0),(830.0,130.0)],


                    [(830.0,130.0), (1010.0,330.0)],
                    [(830.0,530.0),(1010.0,330.0)]
    ]


    for line in line_cordinates:

        line = game_canvas.create_line(line[0],line[1],
                            fill="blue",width=10)


    list_circles = []

    anarquist_image = PhotoImage(
        file = "anarquistAndFacist/logos/anarquist.png"
    )
    facist_image = PhotoImage(
        file = "anarquistAndFacist/logos/facist.png"
    )

    i = 0

    for list in initial_game:
        
        for circle in list:

            if circle == 0:
                continue

            else:

                x,y = circles_cordinates[i]
                i += 1

                if circle == 1:

                    circle_id = game_canvas.create_oval(
                        x, y, x+80, y+80, fill = "red"
                    )

                elif circle == 2:

                    circle_id = game_canvas.create_image(
                        x+40, y+40,
                        image = anarquist_image
                    )

                elif circle == 3:

                    circle_id = game_canvas.create_image(
                        x+40, y+40,
                        image = facist_image
                    )

                list_circles += [circle_id]

    game_canvas.tag_bind(list_circles[0], "<Button-1>", click)


    game_canvas.pack()

    app.mainloop()
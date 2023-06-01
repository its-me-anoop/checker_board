import turtle

t = turtle.Turtle()
t.speed(0)


def draw_square(size, color, thickness, fill_color=None):
    """
    Draws a square with specified parameters using the turtle graphics library.

    Args:
        size (int): The length of the sides of the square.
        color (str): The color of the square's outline.
        thickness (int): The thickness of the square's outline.
        fill_color (str, optional): The color to fill the square with. If None, the square is not filled. Default is None.

    Example usage:
        draw_square(100, 'red', 2, 'blue')

    This will draw a red square of size 100 and thickness 2, filled with blue color.
    """
    t.color(color)
    t.width(thickness)
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for side in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_circle(radius, color):
    """
    Draws a filled circle with specified parameters using the turtle graphics library.

    Args:
        radius (int): The radius of the circle.
        color (str): The color of the circle and its fill.

    Example usage:
        draw_circle(50, 'green')

    This will draw a filled green circle of radius 50.
    """
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def place_checker_piece(row):
    """
    Places a checker piece on a specific row of a checkerboard using the turtle graphics library.

    The function assumes that the checkerboard is drawn such that rows 0 to 2 should be filled with 'green' pieces and rows above 4 with 'red' pieces. Rows 3 and 4 are ignored.

    Args:
        row (int): The row on the checkerboard where the piece should be placed.

    Example usage:
        place_checker_piece(2)

    This will place a green piece in the specified row if the row is less than 3, and a red piece if the row is greater than 4.
    """
    if row < 3 or row > 4:
        t.penup()
        t.goto(t.xcor() + 15, t.ycor() - 27)
        t.pendown()
        if row < 3:
            draw_circle(12, "green")
        else:
            draw_circle(12, "red")
        t.penup()
        t.goto(t.xcor() - 15, t.ycor() + 27)


def draw_column(row):
    """
    Draws a column of a checkerboard and places checker pieces as required using the turtle graphics library.

    The function assumes that it should draw 8 squares for the column, alternating between black and white. For black squares, it calls place_checker_piece(row) which places a piece on the square if it's in the correct rows for pieces.

    Args:
        row (int): The row of the checkerboard that the column should be drawn on.

    Example usage:
        draw_column(2)

    This will draw a column for row 2 of the checkerboard, placing pieces as appropriate.
    """
    for column in range(8):
        if column % 2 == row % 2:
            draw_square(30, "black", 2, "white")
        else:
            draw_square(30, "black", 2, "black")
            # place_checker_piece(row)
        t.penup()
        t.forward(30)
        t.pendown()


def go_to_next_row():
    """
    Moves the turtle to the starting position of the next row in a checkerboard pattern using the turtle graphics library.

    The function assumes that the starting position of the next row is 30 units below and 240 units to the left of the current position of the turtle.

    Example usage:
        go_to_next_row()

    This will move the turtle to the starting position of the next row.
    """
    t.penup()
    t.goto(t.xcor() - 240, t.ycor() - 30)
    t.pendown()


def turtle_start_position(x, y):
    """
    Adjusts the starting position of the turtle so that the checkerboard will be drawn centered on the screen.

    This function assumes the turtle starts at the center of the screen, and it moves the turtle up and left by 120 units to reposition the starting point. This makes the checkerboard, when drawn, appear centered on the screen.

    Example usage:
        turtle_start_position()

    This moves the turtle to an appropriate starting position to draw a centered checkerboard.
    """
    t.penup()
    t.goto(t.xcor() + x, t.ycor() + y)
    t.pendown()


turtle_start_position(-120, 120)
# Draw a checker box
draw_square(240, "black", 3)
for row in range(8):
    draw_column(row)
    go_to_next_row()
# Place the checkers
turtle_start_position(0, 240)
for row in range(8):
    for column in range(8):
        if column % 2 != row % 2:
            place_checker_piece(row)
        t.penup()
        t.forward(30)
        t.pendown()
    go_to_next_row()
t.done()

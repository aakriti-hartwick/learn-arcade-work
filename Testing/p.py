import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
@@ -16,49 +18,40 @@ def draw_section_outlines():
def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = (column*10) + 5# Instead of zero, calculate the proper x location using 'column'
            y =(row *10) + 5 # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

            x = (column * 10) + 5
            y = (row * 10) + 5
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    # Below, replace "pass" with your code for the loop.
    # Use the modulus operator and an if statement to select the color
    # Don't loop from 30 to 60 to shift everything over, just add 300 to x.

    for row in range(30):
        for column in range(30):
            x = (column * 10 )+ 305
            y = (row * 10 )+ 5
            x = (column * 10) + 305
            y = (row * 10) + 5
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)



def draw_section_3():
    # Use the modulus operator and an if/else statement to select the color.
    # Don't use multiple 'if' statements.
    for row in range(30):
        for column in range (30):
            x = (column * 10) +605
        for column in range(30):
            x = (column * 10) + 605
            y = (row * 10) + 5
            if row % 2 == 0:
                arcade.draw_rectangle_filled(x , y, 5, 5, arcade.color.WHITE)
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5 , arcade.color.BLACK)

                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    for row in range(30):
        for column in range(30):
            x = (column * 10) + 905
            y = (row * 10) + 5
            if (column + row)% 2  and column % 2  == 0:
            if (column + row) % 2 and column % 2 == 0:

                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
@@ -67,15 +60,14 @@ def draw_section_4():

def draw_section_5():
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
    for row in range(30):
        for column in range(row - 30):
            x = (column * 10) +5
    for row in range(31):
        for column in range(row + 1, 31):
            x = (column * 10) - 5
            y = (row * 10) + 305

            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)



def draw_section_6():
    for row in range(30):
        for column in range(30 - row):
@@ -87,25 +79,22 @@ def draw_section_6():

def draw_section_7():
    for row in range(30):
        for column in range(row + 1 ):
        for column in range(row + 1):
            x = (column * 10) + 605
            y = (row * 10) + 305
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)



def draw_section_8():
    for row in range(300):
        for column in range(150 * row ):

           x = (column * 10) + 905
           y = (row * 10) + 305
           arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

    for row in range(30):
        for column in range(30 - row, 48):
            x = (column * 10) + 895
            y = (row * 10) + 305
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def main():
    # Create a window

    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

@@ -129,4 +118,4 @@ def main():
    arcade.run()


main()
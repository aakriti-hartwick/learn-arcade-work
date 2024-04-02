""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 850
SCREEN_HEIGHT = 850


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

    def on_draw(self):
        arcade.start_render()

        arcade.draw_lrtb_rectangle_filled(0, 849, 849, 0, arcade.csscolor.FLORAL_WHITE)

        arcade.draw_rectangle_filled(300, 300, 180, 600, arcade.csscolor.ROSY_BROWN)
        arcade.draw_rectangle_filled(75, 75, 60, 400, arcade.csscolor.BLACK)

        arcade.draw_circle_filled(75, 75, 18.75, arcade.csscolor.RED)
        arcade.draw_circle_filled(75, 150, 18.75, arcade.csscolor.GREEN)
        arcade.draw_circle_filled(75, 225, 18.75, arcade.csscolor.YELLOW)

        arcade.draw_rectangle_filled(700, 60, 45, 450, arcade.csscolor.SIENNA)

        arcade.draw_circle_filled(700, 350, 100, arcade.csscolor.DARK_GREEN)
        arcade.draw_rectangle_filled(500, 30, 40, 300, arcade.csscolor.SIENNA)

        arcade.draw_rectangle_filled(300, 300, 50, 50, arcade.csscolor.BLACK)
        arcade.draw_rectangle_filled(300, 400, 50, 50, arcade.csscolor.BLACK)
        arcade.draw_rectangle_filled(300, 500, 50, 50, arcade.csscolor.BLACK)
        arcade.draw_rectangle_filled(300, 200, 50, 50, arcade.csscolor.BLACK)
        arcade.draw_rectangle_filled(300, 80, 60, 150, arcade.csscolor.PURPLE)
        arcade.draw_rectangle_filled(300, 40, 30, 75, arcade.csscolor.WHITE)

        arcade.draw_circle_filled(500, 250, 89, arcade.csscolor.DARK_GREEN)

        arcade.draw_circle_filled(750, 750, 40, arcade.csscolor.SKY_BLUE)

        arcade.draw_circle_filled(750, 790, 40, arcade.csscolor.SKY_BLUE)
        arcade.draw_circle_filled(800, 830, 40, arcade.csscolor.SKY_BLUE)
        arcade.draw_circle_filled(850, 850, 40, arcade.csscolor.SKY_BLUE)
        arcade.draw_circle_filled(700, 800, 40, arcade.csscolor.SKY_BLUE)

        arcade.draw_circle_filled(900, 800, 40, arcade.csscolor.SKY_BLUE)

        arcade.draw_circle_filled(400, 800, 40, arcade.csscolor.SKY_BLUE)
        arcade.draw_circle_filled(350, 780, 40, arcade.csscolor.SKY_BLUE)
        arcade.draw_circle_filled(150, 830, 40, arcade.csscolor.SKY_BLUE)
        arcade.draw_circle_filled(180, 825, 40, arcade.csscolor.SKY_BLUE)

        # draw a sun
        arcade.draw_circle_filled(800, 800, 40, arcade.csscolor.YELLOW)

        arcade.finish_render()


def main():
    window = MyGame()
    arcade.run()


main()










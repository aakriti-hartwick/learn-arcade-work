"""
this is an example of program that is used for drawing from arcade
"""

# working with help of supervision and guidance is to success in life

import arcade

arcade.open_window(600,600,'lab for happy world')

arcade.set_background_color(arcade.csscolor.AQUAMARINE)

arcade.start_render()
# Tree trunk
# Center of 100, 320
# Width of 20
# Height of 60
arcade.draw_rectangle_filled(300, 300, 80, 80, arcade.csscolor.SIENNA)
arcade.draw_rectangle_filled(300,300,40,40,arcade.csscolor.PINK)

# Tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(100,350,15,arcade.csscolor.ORANGE)


arcade.finish_render()

arcade.run()
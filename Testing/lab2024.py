"""
this is an example of program that is used for drawing from arcade
"""

# working with help of supervision and guidance is to success in life

import arcade

arcade.open_window(900,900,'lab for happy world')

arcade.set_background_color(arcade.csscolor.FLORAL_WHITE)

arcade.start_render()


#Draw a rectangle
#left of 0, right of 899
#top of 450, bottom of 0
arcade.draw_lrtb_rectangle_filled(0,899,450,0,arcade.csscolor.DARK_GREEN)

#draw a sun
arcade.draw_circle_filled(800,850,40,arcade.csscolor.YELLOW)
#draw a pentagon
arcade.draw_polygon_filled







# Tree top




arcade.finish_render()

arcade.run()
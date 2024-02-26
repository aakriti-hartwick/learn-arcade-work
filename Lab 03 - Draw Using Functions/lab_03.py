import arcade

screen_width = 800
screen_height = 800

def draw_sun():

    #draw a sun
    arcade.draw_circle_filled(700,700, 40,arcade.csscolor.YELLOW)

    #draw lines for sun
    arcade.draw_line(700, 700, 640, 700, arcade.color.YELLOW, 3)
    arcade.draw_line(700, 700, 760, 700, arcade.color.YELLOW, 3)
    arcade.draw_line(700, 700, 700, 640, arcade.color.YELLOW, 3)
    arcade.draw_line(700, 700, 700, 760, arcade.color.YELLOW, 3)

def draw_ground():

    arcade.draw_lrtb_rectangle_filled(0,799,400,0,arcade.csscolor.LIGHT_GREEN)

def draw_path():

    arcade.draw_lrtb_rectangle_filled(250,550,400,0,arcade.csscolor.SADDLE_BROWN)

def draw_a_house():

    arcade.draw_rectangle_filled(400,200,150,200, arcade.csscolor.WHITE_SMOKE)
    arcade.draw_triangle_filled(400,400,300,270,500,270,arcade.csscolor.GREY)
    arcade.draw_rectangle_filled(350,240,30,30,arcade.csscolor.ORANGE)
    arcade.draw_rectangle_filled(450, 240, 30, 30, arcade.csscolor.ORANGE)
    arcade.draw_rectangle_filled(400,130,40,60,arcade.csscolor.BLACK)

def draw_bird(x,y):

    """" Draw a bird."""

    #draw a bird
    arcade.draw_arc_outline(x,y,20,20,arcade.csscolor.BLACK, 0,140,3)
    arcade.draw_arc_outline(x+20,y,20,20,arcade.csscolor.BLACK, 40,180,3)
    arcade.draw_arc_outline(x+50, y-20, 20, 20, arcade.csscolor.BLACK, 0, 140, 3)
    arcade.draw_arc_outline(x+70,y-20,20,20,arcade.csscolor.BLACK, 40,180,3)
    arcade.draw_arc_outline(x+80, y, 20, 20, arcade.csscolor.BLACK, 0, 140, 3)
    arcade.draw_arc_outline(x+100,y,20,20,arcade.csscolor.BLACK,40,180,3)
def draw_hill(x,y):

    """"Draw a hill"""

    arcade.draw_arc_filled(x,y,600,400,arcade.csscolor.DARK_GREEN,0,180,0,50)
def draw_mountain():

    """Draw a mountain"""

    arcade.draw_triangle_filled(400,650,200,400,600,400,arcade.csscolor.SNOW)

def draw_tree(x,y):

    arcade.draw_rectangle_filled(x, y, 30, 100, arcade.csscolor.BROWN)
    arcade.draw_triangle_filled(x, y + 120, x - 30, y, x + 30, y, arcade.csscolor.DARK_GREEN)
def draw_flower(x,y):

    """"Draw a flower"""

    #draw stem
    arcade.draw_line(x,y,x,y+70,arcade.csscolor.DARK_GREEN,7)
    arcade.draw_line(x+700, y, x+700, y + 90, arcade.csscolor.DARK_GREEN, 7)
    arcade.draw_line(x+60, y+60, x+60,y+180,arcade.csscolor.DARK_GREEN,7)
    arcade.draw_line(x+640, y+100, x+640,200,arcade.csscolor.DARK_GREEN,7)


    #draw petals
    arcade.draw_ellipse_filled(x,y+70,30,40,arcade.csscolor.MEDIUM_PURPLE,0,-1)
    arcade.draw_ellipse_filled(x+20, y + 30, 30, 40, arcade.csscolor.DARK_GREEN, 60, -1)
    arcade.draw_ellipse_filled(x+700, y + 70, 30, 40, arcade.csscolor.HOTPINK, 0, -1)
    arcade.draw_ellipse_filled(x + 720, y + 30, 30, 40, arcade.csscolor.DARK_GREEN, 60, -1)
    arcade.draw_ellipse_filled(x + 680, y + 35, 30, 40, arcade.csscolor.DARK_GREEN, 60, -1)
    arcade.draw_ellipse_filled(x+720, y + 60, 30, 40, arcade.csscolor.HOTPINK, 60, -1)
    arcade.draw_ellipse_filled(x+680, y + 60, 30, 40, arcade.csscolor.HOTPINK, 120,-1)
    arcade.draw_ellipse_filled(x + 60, y + 180, 40, 60, arcade.csscolor.RED, 0,-1)
    arcade.draw_ellipse_filled(x + 640, y + 200, 40, 60, arcade.csscolor.YELLOW, 0, -1)

    #draw leaf
    arcade.draw_ellipse_filled(x + 20, y + 30, 30, 40, arcade.csscolor.DARK_GREEN, 60, -1)
    arcade.draw_ellipse_filled(x + 720, y + 30, 30, 40, arcade.csscolor.DARK_GREEN, 60, -1)
    arcade.draw_ellipse_filled(x + 680, y + 35, 30, 40, arcade.csscolor.DARK_GREEN, 60, -1)
    arcade.draw_ellipse_filled(x + 40, y + 140, 30, 40, arcade.csscolor.DARK_GREEN, 120,-1)
    arcade.draw_ellipse_filled(x + 80, y + 130, 30, 40, arcade.csscolor.DARK_GREEN, 60, -1)
    arcade.draw_ellipse_filled(x + 660, y + 140, 30, 40, arcade.csscolor.DARK_GREEN,60,-1)




def main():

    arcade.open_window(screen_width,screen_height,'lab 3')
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()

    draw_sun()
    draw_ground()
    draw_path()
    draw_a_house()
    draw_bird(50,750)
    draw_bird(500,750)
    draw_bird(275,700)
    draw_mountain()
    draw_hill(50,400)
    draw_hill(750,400)
    draw_tree(100,270)
    draw_tree(750,240)
    draw_flower(50,0)

    arcade.finish_render()
    arcade.run()

main() 

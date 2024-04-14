import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
MOVEMENT_SPEED = 10

class Star:
    """A class representing an object controlled by the mouse."""

    def __init__(self, position_x, position_y, color):
        """Initialize the object."""
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
        self.hit_sound = arcade.load_sound(":resources:sounds/jump2.wav")



    def draw(self):
        """Draw the object."""
        x = self.position_x
        y = self.position_y
        # Draw the object as a star shape
        arcade.draw_line(x - 30, y, x + 30, y, arcade.csscolor.WHITE_SMOKE)
        arcade.draw_line(x, y - 30, x, y + 30, arcade.csscolor.WHITE_SMOKE)
        arcade.draw_line(x - 30, y - 24, x + 30, y + 24, arcade.csscolor.WHITE_SMOKE)
        arcade.draw_line(x - 30, y + 24, x + 30, y - 24, arcade.csscolor.WHITE_SMOKE)

    def update(self, x, y):
        """Update the position of the object."""
        self.position_x = x
        self.position_y = y

        if self.position_x < 0:
            arcade.play_sound(self.hit_sound)

        if self.position_x > SCREEN_WIDTH - 30:
            arcade.play_sound(self.hit_sound)

        if self.position_y > SCREEN_HEIGHT:
            arcade.play_sound(self.hit_sound)

        if self.position_y < SCREEN_HEIGHT - 800 :
            arcade.play_sound(self.hit_sound)


class Snowman:
    def __init__(self, position_x, position_y, change_x, change_y, radius_head, radius_body, radius_bottom, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius_head = radius_head
        self.radius_body = radius_body
        self.radius_bottom = radius_bottom
        self.color = color
        self.hit_sound = arcade.load_sound(":resources:sounds/coin1.wav")

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y + 50, self.radius_bottom, self.color)  # Bottom circle (body)
        arcade.draw_circle_filled(self.position_x, self.position_y + 125, self.radius_body, self.color)  # Middle circle (body)
        arcade.draw_circle_filled(self.position_x, self.position_y + 180, self.radius_head, self.color)  # Top circle (head)
        arcade.draw_circle_filled(self.position_x - 10, self.position_y + 190, 5, arcade.color.BLACK)  # Left eye
        arcade.draw_circle_filled(self.position_x + 10, self.position_y + 190, 5, arcade.color.BLACK)  # Right eye
    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        # Ensure snowman stays within the screen boundaries
        if self.position_x < self.radius_bottom:
            self.position_x = self.radius_bottom
            arcade.play_sound(self.hit_sound)

        elif self.position_x > SCREEN_WIDTH - self.radius_bottom:
            self.position_x = SCREEN_WIDTH - self.radius_bottom
            arcade.play_sound(self.hit_sound)

        if self.position_y < self.radius_bottom - 50:
            self.position_y = self.radius_bottom - 50
            arcade.play_sound(self.hit_sound)

        elif self.position_y > SCREEN_HEIGHT - self.radius_head - 180:
            self.position_y = SCREEN_HEIGHT - self.radius_head - 180
            arcade.play_sound(self.hit_sound)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BLACK)
        self.snowman = Snowman(50, 50, 0, 0, 30, 40, 50, arcade.color.WHITE)
        self.star = Star(200, 200, arcade.color.WHITE)


    def on_draw(self):
        arcade.start_render()
        self.snowman.draw()
        self.star.draw()

    def update(self, delta_time):
        self.snowman.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.snowman.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.snowman.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.snowman.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.snowman.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.snowman.change_x = 0
        elif key in [arcade.key.UP, arcade.key.DOWN]:
            self.snowman.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        """Handle mouse motion events."""
        self.star.update(x, y)



def main():
    window = MyGame(1000, 800, "Drawing Example")
    arcade.run()


main()

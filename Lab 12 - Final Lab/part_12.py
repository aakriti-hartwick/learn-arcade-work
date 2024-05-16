import random
import arcade

# Constants
SCREEN_WIDTH = 1600  # Wider screen
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Simple Mario-like Platformer"

# Scaling constants
CHARACTER_SCALING = 0.4
TILE_SCALING = 0.5
COIN_SCALING = 0.4

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 1
PLAYER_JUMP_SPEED = 25

# How many pixels to keep as a minimum margin between the character and the edge of the screen
LEFT_VIEWPORT_MARGIN = 150
RIGHT_VIEWPORT_MARGIN = 600
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100

# Time limit in seconds
TIME_LIMIT = 120  # 2 minutes


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        """
        Initializer for the game
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each list is for a different
        # type of sprite.
        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # Used to keep track of our scrolling
        self.view_left = 0
        self.view_bottom = 0

        # Keep track of the score
        self.score = 0

        # Load sounds
        self.coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

        # Set the background color
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # Flag to show "Awesome!" message
        self.show_awesome_message = False
        self.awesome_message_timer = 0

        # Remaining time in seconds
        self.remaining_time = TIME_LIMIT

        # Flag to indicate if the game is over
        self.game_over = False

        # Flag to indicate if timing has started
        self.timing_started = False

    def draw_timer(self):
        """Draws the remaining time on the screen"""
        arcade.draw_text(f"Time: {self.remaining_time:.1f}", self.view_left + 10, self.view_bottom + SCREEN_HEIGHT - 30,
                         arcade.csscolor.WHITE, 18)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_fall.png")
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        # Create the ground
        for x in range(0, 5000, 64):  # Extend the ground over a wider range
            wall = arcade.Sprite(":resources:images/tiles/grass_sprout.png", TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        # Create platforms and walls
        coordinate_list = [
            [256, 96], [512, 96], [768, 96], [1024, 96], [1280, 96],
            [300, 200], [400, 300], [500, 400], [600, 500], [700, 400],
            [800, 300], [900, 200], [1000, 300], [1100, 400], [1200, 500],
            [1300, 400], [1400, 300], [1500, 200], [1600, 300], [1700, 400],
            [1800, 500], [1900, 400], [2000, 300], [2100, 200], [2200, 300],
            [2300, 400], [2400, 500], [2500, 400], [2600, 300], [2700, 200],
            [2800, 300], [2900, 400], [3000, 500], [3100, 400], [3200, 300],
            [3300, 200], [3400, 300], [3500, 400], [3600, 500], [3700, 400],
            [3800, 300], [3900, 200], [4000, 300], [4100, 400], [4200, 500],
            [4300, 400], [4400, 300], [4500, 200], [4600, 300], [4700, 400],
            [4800, 500], [4900, 400], [5000, 300], [200, 80]
            # Additional ladder coordinates
        ]

        for coordinate in coordinate_list:
            wall = arcade.Sprite(":resources:images/tiles/mushroomRed.png",
                                 TILE_SCALING * 3)  # Doubling the scaling factor
            wall.position = coordinate
            self.wall_list.append(wall)

        # Create coins without placing them inside walls
        for i in range(120):  # More coins
            coin = arcade.Sprite(":resources:images/pinball/pool_cue_ball.png", COIN_SCALING)
            coin_placed = False

            # Keep trying to place the coin until it's not inside any wall
            while not coin_placed:
                coin.center_x = random.randrange(5000)
                coin.center_y = random.randrange(400, 600)

                # Check for collisions with walls (mushrooms)
                walls_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
                if not walls_hit_list:
                    # If no collision, add the coin to the list and mark it as placed
                    self.coin_list.append(coin)
                    coin_placed = True

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list)

        # Set the score to zero
        self.score = 0

        # Set the viewport to the starting position
        self.view_left = 0
        self.view_bottom = 0

        # Reset game over flag
        self.game_over = False

    def draw_game_over(self):
        """Draws the 'Game Over' sign"""
        arcade.draw_text("Game Over", self.view_left + SCREEN_WIDTH / 2, self.view_bottom + SCREEN_HEIGHT / 2,
                         arcade.csscolor.RED, 48, anchor_x="center", anchor_y="center")

    def on_draw(self):
        """
        Render the screen.
        """

        # Clear the screen to the background color
        self.clear()

        # Draw all the sprites
        self.coin_list.draw()
        self.wall_list.draw()
        self.player_list.draw()

        # Draw the score on the screen
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom, arcade.csscolor.WHITE, 18)

        # Draw the remaining time on the screen
        self.draw_timer()

        # Draw "Awesome!" message if score is 15 and the timer hasn't expired
        if self.show_awesome_message and self.awesome_message_timer > 0:
            arcade.draw_text("Awesome!", 100 + self.view_left, 200 + self.view_bottom, arcade.csscolor.RED, 36)

        # If game over, draw the game over sign
        if self.game_over:
            self.draw_game_over()
        # If all coins collected, draw "You Won" message
        elif len(self.coin_list) == 0:
            arcade.draw_text("You Won!", self.view_left + SCREEN_WIDTH / 2, self.view_bottom + SCREEN_HEIGHT / 2,
                             arcade.csscolor.GREEN, 48, anchor_x="center", anchor_y="center")

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        if not self.game_over:
            # Move the player with the physics engine
            self.physics_engine.update()

            # Check if player hit any coins
            coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

            # Start timing if a coin is touched
            if coin_hit_list:
                self.start_timing()

            # Loop through each coin we hit (if any) and remove it
            for coin in coin_hit_list:
                # Remove the coin
                coin.remove_from_sprite_lists()
                # Play a sound
                arcade.play_sound(self.coin_sound)
                # Add one to the score
                self.score += 1

            # Check if score is 15 to show "Awesome!" message
            if self.score == 15:
                self.show_awesome_message = True
                self.awesome_message_timer = 120  # Display for 2 seconds (60 FPS * 2 seconds)

            # Update the awesome message timer
            if self.awesome_message_timer > 0:
                self.awesome_message_timer -= 1
            else:
                self.show_awesome_message = False

            # Decrement remaining time
            if self.timing_started:
                self.remaining_time -= delta_time

            # Check if the player falls off at the end or time runs out
            if self.player_sprite.center_y < -100 or self.remaining_time <= 0:
                # End the game
                self.game_over = True

        # Draw the "Game Over" sign even if the game is over
        if self.game_over:
            self.draw_game_over()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport
        changed = False

        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            self.view_left = int(self.view_left)
            self.view_bottom = int(self.view_bottom)

            arcade.set_viewport(self.view_left,
                                self.view_left + SCREEN_WIDTH,
                                self.view_bottom,
                                self.view_bottom + SCREEN_HEIGHT)

    def start_timing(self):
        """Starts the timing"""
        self.timing_started = True


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

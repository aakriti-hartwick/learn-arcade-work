import random
import arcade

SPRITE_SCALING_PLAYER = 0.4
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_BOMB = 0.5
COIN_COUNT = 50
BOMB_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Aakriti's Assignment"


class Coin(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()


class Bomb(arcade.Sprite):
    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1
        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.player_sprite_list = None
        self.coin_sprite_list = None
        self.bomb_sprite_list = None

        self.player_sprite = None
        self.score = 0

        self.coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.bomb_sound = arcade.load_sound(":resources:sounds/explosion1.wav")

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

        self.game_over = False

    def setup(self):
        self.player_sprite_list = arcade.SpriteList()
        self.coin_sprite_list = arcade.SpriteList()
        self.bomb_sprite_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            coin = Coin(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            self.coin_sprite_list.append(coin)

        for i in range(BOMB_COUNT):
            bomb = Bomb(":resources:images/space_shooter/meteorGrey_med1.png", SPRITE_SCALING_BOMB)
            bomb.center_x = random.randrange(SCREEN_WIDTH)
            bomb.center_y = random.randrange(SCREEN_HEIGHT)
            self.bomb_sprite_list.append(bomb)

    def on_draw(self):
        self.clear()
        self.coin_sprite_list.draw()
        self.bomb_sprite_list.draw()
        self.player_sprite_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if self.game_over:
            arcade.draw_text("Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                             arcade.color.RED, font_size=50, anchor_x="center")

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        if not self.game_over:
            self.coin_sprite_list.update()
            self.bomb_sprite_list.update()

            coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_sprite_list)

            for coin in coin_hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.coin_sound)

            bomb_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bomb_sprite_list)

            for bomb in bomb_hit_list:
                bomb.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound(self.bomb_sound)

            if len(self.coin_sprite_list) == 0:
                self.game_over = True


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

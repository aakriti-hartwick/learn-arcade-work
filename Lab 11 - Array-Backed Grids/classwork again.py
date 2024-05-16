import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Step 1
        self.WIDTH = 70
        self.HEIGHT = 70
        self.MARGIN = 5
        self.ROW_COUNT = 20
        self.COLUMN_COUNT = 20

        # Step 2
        self.SCREEN_WIDTH = (self.WIDTH + self.MARGIN) * self.COLUMN_COUNT + self.MARGIN
        self.SCREEN_HEIGHT = (self.HEIGHT + self.MARGIN) * self.ROW_COUNT + self.MARGIN

        # Step 8
        self.grid = [[0 for _ in range(self.COLUMN_COUNT)] for _ in range(self.ROW_COUNT)]
        # Step 9
        self.grid[1][5] = 0

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        # step 2
        for row in range(self.ROW_COUNT):
            for column in range(self.COLUMN_COUNT):
                # Step 6
                x = (self.MARGIN + self.WIDTH) * column + self.MARGIN + self.WIDTH / 2
                y = (self.MARGIN + self.HEIGHT) * row + self.MARGIN + self.HEIGHT / 2
                # Step 11
                color = arcade.color.WHITE
                if self.grid[row][column] == 1:
                    color = arcade.color.ROYAL_BLUE
                arcade.draw_rectangle_filled(x, y, self.WIDTH, self.HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        # Step 12
        print("Click")
        # Step 13
        print(f"Mouse coordinates: {x}, {y}")
        # Step 14
        column = x // (self.WIDTH + self.MARGIN)
        row = y // (self.HEIGHT + self.MARGIN)
        print(f"Grid coordinates: {row}, {column}")
        # Step 15
        if 0 <= row < self.ROW_COUNT and 0 <= column < self.COLUMN_COUNT:
            if self.grid[row][column] == 0:  # If cell is white
                self.grid[row][column] = 1  # Change to green
            else:
                self.grid[row][column] = 0  # Change to white


def main():
    window = MyGame(450, 450, "Grid Game")
    arcade.run()


if __name__ == "__main__":
    main()
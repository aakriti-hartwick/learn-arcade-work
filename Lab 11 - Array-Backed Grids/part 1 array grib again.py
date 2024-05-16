import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    # Set width and height
        self.WIDTH = 50
        self.HEIGHT = 50
        # This sets the margin between each cell
        # and on the edges of the screen.
        self.MARGIN = 5

    # Set row and column
        self.ROW_COUNT = 15
        self.COLUMN_COUNT = 15

        # Calculate total screen size
        self.SCREEN_WIDTH = (self.WIDTH + self.MARGIN) * self.COLUMN_COUNT + self.MARGIN
        self.SCREEN_HEIGHT = (self.HEIGHT + self.MARGIN) * self.ROW_COUNT + self.MARGIN

        # Initialize grid with all white squares
        self.grid = [[0 for _ in range(self.COLUMN_COUNT)] for _ in range(self.ROW_COUNT)]

        # Set background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()

        # Draw grid squares
        for row in range(self.ROW_COUNT):
            for column in range(self.COLUMN_COUNT):
                x = (self.MARGIN + self.WIDTH) * column + self.MARGIN + self.WIDTH / 2
                y = (self.MARGIN + self.HEIGHT) * row + self.MARGIN + self.HEIGHT / 2
                color = arcade.color.WHITE if self.grid[row][column] == 0 else arcade.color.PEACH
                arcade.draw_rectangle_filled(x, y, self.WIDTH, self.HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        # Convert screen coordinates to grid coordinates
        column = int(x // (self.WIDTH + self.MARGIN))
        row = int(y // (self.HEIGHT + self.MARGIN))

        # Toggle the color of the clicked square
        self.toggle_square(row, column)

        # Toggle the color of adjacent squares
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue  # Skip the clicked square
                if (0 <= row + dr < self.ROW_COUNT) and (0 <= column + dc < self.COLUMN_COUNT):
                    self.toggle_square(row + dr, column + dc)

    def toggle_square(self, row, column):
        if 0 <= row < self.ROW_COUNT and 0 <= column < self.COLUMN_COUNT:
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0


def main():
    game = MyGame(555, 555, "Grid Game")
    arcade.run()


if __name__ == "__main__":
    main()

import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    # set height and width
        self.WIDTH = 30
        self.HEIGHT = 30

    # This sets the margin between each cell
    # and on the edges of the screen.
        self.MARGIN = 5
    # Set up row and column
        self.ROW_COUNT = 20
        self.COLUMN_COUNT = 20

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
                color = arcade.color.WHITE if self.grid[row][column] == 0 else arcade.color.GREEN
                arcade.draw_rectangle_filled(x, y, self.WIDTH, self.HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):
        # Convert screen coordinates to grid coordinates
        column = int(x // (self.WIDTH + self.MARGIN))
        row = int(y // (self.HEIGHT + self.MARGIN))

        # Toggle the color of the clicked square
        if 0 <= row < self.ROW_COUNT and 0 <= column < self.COLUMN_COUNT:
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

        # Count total selected cells
        total_selected = sum(sum(row) for row in self.grid)
        print(f"Total of {total_selected} cells are selected.")

        # Count selected cells in each row
        for r, row in enumerate(self.grid):
            row_selected = sum(row)
            print(f"Row {r} has {row_selected} cells selected.")

            # Count continuous blocks in a row if greater than 2
            continuous_count = 0
            for cell in row:
                if cell == 1:
                    continuous_count += 1
                    if continuous_count > 2:
                        print(f"There are {continuous_count} continuous blocks selected on row {r}.")
                else:
                    continuous_count = 0

        # Count selected cells in each column
        for c in range(self.COLUMN_COUNT):
            column_selected = sum(row[c] for row in self.grid)
            print(f"Column {c} has {column_selected} cells selected.")

    def toggle_square(self, row, column):
        if 0 <= row < self.ROW_COUNT and 0 <= column < self.COLUMN_COUNT:
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0


def main():
    game = MyGame(495, 495, "Grid Game")
    arcade.run()


if __name__ == "__main__":
    main()


import tkinter as tk
from tkinter import simpledialog, messagebox

# Constants for cell size and colors
CELL_SIZE = 40
DEFAULT_COLOR = "white"
SNOW_COLOR = "lightblue"
MAX_COLOR = "blue"


class SnowTracker:
    def __init__(self, root, rows, cols):
        self.root = root
        self.root.title("Snow Accumulation Tracker")

        # Initialize grid size based on user input
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        # Canvas for drawing grid
        self.canvas = tk.Canvas(
            root, width=self.cols * CELL_SIZE, height=self.rows * CELL_SIZE
        )
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Draw initial grid
        self.draw_grid()

        # Bind mouse events to canvas
        self.canvas.bind("<Button-1>", self.increase_snow)
        self.canvas.bind("<Button-3>", self.decrease_snow)

        # Buttons for actions
        self.largest_group_button = tk.Button(
            root, text="Largest Snow Accumulation", command=self.find_largest_group
        )
        self.largest_group_button.grid(row=1, column=0, sticky="ew")

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_grid)
        self.reset_button.grid(row=1, column=1, sticky="ew")

    def draw_grid(self):
        """Draws the grid on the canvas with current snow levels."""
        self.canvas.delete("all")
        for row in range(self.rows):
            for col in range(self.cols):
                x1, y1 = col * CELL_SIZE, row * CELL_SIZE
                x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
                color = SNOW_COLOR if self.grid[row][col] > 0 else DEFAULT_COLOR
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill=color, outline="black"
                )
                if self.grid[row][col] > 0:
                    self.canvas.create_text(
                        x1 + CELL_SIZE / 2,
                        y1 + CELL_SIZE / 2,
                        text=str(self.grid[row][col]),
                    )

    def increase_snow(self, event):
        """Increases the snow level on a cell by 1."""
        row, col = event.y // CELL_SIZE, event.x // CELL_SIZE
        if row < self.rows and col < self.cols:
            self.grid[row][col] += 1
            self.draw_grid()

    def decrease_snow(self, event):
        """Decreases the snow level on a cell by 1."""
        row, col = event.y // CELL_SIZE, event.x // CELL_SIZE
        if row < self.rows and col < self.cols and self.grid[row][col] > 0:
            self.grid[row][col] -= 1
            self.draw_grid()

    def find_largest_group(self):
        """Finds the largest snow accumulation group."""
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        max_group = []
        max_snow = 0

        # Helper function for DFS traversal
        def dfs(row, col):
            stack = [(row, col)]
            group = []
            snow_total = 0
            while stack:
                r, c = stack.pop()
                if (
                    not (0 <= r < self.rows and 0 <= c < self.cols)
                    or visited[r][c]
                    or self.grid[r][c] == 0
                ):
                    continue
                visited[r][c] = True
                group.append((r, c))
                snow_total += self.grid[r][c]
                # Check neighbors
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    stack.append((r + dr, c + dc))
            return group, snow_total

        # Iterate over each cell to find groups
        for row in range(self.rows):
            for col in range(self.cols):
                if not visited[row][col] and self.grid[row][col] > 0:
                    group, snow_total = dfs(row, col)
                    if snow_total > max_snow:
                        max_snow = snow_total
                        max_group = group

        # Highlight the largest group
        self.draw_grid()
        for row, col in max_group:
            x1, y1 = col * CELL_SIZE, row * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            self.canvas.create_rectangle(
                x1, y1, x2, y2, fill=MAX_COLOR, outline="black"
            )
            self.canvas.create_text(
                x1 + CELL_SIZE / 2,
                y1 + CELL_SIZE / 2,
                text=str(self.grid[row][col]),
                fill="white",
            )

    def reset_grid(self):
        """Resets the grid to all cells with zero snow."""
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.draw_grid()


# Prompt user for grid dimensions
root = tk.Tk()
rows = simpledialog.askinteger("Input", "Enter number of rows:")
cols = simpledialog.askinteger("Input", "Enter number of columns:")

if rows and cols:
    app = SnowTracker(root, rows, cols)
    root.mainloop()
else:
    messagebox.showerror("Error", "Please enter valid grid dimensions!")

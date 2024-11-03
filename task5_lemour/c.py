import tkinter as tk
from tkinter import simpledialog, messagebox

CELL_SIZE = 40
DEFAULT_COLOR = "white"
SNOW_COLOR = "lightblue"
MAX_COLOR = "green"


class SnowTracker:
    def __init__(self, root, rows, cols):
        self.root = root
        self.root.title("Snow Accumulation Tracker")

        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

        self.canvas = tk.Canvas(root, width=cols * CELL_SIZE, height=rows * CELL_SIZE)
        self.canvas.grid(column=0, columnspan=2)

        self.draw_grid()

        self.canvas.bind("<Button-1>", self.increase_snow)
        self.canvas.bind("<Button-3>", self.decrease_snow)

        self.largest_group_button = tk.Button(
            root, text="Largest Snow Accumulation", command=self.find_largest_group
        )
        self.largest_group_button.grid(row=1, column=0, sticky="ew")

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_grid)
        self.reset_button.grid(row=1, column=1, sticky="ew")

    def draw_grid(self):
        """Draws the grid with snow levels."""
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
        """Increases snow level at the clicked location."""
        row, col = event.y // CELL_SIZE, event.x // CELL_SIZE
        if row < self.rows and col < self.cols:
            self.grid[row][col] += 1
            self.draw_grid()

    def decrease_snow(self, event):
        """Decreases snow level at the clicked location."""
        row, col = event.y // CELL_SIZE, event.x // CELL_SIZE
        if row < self.rows and col < self.cols:
            self.grid[row][col] = max(0, self.grid[row][col] - 1)
            self.draw_grid()

    def find_largest_group(self):
        """Finds and highlights the largest connected snow area."""
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        max_group = []
        max_snow = 0

        def dfs(r, c):
            """Depth-First Search to find connected snow areas."""
            stack = [(r, c)]
            group = []
            snow_total = 0
            while stack:
                row, col = stack.pop()
                if not (0 <= row < self.rows and 0 <= col < self.cols):
                    continue
                if visited[row][col] or self.grid[row][col] == 0:
                    continue

                visited[row][col] = True
                group.append((row, col))
                snow_total += self.grid[row][col]

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Adjacent directions
                    stack.append((row + dr, col + dc))
            return group, snow_total

        # Find largest connected snow area
        for row in range(self.rows):
            for col in range(self.cols):
                if not visited[row][col] and self.grid[row][col] > 0:
                    group, snow_total = dfs(row, col)
                    if snow_total > max_snow:
                        max_snow = snow_total
                        max_group = group

        # Highlight the largest group
        self.draw_grid()  # Redraw to clear any previous highlights
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
        """Resets the grid to initial state with no snow."""
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.draw_grid()


# Initialize and run the application
root = tk.Tk()
rows = simpledialog.askinteger("Input", "Enter the number of rows:")
cols = simpledialog.askinteger("Input", "Enter the number of columns:")

if rows and cols:
    app = SnowTracker(root, rows, cols)
    root.mainloop()
else:
    messagebox.showerror("Invalid input", "Please enter valid row and column numbers.")

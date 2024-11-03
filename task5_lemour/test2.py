import tkinter as tk
from tkinter import messagebox
import random

# Initialize the main window
root = tk.Tk()
root.title("Mountain Road Snow Accumulation Tracker")

# Define grid dimensions
rows = 10  # Number of rows (adjustable)
cols = 10  # Number of columns (adjustable)
grid = [[0 for _ in range(cols)] for _ in range(rows)]  # Snow level grid

# Colors
SNOW_COLOR = "white"
DEFAULT_COLOR = "grey"
HIGHLIGHT_COLOR = "blue"
MAX_SNOW_LEVEL = 5


# Functions
def increase_snow(row, col):
    """Increases snow level at the specified location."""
    if grid[row][col] < MAX_SNOW_LEVEL:
        grid[row][col] += 1
    update_grid()


def decrease_snow(row, col):
    """Decreases snow level at the specified location."""
    if grid[row][col] > 0:
        grid[row][col] -= 1
    update_grid()


def update_grid():
    """Updates the visual representation of the grid."""
    for row in range(rows):
        for col in range(cols):
            cell = cell_buttons[row][col]
            snow_level = grid[row][col]
            if snow_level > 0:
                color = SNOW_COLOR
            else:
                color = DEFAULT_COLOR
            cell.config(bg=color)
            cell.config(text=str(snow_level) if snow_level > 0 else "")


def highlight_largest_snow_area():
    """Highlights the largest connected area of snow accumulation."""
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    max_area = 0
    max_area_cells = []

    def dfs(row, col):
        """Depth-first search to count connected snowy areas."""
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or visited[row][col]
            or grid[row][col] == 0
        ):
            return 0, []

        visited[row][col] = True
        area_cells = [(row, col)]
        count = 1

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Adjacent directions
            new_count, new_cells = dfs(row + dr, col + dc)
            count += new_count
            area_cells += new_cells

        return count, area_cells

    # Find the largest connected snowy area
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] > 0 and not visited[row][col]:
                area_size, area_cells = dfs(row, col)
                if area_size > max_area:
                    max_area = area_size
                    max_area_cells = area_cells

    # Highlight the largest area
    for row, col in max_area_cells:
        cell_buttons[row][col].config(bg=HIGHLIGHT_COLOR)

    messagebox.showinfo("Largest Snow Accumulation", f"Largest area size: {max_area}")


def reset_grid():
    """Resets the grid to its initial state."""
    for row in range(rows):
        for col in range(cols):
            grid[row][col] = 0
    update_grid()


# Create grid of buttons
cell_buttons = [[None for _ in range(cols)] for _ in range(rows)]
for row in range(rows):
    for col in range(cols):
        button = tk.Button(
            root,
            width=4,
            height=2,
            bg=DEFAULT_COLOR,
            command=lambda r=row, c=col: increase_snow(r, c),
        )
        button.bind("<Button-1>", lambda e, r=row, c=col: increase_snow(r, c))
        button.bind("<Button-3>", lambda e, r=row, c=col: decrease_snow(r, c))
        button.grid(row=row, column=col)
        cell_buttons[row][col] = button

# Add control buttons
control_frame = tk.Frame(root)
control_frame.grid(row=rows, column=0, columnspan=cols)

highlight_button = tk.Button(
    control_frame, text="Largest Snow Accumulation", command=highlight_largest_snow_area
)
highlight_button.pack(side=tk.LEFT, padx=5, pady=5)

reset_button = tk.Button(control_frame, text="Reset", command=reset_grid)
reset_button.pack(side=tk.LEFT, padx=5, pady=5)

# Start the application
update_grid()
root.mainloop()

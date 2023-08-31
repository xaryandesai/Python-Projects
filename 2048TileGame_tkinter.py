import tkinter as tk
import random

GRID_SIZE = 4
BG_COLOR_EMPTY = "#9e948a"
TILE_COLORS = {
    2: "#FFFFE0",
    4: "#FFFACD",
    8: "#FFE4B5",
    16: "#FFDAB9",
    32: "#EEE8AA",
    64: "#F0E68C",
    128: "#BDB76B",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e"}

class Game2048(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("2048")
        self.geometry("400x400")
        self.grid_cells = []
        self.init_grid()
        self.new_tile()
        self.new_tile()
        self.bind("<Key>", self.handle_key)
        self.mainloop()
    def init_grid(self):
        for row in range(GRID_SIZE):
            grid_row = []
            for col in range(GRID_SIZE):
                cell_frame = tk.Frame(self, bg=BG_COLOR_EMPTY, width=100, height=100)
                cell_frame.grid(row=row, column=col, padx=5, pady=5)
                label = tk.Label(cell_frame, text="", font=("Helvetica", 20, "bold"), bg=BG_COLOR_EMPTY, justify="center")
                label.pack(expand=True)
                grid_row.append(label)
            self.grid_cells.append(grid_row)
    def new_tile(self):
        empty_cells = [(row, col) for row in range(GRID_SIZE) for col in range(GRID_SIZE) if self.grid_cells[row][col]["text"] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            value = 2 if random.random() < 0.9 else 4
            self.grid_cells[row][col]["text"] = str(value)
            self.grid_cells[row][col]["bg"] = TILE_COLORS[value]
    def handle_key(self, event):
        key = event.keysym
        if key in ('Up', 'Down', 'Left', 'Right'):
            self.move_tiles(key)
            self.new_tile()
            if self.is_game_over():
                self.show_game_over()
    def move_tiles(self, direction):
        movement_map = {
            'Up': (0, -1),
            'Down': (0, 1),
            'Left': (-1, 0),
            'Right': (1, 0)}
        dx, dy = movement_map[direction]
        merged = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                tile = self.grid_cells[row][col]["text"]
                if not tile:
                    continue
                new_row, new_col = row, col
                while True:
                    next_row, next_col = new_row + dy, new_col + dx
                    if next_row < 0 or next_row >= GRID_SIZE or next_col < 0 or next_col >= GRID_SIZE:
                        break
                    next_tile = self.grid_cells[next_row][next_col]["text"]
                    if not next_tile:
                        self.grid_cells[next_row][next_col]["text"] = tile
                        self.grid_cells[row][col]["text"] = ""
                        new_row, new_col = next_row, next_col
                    elif tile == next_tile and not merged[next_row][next_col]:
                        value = int(tile) * 2
                        self.grid_cells[next_row][next_col]["text"] = str(value)
                        self.grid_cells[row][col]["text"] = ""
                        self.grid_cells[next_row][next_col]["bg"] = TILE_COLORS[value]
                        merged[next_row][next_col] = True
                        break
                    else:
                        break
    def is_game_over(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                tile = self.grid_cells[row][col]["text"]
                if not tile:
                    return False
                if row > 0 and self.grid_cells[row - 1][col]["text"] == tile:
                    return False
                if row < GRID_SIZE - 1 and self.grid_cells[row + 1][col]["text"] == tile:
                    return False
                if col > 0 and self.grid_cells[row][col - 1]["text"] == tile:
                    return False
                if col < GRID_SIZE - 1 and self.grid_cells[row][col + 1]["text"] == tile:
                    return False
        return True
    def show_game_over(self):
        game_over_label = tk.Label(self, text="Game Over", font=("Helvetica", 30, "bold"))
        game_over_label.place(relx=0.5, rely=0.5, anchor="center")
        
if __name__ == "__main__":
    game = Game2048()



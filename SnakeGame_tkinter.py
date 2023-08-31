import tkinter as tk
import random
GAME_WIDTH = 800
GAME_HEIGHT = 600
UNIT_SIZE = 20
GAME_SPEED = 100

class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(self, width=GAME_WIDTH, height=GAME_HEIGHT)
        self.canvas.pack()
        self.snake = [(UNIT_SIZE, UNIT_SIZE * 2)]
        self.direction = 'Down'
        self.score = 0
        self.fruit = self.spawn_fruit()
        self.bind('<KeyPress>', self.on_key_press)
        self.update_game()

    def spawn_fruit(self):
        x = random.randint(0, (GAME_WIDTH - UNIT_SIZE) // UNIT_SIZE) * UNIT_SIZE
        y = random.randint(0, (GAME_HEIGHT - UNIT_SIZE) // UNIT_SIZE) * UNIT_SIZE
        return x, y

    def on_key_press(self, event):
        key = event.keysym
        if key in ('Up', 'Down', 'Left', 'Right'):
            self.direction = key

    def update_game(self):
        self.move_snake()
        self.check_collisions()
        self.draw_game()
        self.after(GAME_SPEED, self.update_game)

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'Up':
            head_y -= UNIT_SIZE
        elif self.direction == 'Down':
            head_y += UNIT_SIZE
        elif self.direction == 'Left':
            head_x -= UNIT_SIZE
        elif self.direction == 'Right':
            head_x += UNIT_SIZE
        self.snake.insert(0, (head_x, head_y))
        if self.snake[0] == self.fruit:
            self.score += 1
            self.fruit = self.spawn_fruit()
        else:
            self.snake.pop()
    def check_collisions(self):
        head = self.snake[0]
        if (
            head[0] < 0 or head[0] >= GAME_WIDTH or
            head[1] < 0 or head[1] >= GAME_HEIGHT or
            head in self.snake[1:]
        ):
            self.game_over()
    def game_over(self):
        self.canvas.create_text(
            GAME_WIDTH // 2, GAME_HEIGHT // 2,
            text=f"Game Over! Score: {self.score}",
            font=("Helvetica", 30),
            fill="red"
        )
        self.after_cancel(self.update_game)

    def draw_game(self):
        self.canvas.delete('all')
        self.canvas.create_text(
            GAME_WIDTH // 2, 10,
            text=f"Score: {self.score}",
            font=("Helvetica", 15),
            anchor='n'
        )

        for x, y in self.snake:
            self.canvas.create_rectangle(
                x, y, x + UNIT_SIZE, y + UNIT_SIZE,
                fill="green", outline="white"
            )

        fruit_x, fruit_y = self.fruit
        self.canvas.create_oval(
            fruit_x, fruit_y, fruit_x + UNIT_SIZE, fruit_y + UNIT_SIZE,
            fill="red", outline="white"
        )

if __name__ == "__main__":
    game = SnakeGame()
    game.title("Snake Game")
    game.mainloop()

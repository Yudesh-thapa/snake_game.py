import tkinter as tk
import random

WIDTH = 600
HEIGHT = 400
DELAY = 150
BLOCK_SIZE = 28
SNAKE_COLOR = "blue"
FOOD_COLOR = "red"

class SnakeGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SnakeGame")  # Corrected 'tittle' to 'title'
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, background="light blue")
        self.canvas.pack()
        self.root.bind("<KeyPress>", self.change_direction)
        self.direction = "Right"
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.create_food()
        self.score = 0
        self.display_score()
        self.game_over = False
        self.update()

    # Display Score #
    def display_score(self):
        score_text = "Score: {}".format(self.score)
        self.canvas.create_text(50, 10, text=score_text, fill="white", font=("Arial", 10), anchor="nw")  # Corrected 'create_ext' to 'create_text'

    # Food #
    def create_food(self):
        while True:
            x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            if (x, y) not in self.snake:
                return x, y

    def draw(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + BLOCK_SIZE, self.food[1] + BLOCK_SIZE, fill="red")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + BLOCK_SIZE, segment[1] + BLOCK_SIZE, fill="green")

    def move(self):
        head = self.snake[0]
        if self.direction == "Right":
            new_head = (head[0] + BLOCK_SIZE, head[1])
        elif self.direction == "Left":  # Corrected "left" to "Left"
            new_head = (head[0] - BLOCK_SIZE, head[1])  # Corrected "+ BLOCK_SIZE" to "- BLOCK_SIZE"
        elif self.direction == "Up":
            new_head = (head[0], head[1] - BLOCK_SIZE)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + BLOCK_SIZE)
        self.snake.insert(0, new_head)

        if self.snake[0] == self.food:
            self.score += 1
            self.display_score()
            self.food = self.create_food()
        else:
            self.snake.pop()

        if (self.snake[0][0] < 0 or self.snake[0][0] >= WIDTH or
                self.snake[0][1] < 0 or self.snake[0][1] >= HEIGHT or
                self.snake[0] in self.snake[1:]):
            self.game_over = True

    def change_direction(self, event):
        if event.keysym in ["Left", "Right", "Up", "Down"]:
            if (event.keysym == "Right" and self.direction != "Left" or
                event.keysym == "Up" and self.direction != "Down" or
                event.keysym == "Down" and self.direction != "Up" or
                event.keysym == "Left" and self.direction != "Right"):  # Corrected 'Left' to 'Right'
                self.direction = event.keysym

    def update(self):  # Corrected 'udate' to 'update'
        if not self.game_over:
            self.move()
            self.draw()
            self.root.after(DELAY, self.update)  # Corrected 'udate' to 'update'
        else:
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over!", fill="white", font=("Arial", 24))

if __name__ == "__main__":
    game = SnakeGame()
    game.root.mainloop()

        
        
        
         

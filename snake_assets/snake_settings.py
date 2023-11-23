import turtle
import winsound

GAME_WIDTH = 600
GAME_HEIGHT = 600
SPACE_SIZE = 20
BG_COLOR = 'black'
SNAKE_COLOR = 'blue'
FOOD_COLOR = 'red'
SCORE_COLOR = 'white'
SNAKE_SHAPE = 'square'
FOOD_SHAPE = 'circle'

delay = 0.1
score = 0
high_score = 0
blocks = []

#Set up the screen
scr = turtle.Screen()
scr.title('Snake game by Baophungdeptrai')
scr.bgcolor(BG_COLOR)
scr.setup(width = GAME_WIDTH, height = GAME_HEIGHT)
scr.tracer(0) #Lưu lại lệnh nhưng chưa cập nhật lên màn hình, nếu update sẽ cập nhật tất cả 1 lúc

#Set up the score line
score_line = turtle.Turtle()
score_line.speed(0)
score_line.color(SCORE_COLOR)
score_line.penup()
score_line.hideturtle()
score_line.goto(0, 260)
score_line.write('Score: 0  High score: 0', align = 'center', font = ('Arial', 24, 'normal'))

def play_sound():
    winsound.PlaySound("snake-hissing-6092.mp3", winsound.SND_ASYNC)

class Snake:
    def __init__(self, snake):
        self.snake = snake
        self.snake_settings()

    def snake_settings(self):
        self.snake.speed(0)
        self.snake.color(SNAKE_COLOR)
        self.snake.shape(SNAKE_SHAPE)
        self.snake.penup()
        self.snake.goto(0, 0)
        self.snake.direction = 'stop' #Dừng cập nhật vị trí và vẽ đồ họa
    
    def move(self):
        if self.snake.direction == "up":
            y = self.snake.ycor()
            self.snake.sety(y + SPACE_SIZE)

        if self.snake.direction == "down":
            y = self.snake.ycor()
            self.snake.sety(y - SPACE_SIZE)

        if self.snake.direction == "left":
            x = self.snake.xcor()
            self.snake.setx(x - SPACE_SIZE)

        if self.snake.direction == "right":
            x = self.snake.xcor()
            self.snake.setx(x + SPACE_SIZE)

class Food:
    def __init__(self, food):
        self.food = food
        self.food_settings()
    
    def food_settings(self):
        self.food.speed(0)
        self.food.color(FOOD_COLOR)
        self.food.shape(FOOD_SHAPE)
        self.food.penup()
        self.food.goto(0, 100)

class Direction(Snake):
    def __init__(self, snake):
        super().__init__(snake)

    def go_up(self):
        if self.snake.direction != "down":
            self.snake.direction = "up"

    def go_down(self):
        if self.snake.direction != "up":
            self.snake.direction = "down"

    def go_left(self):
        if self.snake.direction != "right":
            self.snake.direction = "left"

    def go_right(self):
        if self.snake.direction != "left":
            self.snake.direction = "right"

my_snake = turtle.Turtle()
snake_game = Snake(my_snake)
my_food = turtle.Turtle()
food_in_game = Food(my_food)
direction = Direction(my_snake)
scr.listen()
scr.onkeypress(direction.go_up, "Up")
scr.onkeypress(direction.go_down, "Down")
scr.onkeypress(direction.go_left, "Left")
scr.onkeypress(direction.go_right, "Right")
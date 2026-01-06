class Snake:
    def __init__(self):
        self.length = 3

    def eat(self):
        self.length += 1
    

my_snake = Snake()
my_snake.eat()

print(my_snake.length)
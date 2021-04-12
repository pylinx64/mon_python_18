# библиотеки
import turtle
import time
import random

#---------------------экран----------------------
# создание экрана
screen = turtle.Screen()
# размер экрана
screen.setup(650, 650)
# название игры
screen.title('Змейка 2077')
# меняет цвет фона
screen.bgcolor('#31F3FF')
#---------------------экран----------------------

#--------------------змейка----------------------
snake=turtle.Turtle()
snake.shape('square')
snake.penup()

# туловище
snake_body = []
#--------------------змейка----------------------

#--------------------яблоко----------------------
food=turtle.Turtle()
food.shape('turtle')
food.penup()
food.goto(random.randint(-300, 300), random.randint(-300, 300))
#--------------------яблоко----------------------

#--------------------управление------------------
# угол, клавиша
screen.onkeypress(lambda: snake.setheading(90), 'Up')
screen.onkeypress(lambda: snake.setheading(270), 'Down')
screen.onkeypress(lambda: snake.setheading(180), 'Left')
screen.onkeypress(lambda: snake.setheading(0), 'Right')
screen.listen()
#--------------------управление------------------

#--------------------игра------------------------
while True:
    
    # кушает еду (если голова касается змеи)
    if snake.distance(food) < 20:
        # перемещаем еду
        food.goto(random.randint(-300, 300), random.randint(-300, 300))
        # добавляем туловище
        snake_segment = turtle.Turtle()
        snake_segment.shape('square')
        snake_segment.penup()
        snake_segment.color('#BBBBBB')
        # ложим кусочек туловища в коробку snake_body
        snake_body.append(snake_segment)
    
    # туловище едет за головой
        
    # скорость змейки
    snake.forward(5)
    
    # обновление экрана
    screen.update()
    
    time.sleep(0.01)

from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
my_score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        my_score.clear()
        my_score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        my_score.game_over()
        game_is_on = False

    # detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            continue
        if segment.position() == snake.head.position():
            my_score.game_over()
            game_is_on = False


screen.exitonclick()
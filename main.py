from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.title("My Snake")
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.tracer(0)

# Initialize the starting positions for the snake
snake = Snake()
food = Food()
score=Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_on = True

# Main game loop
while game_on:
    screen.update()
    time.sleep(0.1)

    # Move each segment to the position of the segment ahead of it
    snake.move()


    if snake.head.distance(food) < 15:
        food.Collide()
        snake.extend()
        score.update_scoreboard()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            game_on=False
            score.game_over()


# Exit on click
screen.exitonclick()

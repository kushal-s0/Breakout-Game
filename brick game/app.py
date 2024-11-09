import turtle

# Setup the screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turns off automatic screen updates for better performance

# Paddle setup
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)  # Makes the paddle wider
paddle.penup()
paddle.goto(0, -250)

# Ball setup
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, -230)
ball.dx = 0.4  # Ball speed
ball.dy = 0.4

# Brick setup
bricks = []
brick_color = ["red", "green", "blue", "yellow"]
brick_width = 70
brick_height = 20
for y in range(150, 250, 30):
    for x in range(-350, 360, brick_width + 10):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(brick_color[(x // 80) % 4])  # Cycle through colors
        brick.shapesize(stretch_wid=1, stretch_len=2)  # Makes the brick wider
        brick.penup()
        brick.goto(x, y)
        bricks.append(brick)

# Score setup
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

speed_increase_threshold = 50  # Increase speed after every 50 points
speed_factor = 1.1

# Paddle movement functions
def paddle_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 20)

def paddle_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 20)

# Keyboard bindings
screen.listen()
screen.onkey(paddle_right, "Right")
screen.onkey(paddle_left, "Left")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boundary check
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.goto(0, -230)
        ball.dy *= -1

    # Paddle collision
    if (ball.ycor() > paddle.ycor() + 10) and (ball.ycor() < paddle.ycor() + 15) and (ball.xcor() > paddle.xcor() - 60) and (ball.xcor() < paddle.xcor() + 60):
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if ball.distance(brick) < 35:
            brick.hideturtle()
            bricks.remove(brick)
            ball.dy *= -1
            score += 10
            score_display.clear()
            score_display.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

    # Win condition (no bricks left)
    if not bricks:
        score_display.clear()
        score_display.goto(0, 0)
        score_display.write("You Win!", align="center", font=("Courier", 24, "normal"))
        break

    # Add a slight delay to make the ball's movement more visible
    turtle.delay(10)

# End the game
screen.bye()

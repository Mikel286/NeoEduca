from serial import Serial
import time
import turtle as game
from random import choice

puerto = 'COM3'   # cambia si es necesario
baudrate = 115200

ser = Serial(puerto, baudrate, timeout=1)
time.sleep(2)  # Esperar a que se establezca la conexión

def making_objetc(speed = 0, form = "square", x_position = 0, y_position = 0, width = 1, height = 1):
    game_objetc = game.Turtle()
    game_objetc.speed(speed)
    game_objetc.shape(form)
    game_objetc.color("white")
    game_objetc.penup()
    game_objetc.goto(x_position, y_position)
    game_objetc.shapesize(stretch_wid = width, stretch_len = height)
    return game_objetc

screen = game.Screen()
screen.title("⚾ Ping Pong Game ⚾")
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.tracer(0)

# Making the player A
player_A = making_objetc(x_position = -700, width = 5, height = 1)
y_A = player_A.ycor()

# Making the player B
player_B = making_objetc(x_position = 700, width = 5, height = 1)
y_B = player_B.ycor()

# Making the ball
ball = making_objetc(form = "circle")
x_ball = ball.xcor()
y_ball = ball.ycor()
direction = choice([1,-1])

def serial_update():
    
    global player_A
    global y_A

    respuesta = ser.readline().decode().strip()
    if respuesta:
        print("Pico:", respuesta)
    if respuesta == "BIDA":
        return False
    elif respuesta == "BIA":
        if y_A < 340:
            y_A += 10
            player_A.sety(y_A)
    elif respuesta == "BDA":
        if y_A > -340:
            y_A -= 10
            player_A.sety(y_A)
    return True

def ball_update():

    global ball
    global x_ball
    global y_ball
    global direction

    global player_B
    global y_B

    if y_ball > 400 or y_ball < -400:
        direction *= -1

    # x_ball += (1 * direction)
<<<<<<< HEAD
    y_ball += (1 * direction)
=======
    y_ball += (10 * direction)
>>>>>>> 39ea3b5495a0a37f901b826624f5fda3fcaef938
    # ball.setx(x_ball)
    ball.sety(y_ball)
    
    # y_B = y_ball
    # player_B.sety(y_B)

bucle  = True
while bucle:

    screen.update()
    bucle = serial_update()
<<<<<<< HEAD
    # ball_update()
=======
    #ball_update()
>>>>>>> 39ea3b5495a0a37f901b826624f5fda3fcaef938

game.bye()


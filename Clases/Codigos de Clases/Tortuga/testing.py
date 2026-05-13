import turtle as T

tortuga = T.Turtle()

def init_config():
    tortuga.pensize(4)
    tortuga.color("#000000")

def main():

    tortuga.penup()
    tortuga.forward(90)
    tortuga.right(90)

    tortuga.pendown()

    for _ in range(360):
        tortuga.forward(2)
        tortuga.right(1)

    T.done()


if __name__ == "__main__":

    init_config()
    main()



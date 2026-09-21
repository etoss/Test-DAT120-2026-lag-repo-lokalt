import turtle


def tegn_firkant(storrelse):
    turtle.forward(storrelse)         # 100 Piksler
    turtle.right(90)            # Vinkel i grader
    turtle.forward(storrelse)
    turtle.right(90)            # Vinkel i grader
    turtle.forward(storrelse)
    turtle.right(90)            # Vinkel i grader
    turtle.forward(storrelse)


if __name__ == "__main__":
    turtle.pensize(3)
    tegn_firkant(100)
    turtle.circle(50)
    turtle.done()

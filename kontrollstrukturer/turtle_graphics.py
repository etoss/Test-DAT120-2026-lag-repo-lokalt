import turtle


def tegn_firkant(storrelse):
    for i in range(4):
        turtle.forward(storrelse) 
        turtle.right(90)            # Vinkel i grader

        
if __name__ == "__main__":
    turtle.pensize(3)
    tegn_firkant(100)
    turtle.circle(50)
    turtle.done()

from turtle import *

def squareDraw(num_of_squares):
    for x in range(num_of_squares):
        for i in range(4):
            forward(100)
            left(90)
        right(90)
        up()
        forward(150)
        down()


square_numbers = int(raw_input("How many squares do you want to draw? "))

squareDraw(square_numbers)

mainloop()

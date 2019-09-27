import turtle,time,random

tt=turtle.Turtle()
def duobianxing(bianshu, bainchang):
    for i in range(bianshu):
        tt.forward(bainchang)
        tt.left(360/bianshu)

duobianxing()


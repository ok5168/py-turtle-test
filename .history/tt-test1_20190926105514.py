import turtle,time,random
turtle.setup(width=0.2,height=0.6)
# turtle.screensize(600,600,"green")
tt=turtle.Turtle()

def duobianxing(bianshu, bainchang):
    for i in range(bianshu):
        tt.forward(bainchang)
        tt.left(360/bianshu)
        # time.sleep(3)

duobianxing(4,200)

turtle.exitonclick()
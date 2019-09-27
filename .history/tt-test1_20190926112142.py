import turtle,time,random
# turtle.setup(width=0.2,height=0.6)

tt=turtle.Turtle()
# tt.screensize(200,100,"green")

def duobianxing(bianshu, bainchang):
    for i in range(bianshu):
        tt.fd(bainchang)
        tt.left(360/bianshu)
        # time.sleep(3)

# duobianxing(4,200)
for i in range(5):
    tt.fd(200)
    tt.left(130)

turtle.exitonclick()
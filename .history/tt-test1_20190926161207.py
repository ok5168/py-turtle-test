import turtle,time,random
# turtle.setup(width=0.2,height=0.6)

tt=turtle.Turtle()
# tt.screensize(200,200,"green")
hongqichang=1000
turtle.setup(hongqichang,hongqichang*(2/3))
def duobianxing(bianshu, bainchang):
    for i in range(bianshu):
        tt.fd(bainchang)
        tt.left(360/bianshu)
        # time.sleep(3)

# duobianxing(4,200)

def wujiaoxin(daxiao):
    tt.down()
    tt.color( "yellow","yellow")
    tt.begin_fill()
    for i in range(5):
        tt.fd(daxiao)
        tt.right(144)
    tt.end_fill()
    tt.up()
tt.pencolor("yellow")
turtle.bgcolor("red")

tt.penup()
tt.goto(-150,150)
wujiaoxin(150)

tt.goto(80,180)
tt.left(30)
wujiaoxin(50)
turtle.exitonclick()
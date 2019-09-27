import turtle,time,random
# turtle.setup(width=0.2,height=0.6)

tt=turtle.Turtle()
# tt.screensize(200,200,"green")
turtle.setup(600,600)
def duobianxing(bianshu, bainchang):
    for i in range(bianshu):
        tt.fd(bainchang)
        tt.left(360/bianshu)
        # time.sleep(3)

# duobianxing(4,200)

def wujiaoxin(daxiao):
    tt.color( "red","yellow")
    tt.begin_fill()
    for i in range(5):
        tt.fd(daxiao)
        tt.left(144)
    tt.end_fill()
tt.fillcolor("red")
tt.goto(50,100)
wujiaoxin(150)
tt.fillcolor("violet")
tt.up()
tt.goto(180,120)
tt.down()
wujiaoxin(20)
turtle.exitonclick()
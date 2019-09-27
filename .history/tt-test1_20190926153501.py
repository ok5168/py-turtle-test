import turtle,time,random
# turtle.setup(width=0.2,height=0.6)

tt=turtle.Turtle()
# tt.screensize(200,200,"green")
# turtle.setup(200,200)
def duobianxing(bianshu, bainchang):
    for i in range(bianshu):
        tt.fd(bainchang)
        tt.left(360/bianshu)
        # time.sleep(3)

# duobianxing(4,200)

def wujiaoxin(daxiao):
    for i in range(5):
        tt.fd(daxiao)
        tt.left(144)
tt.goto(50,100)
wujiaoxin(50)
tt.up()
tt.goto(80,120)
tt.down()
wujiaoxin(20)
turtle.exitonclick()
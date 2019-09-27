import turtle,time,random
# turtle.setup(width=0.2,height=0.6)

tt=turtle.Turtle()
# tt.screensize(200,200,"green")
hongqichang=1000
hongqigao=hongqichang*(2/3)
turtle.setup(hongqichang,hongqigao)
yihengge=hongqichang/2/15
yishuge=hongqigao/2/10

tt.pencolor("yellow")
turtle.bgcolor("red")
tt.speed(0)
def wujiaoxin(daxiao):
    tt.down()
    tt.color( "yellow","yellow")
    tt.begin_fill()
    for i in range(5):
        tt.fd(daxiao)
        tt.right(144)
    tt.end_fill()
    tt.up()


tt.penup()
tt.goto(yihengge*-13,yishuge*6)
wujiaoxin(yihengge*6)

tt.goto(yihengge*-6,yishuge*8.5)
tt.left(-15)
wujiaoxin(yihengge*2)

tt.goto(yihengge*-4,yishuge*6)
tt.left(-25)
wujiaoxin(yihengge*2)

tt.goto(yihengge*-4,yishuge*3.2)
tt.left(-25)
wujiaoxin(yihengge*2)

tt.goto(yihengge*-6,yishuge*1.5)
tt.left(-25)
wujiaoxin(yihengge*2)

# tt.pen
turtle.exitonclick()
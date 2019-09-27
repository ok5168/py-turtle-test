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
tt.goto(yihengge*-10,yihengge*6)
wujiaoxin(yihengge*6)

tt.goto(yihengge*-6,yihengge*8.5)
tt.left(30)
wujiaoxin(yihengge*2)
turtle.exitonclick()
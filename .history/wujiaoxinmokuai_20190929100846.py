'''
画五星红旗

用到turtle,time,random

'''

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
# tt.speed(0)
def wujiaoxin(daxiao,wg=tt):
    '''第一种方法  '''
    wg.down()
    wg.color( "yellow","yellow")

    # ggggggggg
    wg.begin_fill()
    for i in range(5):
        wg.fd(daxiao)
        wg.right(144)
    wg.end_fill()
    wg.up()

def wujiaoxin2(daxiao):
    '''
    第二种画五角星方法：沿边缘画

    daxiao 这个参数是指一个五角星一条小边的长！
    '''
    tt.down()
    tt.color( "yellow","yellow")
    tt.begin_fill()
    daxiao=daxiao/3
    for i in range(5):
        tt.fd(daxiao)
        tt.left(72)
        tt.fd(daxiao)
        tt.right(144)
    tt.end_fill()
    tt.up()

def wuxihonqi():
    '''
    # 画大五角星 主程序
    '''
    tt.penup()
    tt.goto(yihengge*-13,yishuge*6)
    wujiaoxin(yihengge*6)

    tt.goto(yihengge*-6,yishuge*8.5)
    tt.left(8)
    wujiaoxin(yihengge*2)

    tt.goto(yihengge*-4,yishuge*6)
    tt.left(-15)
    wujiaoxin(yihengge*2)

    tt.goto(yihengge*-4,yishuge*3.2)
    tt.left(-15)
    wujiaoxin(yihengge*2)

    tt.goto(yihengge*-6,yishuge*1.5)
    tt.left(-25)
    wujiaoxin(yihengge*2)

tt.speed(0)
wuxihonqi(tt,200)
tt.hideturtle()
# tt.pen

turtle.exitonclick()
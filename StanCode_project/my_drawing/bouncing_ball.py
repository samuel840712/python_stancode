"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX_X = 5  #X速度
VX_Y = 3  #Y速度
DELAY = 10 #延遲
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
count=0 #計算次數

window = GWindow(800, 500, title='bouncing_ball.py')
ball=GOval(SIZE,SIZE,x=START_X, y=START_Y)

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled= True #填色
    ball.color = 'black'
    ball.fill_color='black'
    window.add(ball)
    onmouseclicked(move1)

def move1(event):
    global VX_X,VX_Y, ball,GRAVITY,REDUCE, count #呼叫global
    if count < 3: #計算次數
        if ball.x==START_X: #回到原點
            VX_X = 5
            VX_Y = 3
            while True:
                ball.move(VX_X,VX_Y) #球移動速度
                VX_Y=VX_Y+GRAVITY #速度加重力
                if ball.y+ball.height >= window.height: #碰到邊界反彈
                    ball.y=window.height #回到水平面
                    VX_Y =-VX_Y*REDUCE  #*碰撞係數
                if ball.x+ball.width >= window.width: #碰到右邊編界返回原點
                    ball.x=START_X
                    ball.y=START_Y
                    break
                pause(DELAY)
            count+=1 #計算次數

if __name__ == "__main__":
    main()

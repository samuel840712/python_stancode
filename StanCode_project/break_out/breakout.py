"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts

bol_x=0      #判斷x的初速的方向
bol_y=0      #判斷y的初速的方向
disbrick = 0   #消失方塊



def main():
    graphics = BreakoutGraphics()
    global NUM_LIVES, bol_x, bol_y, disbrick
    while NUM_LIVES > 0:
        pause(FRAME_RATE)
        #定義vx,vy
        vx = graphics.get_dx()
        vy = graphics.get_dy()
        #文字表示狀態
        graphics.score.text= "分數:" + str(disbrick)+ "血量:" + str(NUM_LIVES)
        #點擊後球動作
        if graphics.count == 1:
            graphics.ball.move(vx,vy)
            bo_x=0
            bo_y=0
            #沒接到扣一滴血，球回到原點
            if graphics.ball.y+graphics.ball.height >= graphics.window.height:
                NUM_LIVES -=1
                graphics.count = 0
                graphics.reset_ball()
            #碰撞牆壁
            graphics.check_wall()
            # if graphics.ball.x <=0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
            #     vx *=-1
            # if graphics.ball.y <= 0:
            #     vy *=-1
            # if graphics.window.get_object_at(graphics.ball.x,graphics.ball.y+graphics.ball.height) is graphics.paddle:
            #     vy *=-1
            #定義球4個方位
            obj1=graphics.window.get_object_at(graphics.ball.x,graphics.ball.y)
            obj2=graphics.window.get_object_at(graphics.ball.x+graphics.ball.width,graphics.ball.y)
            obj3=graphics.window.get_object_at(graphics.ball.x,graphics.ball.y+graphics.ball.height)
            obj4=graphics.window.get_object_at(graphics.ball.x+graphics.ball.width,graphics.ball.y+graphics.ball.height)
            #判定碰撞
            bo1= obj1 is not None and obj1 is not graphics.paddle
            bo2= obj2 is not None and obj2 is not graphics.paddle
            bo3= obj3 is not None and obj3 is not graphics.paddle
            bo4= obj4 is not None and obj4 is not graphics.paddle

            #判斷碰撞後xy的初速的方向(定義4個點撞擊到時球會如何跑動):
            if bo1: #偵測到左上方，往右下跑
                bo_x += 1
                bo_y += 1
            if bo2: #偵測到右上方，往左下跑
                bo_x -= 1
                bo_y += 1
            if bo3: #偵測到左下方，往右上跑
                bo_x += 1
                bo_y -= 1
            if bo4: #偵測到右上方，往左上跑
                bo_x -= 1
                bo_y -= 1

            #判斷撞擊後，球移動的方向(將bo_x,b0_個別加總起來判斷(等同偵測碰撞1個角、2個角還是3個角的跑動方式):
            if bo_x > 0:
                graphics.bo_x1 = abs(vx)
                graphics.bouncing()
            elif bo_x < 0:
                graphics.bo_x2 = -abs(vx)
                graphics.bouncing()
            if bo_y > 0 :
                graphics.bo_y1 = abs(vx)
                graphics.bouncing()
            elif bo_y < 0:
                graphics.bo_y2 = -abs(vx)
                graphics.bouncing()

            #取代前面的位置，並刪除方塊(此判斷打掉一個算一分，且可偵測到磚塊是否消失)
            obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            bo1 = obj1 is not None and obj1 is not graphics.paddle
            if bo1:
                graphics.window.remove(obj1)
                disbrick += 1

            obj2 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width,graphics.ball.y)
            bo2 = obj2 is not None and obj2 is not graphics.paddle
            if bo2:
                graphics.window.remove(obj2)
                disbrick += 1

            obj3= graphics.window.get_object_at(graphics.ball.x,graphics.ball.y+graphics.ball.height)
            bo3 = obj3 is not None and obj3 is not graphics.paddle
            if bo3:
                graphics.window.remove(obj3)
                disbrick += 1

            obj4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                 graphics.ball.y + graphics.ball.height)
            bo4 = obj4 is not None and obj4 is not graphics.paddle
            if bo4:
                graphics.window.remove(obj4)
                disbrick += 1
            #當磚塊全部打完
            if disbrick > 100:
                NUM_LIVES = 0
                graphics.score.text="恭喜破關"
            elif NUM_LIVES == 0 :
                graphics.score.text = "可惜，你只打了" + str(disbrick) + '個'

if __name__ == '__main__':
    main()

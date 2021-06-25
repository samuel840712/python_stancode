"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.
COUNT=0



class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout',color='red'):


        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title='Breakout')
        #計算次數
        self.count = COUNT
        # Create a paddle
        self.paddle = GRect(paddle_width,paddle_height,x=(window_width-paddle_width)/2,y=window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2,ball_radius*2,x=window_width/2-ball_radius,y=window_height/2-ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)
        # Default initial velocity for the ball
        #self.velocity()
        #文字
        self.score= GLabel('準備中')
        self.score.font='-30'
        self.window.add(self.score,0,40)
        # Initialize our mouse listeners
        onmouseclicked(self.clicked)
        onmousemoved(self.move)
        self.__dx=0
        self.__dy=0
        # Default initial velocity for the ball
        self.velocity()
        # check wall
        self.check_wall()
        # bouncing
        self.bo_x1 = 0
        self.bo_x2 = 0
        self.bo_y1 = 0
        self.bo_y2 = 0
        self.bouncing()

        # Draw bricks
        for row in range(10):
            for column in range(10):
                self.rect = GRect(brick_width, brick_height)
                self.rect.filled = True
                self.rect.x=column * brick_width + column *brick_spacing
                self.rect.y=row * brick_height + row *brick_spacing+ brick_offset
                if row==0 or row==1:
                    self.rect.fill_color='red'
                if row == 2 or row == 3:
                    self.rect.fill_color = 'orange'
                if row == 4 or row == 5:
                    self.rect.fill_color = 'yellow'
                if row == 6 or row == 7:
                    self.rect.fill_color = 'green'
                if row == 8 or row == 9:
                    self.rect.fill_color = 'blue'
                self.window.add(self.rect)
    #onmousemoved函數(板子移動)
    def move(self,event):
        if event.x >= self.paddle.width/2 and event.x + self.paddle.width/2 <= self.window.width:
            self.paddle.x = event.x - PADDLE_WIDTH/2
    #速度改變
    def velocity(self):
        self.__dx = random.randint(1,MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() >0.5:
            self.__dx = -self.__dx
        if random.random()>0.5:
            self.__dy *=     -1
    #隱藏dx
    def get_dx(self):
        return self.__dx
    # 隱藏dy
    def get_dy(self):
        return self.__dy

    #onmouseclicked(點擊啟動)
    def clicked(self, event):
        if self.count == 0:
            self.count = 1
            self.velocity()
    #球回到原來的點
    def reset_ball(self):
        self.set_ball_position()
        self.velocity()
        self.window.add(self.ball)
    #初點的位置
    def set_ball_position(self):
        self.ball.x = self.window.width/2
        self.ball.y = self.window.height/2
    #確認撞到牆壁
    def check_wall(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx *= -1
        if self.ball.y <= 0:
            self.__dy *= -1
        if self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height) is self.paddle:
            self.__dy *= -1

    #儲存速度，當不為0時，將速度儲存後歸0
    def bouncing(self):
        if self.bo_x1 != 0:
            self.__dx = self.bo_x1
            self.bo_x1 = 0
        if self.bo_x2 != 0:
            self.__dx = self.bo_x2
            self.bo_x2 = 0
        if self.bo_y1 != 0:
            self.__dy = self.bo_y1
            self.bo_y1 = 0
        if self.bo_y2 != 0:
            self.__dy = self.bo_y2
            self.bo_y2 = 0



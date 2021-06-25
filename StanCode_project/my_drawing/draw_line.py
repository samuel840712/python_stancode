"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE=10
window=GWindow()
count=0  #計算次數
old_x=0
old_y=0
def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)
def draw(event):
    global count, old_x, old_y
    if count%2==0: #除2後當餘數為0時
        cir1 = GOval(SIZE, SIZE, x=event.x - SIZE / 2, y=event.y - SIZE / 2) #定義圓的位置
        window.add(cir1)
        old_x=event.x #儲存圓的X
        old_y=event.y #儲存圓的Y
        count+=1 #計算+1
    else:
        point = window.get_object_at(old_x, old_y) #找尋第一個點
        window.remove(point) #刪除
        line = GLine(old_x, old_y, event.x, event.y) #畫線
        window.add(line)
        count+=1 #計算+1
if __name__ == "__main__":
   main()

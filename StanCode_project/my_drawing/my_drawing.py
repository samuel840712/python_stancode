"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:
    """
    window=GWindow(500,400,title='cute') #頭
    head=GOval(200,180)
    head.filled =True
    head.fill_color='khaki'
    head.color='khaki'
    window.add(head, 150,100)

    body = GOval(200,400) #身體
    body.filled = True
    body.fill_color = 'khaki'
    body.color = 'khaki'
    window.add(body,150,140)

    bodya = GArc(180,400,0,180) #內部身體
    bodya.filled = True
    bodya.fill_color = 'ivory'
    bodya.color = 'ivory'
    window.add(bodya,160,310)

    rface = GOval(140, 120)  #右臉
    rface.filled = True
    rface.fill_color = 'beige'
    rface.color = 'beige'
    window.add(rface, 220, 180)

    lface = GOval(140, 120) #左臉
    lface.filled = True
    lface.fill_color = 'beige'
    lface.color = 'beige'
    window.add(lface, 150, 180)

    nose = GOval(80, 80) #鼻子
    nose.filled = True
    nose.fill_color = 'beige'
    nose.color = 'beige'
    window.add(nose, 210, 160)

    reye = GOval(20, 30) #右眼
    reye.filled = True
    reye.fill_color = 'black'
    reye.color = 'black'
    window.add(reye, 290, 150)

    leye = GOval(20, 30) #左眼
    leye.filled = True
    leye.fill_color = 'black'
    leye.color = 'black'
    window.add(leye, 190, 150)

    reyebrow = GOval(20, 10) #右眉毛
    reyebrow.filled = True
    reyebrow.fill_color = 'ivory'
    reyebrow.color = 'ivory'
    window.add(reyebrow, 290, 135)

    leyebrow = GOval(20, 10) #左眉毛
    leyebrow.filled = True
    leyebrow.fill_color = 'ivory'
    leyebrow.color = 'ivory'
    window.add(leyebrow, 190, 135)

    noseb = GOval(25, 20) #鼻子
    noseb.filled = True
    noseb.fill_color = 'black'
    noseb.color = 'black'
    window.add(noseb, 240, 170)

    lineb = GLine(252,190,252,210) #鼻線
    lineb.color = 'black'
    lineb.line_font='-40'
    window.add(lineb)

    mouth = GArc(40,150,0,-180) #嘴吧
    mouth.filled = True
    mouth.fill_color = 'red'
    mouth.color = 'red'
    window.add(mouth,232,180)

    mline = GArc(50,80,110,90) #嘴線
    mline.color='black'
    window.add(mline,250,215)

    linea = GArc(50,50,0,-180) #左鼻線
    linea.color ='black'
    window.add(linea,201,195)

    lined = GArc(50, 50, 0, -180) #右鼻線
    lined.color = 'black'
    window.add(lined, 253, 195)

    lear = GPolygon() #左耳
    lear.add_vertex((200, 110))
    lear.add_vertex((160, 150))
    lear.add_vertex((170, 80))
    lear.filled = True
    lear.fill_color ='khaki'
    lear.color = 'khaki'
    window.add(lear)

    learw = GPolygon() #左內耳
    learw.add_vertex((195, 115))
    learw.add_vertex((168, 140))
    learw.add_vertex((173, 90))
    learw.filled = True
    learw.fill_color = 'ivory'
    learw.color = 'ivory'
    window.add(learw)

    rear = GPolygon() #右耳
    rear.add_vertex((300, 110))
    rear.add_vertex((340, 150))
    rear.add_vertex((330, 80))
    rear.filled = True
    rear.fill_color = 'khaki'
    rear.color = 'khaki'
    window.add(rear)

    rearw = GPolygon() #右內耳
    rearw.add_vertex((305, 115))
    rearw.add_vertex((333, 130))
    rearw.add_vertex((328, 90))
    rearw.filled = True
    rearw.fill_color = 'ivory'
    rearw.color = 'ivory'
    window.add(rearw)

    lhand = GOval(80,200) #左手
    lhand.filled = True
    lhand.fill_color = 'khaki'
    lhand.color = 'khaki'
    window.add(lhand,115,270)

    rhand = GOval(70, 180)  # 右手
    rhand.filled = True
    rhand.fill_color = 'khaki'
    rhand.color = 'khaki'
    window.add(rhand, 320, 180)

    rhanda = GOval(15, 40)  # 右手
    rhanda.filled = True
    rhanda.fill_color = 'khaki'
    rhanda.color = 'khaki'
    window.add(rhanda, 320, 180)

    rhandb = GOval(20, 45)  # 右手
    rhandb.filled = True
    rhandb.fill_color = 'khaki'
    rhandb.color = 'khaki'
    window.add(rhandb, 370, 180)

    rline = GArc(60, 150, 50, -170)  # 右條紋
    rline.filled = True
    rline.fill_color = 'ivory'
    rline.color = 'ivory'
    window.add(rline, 340, 220)

    rlinea = GArc(50, 50, 80, -120)  # 左條紋
    rlinea.color = 'black'
    window.add(rlinea, 370, 180)

    arline = GArc(50, 80, 80, -120)  # 左條紋
    arline.color = 'black'
    window.add(arline, 370, 220)

    rlineb = GArc(50, 50, 100, 120)  # 左條紋
    rlineb.color = 'black'
    window.add(rlineb, 318, 178)

    bline = GArc(50, 80, 100, 120)  # 左條紋
    bline.color = 'black'
    window.add(bline, 318, 220)

    rlinec = GArc(50, 50, 90, 120)  # 左條紋
    rlinec.color = 'black'
    window.add(rlinec, 340, 180)

    rlined = GArc(50, 50, 90, 120)  # 左條紋
    rlined.color = 'black'
    window.add(rlined, 370, 180)

    rlinee = GArc(50, 50, 80, -120)  # 左條紋
    rlinee.color = 'black'
    window.add(rlinee, 320, 178)

    rlinef = GArc(50, 50, 80, -120)  # 左條紋
    rlinef.color = 'black'
    window.add(rlinef, 350, 180)

    handb = GOval(40, 40)  # 右手印
    handb.filled = True
    handb.fill_color = 'sienna'
    handb.color = 'sienna'
    window.add(handb, 335, 215)

    handa = GOval(20, 20)  # 右手印
    handa.filled = True
    handa.fill_color = 'sienna'
    handa.color = 'sienna'
    window.add(handa, 370, 195)

    handc = GOval(20, 20)  # 右手印
    handc.filled = True
    handc.fill_color = 'sienna'
    handc.color = 'sienna'
    window.add(handc, 345, 190)

    handd = GOval(20, 20)  # 右手印
    handd.filled = True
    handd.fill_color = 'sienna'
    handd.color = 'sienna'
    window.add(handd, 320, 195)

    hline = GArc(60, 200, 50, 170) #左條紋
    hline.filled = True
    hline.fill_color = 'ivory'
    hline.color = 'ivory'
    window.add(hline, 122, 280)

    hlineb = GArc(50, 80, 100, 120)  # 左條紋
    hlineb.color = 'black'
    window.add(hlineb, 120, 300)

    hlinea = GArc(50, 50, 70, 180)  # 左條紋
    hlinea.color = 'black'
    window.add(hlinea, 115, 350)

    hlinec = GArc(50, 200, 0, 70)  # 左條紋
    hlinec.color = 'black'
    window.add(hlinec, 175, 340)

    lhanda = GOval(70,50) #左手印
    lhanda.filled = True
    lhanda.fill_color = 'sienna'
    lhanda.color = 'black'
    window.add(lhanda,120, 365)

    hlined = GArc(50, 50, 110, 120)  # 左手印條紋
    hlined.color = 'black'
    window.add(hlined, 140, 390)

    hlinee = GArc(50, 50, 110, 100)  # 左手印條紋
    hlinee.color = 'black'
    window.add(hlinee, 170, 390)

if __name__ == '__main__':
    main()

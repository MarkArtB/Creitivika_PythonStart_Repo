x=0
y=0
z=0
v=0
c=150
#может это правда,красивый проект?
def setup():
    size(600,600)
def draw():
    global x,y,z,v,c
    fill(255)
    textSize(100)
    background(200)
    text(x,300,100)
    rect(150,150,300,300)
    fill(228,245,7)
    text(y,100,550)
    textSize(50)
    text(u"золото",100,450)
    textSize(100)
    fill(220,7,245)
    textSize(50)
    text(u"жетоны",400,450)
    textSize(100)
    text(z,400,550)
    if v == 500:
        frameRate(0.01)
        background(255,255,0)
        textSize(50)
        frameRate(0.01)
        text(u"Конец!!!",100,300)
        frameRate(1)
def mouseClicked():
    global x,y,z,c
    if mouseX > c and mouseX < c+300 and mouseY > c and mouseY < c+300:
        c=random(100,500)
        x=x+1
        y=y+3
        z=z+1
    if x == 30:
        y=y+200
        z=z+100
    if x == 60:
        y=y+300
        z=z+300
    if x == 100:
        frameRate(0.01)
        background(0,255,12)
        textSize(50)
        fill(0,125,75)
        text(u"Первая сотня!!!",100,300)
        frameRate(0.01)
        frameRate(1)
    if x == 200:
        frameRate(0.01)
        background(3,29,255)
        textSize(50)
        frameRate(0.01)
        fill(0,14,137)
        text(u"Вторая сотня!!!",100,300)
        frameRate(1)
    if x == 205:
        frameRate(120)
    if x == 250:
        y=y+random(25,30)
        z=z+random(50,60)
    if x == 300:
        frameRate(0.01)
        background(255,0,225)
        textSize(50)
        frameRate(0.01)
        fill(155,5,135)
        text(u"Третья сотня!!!",100,300)
        frameRate(1)
    if x == 400:
        frameRate(0.01)
        background(255,0,0)
        textSize(50)
        frameRate(0.01)
        fill(113,0,0)
        text(u"Четвёртая сотня!!!",100,300)
        frameRate(1)
    if x == 105 and 205 and 305 and 405:
        frameRate(120)
    if x == 500:
        global v
        v=1

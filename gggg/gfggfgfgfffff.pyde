x=0
y=0
z=0

def setup():
    size(600,600)
def draw():
    global x,y,z
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
def mouseClicked():
    global x,y,z
    if mouseX > 150 and mouseX < 450 and mouseY > 150 and mouseY < 450:
        x=x+1
    if x == 30:
        y=y+200
        z=z+100
    if x == 60:
        y=y+300
        z=z+300

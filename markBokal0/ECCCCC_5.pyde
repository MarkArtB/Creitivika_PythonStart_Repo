x=0
a=0
y=1
def setup():
    global a
    size(600,600)
    a=loadImage("haf.jpg")
def draw():
    translate(300,300)
    global a,x,y
    rotate(x)
    imageMode(CENTER)
    scale(y)
    image(a,0,0,600,150)
    x=x+0.1
    y=y+0.1
    print(y)
    if y > 10:
         y=1



    

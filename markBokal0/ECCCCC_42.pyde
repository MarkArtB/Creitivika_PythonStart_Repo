x=0
y=0
z=0
c=400
a=0
def setup():
    global x,z,a
    size(600,600)
    x=loadImage("dfg.jpg")
    z=loadImage("gaha.jpeg")
    a=loadImage("haf.jpg")
def draw():
    background(155)
    global x,y,z,c,a
    image(a,0,0,600,600)
    image(x,y,200,200,200)
    image(z,c,200,200,200)
    y=y+1
    c=c-0.5
    if y+150 >= c:
        y=0
        c=400


    

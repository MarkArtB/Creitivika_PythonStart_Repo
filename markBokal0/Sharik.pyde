z=0
c=1
x=1
def setup():
    size(600,600)
    colorMode(HSB,255)
    translate(300,300)
def draw():
    translate(300,300)
    global z,c,x
    scale(x)
    fill(z,255,255)
    ellipse(0,0,100,125)
    ellipse(0,85,50,50)
    if mouseButton == CENTER:
        z=z+c
    if mouseButton == LEFT:
        x=x+0.01
    if mouseButton == RIGHT:
        translate(-175,0)
        ellipse(0,0,100,125)
        ellipse(0,85,50,50)
    if z == 255:
        c=-5
    if z == 1:
        c=5

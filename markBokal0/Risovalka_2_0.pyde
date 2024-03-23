x=0
y=0
z=0
c=1
def setup():
    size(600,600)
    colorMode(HSB,255)
    
def draw():
    global x,y,z,c
    x=mouseX
    y=mouseY
    strokeWeight(10)
    line(300,300,x,y)
    rect(0,0,100,100)
    if mouseButton == LEFT:
        stroke(z,255,255)
        fill(z,255,255)
    if mouseButton == RIGHT:
       background(200)
    z=z+c
    if z == 255:
        c=-1
    if z == 1:
        c=1

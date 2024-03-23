x=0
y=0
z=0
c=1
def setup():
    size(600,600)
    colorMode(HSB,255)
    
def draw():
    global x,y,z,c
    strokeWeight(10)
    stroke(z,255,255)
    line(300,300,x,y)
    if mouseButton == LEFT:
       x=mouseX
       y=mouseY
    if mouseButton == RIGHT:
       background(200)
    z=z+c
    if z == 255:
        c=-1
    if z == 1:
        c=1

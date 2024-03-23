x=0
y=0
def setup():
    global x
    size(600,600)
    x=loadImage("image.jpg")
    
def draw():
    translate(300,300)
    global x,y
    if mousePressed == True:
        y=y+1
    rotate(radians(y)) 
    imageMode(CENTER)
    image(x,0,0,700,700)

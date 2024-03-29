x=0
y=0
z=0
def setup():
    global x,y,z
    size(600,600)
    x=loadImage("data.jpeg")
    y=loadImage("gata.jpeg")
    z=loadImage("fat.jpg")
def draw():
    imageMode(CENTER)
    if mouseButton == LEFT:
        image(x,300,300,600,600)
    if mouseButton == CENTER:
        image(y,300,300,600,600)
    if mouseButton == RIGHT:
        image(z,300,300,600,600)

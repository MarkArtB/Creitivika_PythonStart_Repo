x=1
def setup():
    size(600,600)

    
def draw():
    global x
    background(200)
    translate(300,300)
    scale(x)
    ellipse(0,0,100,100)
    if mousePressed == True:
        x=x+0.01
        fill(random(0,255),random(0,255),random(0,255))
    if mousePressed == False:
        x=x-0.01
        fill(random(0,255),random(0,255),random(0,255))

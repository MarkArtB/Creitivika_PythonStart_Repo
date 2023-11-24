
r=1
def setup():
    size(600,600)
    frameRate(2)
def draw():
    global r
    r=r+0.1
    background(100)
    translate(300,300)
    scale(r)
    ellipse(0,70,200,200)
    ellipse(0,-100,150,150)
    ellipse(0,-200,100,100)

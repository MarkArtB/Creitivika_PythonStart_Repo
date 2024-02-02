def setup():
    size(600,600)
    background(50)
def draw():
    strokeWeight(random(1,20))
    stroke(random(228,255),255,random(0,252))
    point(random(0,600),random(0,600))
    if frameCount == 400:
       background(50)

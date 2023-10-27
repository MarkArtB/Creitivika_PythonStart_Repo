def setup():
        size(600,600)
        background(0)
        frameRate(3)
    
def draw():
    fill(random(0,255),random(0,255),random(0,255))
    stroke(random(0,255),random(0,255),random(0,255))
    translate(random(-290,290),random(-290,290))
    ellipse(300,300,random(10,30),random(10,30))
    

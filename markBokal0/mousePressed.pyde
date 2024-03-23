def setup():
    size(600,600)
    rectMode(CENTER)
    
def draw():
    background(175)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(random(0,600),random(0,600),100,100)
    fill(random(0,255),random(0,255),random(0,255))
    rect(random(0,600),random(0,600),100,100)
    fill(random(0,255),random(0,255),random(0,255))
    triangle(random(0,600),random(0,600),random(0,600),random(0,600),random(0,600),random(0,600))
    if mousePressed == False:
        background(175)
    
    

    

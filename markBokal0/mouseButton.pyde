x=50
y=5
def setup():
    size(600,600)
    
    
def draw():
    background(175)
    global x,y
    x=x+y
    ellipse(x,300,100,100)
    if x == 550:
        y=-5
    if x == 50:
        y=5
    if mouseButton == RIGHT:
        x=50
    

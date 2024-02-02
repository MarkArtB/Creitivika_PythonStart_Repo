x=0
def setup():
    size(600,600)
def draw():
    background(155)
    global x
    ellipse(300,300,x,x)
    x=x+1
    if x == 300:
        x=0
    

x=0
def setup():
    size(600,600)
def draw():
    background(155)
    global x
    ellipse(x,x,300,300)
    x=x+10
    if x==1000:
        x=x-1000
    

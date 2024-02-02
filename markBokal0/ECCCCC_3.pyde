x=0
def setup():
    size(600,600)
def draw():
    global x
    ellipse(300,300,300,300)
    fill(x)
    x=x+1
    if x == 255:
         x=0
    

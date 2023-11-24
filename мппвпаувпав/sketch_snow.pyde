x=0
y=0
r=100
def setup():
    size(600,1000)
    
def draw():
    noStroke()
    background(0,65,90)
    global x,y,r
    r=r+1
    x=x+1
    y=y+0.1
    ellipse(100,x,y,y)
    ellipse(200,x,y,y)
    ellipse(300,x,y,y)
    ellipse(400,x,y,y)
    ellipse(500,x,y,y)

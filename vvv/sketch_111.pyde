x1=400
y1=400
x2=200
y2=200
x3=600
y3=200



def setup():
    size(800,800)
    
def draw():
    background(0)
    global x1,y1
    x1=x1+random(-5,5)
    y1=y1+random(-5,5)
    global x2,y2
    x2=x2+random(-5,5)
    y2=y2+random(-5,5)
    global x3,y3
    x3=x3+random(-5,5)
    x2=x2+random(-5,5)
    triangle(x1,y1, x2,y2, x3,y3)

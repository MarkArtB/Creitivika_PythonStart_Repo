x=100
mode="вправо"
def setup():
    size(600,600)
    
def draw():
    background(150)
    global x,mode
    rectMode(CENTER)
    ellipse(x,x,200,200)
    if x == 500:
        mode="влево"
    if x == 100:
        mode="вправо"
    if mode == "вправо":
        x=x+1
    if mode == "влево":
        x=x-1

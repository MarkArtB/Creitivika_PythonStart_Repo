x=15
y=0
mode="вправо"
def setup():
    size(600,600)
def draw():
    global y

    translate(300,300)
    rotate(y)
    background(150)
    global x,mode
    rectMode(CENTER)
    rect(0,0,x,x)
    if x == 250:
        mode="влево"
    if x == 15:
        mode="вправо"
    if mode == "вправо":
        x=x+1
        y=y+0.05
    if mode == "влево":
        x=x-1
        y=y-0.05

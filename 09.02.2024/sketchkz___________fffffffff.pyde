x=300
mode="вправо"
def setup():
    size(600,600)
    
def draw():
    background(150)
    global x,mode
    rectMode(CENTER)
    fill(131,121,60)
    ellipse(300,300,300,300)
    ellipse(300,300,300,300)
    ellipse(400,500,200,200)
    fill(178,163,77)
    ellipse(200,500,200,200)
    fill(131,121,60)
    ellipse(200,500,150,150)
    fill(178,163,77)
    ellipse(400,500,150,150)
    fill(131,121,60)
    ellipse(500,300,200,200)
    fill(178,163,77)
    ellipse(100,x,200,200)
    fill(131,121,60)
    ellipse(100,x,150,150)
    fill(178,163,77)
    ellipse(500,300,150,150)
    fill(131,121,60)
    ellipse(300,100,200,200)
    fill(178,163,77)
    ellipse(250,150,100,100)
    ellipse(350,150,100,100)
    fill(0)
    ellipse(300,115,25,25)
    ellipse(350,80,25,50)
    ellipse(250,80,25,50)
    if x == 400:
        mode="влево"
    if x == 300:
        mode="вправо"
    if mode == "вправо":
        x=x+1
    if mode == "влево":
        x=x-1

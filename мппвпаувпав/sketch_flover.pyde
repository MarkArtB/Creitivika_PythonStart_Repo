s=-290
x=700
y=675
z=725
c=700
def setup():
    size(600,1000)  
    
def draw():
    global x,y,s,z,c
    c=c-1
    x=x-1
    s=s-1
    y=y-1
    z=z-1
    background(160,160,160)
    fill(10,250,0)
    rect(295,1000,20,s)
    fill(255,255,255)
    ellipse(300,y,50,50)
    ellipse(300,z,50,50)
    ellipse(275,x,50,50)
    ellipse(325,x,50,50)
    fill(240,255,0)
    ellipse(300,c,50,50)

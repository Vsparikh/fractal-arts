size(800,800)
background(255)
left = (400,0)
right = (400,0)
previousLeft = (400,0)
previousRight= (400,0)
strokeWeight(2)

def drawlevels(n, x, y,spread,levelHeight,sfactor,hfactor):
    if n <= 0:
        return
    ellipse(x,y,2,2)
    stroke(random(255),random(255),random(255))
    line(x,y, x - x//spread, y + levelHeight)
    line(x,y, x + x//spread,y +  levelHeight)
    drawlevels(n-1,x - x//spread, y + levelHeight,spread/sfactor,levelHeight*hfactor,sfactor,hfactor)
    drawlevels(n-1, x + x//spread, y + levelHeight,spread/sfactor, levelHeight*hfactor,sfactor,hfactor)
    

drawlevels(15,400, 30,10, 150,0.7,0.8)

import math
def buildHTree(x, y, d, l):
  if d == 0:
    return

  x0 = x - (l/2)
  y0 = y - (l/2)
  x1 = x + (l/2)
  y1 = y + (l/2)
  
  drawLine(x0, y0, x1, y0)
  drawLine(x0, y0, x0, y1) 
  drawLine(x1, y1, x1, y0) 
  
  l = l / math.sqrt(2)
  
  buildHTree(x0, y0, d-1, l)
  buildHTree(x0, y1, d-1, l)
  buildHTree(x1, y1, d-1, l)
  buildHTree(x1, y0, d-1, l)
  
def drawLine(x1, y1, x2, y2):
  print(x1,y1, x2, y2)
  

  
buildHTree(0,0,2,2)
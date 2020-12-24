# (This problem is an interactive problem.)

# Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship.

# You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true If there is at least one ship in the rectangle represented by the two points, including on the boundary.

# Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is guaranteed that there are at most 10 ships in that rectangle.

# Submissions making more than 400 calls to hasShips will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

# Example :



# Input: 
# ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
# Output: 3
# Explanation: From [0,0] to [4,4] we can count 3 ships within the range.

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def findShips(x2,y2,x1,y1):
            if x1 > x2 or y1 > y2 or not sea.hasShips(Point(x2,y2), Point(x1, y1)):
                return 0
            if x1 == x2 and y1 == y2:
                return 1
            
            xm = floor((x1 + x2) // 2)
            ym = floor((y1 + y2) // 2)
            
            q1 = findShips(x2,y2,xm+1,ym+1)
            q2 = findShips(xm,ym,x1,y1)
            q3 = findShips(x2,ym,xm+1,y1)
            q4 = findShips(xm,y2,x1,ym+1)
            
            return q1+q2+q3+q4
        
        return findShips(topRight.x, topRight.y, bottomLeft.x, bottomLeft.y)


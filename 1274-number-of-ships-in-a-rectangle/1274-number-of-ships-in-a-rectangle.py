# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # 1. Base Case: Invalid rectangle or no ships in this area
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        # 2. Base Case: Found a single point with a ship
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        
        # 3. Recursive Step: Split along the larger dimension
        width = topRight.x - bottomLeft.x
        height = topRight.y - bottomLeft.y
        
        if width >= height:
            # Split vertically (divide the x-axis)
            mid_x = (topRight.x + bottomLeft.x) // 2
            return self.countShips(sea, Point(mid_x, topRight.y), bottomLeft) + \
                   self.countShips(sea, topRight, Point(mid_x + 1, bottomLeft.y))
        else:
            # Split horizontally (divide the y-axis)
            mid_y = (topRight.y + bottomLeft.y) // 2
            return self.countShips(sea, Point(topRight.x, mid_y), bottomLeft) + \
                   self.countShips(sea, topRight, Point(bottomLeft.x, mid_y + 1))
        
        
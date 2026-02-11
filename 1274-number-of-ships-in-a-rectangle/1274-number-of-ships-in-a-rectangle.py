class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1

        midX = (topRight.x + bottomLeft.x) // 2
        midY = (topRight.y + bottomLeft.y) // 2

        quadrantBoundaries = [
            (midX, midY, bottomLeft.x, bottomLeft.y),
            (topRight.x, topRight.y, midX + 1, midY + 1),
            (midX, topRight.y, bottomLeft.x, midY + 1),
            (topRight.x, midY, midX + 1, bottomLeft.y)
        ]

        totalShips = 0
        for nextTopX, nextTopY, nextBottomX, nextBottomY in quadrantBoundaries:
            if nextBottomX <= nextTopX and nextBottomY <= nextTopY:
                nextTopRight = Point(nextTopX, nextTopY)
                nextBottomLeft = Point(nextBottomX, nextBottomY)
                
                if sea.hasShips(nextTopRight, nextBottomLeft):
                    totalShips += self.countShips(sea, nextTopRight, nextBottomLeft)

        return totalShips
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()

        rotated = zip(*matrix)
        
        # Clear and extend modifies the original object in-place
        matrix.clear()
        matrix.extend(rotated)
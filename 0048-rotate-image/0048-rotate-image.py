class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rotated = [list(row[::-1]) for row in zip(*matrix)]
        matrix.clear()
        matrix.extend(rotated)
        
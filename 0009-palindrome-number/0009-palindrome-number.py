class Solution:
    def isPalindrome(self, x: int) -> bool:
        iterable = str(x)
        left, right = 0, len(iterable) - 1

        while left <= right:
            if iterable[left] != iterable[right]:
                return False
            left += 1
            right -= 1  

        return True  

        
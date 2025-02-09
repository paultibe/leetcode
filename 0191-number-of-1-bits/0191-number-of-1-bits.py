class Solution:
    def hammingWeight(self, n: int) -> int:
        # 1 = 01 
        # 2 = 10
        # 3 = 11
        # 4 = 100
        # 5 = 101
        # 6 = 110
        # 7 = 111
        # 8 = 1000
        # odd numbers have least significant bit of 1
        # how can isolate least significant bit? check if number is even or odd
        result = 0
        for i in range(32): # because of constraint of max of 31 bits
            if n % 2 == 1: # or do n && 1
                result += 1
            n = n >> 1
        return result
        

        # how do you know how many times to shift????????
        
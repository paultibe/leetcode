class Solution:
    def arrangeCoins(self, n: int) -> int:
        coins_for_row = 1
        coins_remaining = n 
        number_of_rows = 0

        """
        1, 5
        """
        while coins_remaining >= coins_for_row:
            number_of_rows += 1
            coins_remaining -= coins_for_row
            coins_for_row += 1
        
        return number_of_rows


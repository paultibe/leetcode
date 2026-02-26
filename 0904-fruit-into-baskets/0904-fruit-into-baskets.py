class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        """
        scratch notes
        keep map of fruit type -> count
        """
        max_fruits_collected = 0
        baskets = defaultdict(int)
        start_index = 0

        for end_index, fruit_type in enumerate(fruits):
            baskets[fruit_type] += 1

            while len(baskets) > 2:
                left_fruit = fruits[start_index]
                baskets[left_fruit] -= 1
            
                if baskets[left_fruit] == 0:
                    del baskets[left_fruit]
                
                start_index += 1
            current_window_size = end_index - start_index + 1
            max_fruits_collected = max(max_fruits_collected, current_window_size)

        return max_fruits_collected
        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []  # This is the shared result list

        def backtrack(current_nums, path):
            # Base Case: If no numbers are left to pick, we found a permutation
            if not current_nums:
                res.append(path) 
                return

            for i in range(len(current_nums)):
                # Choose: Pick one number
                new_nums = current_nums[:i] + current_nums[i+1:]
                new_path = path + [current_nums[i]]
                
                # Explore: Move to the next level with the remaining numbers
                backtrack(new_nums, new_path)

        backtrack(nums, [])
        return res
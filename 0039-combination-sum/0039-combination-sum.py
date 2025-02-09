class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def combination(selected: List[int], options: List[int], total: int):
            if total == target:
                result.append(selected.copy())
                return
            if len(options) == 0 or total > target:
                return
            # make choice
            choice = options.copy().pop()
            selected.append(choice)
            # call with choice (it still has the option available)
            copy = options.copy()
            combination(selected, copy, total + choice)
            # afterwards, undo choice
            # if choice has been chosen, don't choose again
            selected.pop()
            options.pop()
            combination(selected, options, total)
        combination([], candidates, 0)
        return result
        
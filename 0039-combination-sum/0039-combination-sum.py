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
            selected.append(options[-1])
            previousOptions = options.copy()
            # call with choice (it still has the option available)
            combination(selected, options, total + options[-1])
            # afterwards, undo choice
            # if choice has been chosen, don't choose again
            selected.pop()
            previousOptions.pop()
            combination(selected, previousOptions, total)
        combination([], candidates, 0)
        return result
        
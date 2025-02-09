class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def combination(selected: List[int], options: List[int]):
            if sum(selected) == target:
                result.append(selected.copy())
                return
            if len(options) == 0 or sum(selected) > target:
                return
            # make choice
            choice = options.copy().pop()
            selected.append(choice)
            # call with choice (it still has the option available)
            copy = options.copy()
            combination(selected, copy)
            # afterwards, undo choice
            # if choice has been chosen, don't choose again
            selected.pop()
            options.pop()
            combination(selected, options)
        combination([], candidates)
        return result
        
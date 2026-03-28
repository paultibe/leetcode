from itertools import product
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MODULUS = 10**9 + 7
        NUM_COLORS = 3

        def is_vertically_valid(column_pattern: tuple) -> bool:
            return all(
                column_pattern[row] != column_pattern[row + 1]
                for row in range(len(column_pattern) - 1)
            )

        def are_horizontally_compatible(left_col: tuple, right_col: tuple) -> bool:
            return all(left_col[row] != right_col[row] for row in range(len(left_col)))

        all_column_patterns = [
            pattern
            for pattern in product(range(NUM_COLORS), repeat=m)
            if is_vertically_valid(pattern)
        ]

        compatible_successors = {
            pattern: [
                other for other in all_column_patterns
                if are_horizontally_compatible(pattern, other)
            ]
            for pattern in all_column_patterns
        }

        # dp[pattern] = number of valid colorings up to the current column
        # ending with this column pattern
        dp = {pattern: 1 for pattern in all_column_patterns}

        for _ in range(n - 1):
            next_dp = {pattern: 0 for pattern in all_column_patterns}
            for pattern, ways in dp.items():
                for successor in compatible_successors[pattern]:
                    next_dp[successor] = (next_dp[successor] + ways) % MODULUS
            dp = next_dp

        return sum(dp.values()) % MODULUS
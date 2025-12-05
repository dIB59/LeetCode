from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)

        for current in range(n):
            left_max = max(height[:current+1])
            right_max = max(height[current:])

            total += min(left_max, right_max) - height[current]
        return total

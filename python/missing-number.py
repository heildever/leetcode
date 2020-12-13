from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # taking advantage of sum formula
        n = len(nums)
        return ((n * (n + 1)) // 2) - sum(nums)

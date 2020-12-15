from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxima = current = 0

        for num in nums:
            if num:
                current += 1
            else:
                if current > maxima:
                    maxima = current
                current = 0

        return max(maxima, current)

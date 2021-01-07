# question can be found on leetcode.com/problems/relative-ranks/
from typing import List


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        lookup = {score: rank for rank, score in enumerate(sorted(nums, reverse=True))}
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [
            str(i) for i in range(4, len(nums) + 1)
        ]
        return [medals[lookup[n]] for n in nums]

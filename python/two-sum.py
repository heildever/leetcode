# question can be found at leetcode.com/problems/subdomain-visit-count/
from Typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        occurences = {}
        for idx, num in enumerate(nums):
            if num in occurences:
                return [occurences[num], idx]
            occurences[target - num] = idx

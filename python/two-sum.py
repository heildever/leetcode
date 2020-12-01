# question can be found at leetcode.com/problems/subdomain-visit-count/
from Typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for idx, num in nums:
            if num in lookup:
                return [lookup[num], idx]
            lookup[target - num] = idx

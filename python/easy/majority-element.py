# question can be found at leetcode.com/problems/majority-element/
from Typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lookup = {}

        for num in nums:
            if num not in lookup:
                lookup[num] = 1

            if lookup[num] > len(nums) // 2:
                return num
            else:
                lookup[num] += 1

        # hacky solution relying on question statement
        # return sorted(nums)[len(nums) // 2]

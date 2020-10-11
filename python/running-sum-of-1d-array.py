# question can be found at leetcode.com/problems/running-sum-of-1d-array/
from Typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        val = [nums[0]]
        for idx, num in enumerate(nums[1:]):
            val.append(val[idx] + num)
        return val

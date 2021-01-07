# question can be found on leetcode.com/problems/create-target-array-in-the-given-order/
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for idx, num in enumerate(index):
            target.insert(num, nums[idx])

        return target

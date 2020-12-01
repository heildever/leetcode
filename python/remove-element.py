# question can be found at leetcode.com/problems/remove-element/
from Typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [i for i in nums if i != val]
        return len(nums)

# question can be found on leetcode.com/problems/remove-duplicates-from-sorted-array/
from Typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)

# question can be found on leetcode.com/problems/find-peak-element
from typing import List


# basically binary search
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while end > start:
            mid = (end + start) // 2
            if nums[mid] >= nums[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start

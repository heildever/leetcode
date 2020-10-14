# question can be found on leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
from Typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums2).intersection(set(nums2))
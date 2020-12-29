# question can be found at leetcode.com/problems/median-of-two-sorted-arrays/
from tpying import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        len_nums = len(nums)
        median_idx = len_nums // 2
        if len_nums % 2 == 0:
            return nums[median_idx - 1] + nums[median_idx] / 2
        else:
            return nums[median_idx]

# question can be found at leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
from Typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counting_list = [
            len([number for number in nums if num > number]) for num in nums
        ]

        ## alternative solution
        sorted_nums = nums
        counting_list = [len(sorted_nums[: sorted_nums.index(num)]) for num in nums]

        return counting_list

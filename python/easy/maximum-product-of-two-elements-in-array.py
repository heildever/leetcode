# question can be found on leetcode.com/maximum-product-of-two-elements-in-an-array/
# I solved this question without using the built-in max() fn
from Typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        greatest = 0
        great = 0
        for num in nums:
            if num > greatest:
                great = greatest
                greatest = num
            elif greatest >= num > great:
                great = num
        return (greatest - 1) * (great - 1)

    ## Sorting Solution
    # Python's sort() implements Timsort which has O(n.logn) avg complexity

    def maxProduct(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        return (sorted_nums[-1] - 1) * (sorted_nums[-2] - 1)

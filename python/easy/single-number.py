# question can be found at leetcode.com/problems/single-number/
# asked to implemented in linear runtime complexity and without using extra memory
from Typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter_dict = {}
        for num in nums:
            counter_dict[num] = counter_dict.get(num, 0) + 1
        for pair in counter_dict:
            if counter_dict[pair] == 1:
                return pair

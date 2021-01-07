# question can be found at leetcode.com/problems/number-of-good-pairs/
from Typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        for idx, pair1 in enumerate(nums[:-1]):
            for pair2 in nums[idx + 1:]:
                if pair1 == pair2:
                    good_pairs += 1
        return good_pairs

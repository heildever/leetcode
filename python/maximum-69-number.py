# question can be found at leetcode.com/problems/maximum-69-number/


class Solution:
    def maximum69Number(self, nums: int) -> int:
        return str(nums).replace("6", "9", 1)

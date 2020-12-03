# question can be found on leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(0, n)]
        res = nums[0]
        for item in nums[1:]:
            res ^= item
        return res
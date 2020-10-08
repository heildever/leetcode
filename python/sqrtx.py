# question can be found at leetcode.com/problems/sqrtx/
# The original implementation does a Binary search


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        i, result = 1, 1
        while result <= x:
            i += 1
            result = pow(i, 2)
        return i - 1
        # or literally return x ** 0.5 :lel:

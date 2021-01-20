# question can be found on leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        for num in str(n):
            product *= int(num)
            total += int(num)
        return product - total

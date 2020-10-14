# question can be found on leetcode.com/problems/count-odd-numbers-in-an-interval-range/


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        number = (high - low + 1) // 2
        if low % 2 != 0 and high % 2 != 0:
            return number + 1
        else:
            return number

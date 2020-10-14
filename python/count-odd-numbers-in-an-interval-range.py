# question can be found on leetcode.com/problems/destination-city/


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        number = (high - low + 1) // 2
        if low % 2 != 0 and high % 2 != 0:
            return number + 1
        else:
            return number

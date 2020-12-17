# question can be found on leetcode.com/problems/count-of-matches-in-tournament/


class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        remainder = n
        while remainder >= 2:
            if remainder % 2 == 0:
                remainder = remainder / 2
                matches += remainder
            else:
                remainder = (remainder + 1) / 2
                matches += remainder - 1

        return int(matches)

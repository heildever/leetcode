# question can be found on leetcode.com/problems/calculate-money-in-leetcode-bank/


class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        saved = 0

        if weeks > 0:
            for i in range(weeks):
                saved += 7 * (4 + i)

        if days > 0:
            saved += sum(range(weeks + 1, weeks + days + 1))

        return saved

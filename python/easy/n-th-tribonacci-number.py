# question can be found on leetcode.com/problems/n-th-tribonacci-number/


class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [0, 1, 1]
        if 2 >= n:
            return memo[n]

        for _ in range(3, n + 1):
            memo.append(sum(memo))
            memo.pop(0)

        return memo[-1]

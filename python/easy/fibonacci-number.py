# question can be found on leetcode.com/problems/fibonacci-number/


class Solution:
    def fib(self, n: int) -> int:
        memo = [0, 1]
        if 1 >= n:
            return memo[n]

        for _ in range(2, n + 1):
            memo.append(sum(memo))
            memo.pop(0)

        return memo[-1]

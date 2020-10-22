# question can be found at leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
                steps += 1
            else:
                num = (num - 1) / 2
                steps += 2

        return steps - 1 if steps > 0 else 0

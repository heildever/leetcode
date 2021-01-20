# question can be found at leetcode.com/problems/fizz-buzz
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ls = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ls.append("FizzBuzz")
            elif i % 5 == 0:
                ls.append("Buzz")
            elif i % 3 == 0:
                ls.append("Fizz")
            else:
                ls.append(str(i))
        return ls

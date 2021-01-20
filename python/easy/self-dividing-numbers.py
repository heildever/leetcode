# question can be found on leetcode.com/problems/self-dividing-numbers/
from Typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def isSelfDividing(num):
            digits = set(str(num))
            dividers = 0
            if "0" in digits:
                return False
            for digit in digits:
                if num % int(digit) == 0:
                    dividers += 1
            return len(digits) == dividers

        potentials = []
        for num in range(left, right + 1):
            if isSelfDividing(num):
                potentials.append(num)

        return potentials

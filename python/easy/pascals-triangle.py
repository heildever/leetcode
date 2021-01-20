# question can be found on leetcode.com/problems/pascals-triangle/
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # The trick here is to know the math behind
        # how the triangle is constructed which is
        # binomial coeffiecients
        triangle = [[1] * idx for idx in range(1, numRows + 1)]
        for level in triangle:
            level = [
                self.combinations(len(level) - 1, idx) for idx in range(len(level))
            ]

    # math.comb() starting from python3.8 or
    # def calculate_combinations(n, r):
    #     from math import factorial
    #     return factorial(n) // factorial(r) // factorial(n-r)

    def combinations(self, num1, num2):
        if num1 >= num2 >= 0:
            num1tok, num2tok = 1, 1
            for t in range(1, min(num2, num1 - num2) + 1):
                num1tok *= num1
                num2tok *= t
                num1 -= 1
            return num1tok // num2tok
        else:
            pass

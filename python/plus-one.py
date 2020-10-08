# question can be found at leetcode.com/problems/plus-one
from Typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ## Solution 0
        reversed_digits = reversed(digits)
        num = 0
        for idx, digit in enumerate(reversed_digits):
            num += digit * 10**(idx)
        return [digit for digit in str(num + 1)]

        ## Solution 1
        # number = int("".join(map(str, digits)))+1
        # return([int(d) for d in str(number)])

        ## Solution 2
        # number = ""
        # for digit in digits:
        #     number += str(digit)
        # return [num for num in str(int(number) + 1)]

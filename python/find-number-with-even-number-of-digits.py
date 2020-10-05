# question can be found on leetcode.com/problems/find-numbers-with-even-number-of-digits/
from Typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([num for num in nums if len(str(num)) % 2 == 0])

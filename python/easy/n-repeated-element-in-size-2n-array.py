# question can be found at leetcode.com/problems/n-repeated-element-in-size-2n-array/
from Typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        # hacky solution, knowing there is only 1 item that has .count() > 1
        for num in A:
            if A.count(num) > 1:
                return num

        # dict based solution
        counter = {}
        for num in A:
            if num in counter:
                return num
            else:
                counter[num] = 1

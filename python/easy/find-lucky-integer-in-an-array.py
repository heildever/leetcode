# question can be found on leetcode.com/problems/find-lucky-integer-in-an-array/
from Typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num_lookup = {}
        for num in arr:
            if num in num_lookup:
                num_lookup[num] += 1
            else:
                num_lookup.update({num: 1})

        luckies = [num for num in num_lookup if num == num_lookup[num]]

        return max(luckies) if len(luckies) >= 1 else -1

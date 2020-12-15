# question can be found on leetcode.com/problems/duplicate-zeros
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        idx = 0
        while len(arr) > idx:
            if arr[idx] == 0:
                arr.insert(idx+1, 0)
                arr.pop()
                idx += 1
            idx += 1

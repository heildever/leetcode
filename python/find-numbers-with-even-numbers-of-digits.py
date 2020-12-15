from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evens = [num for num in nums if len(str(num)) % 2 == 0]
        return len(evens)

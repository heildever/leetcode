# question can be found on leetcode.com/problems/decompress-run-length-encoded-list/
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for num in range(0, int(len(nums)), 2):
            result.extend([nums[num + 1]] * nums[num])
        return result

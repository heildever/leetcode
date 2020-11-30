# question can be found at leetcode.com/problems/shuffle-the-array/
from Typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        rl = []
        for idx, num in enumerate(nums[:n]):
            rl.extend([num, nums[idx+n]])
        return rl

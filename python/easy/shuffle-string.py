# question can be found on leetcode.com/problems/shuffle-string/
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lookup = dict(zip(indices, s))
        result = ""
        for idx in sorted(lookup.keys()):
            result += lookup[idx]
        return result

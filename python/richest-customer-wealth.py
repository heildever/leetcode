# question can be found at leetcode.com/problems/richest-customer-wealth/
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(item) for item in accounts])

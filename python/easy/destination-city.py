# question can be found on leetcode.com/problems/destination-city/
from Typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ox, dx = [], []
        for pair in paths:
            ox.append(pair[0])
            dx.append(pair[1])
        return [set(dx) - set(ox)][0]

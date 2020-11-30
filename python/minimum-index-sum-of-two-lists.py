# question can be found on leetcode.com/problems/minimum-index-sum-of-two-lists/
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lookup1 = {item: idx for idx, item in enumerate(list1)}
        lookup2 = {item: idx + lookup1[item] for idx, item in enumerate(list2) if item in lookup1}
        return [key for key, value in lookup2.items() if value == min(lookup2.values())]

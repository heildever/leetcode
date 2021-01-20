# question can be found at leetcode.com/problems/unique-number-of-occurrences/
# btw collections.Counter() would solve this questions easily, rapildy
# but that's not the point, right?
from Typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter_set = set(arr.count(num) for num in arr)
        return len(counter_set) == len(set(arr))

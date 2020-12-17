# question can be found at leetcode.com/problems/leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hashmap = {}
        for idx, size in enumerate(groupSizes):
            if size not in hashmap:
                hashmap[size] = [idx]
            else:
                hashmap[size].append(idx)

        result = []
        for group in hashmap:
            length = len(group)
            for i in range(0, size, group):
                result.append(hashmap[group][i:i + length])

        return result

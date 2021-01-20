# question can be found at leetcode.com/problems/find-the-difference/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = sorted(s)
        for idx, st in enumerate(sorted(t)):
            if len(s) > idx:
                if st != sorted_s[idx]:
                    return st
            else:
                return st

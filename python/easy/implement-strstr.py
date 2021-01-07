# question can be found at leetcode.com/problems/implement-strstr/


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif needle not in haystack:
            return -1
        else:
            return haystack.index(needle)

    # or literally return haystack.find(needle) if len(needle) != 0 else 0

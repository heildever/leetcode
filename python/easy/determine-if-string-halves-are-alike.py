# question can be found on leetcode.com/problems/determine-if-string-halves-are-alike/


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        le = len(s) // 2
        wovels = "aeiouAEIOU"
        aw = [1 for char in s[:le] if char in wovels]
        bw = [1 for char in s[le:] if char in wovels]

        return sum(aw) == sum(bw)

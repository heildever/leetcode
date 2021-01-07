# question can be found at leetcode.com/problems/length-of-last-word/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s.split()) > 0:
            return len(s.split()[-1])
        else:
            return 0

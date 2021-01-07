# question can be found on leetcode.com/generate-a-string-with-characters-that-have-odd-counts/


class Solution:
    def generateTheString(self, n: int) -> str:
        if n // 2 == 1:
            return "a" * (n - 2) + "b" + "c"
        else:
            return "a" * (n - 2) + "b"

# question can be found on leetcode.com/problems/valid-palindrome


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join([c for c in s if c.isalnum()]).upper()
        return clean_s == clean_s[::-1]

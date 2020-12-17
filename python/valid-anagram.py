# question can be found at leetcode.com/problems/valid-anagram/


def isAnagram3(self, s, t):
    return sorted(s) == sorted(t)

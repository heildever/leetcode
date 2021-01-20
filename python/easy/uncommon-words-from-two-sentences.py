# question can be found at leetcode.com/problems/uncommon-words-from-two-sentences/
from Typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        C = A.split(" ") + B.split(" ")
        return [word for word in set(C) if C.count(word) == 1]

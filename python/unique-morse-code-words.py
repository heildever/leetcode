# question can be found at leetcode.com/problems/unique-morse-code-words/
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        trx = set()
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        abc = "abcdefghijklmnopqrstuvwxyz"
        for word in words:
            tx = ""
            for char in word:
                tx += morse[abc.index(char)]

            trx.add(tx)

        return len(trx)

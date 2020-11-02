# question can be found at leetcode.com/problems/keyboard-row/
from Typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "QWERTYUIOPqwertyuiop"
        second_row = "ASDFGHJKLasdfghjkl"
        third_row = "ZXCVBNMzxcvbnm"
        ables = []
        for word in words:
            first_char = word[0]
            if first_char in first_row:
                if len([char for char in word[1:] if char in first_row
                        ]) + 1 == len(word):
                    ables.append(word)
            elif first_char in second_row:
                if len([char for char in word[1:] if char in second_row
                        ]) + 1 == len(word):
                    ables.append(word)
            else:
                if len([char for char in word[1:] if char in third_row
                        ]) + 1 == len(word):
                    ables.append(word)
        return ables

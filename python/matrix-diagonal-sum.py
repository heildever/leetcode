from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        counter = 0
        length = len(mat)
        for idx in range(length):
            counter += mat[idx][idx]
            counter += mat[idx][length - idx - 1]

        if length % 2 == 1:
            return counter - mat[length // 2][length // 2]
        else:
            return counter

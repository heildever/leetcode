# question can be found on leetcode.com/problems/cells-with-odd-values-in-a-matrix/
from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows, columns = [0] * n, [0] * m
        for row, column in indices:
            rows[row] += 1
            columns[column] += 1

        return sum([(row + column) % 2 for row in rows for column in columns])

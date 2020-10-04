from Typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        num = 0
        for idx, point in enumerate(points[:-1]):
            num += max(abs(points[idx + 1][0] - point[0]),
                       abs(points[idx + 1][1] - point[1]))
        return num

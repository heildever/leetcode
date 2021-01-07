# question can be found on leetcode.com/problems/distance-between-bus-stops/
from Typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int,
                                destination: int) -> int:
        if destination > start:
            first, last = start, destination
        elif start > destination:
            first, last = destination, last

        cw = sum(distance[first:last])
        ccw = sum(distance[:last] + distance[first:])

        return min(cw, ccw)

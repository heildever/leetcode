# question can be found on leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
from Typing import List


class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        return len(
            [1 for st_i, et_i in zip(startTime, endTime) if (et_i >= queryTime >= st_i)]
        )

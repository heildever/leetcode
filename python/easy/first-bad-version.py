# question can be found at leetcode.com/problems/minimum-time-visiting-all-points/
# it's basically a fancy way of asking for a binary search algorithm
# actually, you prob can implement different searches too

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 0, n - 1
        while end >= start:
            mid = (end + start) // 2
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        return start

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter

        x1, x2 = Counter(nums1), Counter(nums2)

        xsec = x1 & x2
        res = []
        for key in xsec:
            res.extend([key for _ in range(xsec[key])])

        return res

        # or even better
        set1, set2 = Counter(nums1), Counter(nums2)
        common = set1 & set2
        return [num for num in common.elements()]

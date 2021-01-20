from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # First I did a 3 item sliding window based linear search
        #
        # peak_idx = 0
        # for idx in range(len(arr)-2):
        #     window = [arr[idx], arr[idx+1], arr[idx+2]]
        #     if max(window) == arr[idx+1]:
        #         peak_idx = idx+1
        #
        # return peak_idx
        #
        # But question kinda just ask index of max(arr)
        maks = max(arr)
        maks_idx = arr.index(maks)
        return maks_idx

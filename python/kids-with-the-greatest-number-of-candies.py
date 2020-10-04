from Typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int],
                        extraCandies: int) -> List[bool]:
        return [
            True if idx + extraCandies >= max(candies) else False
            for idx in candies
        ]

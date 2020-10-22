class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        if target > max(nums):
            return len(nums)
        elif min(nums) > target:
            return 0
        elif len(nums) == 1:
            return 1 if target > nums[0] else 0

        for idx, num in enumerate(nums[:-1]):
            if nums[idx + 1] > target > nums[idx]:
                return idx + 1

        # I found this very smart
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)

        # or even this
        return len([x for x in nums if x < target])

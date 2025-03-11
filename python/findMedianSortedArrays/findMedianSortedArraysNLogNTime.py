class Solution:
    # Time: O(log(n))
    # Space: O(1)
    def bisectLeft(self, nums: list[int], num: int):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)// 2
            if nums[mid] > num:
                right = mid
            else:
                left = mid + 1
        return left

    # Time: O(n*log(n))
    # Space: O(n+m)
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1

        # O(n)
        for i, num2 in enumerate(nums2):
            # O(log(n))
            j = self.bisectLeft(nums, num2)
            nums.insert(j, num2)

        mid = len(nums) // 2
        if len(nums) % 2 == 0:
            return (nums[mid - 1] + nums[mid])/2

        return nums[mid]

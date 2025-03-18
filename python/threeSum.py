# https://leetcode.com/problems/3sum/

# Sort nums
# Iterate i through nums, this is first number
# Use sliding window i and j to find the second and third number
# If sum == 0, shrink i and j
# If sum < 0, increase j
# If sum > 0, decrease k
# If the next values in our sliding window are the the same, skip them
# Shrink until j and k meets
# If the next values in our iteration i are the same, skip them

# [-1, 0, 1, 2, -1, -4]
# [-4, -1, -1, 0, 1, 2]
#   i
#       j
#                     k
# [-1,-1,2], [-1,0,1]

class Solution:
    # Time: O(n^2)
    # Space: O(n)
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result, seen = [], set()
        for i in range(n - 2):
            if nums[i] in seen: continue
            j = i + 1
            k = n - 1
            while j < k:
                num = nums[i] + nums[j] + nums[k]
                if num == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]: j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]: k -= 1
                elif num < 0: j += 1
                elif num > 0: k -= 1
            seen.add(nums[i])
        return result

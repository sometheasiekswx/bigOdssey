# https://leetcode.com/problems/trapping-rain-water

'''
- For every position, find longest left wall
- For every position, find longest right wall
- Each puddle of water = min(longest left wall, longest right wall) minus height of the puddle

   [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
   [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3] <- left wall
   [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0] <- right wall
   [0,0,1,0,1,2,1,0,0,1,0,0] <- result
'''
class Solution:
    # Time: O(n)
    # Space: O(n)
    def trap(self, height: list[int]) -> int:
        n = len(height)

        leftWalls = [0] * n
        leftLongest = 0
        for i, h in enumerate(height):
            leftLongest = max(leftLongest, h)
            leftWalls[i] = leftLongest

        rightWalls = [0] * n
        rightLongest = 0
        for i in range(n-1,-1,-1):
            rightLongest = max(rightLongest, height[i])
            rightWalls[i] = rightLongest

        result = 0
        for i in range(n):
            maxWaterHeight = min(leftWalls[i], rightWalls[i])
            total = maxWaterHeight - height[i]
            if total > 0:
                result += total

        return result

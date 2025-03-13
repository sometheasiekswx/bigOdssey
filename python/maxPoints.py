# Link: https://leetcode.com/problems/max-points-on-a-line

from collections import defaultdict

class Solution:
    # Time: O(n^2)
    # Space: O(1)
    def maxPoints(self, points: list[list[int]]) -> int:
        n, highestCount = len(points), 1
        if n < 3:
            return n
        # O(n)
        for i in range(n):
            slopes = defaultdict(lambda: 1)
            # O(n)
            for j in range(i+1,n):
                # slope = (y2 - y1) / (x2 - x1)
                y2, y1 = points[j][1], points[i][1]
                x2, x1 = points[j][0], points[i][0]
                numerator, donominator = y2 - y1, x2 - x1
                slope = 0
                if numerator == 0:
                    slope = "x" + str(y2)
                elif donominator == 0:
                    slope = "y" + str(x2)
                else:
                    slope = numerator/donominator
                slopes[slope] += 1
                highestCount = max(highestCount, slopes[slope])
        return highestCount

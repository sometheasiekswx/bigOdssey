'''
https://leetcode.com/problems/triangle

Use bottom-up dynamic programming to find minimum path sum:
1. Start from bottom row
2. For each number above current row:
   - Add it to the smaller of the two numbers below it
3. The top number will have the minimum total path sum

Example:

       2
     3   4
   6   5   7      
 4   1   8   3     

Bottom-up calculation:

[4   1   8   3]     -> Initial bottom row
  [7   6  10]       -> min(6+4,6+1), min(5+1,5+8), min(7+8,7+3)
    [9  14]         -> min(3+7,3+6), min(4+6,4+10)
     [11]           -> min(2+9,2+10)
'''
class Solution:
    # Time: O(len(triangle)^2)
    # Space: O(len(triangle[-1]))
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        previous = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            rowLength = i + 1
            current = [0] * rowLength
            for j in range(rowLength):
                current[j] = triangle[i][j] + min(previous[j], previous[j+1])
            previous = current
        return previous[0]
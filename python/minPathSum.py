from typing import List
from math import inf

'''
https://leetcode.com/problems/minimum-path-sum/

Dynamic Programming:
1. Start with a 1D array (dp) to track minimum path sums
2. Initialize dp with the bottom row
3. For each cell from bottom-right to top-left:
   - If in last column: only option is to go down
   - Otherwise: take minimum of going right or down
4. Final answer is in dp[0] representing minimum path from top-left to bottom-right
'''
class Solution:
    # Time: O(rows*cols)
    # Space: O(cols)
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = grid[-1].copy()
        for col in range(cols - 2, -1, -1):
            dp[col] += dp[col + 1]
        for row in range(rows - 2, -1, -1):
            dp[-1] += grid[row][-1]
            for col in range(cols - 2, -1, -1):
                dp[col] = grid[row][col] + min(dp[col], dp[col + 1])
        return dp[0]
    
    # Time: O(rows*cols)
    # Time: O(cols)
    def minPathSumMoreOptimized(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        previous = grid[-1]
        for col in range(cols - 2, -1, -1):
            previous[col] += previous[col + 1]

        down = (1,0)
        right = (0,1)
        directions = [down, right]
        for row in range(rows - 2, -1, -1):
            current = [inf] * cols
            for col in range(cols - 1, -1, -1):
                for addRow, addCol in directions:
                    newCol = col + addCol
                    if not 0 <= newCol < cols:
                        continue
                    newValue = (
                        grid[row][col] + previous[col] if addRow 
                        else grid[row][col] + current[newCol]
                    )
                    current[col] = (
                        newValue if current[col] == inf 
                        else min(current[col], newValue)
                    )
            previous = current
        return previous[0]

    # Time: O(rows*cols)
    # Time: O(cols)
    def minPathSumSpaceOptimized(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        previous = grid[-1]
        for col in range(cols - 2, -1, -1):
            previous[col] += previous[col + 1]

        down = (1,0)
        right = (0,1)
        directions = [down, right]
        for row in range(rows - 2, -1, -1):
            current = [inf] * cols
            for col in range(cols - 1, -1, -1):
                for addRow, addCol in directions:
                    newCol = col + addCol
                    if not 0 <= newCol < cols:
                        continue
                    newRow = row + addRow
                    if not 0 <= newRow < rows:
                        continue
                    if row == newRow:
                        current[col] = min(
                            current[col], 
                            grid[row][col] + current[newCol] 
                        )
                    else:
                        current[col] = min(
                            current[col], 
                            grid[row][col] + previous[col] 
                        )
            previous = current
        return previous[0]

    # Time: O(rows*cols)
    # Space: O(rows*cols)
    def minPathSumInitial(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        costs = [[inf] * cols for _ in range(rows)]
        costs[-1][-1] = grid[-1][-1]
        down = (1,0)
        right = (0,1)
        directions = [down, right]

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                for addRow, addCol in directions:
                    newRow = row + addRow
                    if not 0 <= newRow < rows:
                        continue
                    newCol = col + addCol
                    if not 0 <= newCol < cols:
                        continue
                    costs[row][col] = min(
                        costs[row][col], 
                        grid[row][col] + costs[newRow][newCol]
                    )
        return costs[0][0]
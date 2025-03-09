"""
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix?envType=problem-list-v2&envId=2wyykuvs
#
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# [
#   [1,1,2,],
#   [2,2,1,],
#   [3,4,1,]
# ]
#
# ---
#
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# [
#   [0,0,0,],
#   [0,0,0,],
#   [0,0,0,],
# ]
#
"""
class Solution:
    # Time: O(row * col)
    # Space: O(row * col)
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0]*cols for _ in range(rows)]
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        longestPath = 0

        def exploreCell(row: int, col: int) -> int:
            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]
                if not 0 <= newRow < rows or not 0 <= newCol < cols:
                    continue
                if matrix[newRow][newCol] <= matrix[row][col]:
                    continue
                if dp[newRow][newCol] > 0:
                    dp[row][col] = max(dp[row][col], 1 + dp[newRow][newCol])
                    continue

                dp[row][col] = max(dp[row][col], 1 + exploreCell(newRow,newCol))

            dp[row][col] = max(1, dp[row][col])
            return dp[row][col]

        for row in range(rows):
            for col in range(cols):
                longestPath = max(exploreCell(row, col), longestPath)

        return longestPath

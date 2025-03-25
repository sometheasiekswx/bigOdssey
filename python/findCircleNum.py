# https://leetcode.com/problems/number-of-provinces

"""
Visit every row, for every row visited
    - Increase province count
    - After first row
        - Only visit new rows not connected to existing rows
    - If row is connected to another row
        - Mark that row was visited
        - Go to that row and find more rows connected
"""

class Solution:
    # Time: O(rows*cols)
    # Space: O(rows)
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        rows, cols = len(isConnected), len(isConnected[0])
        rowVisited = [False] * rows
        provinceCount = 0

        def findAllConnected(row: int) -> None:
            for col in range(cols):
                if isConnected[row][col] == 0: continue
                if rowVisited[col]: continue
                rowVisited[col] = True
                findAllConnected(col)

        for row in range(rows):
            if rowVisited[row]: continue
            provinceCount += 1
            findAllConnected(row)

        return provinceCount

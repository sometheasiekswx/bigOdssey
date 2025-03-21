from copy import deepcopy

class Solution:
    # Time: O(minute*rows*cols)
    # Space: O(rows*cols)
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        minute, newGrid = 0, [[0]]
        rotCanSpread = containsFresh = True
        while rotCanSpread:
            containsFresh = rotCanSpread = False
            newGrid = deepcopy(grid)
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 1: containsFresh = True
                    if grid[row][col] != 2 or visited[row][col]: continue
                    visited[row][col] = True
                    for direction in directions:
                        newRow = row + direction[0]
                        newCol = col + direction[1]
                        if not (0 <= newRow < rows and 0 <= newCol < cols): continue
                        if grid[newRow][newCol] == 0 or grid[newRow][newCol] == 2: continue
                        newGrid[newRow][newCol] = 2
                        rotCanSpread = True
            grid = newGrid
            if rotCanSpread: minute += 1
        if containsFresh:
            return -1
        return minute

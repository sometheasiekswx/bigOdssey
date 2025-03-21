from collections import deque

class Solution:
    # Time: O(rows*cols)
    # Space: O(rows*cols)
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rotten, oranges = deque(), 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1: oranges += 1
                if grid[row][col] != 2: continue
                rotten.append((row, col))
        if not rotten and oranges: return -1
        if not rotten and not oranges: return 0

        minute = 0
        while rotten:
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                for direction in directions:
                    newRow = row + direction[0]
                    if not 0 <= newRow < rows: continue
                    newCol = col + direction[1]
                    if not 0 <= newCol < cols: continue
                    if grid[newRow][newCol] != 1: continue
                    grid[newRow][newCol] = 2
                    rotten.append((newRow, newCol))
                    oranges -= 1
            minute += 1
        if oranges:
            return -1
        return minute - 1

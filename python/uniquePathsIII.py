# https://leetcode.com/problems/unique-paths-iii/

from copy import deepcopy

# Time: O(4^n)
# Space: O(4^n*rows*cols)
class Solution:
    def __init__(self):
        self.grid = [[]]
        self.rows = 0
        self.cols = 0
        self.paths = 0
        self.directions = [(0,1), (0,-1), (1,0), (-1,0)]
        self.endRow = 0
        self.endCol = 0
        self.startRow = 0
        self.startCol = 0
        self.initialVisited = [[]]

    def allTrue(self, visited: list[list[int]]) -> bool:
        for row in range(self.rows):
            if not all(visited[row]):
                return False
        return True

    def findStartEndInitialVisited(self):
        self.initialVisited = [[False]*self.cols for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == 1:
                    self.startRow, self.startCol = row, col
                elif self.grid[row][col] == -1:
                    self.initialVisited[row][col] = True
                elif self.grid[row][col] == 2:
                    self.initialVisited[row][col] = True
                    self.endRow, self.endCol = row, col

    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        self.grid, self.rows, self.cols = grid, len(grid), len(grid[0])
        self.findStartEndInitialVisited()
        self.exploreAllPaths(self.startRow, self.startCol, self.initialVisited)
        return self.paths

    def exploreAllPaths(self, row, col, visited):
        visited[row][col] = True
        for addRow, addCol in self.directions:
            newRow = row + addRow
            if not 0 <= newRow < self.rows:
                continue
            newCol = col + addCol
            if not 0 <= newCol < self.cols:
                continue

            if newRow == self.endRow and newCol == self.endCol:
                if self.allTrue(visited):
                    self.paths += 1

            if visited[newRow][newCol]:
                continue

            self.exploreAllPaths(newRow, newCol, deepcopy(visited))

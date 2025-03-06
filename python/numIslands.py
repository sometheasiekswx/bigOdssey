# https://leetcode.com/problems/number-of-islands

class Solution:
    # Time: O(row*col)
    # Space: O(row*col)
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        islands = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        for row in range(rows):
            for col in range(cols):
                if visited[row][col]:
                    continue

                if grid[row][col] == "0":
                    visited[row][col] = True
                    continue

                toVisits = [(row, col)]
                while toVisits:
                    toVisit = toVisits.pop()
                    visited[toVisit[0]][toVisit[1]] = True
                    for direction in directions:
                        newRow = toVisit[0] + direction[0]
                        newCol = toVisit[1] + direction[1]

                        if not (0 <= newRow < rows and 0 <= newCol < cols):
                            continue
                        if visited[newRow][newCol]:
                            continue
                        if grid[newRow][newCol] != "1":
                            continue

                        toVisits.append((newRow, newCol))
                islands += 1

        return islands

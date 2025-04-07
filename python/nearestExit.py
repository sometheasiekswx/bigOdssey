# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze

from collections import deque

class Solution:
    '''
    BFS approach to find shortest path to exit:
    - Use queue to track moves, start from entrance
    - Mark that position as wall to avoid revisiting
    - For each position:
        - Skip if out of bounds or wall
        - Return steps if at border (exit found)
        - Mark as wall and add valid positions to queue
    
    Time: O(rows*cols)
    Space: O(rows*cols)
    '''
    def nearestExit(self, maze, entrance):
        rows, cols = len(maze), len(maze[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        maze[entrance[0]][entrance[1]] = '+'
        moves = deque([(entrance[0], entrance[1])])
        moveCount = 0
        while moves:
            moveCount += 1
            for _ in range(len(moves)):
                row, col = moves.popleft()
                for addRow, addCol in directions:
                    newRow = row + addRow
                    if not 0 <= newRow < rows:
                        continue
                    newCol = col + addCol
                    if not 0 <= newCol < cols:
                        continue
                    if maze[newRow][newCol] == "+":
                        continue
                    if newCol in [0, cols-1]:
                        return moveCount
                    if newRow in [0, rows-1]:
                        return moveCount
                    maze[newRow][newCol] = '+'
                    moves.append((newRow, newCol))
        return -1

    '''
    BFS approach to find shortest path to exit:
    - Use queue to track moves, start from entrance
    - Mark that position as visited
    - For each position:
        - Skip if out of bounds, wall, or visited
        - Return steps if at border (exit found)
        - Mark visited and add valid positions to queue
    - Return -1 if no exit found

    Time: O(rows*cols)
    Space: O(rows*cols)
    '''
    def nearestExitMoreSpace(self, maze, entrance):
        rows, cols = len(maze), len(maze[0])
        visited = [[False] * cols for _ in range(rows)]
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited[entrance[0]][entrance[1]] = True
        moves = deque([(entrance[0], entrance[1])])
        moveCount = 0
        while moves:
            moveCount += 1
            for _ in range(len(moves)):
                row, col = moves.popleft()
                for addRow, addCol in directions:
                    newRow = row + addRow
                    if not 0 <= newRow < rows:
                        continue
                    newCol = col + addCol
                    if not 0 <= newCol < cols:
                        continue
                    if maze[newRow][newCol] == "+":
                        continue
                    if visited[newRow][newCol]:
                        continue
                    if newCol in [0, cols-1]:
                        return moveCount
                    if newRow in [0, rows-1]:
                        return moveCount
                    visited[newRow][newCol] = True
                    moves.append((newRow, newCol))
        return -1

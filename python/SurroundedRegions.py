# https://leetcode.com/problems/surrounded-regions

# Add Os on edge to stack
# For each Os on edge, find Os connected
# Mark all of the connected Os as unchangable
# Change everything still changable to Xs

class Solution:
    # Time: O(rows*cols)
    # Space: O(rows*cols)
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        changeable = [[True] * cols for _ in range(rows)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        edgeOs = self.findEdgeOs(board, rows, cols)
        while edgeOs:
            row, col = edgeOs.pop()
            changeable[row][col] = False
            for addRow, addCol in directions:
                newRow = row + addRow
                newCol = col + addCol
                if not 0 <= newRow < rows: continue
                if not 0 <= newCol < cols: continue
                if board[newRow][newCol] != "O": continue
                if not changeable[newRow][newCol]: continue
                edgeOs.append((newRow, newCol))
        self.convertChangeablesToXs(board, rows, cols, changeable)

    def findEdgeOs(self, board: list[list[str]], rows: int, cols: int) -> list[tuple]:
        edgeOs = []
        for i in range(rows):
            leftRow, leftCol = left = (i, 0)
            rightRow, rightCol = right = (i, cols-1)
            if board[leftRow][leftCol] == "O": edgeOs.append(left)
            if board[rightRow][rightCol] == "O": edgeOs.append(right)
        for i in range(1,cols-1):
            topRow, topCol = top = (0,i)
            bottomRow, bottomCol = bottom = (rows-1, i)
            if board[topRow][topCol] == "O": edgeOs.append(top)
            if board[bottomRow][bottomCol] == "O": edgeOs.append(bottom)
        return edgeOs

    def convertChangeablesToXs(self, board: list[list[str]], rows: int, cols: int, changeable: list[list[bool]]):
        for row in range(rows):
            for col in range(cols):
                if not changeable[row][col]: continue
                if board[row][col] != "O": continue
                board[row][col] = "X"

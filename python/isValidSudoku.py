# https://leetcode.com/problems/valid-sudoku

class Solution:
    def __init__(self) -> None:
        self.board = [[str]]
        self.rows = 0
        self.cols = 0

    # Time: O(rows*cols)
    # Space: O(rows*cols)
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        self.board = board
        self.rows = len(self.board)
        self.cols = len(self.board[0])

        if not self.validRows():
            return False

        if not self.validCols():
            return False

        if not self.validSubBoxes():
            return False

        return True

    def validRows(self) -> bool:
        for row in range(self.rows):
            seen = set()
            for col in range(self.cols):
                num = self.board[row][col]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        return True

    def validCols(self) -> bool:
        for col in range(self.cols):
            seen = set()
            for row in range(self.rows):
                num = self.board[row][col]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        return True

    def validSubBoxes(self) -> bool:
        directions = [
            (-1,-1),(-1,0),(-1,1),
            (0,-1), (0,0), (0,1),
            (1,-1), (1,0), (1,1),
        ]
        for row in range(1, self.rows, 3):
            for col in range(1, self.cols, 3):
                seen = set()
                for addRow, addCol in directions:
                    newRow = row + addRow
                    newCol = col + addCol
                    num = self.board[newRow][newCol]
                    if num == '.':
                        continue
                    if num in seen:
                        return False
                    seen.add(num)
        return True

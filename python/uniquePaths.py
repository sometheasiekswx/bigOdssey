# https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def backtrack(row,col):
            if row==m-1 and col == n-2:
                return 1
            if row==m - 2 and col == n-1:
                return 1
            if row==m-1 and col==n-1:
                return 1

            if (row, col) in cache:
                return cache[(row,col)]

            goDown = 0
            if row+1 < m:
                goDown = backtrack(row+1,col)
                cache[(row+1, col)] = goDown

            goRight = 0
            if col+1 < n:
                goRight = backtrack(row, col+1)
                cache[(row, col+1)] = goRight

            return goDown + goRight

        return backtrack(0,0)

if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(10, 9))
    print(solution.uniquePaths(5,6))
    print(solution.uniquePaths(20,30))

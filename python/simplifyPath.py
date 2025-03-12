# Link: https://leetcode.com/problems/simplify-path?envType=study-plan-v2&envId=top-interview-150

from collections import deque

class Solution:
    # Time: O(n)
    # Space: O(n)
    def simplifyPath(self, path: str) -> str:
        paths = []
        pathsRaw = path.strip().split('/')
        for i in range(len(pathsRaw)):
            p = pathsRaw[i].strip()
            if p == ".." and paths:
                paths.pop()
                continue
            if p in [".", "", ".."]:
                continue
            paths.append(pathsRaw[i])

        if not paths:
            return "/"
        return "/" + "/".join(paths)

# https://leetcode.com/problems/merge-intervals

class Solution:
    # Time: O(n*log(n))
    # Space: O(n)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda item: (item[0], item[1]))
        n = len(intervals)
        first = intervals[0][0]
        last = intervals[0][1]
        mergedInterval = []
        for i in range(1, n):
            newFirst = intervals[i][0]
            if last < newFirst:
                mergedInterval.append([first, last])
                first = newFirst
            last = max(last, intervals[i][1])
        mergedInterval.append([first, last])
        return mergedInterval

    # Time: O(n*log(n))
    # Space: O(n)
    def mergeLessClean(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda item: (item[0], item[1]))
        n = len(intervals)
        first = intervals[0][0]
        last = intervals[0][1]
        mergedInterval = []
        for i in range(1, n):
            if last >= intervals[i][0]:
                last = max(last, intervals[i][1])
                continue
            mergedInterval.append([first, last])
            first = intervals[i][0]
            last = max(last, intervals[i][1])
        mergedInterval.append([first, last])
        return mergedInterval

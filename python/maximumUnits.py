# https://leetcode.com/problems/maximum-units-on-a-truck

class Solution:
    # Time: O(nlogn)
    # Space: O(1)
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda k: (-k[1], -k[0]))
        remains = truckSize
        maxUnits = 0
        for numOfBoxes, units in boxTypes:
            diff = remains - numOfBoxes
            if diff <= 0:
                maxUnits += remains * units
                break
            maxUnits += numOfBoxes * units
            remains = diff

        return maxUnits

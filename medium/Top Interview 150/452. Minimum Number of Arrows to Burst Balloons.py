from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrows = 1
        x = points[0][1]

        for i in range(len(points)):
            if points[i][0] > x:
                arrows += 1
                x = points[i][1]

        return arrows

class Solution:
    def timeToMinutes(self, data) -> int:
        hours, minutes = map(int, data.split(":"))
        return hours * 60 + minutes

    def findMinDifference(self, timePoints: list[str]) -> int:
        minutes_list = sorted([self.timeToMinutes(time) for time in timePoints])

        min_diff = float('inf')

        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i - 1])

        min_diff = min(min_diff, (minutes_list[0] + 1440) - minutes_list[-1])

        return min_diff

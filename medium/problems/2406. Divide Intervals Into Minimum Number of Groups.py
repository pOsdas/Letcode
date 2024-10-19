class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        events = []

        for start, end in intervals:
            events.append((start, 1))
            events.append((end + 1, -1))

        events.sort()

        max_active = 0
        current_active = 0

        for time, event in events:
            current_active += event
            max_active = max(max_active, current_active)

        return max_active

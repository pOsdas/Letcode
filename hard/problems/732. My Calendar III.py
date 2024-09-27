from collections import defaultdict


class MyCalendarThree:
    def __init__(self):
        self.timeline = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        self.timeline[startTime] += 1
        self.timeline[endTime] -= 1

        max_bookings = active_bookings = 0

        for time in sorted(self.timeline):
            active_bookings += self.timeline[time]
            max_bookings = max(max_bookings, active_bookings)

        return max_bookings

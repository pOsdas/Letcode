class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        for db_start, db_end in self.double_bookings:
            if (start < db_end) and (end > db_start):
                return False

        for even_start, even_end in self.bookings:
            if (start < even_end) and (end > even_start):
                overlap_str = max(start, even_start)
                overlap_end = min(end, even_end)
                self.double_bookings.append((overlap_str, overlap_end))

        self.bookings.append((start, end))
        return True

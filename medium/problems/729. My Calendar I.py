class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for even_start, even_end in self.bookings:
            if (start < even_end) and (end > even_start):
                return False

        self.bookings.append((start, end))
        return True

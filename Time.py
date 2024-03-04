class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.

        hour: int
        minute: int
        second: int or float
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Returns a string representation of the time."""
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.time_to_int() > other.time_to_int()

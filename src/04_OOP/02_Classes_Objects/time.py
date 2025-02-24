class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        if (
                0 <= hours <= Time.max_hours and
                0 <= minutes <= Time.max_minutes and
                0 <= seconds <= Time.max_seconds
        ):
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
        if self.minutes > Time.max_minutes:
            self.minutes = 0
            self.hours += 1
        if self.hours > Time.max_hours:
            self.hours = 0
        return self.get_time()

    def get_time(self):
        hour = str(self.hours) if self.hours > 9 else f"0{self.hours}"
        minute = str(self.minutes) if self.minutes > 9 else f"0{self.minutes}"
        second = str(self.seconds) if self.seconds > 9 else f"0{self.seconds}"
        return f"{hour}:{minute}:{second}"

time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())


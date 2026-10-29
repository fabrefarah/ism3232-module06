# my_tool.py
# Author: Farah Fabre


class AppointmentTool:
    """A tool that knows which appointment times are available."""

    def __init__(self, schedule):
        """Store the available appointment times."""
        self.schedule = schedule

    def find_day(self, text):
        """Find a weekday mentioned in the message."""
        text = text.lower()
        for day in self.schedule:
            if day.lower() in text:
                return day
        return None

    def times_for(self, day):
        """Return available times for a day, or None if unknown."""
        if day in self.schedule:
            return self.schedule[day]
        return None

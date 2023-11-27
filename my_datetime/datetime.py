# my_datetime/datetime.py
import datetime

class Datetime:
    def __init__(self, year=None, month=None, day=None, hour=0, minute=0, second=0):
        # Check for None values and use the current date and time if needed
        if year is None or month is None or day is None:
            self.date_time = datetime.datetime.now()
        else:
            self.date_time = datetime.datetime(year, month, day, hour, minute, second)

    @staticmethod
    def date_from_string(date_string):
        # Create a date object from a string
        return Datetime(*map(int, date_string.split('-')))

    @staticmethod
    def validate_date(day, month, year):
        # Validate whether a given set of date arguments forms a valid date
        try:
            datetime.datetime(year, month, day)
            return True
        except ValueError:
            return False

    @staticmethod
    def date_difference(date1, date2, unit='days'):
        # Calculate the difference between two dates
        delta = date2.date_time - date1.date_time
        if unit == 'days':
            return delta.days
        elif unit == 'weeks':
            return delta.days // 7
        elif unit == 'months':
            return date2.date_time.month - date1.date_time.month + 12 * (date2.date_time.year - date1.date_time.year)
        else:
            raise ValueError(f"Invalid unit: {unit}")

    def iso_format(self):
        # Display the datetime in ISO 8601 format
        return self.date_time.isoformat()

    def human_readable_format(self):
        # Display the datetime in a human-readable format
        return self.date_time.strftime("%A, %B %d, %Y %I:%M %p")

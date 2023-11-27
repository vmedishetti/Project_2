# tests/test_datetime.py
import pytest
from my_datetime.datetime import Datetime

def test_constructor_defaults():
    dt = Datetime()
    assert dt.date_time.year == datetime.datetime.now().year
    assert dt.date_time.month == datetime.datetime.now().month
    assert dt.date_time.day == datetime.datetime.now().day
    assert dt.date_time.hour == 0
    assert dt.date_time.minute == 0
    assert dt.date_time.second == 0

def test_iso_format():
    dt = Datetime(2023, 11, 26, 19, 3, 27)
    assert dt.iso_format() == '2023-11-26T19:03:27'

# Add more test assertions for other methods and properties as needed

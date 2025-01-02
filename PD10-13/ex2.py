import pandas as pd

df = pd.read_csv("gym2_q1.csv", sep=";", parse_dates=["date"])

""" Using the Pandas library and date/time functionality create a function 'solve(datestr, timezone)' to answer the following:
Given a date string (YYYYY-MM-DD HH:MM:SS) and a timezone, assume the date is in UTC and convert it to the given timezone. Return the new date.
"""


def solve(datestr, tz_str):
    from datetime import datetime, timedelta, timezone

    timezones = {
        "Pacific/Norfolk": 12 * 3600,
    }

    dt = datetime.strptime(datestr, "%Y-%m-%d %H:%M:%S")

    offset = timezones.get(tz_str, 0)
    new_dt = dt.replace(tzinfo=timezone.utc) + timedelta(seconds=offset)

    return new_dt.isoformat()


print(solve("2022-01-25 16:30:45", "Pacific/Norfolk"))

from calendar import Calendar

week_days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

week_values = (
    "last",
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
)


class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


def teenth(month, weeks, day_of_week):
    for week in weeks:
        date = week[day_of_week]
        if date.month == month and 12 < date.day < 20:
            return date

    raise MeetupDayException("That day does not exist.")


def nth(month, weeks, day_of_week, n):
    if len(weeks) < n:
        raise MeetupDayException("That day does not exist.")

    dates = [w[day_of_week] for w in weeks if w[day_of_week].month == month]

    try:
        return dates[n - 1]
    except IndexError:
        raise MeetupDayException("That day does not exist.")


def meetup(year, month, week, day_of_week):
    weeks = Calendar().monthdatescalendar(year, month)
    index = week_days.index(day_of_week)

    if week == "teenth":
        return teenth(month, weeks, index)
    else:
        n = week_values.index(week)
        return nth(month, weeks, index, n)

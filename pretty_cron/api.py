import datetime


_WEEKDAYS = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
}


def _ordinal(n):
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
        return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, "th")


def _human_week_day(day):
    return _WEEKDAYS.get(day)


def _human_month(month):
    return datetime.datetime(2014, month, 1).strftime("%B")


def _pretty_time(minute, hour):
    if minute != "*" and hour != "*":
        time = datetime.datetime(year=2014, month=1, day=1, hour=hour, minute=minute)
        pretty_time = "At {0}".format(time.strftime("%H:%M"))

    elif minute != "*" and hour == '*':
        pretty_time = "At {0} minutes past every hour of".format(minute)

    elif minute == "*" and hour != '*':
        start_time = datetime.datetime(year=2014, month=1, day=1, hour=hour)
        end_time = start_time + datetime.timedelta(minutes=59)

        pretty_time = "Every minute between {0} and {1}".format(
            start_time.strftime("%H:%M"),
            end_time.strftime("%H:%M"),
        )
    else:
        pretty_time = "Every minute of"

    return pretty_time


def _pretty_date(month_day, month, week_day):

    if month_day == "*" and week_day == "*":
        pretty_date = "every day"

        if month != '*':
            pretty_date += " in {0}".format(_human_month(month))
    else:
        month_day_date = "on the {0}".format(_ordinal(month_day)) if month_day != "*" else ""
        week_day_date = "every {0}".format(_human_week_day(week_day)) if week_day != "*" else ""

        if month_day_date:
            month_day_date += " of {0}".format(_human_month(month)) if month != "*" else " of every month"

        if week_day_date and month != "*":
            week_day_date = "on {0} in {1}".format(week_day_date, _human_month(month))

        pretty_date = " and ".join(c for c in [month_day_date, week_day_date] if c)

    return pretty_date


def prettify(expression):
    try:
        expression = map(lambda c: int(c) if c != "*" else c, expression.split(" "))
    except ValueError:
        # */2 and other cron expressions aren't supported yet
        return expression

    try:
        minute, hour, month_day, month, week_day = expression
    except ValueError:
        raise ValueError("Invalid cron expression")

    time = _pretty_time(minute, hour)
    date = _pretty_date(month_day, month, week_day)

    return " ".join(c for c in [time, date] if c)

# -*- coding: utf-8 -*-
import datetime


def prettify_cron(expression):
    """
    Converts the given string cron expression into a pretty, human-readable,
    English description of what it means. If the string is not a valid cron
    expression, or it includes features not currently supported, it is returned
    as-is.
    """
    pieces = []
    for i, piece in enumerate(expression.split(" ")):
        # support comma-separated values for ordinal days, weekdays and months
        if i in (2, 3, 4) and ',' in piece:
            try:
                piece = tuple(int(p) for p in piece.split(','))
            except ValueError:
                # non-integers in comma-separated list aren't supported yet -
                # return as-is
                return expression
        elif piece != '*':
            try:
                piece = int(piece)
            except ValueError:
                # */2 and other cron expressions aren't supported yet - return
                # as-is
                return expression
        pieces.append(piece)

    try:
        minute, hour, month_day, month, week_day = pieces
    except ValueError:
        # More or fewer pieces than expected - return as-is
        return expression

    date = _pretty_date(month_day, month, week_day)
    time = _pretty_time(minute, hour)

    return " ".join(
        filter(None, (time, date))
    )


def _pretty_date(month_day, month, week_day):
    if month_day == "*" and week_day == "*":
        pretty_date = "every day"

        if month != '*':
            pretty_date += " in {0}".format(_human_month(month))
    else:
        if month_day != "*":
            month_day_date = "on the {0}".format(_ordinal(month_day))
        else:
            month_day_date = ""

        if week_day != "*":
            week_day_date = "every {0}".format(_human_week_day(week_day))
        else:
            week_day_date = ""

        if month_day_date:
            if month != '*':
                month_day_date += " of {0}".format(_human_month(month))
            else:
                month_day_date += " of every month"

        if week_day_date and month != "*":
            week_day_date = "on {0} in {1}".format(
                week_day_date,
                _human_month(month)
            )

        pretty_date = " and ".join(
            filter(None, (month_day_date, week_day_date))
        )

    return pretty_date


def _human_month(month):
    if isinstance(month, tuple):
        months = month
    else:
        months = (month,)

    return _human_list([
        datetime.date(2014, m, 1).strftime('%B')
        for m in months
    ])


def _human_list(listy):
    """
    Combines a list of strings into a string representing the list in plain
    English, i.e.
    >>> _human_list(["a"])
    "a"
    >>> _human_list(["a", "b"])
    "a and b"
    >>> _human_list(["a", "b", "c"])
    "a, b and c"
    """
    if len(listy) == 1:
        return listy[0]

    rest, penultimate, ultimate = listy[:-2], listy[-2], listy[-1]
    if rest:
        return ", ".join(rest) + ", {} and {}".format(penultimate, ultimate)
    return "{} and {}".format(penultimate, ultimate)


_WEEKDAYS = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}


def _human_week_day(day):
    if isinstance(day, tuple):
        days = day
    else:
        days = (day,)

    return _human_list([_WEEKDAYS[d] for d in days])


_ORDINAL_SUFFIXES = {
    1: 'st',
    2: 'nd',
    3: 'rd'
}


def _ordinal(num):
    if isinstance(num, tuple):
        nums = num
    else:
        nums = (num,)

    ordinal_days = []
    for d in nums:
        if 10 <= (d % 100) < 20:
            suffix = 'th'
        else:
            suffix = _ORDINAL_SUFFIXES.get(d % 10, 'th')
        ordinal_days.append(str(d) + suffix)

    return _human_list(ordinal_days)


def _pretty_time(minute, hour):
    if minute != "*" and hour != "*":
        the_time = datetime.time(hour=hour, minute=minute)
        pretty_time = "At {0}".format(the_time.strftime("%H:%M"))

    elif minute != "*" and hour == '*':
        pretty_time = "At {0} minutes past every hour of".format(minute)

    elif minute == "*" and hour != '*':
        start_time = datetime.time(hour=hour)
        end_time = datetime.time(hour=hour, minute=59)

        pretty_time = "Every minute between {0} and {1}".format(
            start_time.strftime("%H:%M"),
            end_time.strftime("%H:%M"),
        )
    else:
        pretty_time = "Every minute of"

    return pretty_time

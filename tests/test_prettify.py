from pretty_cron import prettify_cron as pc


def test_yearly():
    assert pc("0 0 1 1 *") == "At 00:00 on the 1st of January"


def test_one_day_in_month():
    assert pc("0 0 1 * *") == "At 00:00 on the 1st of every month"


def test_one_day_in_month_2nd():
    assert pc("0 0 2 * *") == "At 00:00 on the 2nd of every month"


def test_one_day_in_month_11th():
    assert pc("0 0 11 * *") == "At 00:00 on the 11th of every month"


def test_one_day_in_month_21st():
    assert pc("0 0 21 * *") == "At 00:00 on the 21st of every month"


def test_every_day_in_month():
    assert pc("12 15 * 1 *") == "At 15:12 every day in January"


def test_every_day_in_months():
    assert (
        pc("12 15 * 1,12 *") ==
        "At 15:12 every day in January and December"
    )


def test_every_specific_day_in_month():
    assert pc("0 0 * 1 1") == "At 00:00 on every Monday in January"


def test_every_pair_of_days_in_month():
    assert (
        pc("0 0 * 1 1,2") ==
        "At 00:00 on every Monday and Tuesday in January"
    )


def test_every_three_days_in_month():
    assert (
        pc("0 0 * 1 1,2,3") ==
        "At 00:00 on every Monday, Tuesday and Wednesday in January"
    )


def test_every_specific_day_in_months():
    assert (
        pc("0 0 * 1,2 1") ==
        "At 00:00 on every Monday in January and February"
    )


def test_every_specific_day_in_months_and_then_more():
    assert (
        pc("0 0 * 1,2,4,5 1") ==
        "At 00:00 on every Monday in January, February, April and May"
    )


def test_every_multiple_days_in_multiple_months():
    assert (
        pc("0 0 * 1,2,4,5 1,2,3") ==
        "At 00:00 on every Monday, Tuesday and Wednesday "
        "in January, February, April and May"
    )


def test_weekly():
    assert pc("0 0 * * 0") == "At 00:00 every Sunday"


def test_day_7_is_sunday():
    assert pc("0 0 * * 7") == "At 00:00 every Sunday"


def test_monthly_and_weekly():
    assert (
        pc("0 0 1 * 1") ==
        "At 00:00 on the 1st of every month and every Monday"
    )


def test_every_specific_day_in_month_and_weekly():
    assert (
        pc("0 0 1 1 1") ==
        "At 00:00 on the 1st of January and on every Monday in January"
    )


def test_every_specific_day_in_months_and_weekly():
    assert (
        pc("0 0 1 1,2 1") ==
        "At 00:00 on the 1st of January and February and on every Monday "
        "in January and February"
    )


def test_every_pair_of_days_in_multiple_months_and_weekly():
    assert (
        pc("0 0 1,23 1,2 1") ==
        "At 00:00 on the 1st and 23rd of January and February and on "
        "every Monday in January and February"
    )


def test_every_pair_of_days_in_multiple_months_and_twice_weekly():
    assert (
        pc("0 0 1,23 1,2 1,4") ==
        "At 00:00 on the 1st and 23rd of January and February and on "
        "every Monday and Thursday in January and February"
    )


def test_every_pair_of_days_in_multiple_months_and_three_days_weekly():
    assert (
        pc("0 0 1,23 1,2 1,4,6") ==
        "At 00:00 on the 1st and 23rd of January and February and on "
        "every Monday, Thursday and Saturday in January and February"
    )


def test_every_multiple_days_in_multiple_months_and_weekly():
    assert (
        pc("0 0 1,2,3,4 1,2 1") ==
        "At 00:00 on the 1st, 2nd, 3rd and 4th of January and February "
        "and on every Monday in January and February"
    )


def test_every_specific_day_in_months_and_more_and_weekly():
    assert (
        pc("0 0 1 1,2,3 1") ==
        "At 00:00 on the 1st of January, February and March and on every "
        "Monday in January, February and March"
    )


def test_daily():
    assert pc("0 0 * * *") == "At 00:00 every day"


def test_hourly():
    assert pc("0 * * * *") == "At 0 minutes past every hour of every day"


def test_minutely():
    assert (
        pc("* 5 * * *") == "Every minute between 05:00 and 05:59 every day"
    )


def test_continuous():
    assert pc("* * * * *") == "Every minute of every day"


def test_unsupported():
    assert pc("* */6 * * *") == "* */6 * * *"


def test_invalid_unchanged():
    assert pc('* * * * * *') == '* * * * * *'


def test_nonsense_unchanged():
    assert pc('Lalalala') == 'Lalalala'

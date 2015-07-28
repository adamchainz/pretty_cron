import unittest

from pretty_cron import prettify_cron as pc


class PrettyCronTest(unittest.TestCase):
    def test_yearly(self):
        assert pc("0 0 1 1 *") == "At 00:00 on the 1st of January"

    def test_one_day_in_month(self):
        assert pc("0 0 1 * *") == "At 00:00 on the 1st of every month"

    def test_one_day_in_month_2nd(self):
        assert pc("0 0 2 * *") == "At 00:00 on the 2nd of every month"

    def test_one_day_in_month_11th(self):
        assert pc("0 0 11 * *") == "At 00:00 on the 11th of every month"

    def test_one_day_in_month_21st(self):
        assert pc("0 0 21 * *") == "At 00:00 on the 21st of every month"

    def test_every_day_in_month(self):
        assert pc("12 15 * 1 *") == "At 15:12 every day in January"

    def test_every_specific_day_in_month(self):
        assert pc("0 0 * 1 1") == "At 00:00 on every Monday in January"

    def test_weekly(self):
        assert pc("0 0 * * 0") == "At 00:00 every Sunday"

    def test_monthly_and_weekly(self):
        assert (
            pc("0 0 1 * 1") ==
            "At 00:00 on the 1st of every month and every Monday"
        )

    def test_every_specific_day_in_month_and_weekly(self):
        assert (
            pc("0 0 1 1 1") ==
            "At 00:00 on the 1st of January and on every Monday in January"
        )

    def test_daily(self):
        assert pc("0 0 * * *") == "At 00:00 every day"

    def test_hourly(self):
        assert pc("0 * * * *") == "At 0 minutes past every hour of every day"

    def test_minutely(self):
        assert (
            pc("* 5 * * *") == "Every minute between 05:00 and 05:59 every day"
        )

    def test_continuous(self):
        assert pc("* * * * *") == "Every minute of every day"

    def test_unsupported(self):
        assert pc("* */6 * * *") == "* */6 * * *"

    def test_invalid_unchanged(self):
        assert pc('* * * * * *') == '* * * * * *'

    def test_nonsense_unchanged(self):
        assert pc('Lalalala') == 'Lalalala'

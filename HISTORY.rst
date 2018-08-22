.. :changelog:

History
-------

Pending Release
---------------

* **Retired** in favour of cron_descriptor_. This project is no longer maintained.

.. _cron_descriptor: https://pypi.org/project/cron_descriptor/

1.1.0 (2018-08-19)
------------------

* Now always returns ``unicode`` on Python 2 for consistency.

1.0.2 (2016-05-03)
------------------

* Now supports expressions with multiple weekdays and ordinal days - thanks
  @jbondia.

1.0.1 (2016-02-09)
------------------

* Now interprets day 7 as Sunday as well as 0, like Linux crontab parsers -
  thanks @vetyy.
* Now supports expressions with multiple months separated by commas - thanks
  @MerreM.

1.0.0 (2015-07-28)
------------------

* First release on PyPI, featuring ``prettify_cron`` function.

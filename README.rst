===========
pretty-cron
===========

Converts crontab expressions to human-readable descriptions.

API
===

``prettify(cron_expression)``
-----------------------------

Converts the given string cron expression into a pretty, human-readable,
English description of what it means.

For example:

.. code-block:: python

    >>> import pretty_cron
    >>> pretty_cron.prettify("0 * * * *")
    "At 0 minutes past every hour of every day"
    >>> pretty_cron.prettify("0 0 1 1 *")
    "At 00:00 on the 1st of January"
    >>> pretty_cron.prettify("12 15 * 1 *")
    "At 15:12 every day in January"

To-do
-----

* Support languages other than English
* Support ``*/2`` style expressions.

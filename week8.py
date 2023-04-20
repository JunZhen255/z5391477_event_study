import datetime as dt

x = dt.datetime(2023, 12, 31, 9, 30, 33)

#   The `strftime` method
# ----------------------------------------------------------------------------

# | Directive | Meaning                                                       | Example                  |
# |-----------|---------------------------------------------------------------|--------------------------|
# | %a        | Weekday as locale's abbreviated name.                         | Sun, Mon,...             |
# | %A        | Weekday as locale's full name.                                | Sunday, Monday,...       |
# | %w        | Weekday as a decimal number (Sunday=0,Saturday=6)             | 0, 1,..., 6              |
# | %d        | Day of the month as a zero-padded decimal number.             | 01, 02, …, 31            |
# | %b        | Month as locale's abbreviated name.                           | Jan, Feb,..., Dec        |
# | %B        | Month as locale's full name.                                  | January, February,...    |
# | %m        | Month as a zero-padded decimal number.                        | 01, 02, …, 12            |
# | %y        | Year without century as a zero-padded decimal number.         | 00, 01,..., 99           |
# | %Y        | Year with century as a decimal number.                        | 0001, 1999, 2013, 2014   |
# | %H        | Hour (24-hour clock) as a zero-padded decimal number.         | 00, 01, …, 23            |
# | %I        | Hour (12-hour clock) as a zero-padded decimal number.         | 01, 02, …, 12            |
# | %p        | Locale's equivalent of either AM or PM.                       | AM, PM                   |
# | %M        | Minute as a zero-padded decimal number.                       | 00, 01, …, 59            |
# | %S        | Second as a zero-padded decimal number.                       | 00, 01, …, 59            |
# | %j        | Day of the year as a zero-padded decimal number.              | 001, 002, …, 366         |
# | %U        | Week number of the year (Sunday as the first day of the week) | 00, 01, …, 53            |
# | %W        | Week number of the year (Monday as the first day of the week) | 00, 01, …, 53            |
# | %c        | Locale's appropriate date and time representation.            | Tue Aug 16 21:30:00 1988 |

s = x.strftime('%A of week number %U of the year %Y ')
print(s)



# You should not import any other module
import datetime as dt


def time_it(func, parms):
    """ Returns the number of microseconds it took to execute a function.

    Parameters
    ----------
    func : any function

    parms : dict
        A dictionary with the parameters that will be passed to the function.
        For instance, if `parms` is {'parm1': 1}, then the function call will be
        `func(parm1=1)`

    Returns
    -------
    int
        The number of microseconds it took to execute `func` with the parameters `parms`.

    Example
    -------

    Suppose there is a function called `my_func` that takes a single parameter called `parm1`.

        >> res = time_it(my_func, {'parm1': 3})
        >> print(res)
        >> 8010000

    In the example above, we are assuming it took 8010000 microseconds to execute
    the function `my_func(parm1=3)`.

    Note
    ----
    - You should not use the `time` module inside this function
      (meaning, do not use `import time` inside this function)

    """
    start = dt.datetime.now().microsecond
    func(**parms)
    end = dt.datetime.now().microsecond
    duration = end - start
    return duration


def _test_time_it():
    """ This function uses the time.sleep to test the function time_it.
    The output of this function should be:

        It took about 5000000 microseconds to execute this function.

    NOTE
    ----
    - The number of microsecs in the output will almost certainly be different
      when you run this function due to server latency.

    """
    import time
    def _my_func(secs):
        time.sleep(secs)

    res = time_it(_my_func, {'secs': 5})
    print(f"It took about {res} microseconds to execute this function.")


if __name__ == "__main__":
    pass
    _test_time_it()

import pandas as pd
import numpy as np

s = pd.Series([1, 2, np.nan, 4])

result = s.dropna()

print(result)
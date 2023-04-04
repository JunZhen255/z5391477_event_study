""" main.py
Code challenge
"""

import numpy as np
import pandas as pd
import yfinance as yf # Uncomment this line if you are wish to work with `yfinance` outside of Ed

# Write this function
def fx_code(from_cur, to_cur):
    """ Creates a string with the ticker required to download exchange rates
    using yfinance. The exchange rate will be the price of one unit of the `from_cur` in terms
    of the `to_cur`.

    Parameters
    ----------
    from_cur : str
        The ISO code of the currency to be priced.

    to_cur : str
        The ISO code of the currency with the value of one unit of `from_cur`.


    Returns
    -------
        A string that meets the `yfinance` ticker standards with ALL characters in upper case.
        The function should also be able to ignore leading and trailing spaces. For example,
        " aud", "Aud ", and " AUD " all are treated as "AUD" internally. See the
        Notes section below for more information.

    Notes
    -----
    Yahoo finance uses the following naming rules to define the ticker of the
    exchange rate AAA/BBB:
    usd/aud

    1. If AAA is the USD, then the ticker is "BBB=X", i.e., the second currency
       code with "=X" added at the end.
    2. If AAA is not the USD, then the ticker is "AAABBB=X"

    For example, the ticker for AUD/USD is "AUDUSD=X", while the ticker for
    USD/AUD is "AUD=X"

    So, if `from_cur=AAA` and the `to_cur=BBB`, the YF ticker will be:
    1. "BBB=X" if AAA is USD
    2. "AAABBB=X" if AAA is not the USD
    """
    from_cur= from_cur.upper().strip()
    to_cur = to_cur.upper().strip()
    ticker = f'{from_cur}{to_cur}=X'
    print(ticker)
    return ticker

# get_fx is provided to demonstrate how you can download currency data from `yfinance`.
# Once your fx_code function above is correct, get_fx should work on a computer
# that has the `yfinance` package installed.
def get_fx(from_cur, to_cur, period=None, interval=None):
    """ Downloads the exchange rate between the `from_cur` and the `to_cur`.
    The exchange rate will be the price of one unit of the `from_cur` in terms
    of the `to_cur`

    Parameters
    ----------
    from_cur : str
        The ISO code of the currency to be priced

    to_cur : str
        The ISO code of the currency with the value of one unit of
        `from_cur`.

    period : str, None
        valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
        (optional, default is '1mo')

    interval : str, None
        valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
        (optional, default is '1d')

    Returns
    -------
    df
        Dataframe with daily exchange rates from Yahoo Finance

    """
    # Defaults
    if period is None:
        period = '1mo'
    if interval is None:
        interval = '1d'

    tic = fx_code(from_cur, to_cur)

    # fetches the data
    df = yf.download(tic, period=period, interval=interval)

    return df


get_fx('USD', 'AUD', period=None, interval=None)




import pandas as pd
import numpy as np
aud_usd_lst = [
    ('2020-09-08', 0.7280),
    ('2020-09-09', 0.7209),
    ('2020-09-11', 0.7263),
    ('2020-09-14', 0.7281),
    ('2020-09-15', 0.7285),
    ]

eur_aud_lst = [
    ('2020-09-08',  1.6232),
    ('2020-09-09',  1.6321),
    ('2020-09-10',  1.6221),
    ('2020-09-11',  1.6282),
    ('2020-09-15',  1.6288),
    ]

# Replace unanswered with your solution.
aud_usd_series = pd.Series(dict(aud_usd_lst))
eur_aud_series = pd.Series(dict(eur_aud_lst))
df = pd.DataFrame({'aud:usd': aud_usd_series, 'eur:aud': eur_aud_series})
print(df)

import pandas as pd
import numpy as np

# Write this function
def mk_df(date_info, aud_usd_info, eur_aud_info):
    """ Combines the information from different sources to produce a dataframe
    with dates row labels. Row labels must be sorted

    Parameters
    ----------
    date_info : list
        date_info = [(row_id, date)]

    aud_usd_info : list
        aud_usd_info = [(row_id, aud/usd)]


    eur_aud_info : list
        eur_aud_info = [(row_id, eur/aud)]

    Returns
    -------
    df
    """
    import pandas as pd
    import numpy as np

    # Write this function
    def mk_df(date_info, aud_usd_info, eur_aud_info):
        """ Combines the information from different sources to produce a dataframe
        with dates row labels. Row labels must be sorted

        Parameters
        ----------
        date_info : list
            date_info = [(row_id, date)]

        aud_usd_info : list
            aud_usd_info = [(row_id, aud/usd)]


        eur_aud_info : list
            eur_aud_info = [(row_id, eur/aud)]

        Returns
        -------
        df
        """
        date_info_dict = dict(date_info)
        aud_usd_info_dict = dict(aud_usd_info)
        eur_aud_info_dict = dict(eur_aud_info)

        df = pd.dataframe(index=date_info_dict.keys())
        df.colums = ({'AUD/USD': aud_usd_info_dict, 'EUR/AUD': eur_aud_info_dict})

        pass


# Sample data for you to develop your function
# date_info = [(row_id, date)]
date_info = [
    (11 , '2020-09-08'),
    (70 , '2020-09-09'),
    (99 , '2020-09-10'),
    (4  , '2020-09-11'),
    (7  , '2020-09-14'),
    (100, '2020-09-15'),
    ]

# aud_usd_info = [(row_id, aud/usd)]
aud_usd_info = [
    (70 ,  0.7209),
    (4  ,  0.7263),
    (11 ,  0.7280),
    (7  ,  0.7281),
    (100,  0.7285),
]


# eur_aud_info = [(row_id, eur/aud)]
eur_aud_info = [
    (70 ,  1.6321),
    (4  ,  1.6282),
    (99 ,  1.6221),
    (100,  1.6288),
    (11 ,  1.6232),
    ]

df = mk_df(date_info, aud_usd_info, eur_aud_info)
print(df)

import tk_utils
help(tk_utils)

tk_utils.backup()

tk_utils.sync_dbox()

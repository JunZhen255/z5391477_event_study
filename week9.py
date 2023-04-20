import pandas as pd
df = pd.DataFrame({'col1': range(10),'col2': range(10,20)})
print(df)

cond = (df.loc[:,'col2'] % 3 == 0) | (df.loc[:,'col2'] % 2 == 0)
df.loc[cond,'col2'] = -1
print(df)


nba_stats = pd.DataFrame({'team': ['lakers', 'lakers', 'nets', 'nets', '76ers', '76ers'],
'player': ['lebron', 'davis', 'kyrie', 'durant', 'harden', 'embiid'],
'ppg': [30, 20, 29, 16, 26, 28]})

print(nba_stats)

#What is the highest points per game (ppg) scored by a player from each team?
print(nba_stats.groupby('team').max())

import pandas as pd


data = {'type': ['x', 'x', 'y'],
        'A': [1, 0, 1],
        'B': [0, 0, 0],
        'C': [1, 1, 1]}

df = pd.DataFrame(data)

print(df)

def mean_by_type(df):
        groups = df.groupby('type')
        means = groups.mean()
        print(means)
        return means

mean_by_type(df)

""" main.py

"""

import pandas as pd



def last_by_type_v0(df):
        """ Returns a data frame with the last "row" of DF for each unique
        value of the column "type".

        The last row is defined as the row with the largest index value
        (if DatetimeIndex, the row with the most recent index value).

        Parameters
        ----------
        data frame:
            ANY data frame with at least two columns. One of the columns must
            be called "type". The dtype of the column "type" can be anything.
            The dtype of the other columns must be a numeric type. This data frame
            must not include any NaN.

            You can assume that the `df` data frame will meet the description
            above. There is no need to check for that. For instance, there is not
            need to check that the `df` data frame includes at least two columns,
            or that one of them is called "type", or that it does not include any
            NaN.

        Returns
        -------
        data frame
            Columns: Same columns as df (INCLUDING "type").
                     The order of the columns does not matter

            Index: Unique values of the column "type"

        Example
        -------
        If the data frame is

                type  A  B  C
            idx
            0      x  1  0  1
            1      x  0  0  1
            2      y  1  0  1

        This function will return the following data frame:

                  A  B  C type
            type
            x     0  0  1    x
            y     1  0  1    y

        Note: The order of the columns does not matter

        """
        groups = df.groupby('type')
        new_df = pd.DataFrame(groups)
        return new_df


# ----------------------------------------------------------------------------
#   Please do not modify this function
# ----------------------------------------------------------------------------
def _mk_test_df():
        """ Creates a testing data frame


        Notes
        -----

        Given this example data frame a valid output for
        last_by_type_v0(df) is

                         A         B         C  type
            type
            1     3.252369  6.498818  0.802957     1
            2     6.470209  9.675518  8.548817     2

        """
        cnts = """
    date      , type,        A,        B,        C
    2020-01-05,    1, 3.319464, 8.629389, 3.133565
    2020-01-07,    2, 6.421113, 2.182970, 7.779123
    2020-01-07,    1, 1.954982, 2.868030, 4.212673
    2020-01-04,    1, 7.810074, 0.798035, 1.118955
    2020-01-05,    2, 5.606010, 7.690301, 0.688441
    2020-01-06,    2, 6.754960, 7.971680, 0.152985
    2020-01-09,    1, 3.252369, 6.498818, 0.802957
    2020-01-08,    1, 0.130774, 6.271210, 9.657531
    2020-01-09,    2, 6.470209, 9.675518, 8.548817
    2020-01-07,    1, 0.691137, 7.830912, 7.055062
    """
        fcsv = utils.fake_csv_file(cnts)
        df = pd.read_csv(fcsv, parse_dates=['date'], index_col='date')
        return df


if __name__ == "__main__":
        df = _mk_test_df()
        utils.pprint(df, df_info=False)

        res = last_by_type_v0(df)
        utils.pprint(res, df_info=False)

""" main.py

"""

import pandas as pd

import utils


def last_by_type_v0(df):
        """ Returns a data frame with the last "row" of DF for each unique
        value of the column "type".

        The last row is defined as the row with the largest index value
        (if DatetimeIndex, the row with the most recent index value).

        Parameters
        ----------
        data frame:
            ANY data frame with at least two columns. One of the columns must
            be called "type". The dtype of the column "type" can be anything.
            The dtype of the other columns must be a numeric type. This data frame
            must not include any NaN.

            You can assume that the `df` data frame will meet the description
            above. There is no need to check for that. For instance, there is not
            need to check that the `df` data frame includes at least two columns,
            or that one of them is called "type", or that it does not include any
            NaN.

        Returns
        -------
        data frame
            Columns: Same columns as df (INCLUDING "type").
                     The order of the columns does not matter

            Index: Unique values of the column "type"

        Example
        -------
        If the data frame is

                type  A  B  C
            idx
            0      x  1  0  1
            1      x  0  0  1
            2      y  1  0  1

        This function will return the following data frame:

                  A  B  C type
            type
            x     0  0  1    x
            y     1  0  1    y

        Note: The order of the columns does not matter

        """
        groups = df.sort_index().groupby('type').last()
        groups['type'] = groups.index
        return groups


# ----------------------------------------------------------------------------
#   Please do not modify this function
# ----------------------------------------------------------------------------
def _mk_test_df():
        """ Creates a testing data frame


        Notes
        -----

        Given this example data frame a valid output for
        last_by_type_v0(df) is

                         A         B         C  type
            type
            1     3.252369  6.498818  0.802957     1
            2     6.470209  9.675518  8.548817     2

        """
        cnts = """
    date      , type,        A,        B,        C
    2020-01-05,    1, 3.319464, 8.629389, 3.133565
    2020-01-07,    2, 6.421113, 2.182970, 7.779123
    2020-01-07,    1, 1.954982, 2.868030, 4.212673
    2020-01-04,    1, 7.810074, 0.798035, 1.118955
    2020-01-05,    2, 5.606010, 7.690301, 0.688441
    2020-01-06,    2, 6.754960, 7.971680, 0.152985
    2020-01-09,    1, 3.252369, 6.498818, 0.802957
    2020-01-08,    1, 0.130774, 6.271210, 9.657531
    2020-01-09,    2, 6.470209, 9.675518, 8.548817
    2020-01-07,    1, 0.691137, 7.830912, 7.055062
    """
        fcsv = utils.fake_csv_file(cnts)
        df = pd.read_csv(fcsv, parse_dates=['date'], index_col='date')
        return df


if __name__ == "__main__":
        df = _mk_test_df()
        utils.pprint(df, df_info=False)

        res = last_by_type_v0(df)
        utils.pprint(res, df_info=False)

""" main.py


"""

import pandas as pd

import utils


def fuzzy_colnames(df):
        """ Renames the columns in `df` according to the following criteria (in
        this order):

        For each column label:

            1. Reverse the string (e.g., column "ABC" becomes "CBA").

            2. If the column label includes the (upper case) letter "B", we have
            two cases:

                a. If the (lower case) letter "b" is NOT in the column name,
                reverse the case of any occurrence of "B" (so each upper case "B"
                will become lower case "b").

                b. If the column name also includes the (lower case) letter "b", do
                nothing.

                For example:

                - "CBA" becomes "CbA"
                - "ZbB" does not change (because name includes a lower case "b')
                - "BBa" becomes "bba"
                - "ZZZ" does not change


        Parameters
        ----------
        df : data frame
            Any data frame with strings column labels.

            You can assume that the data frame `df` will only include strings as
            column labels. There is no need to check for that.


        Returns
        -------
        data frame:
            A data frame with column labels renamed according to the criteria
            above. The order of the columns does not matter.


        Example
        -------

        If the data frame `df` is:

                 ABC  Xxb  zy  Bxb
            idx
            0      1    0  10   20
            1      0    0  11   21
            2      1    0  12   22

        This function will return the following data frame:

                 CbA  bxX  yz  bxB
            idx
            0      1    0  10   20
            1      0    0  11   21
            2      1    0  12   22

        Note: The order of the columns does not matter

        """
        cols = df.columns.tolist()
        for i, col in enumerate(cols):
                col_reversed = col[::-1]
                if "B" in col and "b" not in col:
                        col_reversed = col_reversed.replace("B", "b")
                cols[i] = col_reversed
                df.columns = cols
        return df


# ----------------------------------------------------------------------------
#   Please do not modify this function
# ----------------------------------------------------------------------------
def _mk_test_df():
        """ Creates a testing data frame

                 ABC  Xxb  zy  Bxb
            idx
            0      1    0  10   20
            1      0    0  11   21
            2      1    0  12   22

        Notes
        -----

        For this example df, a valid output for `fuzzy_colnames(df)` is


                 CbA  bxX  yz  bxB
            idx
            0      1    0  10   20
            1      0    0  11   21
            2      1    0  12   22

        """
        cnts = """
    idx , ABC, Xxb, zy, Bxb
    0   , 1  , 0  , 10, 20
    1   , 0  , 0  , 11, 21
    2   , 1  , 0  , 12, 22
    """
        fcsv = utils.fake_csv_file(cnts)
        df = pd.read_csv(fcsv, index_col='idx')
        return df


if __name__ == "__main__":
        df = _mk_test_df()
        utils.pprint(df, df_info=False)

        res = fuzzy_colnames(df)
        utils.pprint(res, df_info=False)

""" main.py


"""

import pandas as pd

import utils


def fuzzy_values(df):
        """ Replaces the values in THE FIRST column of the data frame `df` according to
        the following criteria (IN THIS ORDER):

        For each value in the FIRST column of `df` perform the following
        operations (in this order):

        1. If the value is a number between 0 and 0.5 (so 0 <= value <= 0.5),
        replace this value with the sum of the values of all columns in this row.

        2. If the value is between 1.0 and 2.0 (so 1.0 <= value <= 2.0), replace
        this value with -99.

        Important: The order matters! For instance, if in part 1. the original
        value is 0.1 and the sum of all columns (in that row) is 1.5, this value
        will be then replaced by -99 in part 2.


        Parameters
        ----------
        df : data frame
            Any data frame including only numeric data types (and no NaN). This
            data frame must include at least two columns.

            You can assume that the `df` data frame will meet the description
            above. There is no need to check for that. For instance, there is no
            need to check that the `df` data frame includes at least two columns,
            or that it does not include any NaN.

        Returns
        -------
        data frame:
            A data frame with values renamed according to the criteria
            above.

            Columns: The same columns as df.columns (in the same order)

            Index: The same index as df.index (in the same order)


        Example
        -------

        If the data frame `df` is:

                    A      B
            idx
            0     0.4    1.0
            1     0.0    0.5
            2    10.0    0.0
            3     1.5 -100.0
            4     0.1    0.1
            5     0.5  -10.0


        This function will return the following data frame:

                    A      B
            idx
            0   -99.0    1.0
            1     0.5    0.5
            2    10.0    0.0
            3   -99.0 -100.0
            4     0.2    0.1
            5    -9.5  -10.0


        """
        for idex, row in df.iterrows():
                if df.iloc[idex, 0] >= 0 and df.iloc[idex, 0] <= 0.5:
                        df.iloc[idex, 0] = df.iloc[idex].sum()
                        if df.iloc[idex, 0] >= 1.0 and df.iloc[idex, 0] <= 2.0:
                                df.iloc[idex, 0] = -99
                elif df.iloc[idex, 0] >= 1.0 and df.iloc[idex, 0] <= 2.0:
                        df.iloc[idex, 0] = -99
        return df


# ----------------------------------------------------------------------------
#   Please do not modify this function
# ----------------------------------------------------------------------------
def _mk_test_df():
        """ Creates a testing data frame

                    A      B
            idx
            0     0.4    1.0
            1     0.0    0.5
            2    10.0    0.0
            3     1.5 -100.0
            4     0.1    0.1
            5     0.5  -10.0

        Notes
        -----

        For this example df, a valid output for `fuzzy_values(df)` is

                    A      B
            idx
            0   -99.0    1.0
            1     0.5    0.5
            2    10.0    0.0
            3   -99.0 -100.0
            4     0.2    0.1
            5    -9.5  -10.0



        """
        cnts = """
    idx , A   , B
    0   , 0.4 , 1
    1   , 0   , 0.5
    2   , 10  , 0
    3   , 1.5 , -100
    4   , 0.1 , 0.1
    5   , 0.5 , -10
    """
        fcsv = utils.fake_csv_file(cnts)
        df = pd.read_csv(fcsv, index_col='idx')
        return df


if __name__ == "__main__":
        df = _mk_test_df()
        utils.pprint(df, df_info=False)

        res = fuzzy_values(df)
        utils.pprint(res, df_info=False)

""" main.py


"""

import pandas as pd

import utils


def last_by_type_v1(df):
        """ Returns a data frame with the last "row" of DF for each unique
        value of the column "type" AND a column called "org_index" with the value
        of the index in the original data frame associated with this row.

        The last row is defined as the row with the largest index value within
        each group (if DatetimeIndex, the row with the most recent index value).

        Parameters
        ----------
        data frame:
            ANY data frame with at least two columns. One of the columns must
            be called "type". The dtype of the column "type" can be anything.
            The dtype of the other columns must be a numeric type.

            You can assume that the `df` data frame will meet the description
            above. There is no need to check for that. For instance, there is not
            need to check that the `df` data frame includes at least two columns,
            or that one of them is called "type", or that it does not include any
            NaN.

        Returns
        -------
        data frame

            Columns: All the columns of `df` (INCLUDING "type") plus the
            "org_index" column described above (the order of the columns does not
            matter)

            Index: Unique values of the column "type"

        Example
        -------
        If the data frame is

                type  A  B  C
            idx
            0      x  1  0  1
            1      x  0  0  1
            2      y  1  0  1

        This function will return:

                 type  A  B  C org_index
            type
            x       x  0  0  1         1
            y       y  1  0  1         2


        Note: The order of the columns does not matter

        """
        groups = df.sort_index().groupby('type').last()
        groups["type"] = groups.index
        groups['org_index'] = df.index.max()
        return groups


# ----------------------------------------------------------------------------
#   Please do not modify this function
# ----------------------------------------------------------------------------
def _mk_test_df():
        """ Creates a testing data frame

        Notes
        -----

        Given this example data frame a valid output for
        last_by_type_v1(df) is

              type         A         B         C  type  org_index
        type
        1        1  3.252369  6.498818  0.802957     1 2020-01-09
        2        2  6.470209  9.675518  8.548817     2 2020-01-09


        """
        cnts = """
    date      , type,        A,        B,        C
    2020-01-05,    1, 3.319464, 8.629389, 3.133565
    2020-01-07,    2, 6.421113, 2.182970, 7.779123
    2020-01-07,    1, 1.954982, 2.868030, 4.212673
    2020-01-04,    1, 7.810074, 0.798035, 1.118955
    2020-01-05,    2, 5.606010, 7.690301, 0.688441
    2020-01-06,    2, 6.754960, 7.971680, 0.152985
    2020-01-09,    1, 3.252369, 6.498818, 0.802957
    2020-01-08,    1, 0.130774, 6.271210, 9.657531
    2020-01-09,    2, 6.470209, 9.675518, 8.548817
    2020-01-07,    1, 0.691137, 7.830912, 7.055062
    """
        fcsv = utils.fake_csv_file(cnts)
        df = pd.read_csv(fcsv, parse_dates=['date'], index_col='date')
        return df


if __name__ == "__main__":
        df = _mk_test_df()
        utils.pprint(df, df_info=False)

        res = last_by_type_v1(df)
        utils.pprint(res, df_info=False)




























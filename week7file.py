import pandas as pd

df = pd.DataFrame({'col1': range(10), 'col2': range(10, 20)}, index=list('acgfhibdje'))
print(df)

df2 = df.copy()
df2.sort_index(inplace=True)
x = df2.loc[['b','c','d','e'], 'col1']
print(x)

import pandas as pd
df = pd.DataFrame({'col1': range(10), 'col2': range(10, 20)}, index=list('acgfhibdje'))
print(df)
df.sort_index(inplace=True)
x = df.loc[['b','d','f','j'],['col1']]
print(x)


import pandas as pd
import numpy as np

data = {
    'AUD/USD': [ 0.7280, 0.7209, np.nan, 0.7263, 0.7281, 0.7285,],
    'EUR/AUD': [ 1.6232, 1.6321, 1.6221, 1.6282, np.nan, 1.6288,],
    }
index = [ '2020-09-08', '2020-09-09', '2020-09-10', '2020-09-11', '2020-09-14', '2020-09-15',]
df = pd.DataFrame(data, index)

x = df.loc['a':'z']
print(x)

y = df.loc['0':'z']
print(y)

new_df = df.copy()
new_df.loc['1', :] = 1
z = new_df.loc['1', 'z']
print(z)

a= df.iloc[100:1000]
print(a)

b= df.loc[:, 'AUD/USD']
print(b)

c= df.loc['AUD/USD']
print(c)

x=0
if [False]:
    x=x+1

print(x)



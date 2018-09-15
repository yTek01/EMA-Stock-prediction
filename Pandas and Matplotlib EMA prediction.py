import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#%matplotlib inline
import seaborn as sns
#sns.set(style='darkgrid', context='talk', palette='Dark2')

#my_year_month_fmt = mdates.DateFormatter('%m/%y')

df = pd.read_csv('C:\\Users\\OLASEHINDE\\Desktop\\My Project Files\\My Project Doc\\GTB_new_StockData.csv')
#print(data.head(10).dtypes)
df.columns =df.columns.to_series().apply(lambda x: x.strip())
df['Add'] = df['Open'] + df['High']
print(df.head())
df_close = pd.DataFrame(df.Close)
#df['Open'].plot()
#plt.show()
# Calculating the short-window simple moving average
short_rolling = df.rolling(window=20).mean()
print(short_rolling.head(20))

# Calculating the long-window simple moving average
#long_rolling = df.rolling(window=100).mean()
#long_rolling.tail()


#start_date = '2015-01-01'
#end_date = '2016-12-31'

#fig, ax = plt.subplots(figsize=(16,9))

#ax.plot(data.loc[start_date:end_date, :].index, data.loc[start_date:end_date, 'MSFT'], label='Price')
#ax.plot(long_rolling.loc[start_date:end_date, :].index, long_rolling.loc[start_date:end_date, 'MSFT'], label = '100-days SMA')
#ax.plot(short_rolling.loc[start_date:end_date, :].index, short_rolling.loc[start_date:end_date, 'MSFT'], label = '20-days SMA')

#ax.legend(loc='best')
#ax.set_ylabel('Price in $')

#ax.xaxis.set_major_formatter(my_year_month_fmt)

# Using Pandas to calculate a 20-days span EMA. adjust=False specifies that we are interested in the recursive calculation mode.
#ema_short = data.ewm(span=20, adjust=False).mean()

#fig, ax = plt.subplots(figsize=(15,9))

#ax.plot(data.loc[start_date:end_date, :].index, data.loc[start_date:end_date, 'MSFT'], label='Price')
#ax.plot(ema_short.loc[start_date:end_date, :].index, ema_short.loc[start_date:end_date, 'MSFT'], label = 'Span 20-days EMA')
#ax.plot(short_rolling.loc[start_date:end_date, :].index, short_rolling.loc[start_date:end_date, 'MSFT'], label = '20-days SMA')

#ax.legend(loc='best')
#ax.set_ylabel('Price in $')
#ax.xaxis.set_major_formatter(my_year_month_fmt)








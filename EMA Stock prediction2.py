import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\OLASEHINDE\\Desktop\\My Project Files\\My Project Doc\\GTB_new_StockData.csv')
df.dtypes
df.columns =df.columns.to_series().apply(lambda x: x.strip())
df_close = pd.DataFrame(df.Close)
df.columns =df.columns.to_series().apply(lambda x: x.strip())
df_close = pd.DataFrame(df.Close)
short_rolling = df['Close'].rolling(window=20).mean()
print(short_rolling.head(20))
long_rolling = df['Close'].rolling(window=100).mean()
print(long_rolling.head(20))
print(short_rolling.tail(20))
fig, ax = plt.subplots(figsize=(16,9))
ax.plot(df.loc[0:4344, :].index, df.loc[0:4344, 'Close'], label='Price')
plt.figure(figsize=(5,10))
plt.grid(True)
df_close
plt.plot(df_close['Close'], label = 'Close')
plt.plot(short_rolling, label='short_rolling')
plt.plot(long_rolling, label='long_rolling')
plt.legend(loc=2)
plt.show()

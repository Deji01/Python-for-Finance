import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

#SELECTING THE STYLE TO USE FOR PLOTTING
style.use('ggplot')

#SELECTING START & END DATES
#start = dt.datetime(2016,12,31)
#end = dt.datetime(2021,6,12)

#CREATING A DATA FRAME & SPECIFYING A TICKER (TSLA)
#df = web.DataReader('TSLA','yahoo', start, end)

#STORING THE DATA AS A CSV FILE
#df.to_csv('tsla.csv')

#PARSING THROUGH THE CSV FILE WITH A CSV READER
df = pd.read_csv('tsla.csv ', parse_dates=True, index_col=0)

# PRINTS THE FIRST FIVE ROWS OF OPEN & HIGH COLUMNS TO THE TERMINAL
#print(df[['Open', 'High']].head())

#PLOTS THE ADJUSTED CLOSE
#df['Adj Close'].plot()

#SHOWS THE PLOT
#plt.show()

#100 MOVING AVERAGE COLUMN
#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
#print(df.head())
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

#SPECIFYING THE NO OF ROWS AND COLUMNS 
#ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
#ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex = ax1)
#ax1.xaxis_date()

#candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
#ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
#PLOTTING ON THE X & Y AXIS
#ax1.plot(df.index, df['Adj Close'])
#ax1.plot(df.index, df['100ma'])
#ax2.bar(df.index, df['Volume'])
#plt.show()


#%%
import pandas as pd
import numpy as np
from pandas_datareader import data, wb
import matplotlib.pyplot as plt


#%%
get_ipython().run_line_magic('matplotlib', 'inline')
pd.set_option('display.max_colwidth', 200)


#%%
import pandas_datareader as pdr
start_date = pd.to_datetime('2010-01-01')
stop_date = pd.to_datetime('2016-03-01')
spy = pdr.data.get_data_yahoo('SPY', start_date, stop_date)
spy


#%%
spy_c = spy['Close']


#%%
fig, ax = plt.subplots(figsize=(15, 10))
spy_c.plot(color='g')
plt.title("SPY", fontsize = 20)


#%%
first_open = spy['Open'].iloc[0]
first_open


#%%
last_close = spy['Close'].iloc[-1]
last_close


#%%
last_close - first_open


#%%
spy['Daily Change'] = pd.Series(spy['Close'] - spy['Open'])


#%%
spy['Daily Change']


#%%
spy['Daily Change'].sum()


#%%
np.std(spy['Daily Change'])


#%%
spy['Overnight Change'] = pd.Series(spy['Open'] - spy['Close'].shift(1))
np.std(spy['Overnight Change'])


#%%
spy[spy['Daily Change']<0]['Daily Change'].mean()


#%%
spy[spy['Overnight Change']<0]['Overnight Change'].mean()


#%%
daily_rtn = ((spy['Close'] - spy['Close'].shift(1))/spy['Close'].shift(1))*100
id_rtn = ((spy['Close'] - spy['Open'])/spy['Open'])*100
on_rtn = ((spy['Open'] - spy['Close'].shift(1))/spy['Close'].shift(1))*100


#%%
daily_rtn


#%%
id_rtn


#%%
on_rtn


#%%
def get_stats(s, n=252):
    s = s.dropna()
    wins = len(s[s>0])
    losses = len(s[s<0])
    evens = len(s[s==0])
    mean_w = round(s[s>0].mean(), 3)
    mean_l = round(s[s<0].mean(), 3)
    win_r = round(wins/losses, 3)
    mean_trd = round(s.mean(), 3)
    sd = round(np.std(s), 3)
    max_l = round(s.min(), 3)
    max_w = round(s.max(), 3)
    sharpe_r = round((s.mean()/np.std(s))*np.sqrt(n), 4)
    cnt = len(s)
    print('Trades:', cnt,         '\nWins:', wins,         '\nLosses:', losses,         '\nBreakeven:', evens,         '\nWin/Loss Ratio:', win_r,         '\nMean Win:', mean_w,         '\nMean Loss:', mean_l,         '\nMean:', mean_trd,         '\nStd Dev:', sd,         '\nMax Loss:', max_l,         '\nMax Win:', max_w,         '\nSharp Ratio:', sharpe_r)


#%%
get_stats(daily_rtn)


#%%
get_stats(id_rtn)


#%%
get_stats(on_rtn)


#%%
start_date = pd.to_datetime('2000-01-01')
stop_date = pd.to_datetime('2016-03-01')
sp = pdr.data.get_data_yahoo('SPY', start_date, stop_date)
sp


#%%
fig, ax = plt.subplots(figsize=(15,10))
sp['Close'].plot(color='k')
plt.title('SPY', fontsize = 20)


#%%
long_day_rtn = ((sp['Close'] - sp['Close'].shift(1))/sp['Close'].shift(1))*100
long_id_rtn = ((sp['Close'] - sp['Open'])/sp['Open'])*100
long_on_rtn = ((sp['Open'] - sp['Close'].shift(1))/sp['Close'].shift(1))*100


#%%
(sp['Close'] - sp['Close'].shift(1)).sum()


#%%
(sp['Close'] - sp['Open']).sum()


#%%
(sp['Open'] - sp['Close'].shift(1)).sum()


#%%
get_stats(long_day_rtn)


#%%
get_stats(long_id_rtn)


#%%
get_stats(long_on_rtn)


#%%




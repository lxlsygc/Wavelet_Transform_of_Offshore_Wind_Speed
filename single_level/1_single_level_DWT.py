import matplotlib as mpl
import pandas as pd
import pywt
mpl.rcParams['agg.path.chunksize'] = 100000
pd.options.display.width = 0

df = pd.read_csv("combined_2019_10min_NNAN.csv")
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])
df.set_index('TimeStamp', inplace=True)

df = df['2019-04-03 00:00':'2019-07-04 23:00']
df = df['Anemo_2']

cA, cD = pywt.dwt(df, 'haar')

signal_datasets = pd.DataFrame({'cA': cA, 'cD': cD})
signal_datasets.to_csv('signal_datasets.csv')

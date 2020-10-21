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

df.to_csv('used_datasets_datasets.csv')

coeffs = pywt.wavedec(df, 'haar', level=2, mode='sym')
cA2, cD2, cD1 = coeffs

multiple2_datasets = pd.DataFrame({'cA2': cA2, 'cD2': cD2})
multiple2_datasets.to_csv('multiple2_datasets.csv')

multiple1_datasets = pd.DataFrame({'cD1': cD1})
multiple1_datasets.to_csv('multiple1_datasets.csv')

import matplotlib as mpl
import pandas as pd
import pywt

mpl.rcParams['agg.path.chunksize'] = 100000
pd.options.display.width = 0

df = pd.read_csv("signal_datasets.csv")

inverse = pywt.idwt(df['cA'], df['cD'], 'haar')   #IWT

signal_datasets_inverse = pd.DataFrame({'inverse': inverse})
signal_datasets_inverse.to_csv('signal_datasets_inverse.csv')

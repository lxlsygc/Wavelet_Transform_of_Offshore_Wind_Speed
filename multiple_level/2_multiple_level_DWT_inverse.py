import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt
import pywt
mpl.rcParams['agg.path.chunksize'] = 100000
pd.options.display.width = 0

df1 = pd.read_csv("multiple1_datasets.csv")
df2 = pd.read_csv("multiple2_datasets.csv")

coeffs = df2['cA2'], df2['cD2'], df1['cD1']

inverse = pywt.waverec(coeffs, 'haar', mode='sym')   #IWT

inverse = pd.DataFrame({'inverse': inverse})
inverse.to_csv('inverse.csv')

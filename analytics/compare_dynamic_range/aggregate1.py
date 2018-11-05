import matplotlib.pyplot as plt
#from baseline_10day_avg import *
import pandas as pd

def run(res):
    df = pd.DataFrame.from_records(res)
    df.dropna(inplace=True)
    df = df[df['min']<50000]
    ax = plt.scatter(x=df['min'],y=df['max'],s=100)
    plt.xlabel('Min demand (W)')
    plt.ylabel('Max demand (W)')
    fig = plt.gcf()
    fig.set_size_inches(10,10, forward=True)
#for r in res:
#    if isinstance(r, list):
#        continue
#    rec.append({'min': r['df'].min().min(), 'max': r['df'].max().max(), 'site': r['sitename']})
#df = pd.DataFrame.from_records(rec)
#df.dropna(inplace=True)
#df = df[df['min']<50000]
#ax = plt.scatter(x=df['min'],y=df['max'],s=100)
#plt.xlabel('Min demand (W)')
#plt.ylabel('Max demand (W)')
#fig = plt.gcf()
#fig.set_size_inches(10,10, forward=True)
#
##df['diff'] = (df['max'] - df['min'])
##ax = df['diff'].hist(bins=20)
##plt.xlabel('Diference between min and max demand (W)')
##print(df.describe())


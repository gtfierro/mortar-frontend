from sklearn.metrics import mean_squared_error
from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR
from datetime import timedelta
import pandas as pd

def run(m, indata):
    df = indata['train_clean']
    nd = indata['test_clean']
    freq = pd.infer_freq(nd.index)

    streams = []
    for t in rrule(freq=DAILY, count=10, byweekday=(MO,TU,WE,TH,FR), dtstart=nd.index[0]-timedelta(days=14)):
        fullidx = pd.date_range(t,t+timedelta(days=1), freq=freq)
        data = df[t:t+timedelta(days=1)].reindex(fullidx).fillna(method='ffill')
        data = data[:len(nd.index)]
        data.index = nd.index
        streams.append(data.copy())

    if len(streams) < 3:
        return
    streams.sort(key=lambda x: x.sum(), reverse=True)
    top3 = pd.concat(streams[:3], axis=1).mean(axis=1).fillna(method='ffill')

    if len(top3.dropna()) == 0: return

    try:
        e = mean_squared_error(nd.values, top3.values)
        
        return {indata['train']['sitename']: e}
    except Exception as e:
        print(e)
        import IPython ; IPython.embed()

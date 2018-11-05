import pandas as pd

def run(m, inobject):
    df = inobject['df'].copy()
    df.dropna(inplace=True)
    # add meters if we have them
    meters = df.sum(axis=1)
    # remove everything thats more than 3 standard deviations away from the mean
    meters = meters[pd.np.abs(meters-meters.mean()) <= (3*meters.std())]
    inobject['meter'] = meters
    return inobject

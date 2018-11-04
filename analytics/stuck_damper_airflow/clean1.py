
def run(m, inobject):
    #df = data['raw'].copy()
    df = inobject['df'].copy()
    df.fillna(method='ffill',inplace=True)
    df.dropna(inplace=True)

    if len(df) == 0:
        return None

    inobject['cleaned'] = df
    return inobject

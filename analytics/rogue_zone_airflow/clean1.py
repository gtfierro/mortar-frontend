def run(m, inobject):
    df = inobject['df'].copy()
    df.dropna(inplace=True)
    inobject['cleaned'] = df
    return inobject

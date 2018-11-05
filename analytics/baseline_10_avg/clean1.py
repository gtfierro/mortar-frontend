def run(m, data):
    df = data['train']['df'].copy()
    df.fillna(method='ffill',inplace=True)
    df = df.sum(axis=1)
    data['train_clean'] = df

    df2 = data['test']['df'].copy()
    df2.fillna(method='ffill',inplace=True)
    df2 = df2.sum(axis=1)

    data['test_clean'] = df2

    return data

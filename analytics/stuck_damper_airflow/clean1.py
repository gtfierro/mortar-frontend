
def run(m, inobject):
    data = m.cache.get(inobject).copy()

    print('clean?')
    #df = data['raw'].copy()
    #df.dropna(inplace=True)

    #data['cleaned'] = df
    if len(data) == 0:
        return None

    return m.cache.put(data)

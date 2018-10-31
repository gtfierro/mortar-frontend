def run(m, inobject):
    if inobject is None:
        return
    data = m.cache.get(inobject)
    print('here!', data.describe())

    return data.mean()


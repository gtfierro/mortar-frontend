def run(m, inobject):
    if inobject is None:
        return
    data = m.cache.get(inobject)

    return data['df'].mean()

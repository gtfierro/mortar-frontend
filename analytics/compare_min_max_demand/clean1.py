
def run(m, inobject):
    data = m.cache.get(inobject).copy()

    if len(data) == 0:
        return None

    return inobject

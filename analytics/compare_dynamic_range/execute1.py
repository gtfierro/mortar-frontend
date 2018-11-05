def run(m, inobject):
    meter = inobject['meter']

    return {'sitename': inobject['sitename'], 'min': meter.min(), 'max': meter.max()}

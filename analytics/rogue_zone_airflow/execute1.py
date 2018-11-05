def run(m, inobject):
    df = inobject['cleaned'].copy()

    ctx = inobject['context']
    m = inobject['mapping']

    runset = [d for d in ctx.values() if '?setpoint' in d and '?sensor' in d]
    for r in runset:
        for c in ctx.values():
            if c['?equip'] == r['?equip']:
                r.update(c)

    for r in runset:
        cols = [r['?setpoint_uuid'], r['?sensor_uuid']]
        dd = df[cols]
        dd.columns = ['setpoint','airflow']
        bad = dd.airflow < dd.setpoint
        if len(dd[bad]) == 0: continue
        df['same'] = bad.astype(int).diff(1).cumsum()
        print("---")
        print(dd[bad].describe())
        dd[bad].plot(figsize=(15,10))

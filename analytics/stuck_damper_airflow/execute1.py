def run(m, inobject):
    df = inobject['cleaned']
    res = []
    for col in df.columns:
        dmp = df[[col]]
        ctx = inobject['context'][col]
        dmp.columns = ['pos']
        groups = dmp.groupby(dmp.pos.diff().ne(1).cumsum()).groups
        for key, grp in groups.items():
            if len(grp) > 3:
                print('zone %s stuck at %s over (%s - %s)' % (ctx['?vav'].split('#')[-1], key, grp[0], grp[-1]))
                res.append(ctx['?vav'], key, grp[0], grp[-1])
    return res

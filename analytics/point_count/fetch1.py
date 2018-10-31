request = {
    "Composition": ["points"],
    "Aggregation": {
        "points": ["COUNT"],
    },
    "Variables": {
        "points": {
            "Definition": """SELECT ?uuid FROM %s WHERE {
                ?meter bf:uuid ?uuid
            };""",
        },
    },
    "Time": {
        "Start":  "2008-01-01T10:00:00-07:00",
        "End":  "2018-01-01T10:00:00-07:00",
        "Window": '3650d',
        "Aligned": True,
    },
}

def run(m, sites):
    print(sites)
    for site in sites:
        res, objectid = m.fetch(site, request)
        if res is None:
            continue
        yield objectid

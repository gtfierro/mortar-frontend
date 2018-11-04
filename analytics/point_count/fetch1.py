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

def run(m, site):
    res = m.fetch(site, request)
    return res

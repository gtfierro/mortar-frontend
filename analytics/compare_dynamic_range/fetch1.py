request = {
    "Composition": ["meter"],
    "Aggregation": {
        "meter": ["MEAN"],
    },
    "Variables": {
        "meter": {
            "Definition": """SELECT ?meter ?meter_uuid FROM %s WHERE {
                ?meter rdf:type brick:Building_Electric_Meter .
                ?meter bf:uuid ?meter_uuid
            };""",
        },
    },
    "Time": {
        "Start":  "2018-03-01T10:00:00-07:00",
        "End":  "2018-05-14T10:00:00-07:00",
        "Window": '30min',
        "Aligned": True,
    },
}

def run(m, site):
    return m.fetch(site, request)

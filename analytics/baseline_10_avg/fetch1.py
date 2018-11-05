request = {
    "Composition": ["temp"],
    "Aggregation": {
        "temp": ["MEAN"],
    },
    "Variables": {
        "temp": {
            "Definition": """SELECT ?meter ?meter_uuid FROM %s WHERE {
                ?meter rdf:type brick:Building_Electric_Meter .
                ?meter bf:uuid ?meter_uuid
            };""",
        },
    },
    "Time": {
        "Start":  "2018-01-01T10:00:00-07:00",
        "End":  "2018-10-14T10:00:00-07:00",
        "Window": '30min',
        "Aligned": True,
    },
}

trainstart = "2018-01-01T10:00:00-07:00"
trainend = "2018-10-14T10:00:00-07:00"

teststart = "2018-10-14T00:00:00-07:00"
testend = "2018-10-15T00:00:00-07:00"

def run(m, site):
    data = {}

    request["Time"]["Start"] = trainstart
    request["Time"]["End"] = trainend
    
    res = m.fetch(site, request)
    data['train'] = res

    request["Time"]["Start"] = teststart
    request["Time"]["End"] = testend

    nextday = m.fetch(site, request)
    data['test'] = nextday

    return data

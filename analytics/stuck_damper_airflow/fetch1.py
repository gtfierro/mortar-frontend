request = {
    "Composition": ["airflow","setpoint"],
    "Aggregation": {
        "airflow": ["MEAN"],
        "setpoint": ["MEAN"],
    },
    "Variables": {
        "airflow": {
            "Definition": """SELECT ?vav ?sensor ?sensor_uuid FROM %s WHERE {
                ?sensor    rdf:type/rdfs:subClassOf*     brick:Air_Flow_Sensor .
                ?sensor  bf:isPointOf ?equip .
                ?sensor     bf:uuid  ?sensor_uuid .
            };""",
        },
        "setpoint": {
            "Definition": """SELECT ?vav ?sensor ?setpoint ?setpoint_uuid FROM %s WHERE {
                ?setpoint  rdf:type/rdfs:subClassOf*     brick:Air_Flow_Setpoint .
                ?setpoint  bf:isPointOf ?equip .
                ?setpoint   bf:uuid  ?setpoint_uuid .
            };""",
        },
    },
    "Time": {
        "Start":  "2018-01-01T10:00:00-07:00",
        "End":  "2018-05-12T10:00:00-07:00",
        "Window": '20m',
        "Aligned": True,
    },
}

def run(m, sites):
    for site in sites:
        print(site)
        df, objectid = m.fetch(site, request)
        if df is None:
            continue
        print(df.describe())
        yield objectid

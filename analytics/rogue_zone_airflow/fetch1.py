request = {
    "Composition": ["airflow","setpoint"],
    "Aggregation": {
        "airflow": ["MEAN"],
        "setpoint": ["MIN"],
    },
    "Variables": {
        "airflow": {
            "Definition": """SELECT ?equip ?sensor ?sensor_uuid FROM %s WHERE {
                ?sensor    rdf:type/rdfs:subClassOf*     brick:Air_Flow_Sensor .
                ?sensor  bf:isPointOf ?equip .
                ?sensor     bf:uuid  ?sensor_uuid .
            };""",
        },
        "setpoint": {
            "Definition": """SELECT ?equip ?sensor ?setpoint ?setpoint_uuid FROM %s WHERE {
                ?setpoint  rdf:type/rdfs:subClassOf*     brick:Air_Flow_Setpoint .
                ?setpoint  bf:isPointOf ?equip .
                ?setpoint   bf:uuid  ?setpoint_uuid .
            };""",
        },
    },
    "Time": {
        "Start":  "2015-05-01T10:00:00-07:00",
        "End":  "2015-05-12T10:00:00-07:00",
        "Window": '10m',
        "Aligned": True,
    },
}


def run(m, site):
    res = m.fetch(site, request)
    return res

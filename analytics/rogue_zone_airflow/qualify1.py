def run(m):
    sites = m.qualify(["""
    SELECT ?equip ?sensor ?setpoint ?sensor_uuid ?setpoint_uuid WHERE {
        ?setpoint  rdf:type/rdfs:subClassOf*     brick:Air_Flow_Setpoint .
        ?sensor    rdf:type/rdfs:subClassOf*     brick:Air_Flow_Sensor .
        ?setpoint  bf:isPointOf ?equip .
        ?sensor    bf:isPointOf ?equip .
        ?setpoint  bf:uuid  ?setpoint_uuid .
        ?sensor    bf:uuid  ?sensor_uuid .
    };"""])
    return sites


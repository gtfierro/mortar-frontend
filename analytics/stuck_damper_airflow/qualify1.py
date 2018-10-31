def run(m):
    sites = m.qualify(["""
    SELECT ?sensor ?equip ?sensor_uuid WHERE {
        ?sensor    rdf:type/rdfs:subClassOf*     brick:Air_Flow_Sensor .
        ?sensor  bf:isPointOf ?equip .
        ?sensor     bf:uuid  ?sensor_uuid .
    };"""])
    return sites

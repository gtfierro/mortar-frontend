def run(m):
    sites = m.qualify(["""
    SELECT ?meter ?meter_uuid WHERE {
    ?meter rdf:type brick:Building_Electric_Meter .
    ?meter bf:uuid ?meter_uuid
    };"""])
    return sites


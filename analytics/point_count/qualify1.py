def run(m):
    sites = m.qualify(["""
    SELECT ?uuid WHERE {
        ?x bf:uuid ?uuid
    };"""])
    return sites

import pymortar
m = pymortar.MortarClient()

res = m.RUN("rogue_zone_airflow.qualify1","rogue_zone_airflow.fetch1", "rogue_zone_airflow.clean1", "rogue_zone_airflow.execute1")


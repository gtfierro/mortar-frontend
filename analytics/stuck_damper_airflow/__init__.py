import pymortar
m = pymortar.MortarClient('172.17.0.1:9001')

res = m.RUN("stuck_damper_airflow.qualify1","stuck_damper_airflow.fetch1","stuck_damper_airflow.clean1","stuck_damper_airflow.execute1")

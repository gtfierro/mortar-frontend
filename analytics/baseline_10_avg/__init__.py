import pymortar
m = pymortar.MortarClient()

res = m.RUN("baseline_10_avg.qualify1","baseline_10_avg.fetch1", "baseline_10_avg.clean1", "baseline_10_avg.execute1")


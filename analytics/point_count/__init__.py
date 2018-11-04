import pymortar
m = pymortar.MortarClient()

res = m.RUN("point_count.qualify1","point_count.fetch1", None, None)

num_points = 0
num_streams = 0
for r in res:
    if not isinstance(r,dict): continue
    num_points += r['df'].sum().sum()
    num_streams += len(r['df'].columns)

print("NUM POINTS:", num_points)
print("NUM STREAMS:", num_streams)

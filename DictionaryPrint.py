d1=input("data1: ").split(',')
d2=input("data2: ").split(',')
d=dict(zip(d1,d2))
for k,v in sorted(d.items()):
    print(k,v)

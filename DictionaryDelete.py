d1=input("data1: ").split(',')
d2=input("data2: ").split(',')
d=dict(zip(d1,d2))
k=input("key: ")
if k in d:
    print("value:",d.pop(k))
    print("dictionary:",sorted(d.items()))
else:
    print("key does not exist")

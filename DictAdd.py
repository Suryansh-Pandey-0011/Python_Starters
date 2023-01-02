l11=list(map(lambda x:int(x) ,input("Keys for Dict1: ").split(',')))
l12=list(map(lambda x:int(x) ,input("Values for Dict1: ").split(',')))
l21=list(map(lambda x:int(x) ,input("Keys for Dict2: ").split(',')))
l22=list(map(lambda x:int(x) ,input("Values for Dict2: ").split(',')))
d1=dict(zip(l11,l12))
d2=dict(zip(l21,l22))
d3={}
for i in sorted(d1)+sorted(d2):
    d3[i]=d1.get(i,0)+d2.get(i,0)
print(sorted(d3.items()))

l1=list(map(lambda x:int(x) ,input("data1: ").split(',')))
l2=list(map(lambda x:int(x) ,input("data2: ").split(',')))
l3=list(map(lambda x:int(x) ,input("data3: ").split(',')))
m=[l1,l2,l3]
for i in range(3):
    for j in range(3):
        print(m[i][j],end='\t')
    print()
r=len(m)
c=len(m[0])
s=r*c
count=l1.count(0)+l2.count(0)+l3.count(0)
if(count>(s/2)):
    print("Sparse Matrix")
else:
    print("Not a Sparse Matrix")

d1=input("data1: ")
d2=input("data2: ")
l1=d1.split(',')
l1=list(map(lambda x:int(x) ,l1))
l2=d2.split(',')
l2=list(map(lambda x:int(x) ,l2))
l3=[]
if len(l1)==len(l2):
    l3=list(map(lambda x,y: x+y , l1,l2))
    print("sum:",l3)
else:
    print("Lenths are different")

d=input("data1: ")
l=d.split(',')
l=list(map(lambda x:int(x) , l))
l2=[]
for i in range(len(l)):
    if i%2!=0:
        l2.append(l[i])
print("odd index elements:",l2)

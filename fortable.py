n1=int(input("x:"))
n2=int(input("y:"))
if(n2<=20):
    t=n2
else:
    t=20
for i in range(1,t+1):
    print(n1,"*",i,"=",(n1*i))
else:
    if(n2>20):
        print("row is limited to 20")

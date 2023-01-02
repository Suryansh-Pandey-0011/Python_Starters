'''n=input("n: ")
l=len(n)
n1=int(n)
sum=0
while(n1!=0):
    dig=n1%10
    n1=int(n1/10)
    sum+=(dig**l)
if(sum==int(n)):
    print("Armstrong")
else:
    print("not Armstrong")'''
n=input("n: ")
l=len(n)
sum=0
for i in n:
    sum+=(int(i)**l)
if(sum==int(n)):
    print("Armstrong")
else:
    print("not Armstrong")

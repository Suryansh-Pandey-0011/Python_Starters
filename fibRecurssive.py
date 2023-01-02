def fib(x,y,n):
    if n>2:
        print(x+y)
        fib(y,x+y,n-1)
n=int(input("N: "))
print("The Fibbonacci series is:")
if(n!=0):
    print("0")
if(n!=0 and n!=1):
    print("1")
fib(0,1,n)
'''def fibb(n):
    if n<=1:
        return n
    else:
        return (fibb(n-1))+(fibb(n-2))
n=int(input("n: "))
for i in range(n):
    print(fibb(i))'''

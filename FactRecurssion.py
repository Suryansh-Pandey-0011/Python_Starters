def fact(n):
    if(n==1):
        return 1
    else:
        return(n*fact(n-1))
n1=int(input())
print(fact(n1))

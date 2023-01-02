def add(x,y):
    if(y==0):
        return x
    else:
        return(1+add(x,y-1))
a=int(input("a: "))
b=int(input("b: "))
print(add(a,b))

def sum_avg(x,y):
    return ((x+y),((x+y)/2))
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
a=int(input("a: "))
b=int(input("b: "))
print("sum, average: ",sum_avg(a,b))
print("sub: ",type(sum_avg(a,b)))
print("sub: ",sub(a,b))
print("sub: ",type(sub(a,b)))
print("mul: ",mul(a,b))

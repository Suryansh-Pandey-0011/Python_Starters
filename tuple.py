t=('i','love','python')
print("Given Tuple:",t)
t=list(t)
print("After converting tuple to list:",t)
t[1]='practice'
print("After changing element:",t)
t=tuple(t)
print("After converting list to tuple:",t)

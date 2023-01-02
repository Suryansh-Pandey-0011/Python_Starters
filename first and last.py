s=input("input: ")
print("Output: ",end='')
if len(s)<3:
    print(s)
else:
    print(s[:2]+s[-2:])

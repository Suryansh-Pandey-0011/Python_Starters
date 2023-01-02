s=input("str: ")
if len(s)==0:
    print("null")
elif len(s)==1:
    print(s)
else:
    print(s[-1]+s[1:-1]+s[0])

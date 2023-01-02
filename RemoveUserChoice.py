s=input("str: ")
n=int(input("num: "))
print("output: ",end='')
if 0<=n<len(s):
    print(s[:n]+s[n+1:])
else:
    print("num should be positive and in range of string")

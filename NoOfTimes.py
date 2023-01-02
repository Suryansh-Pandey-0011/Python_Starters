s=input("str: ")
n=int(input("num: "))
if 0<=n<len(s):
    print(s[:n]*n)
else:
    print("num should be positive, less than length of string")

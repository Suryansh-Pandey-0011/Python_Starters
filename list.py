d=input("data: ")
l=d.split(',')
i=int(input("index: "))
if -(len(l))<=i<len(l):
    print("element:",l[i])
else:
    print("Invalid")

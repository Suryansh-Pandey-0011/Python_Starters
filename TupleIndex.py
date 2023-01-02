t=tuple((input("data: ")).split(','))
print(t)
e=input("element: ")
l=list(t)
for i in range(len(l)):
    if(l[i]==e):
        print("index:",i)
        break
else:
    print("enter an element that exists in tuple")

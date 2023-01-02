import random
p=int(input("How many pieces the cake should have: "))
print("1. Equal sizes")
print("2. Any Sizes")
print("3. No two pieces with equal size")
d=int(input("Enter the index of your choice: "))
if(d==1)and(p>0):
    if ((360/p)==int(360/p)):
        print("Angle of each piece is %.2f degrees"%(360/p))
    else:
        print("Cake cannot be cut into",p,"equal integral angled pieces")
elif(d==2)and(p>0):
    t=[]
    for i in range(p-1):
        t.append(random.randint(1,360//p))
    t.append(360-sum(t))
    for i in range(len(t)):
        print("Piece %d:"%(i+1),t[i],"degrees")
elif(d==3)and(p>0):
    if(p>26):
        print(p,"distinct itegral angled pieces not possible")
    else:
        c=0
        for i in range(1,p):
            print("Piece %d: %d degrees"%(i,i))
            c+=i
        print("Piece %d: %d degrees"%(p,360-c))
else:
    print("Enter a valid input")

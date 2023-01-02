x=int(input("x: "))
y=int(input("y: "))
'''for i in range(x,y+1):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c+=1
    if(c==2):
        print(i)
       OR
        '''
for i in range(x,y+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)

'''k=input().split(',')
v=list(map(lambda x:int(x) ,input("values").split(',')))
c=input().split(',')
d=dict(zip(k,v))
print(d)
d1={}
for i in range(len(c)):
    dt={}
    dt[k[i]]=v[i]
    d1[c[i]]=dt
print(d1)'''
'''k=list(map(lambda x:int(x) ,input().split(',')))
def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
d={}
for i in k:
    d[i]=fact(i+1)
print(d)'''
'''k=list(map(lambda x:int(x) ,input().split(',')))
def div(n):
    l=[]
    for i in range(2,n):
        if n%i==0:
            l.append(i)
    return l
d={}
for i in k:
    d[i]=div(i)
print(d)'''
'''k=list(map(lambda x:int(x) ,input().split(',')))
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return "not prime"
                break
        else:
            return "prime"
    else:
        return "not prime"
d={}
for i in k:
    d[i-1]=prime(i-1)
print(d)'''
'''d={}
print(d)
k=input("keys: ").split(',')
v=list(map(lambda x:int(x) ,input("values: ").split(',')))
d=dict(zip(k,v))
print(d)
d1={}
for i in range(3):
    l=input().split(',')
    d1[l[0]]=int(l[1])
d.update(d1)
print(d)'''
'''l=sorted(list(map(lambda x:int(x) ,input().split(','))))
d={}
t=l[0]
c=0
for i in range(len(l)):
    if t==l[i]:
        c+=1
    else:
        d[l[i-1]]=c
        t=l[i]
        c=1
d[l[-1]]=c
print(d)'''
'''k=list(map(lambda x:int(x) ,input("keys: ").split(',')))
v=input("values: ").split(',')
d=dict(zip(k,v))
print(d)'''
'''k=input("keys: ").split()
for i in range(len(k))'''
class Solution:
    def isPangram(self,a):
        t="abcdefghijklmnopqrstuv"
        f=True
        for i in t:
            if i not in a.lower():
                f=False
        if f:
            print("YES")
        else:
            print("NO")
a=input()
Solution().isPangram(a)

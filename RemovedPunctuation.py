import string
s=input("str = ")
y=""
t=string.punctuation
for i in s:
    if i not in t:
        y+=i
print(y)
    

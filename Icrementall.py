s=input("str: ")
y=""
'''for i in range(len(s)):
    for j in range(i+1):
        y+=s[j]
print(y)'''
for i in range(len(s)):
    y+=s[:i+1]
print(y)

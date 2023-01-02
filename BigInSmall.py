s1=input("str1: ")
s2=input("str2: ")
if (len(s1)>len(s2)):
    print(s2+s1+s2)
elif (len(s1)<len(s2)):
    print(s1+s2+s1)
else:
    print("strings are same length")

try:
    a=int(input("a: "))
    b=int(input("b: "))
    c=a/b
    print(c)
except:
    print("Exception occured")

else:
    print("The code is already running")
finally:
    print("Always present")

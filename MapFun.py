#Using map with regular function
def cube(r):
    return r**3
l1=[2,3,5,7,8]
print(list(map(cube,l1)))
#Using map with lambda function
print(list(map(lambda x:x**10,l1)))
#List
print([i**2 for i in l1])

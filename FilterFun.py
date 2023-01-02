#Filter with lambda function
l1=[4, 9, 25, 49, 64]
print(list(filter(lambda x:x%2==0,l1)))
print(list((lambda x:x%2==0,l1)))
#Filter with lambda function
print([i for in in l1 if i%2==0])

def largestNumber(*num):
    max=num[0]
    for i in num:
        if i>max:
            max=i
    return max
print(largestNumber(2,1,4))
print(largestNumber(1,2,6,9,4,5))

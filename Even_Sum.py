n=int(input("Enter a positive integer: "))
if n%2==0:
      t=n
else:
    t=n-1
sum=0
i=0
while (i<=t):
    sum+=i
    i+=2
print("The sum of even numbers is:",sum)
    

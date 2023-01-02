'''def intro(*,name,age):
    print("Name: ",name,"\nAge: ",age)
intro(age=19,name="Nikhil")
intro("Nikhil",19)#Positional Arguments
#intro(19,"Nikhil")'''
def fun1(a,b=200,c=50):
    print(a+b+c)
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
fun1(a)
fun1(a,b)
fun1(a,b,c)

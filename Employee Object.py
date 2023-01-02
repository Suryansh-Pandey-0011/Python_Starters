class Employee:
    def pri(n):
        n=input("name%d: "%n)
        s=int(input("salary%d: "%n))
        print("Emp_%n.name:",n)
        print("Emp_%n.salary:",n)
n=int(input("Enter the number of employees: "))
for i in range(n):
    s=Employee()
    s.pri(i)


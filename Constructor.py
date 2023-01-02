class Student:
    def __init__(self,na,ag,ro):
        self.n=na
        self.a=ag
        self.r=ro
    def pr(self):
        print("S1: ",self.n,self.a,self.r)
s1=Student(input("name"),int(input("Age")),int(input("Roll No.")))
s2=Student(input("name"),int(input("Age")),int(input("Roll No.")))
s1.pr()
s2.pr()

class Student:
    __group="ECE"
    __report="fail"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def setdetails(self,__group,__report):
        self.__group=__group
        self.__report=__report
    def getdetails(self):
        print(self.name,self.age,self.__group,self.__report)
s1=Student("Suryansh",21)
s1.setdetails("CSE","pass")
s1.getdetails()

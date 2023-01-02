class Employee:
    def setuid(self,id):
        self.id=id
    def getuid(self):
        print(self.id)
    def setname(self,name):
        self.name=name
    def getname(self):
        print(self.name)
class Faculty(Employee):
    def setcourse(self,course):
        self.course=course
    def getcourse(self):
        return self.course
class doc_faculty(Faculty):
    def setnam(self,nam):
        self.nam=nam
    def getnam(self):
        return self.nam
f=doc_faculty()
f.setuid(123)
f.getuid()
f.setname("Aditya")
f.getname()
f.setcourse("Maths")
print(f.getcourse())
f.setnam("Rohan")
print(f.getnam())

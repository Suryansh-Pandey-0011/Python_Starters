class Car:
    def setName(self,name):
        self.n=name
    def getName(self):
        return self.n
Honda=Car()
Honda.setName((input("car name: ")))
print("Honda car name:",Honda.getName())

class Abs:
    def fun1(self):#Abstract method without implementation
        pass
class derived(Abs):
    def fun1(self):#Overriding Method
        print("Hello")
o=derived()
o.fun1()

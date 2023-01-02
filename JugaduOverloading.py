class Greet:
    def sayHello(self,name=None,wish=None):
        if name is not None and wish is not None:
            print("Hello!",name,wish)
        elif name is not None and wish is None:
            print("Hello!",name)
        else:
            print("Hello!")
g=Greet()
g.sayHello()
g.sayHello("Suryansh")
g.sayHello("Suryansh","Good Morning")

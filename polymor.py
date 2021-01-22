class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def info(self):
        print(f"hi this is {self.name}. I am {self.age} years old")
    def makeSound(self):
        print("Meow")

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def info(self,):
        print(f"hi this is {self.name}. I am {self.age} years old")
    def makeSound(self):
        print("Bow")

c = Cat('pussy',1)
d = Dog('snoopy',0.5)
c.info()
d.info()
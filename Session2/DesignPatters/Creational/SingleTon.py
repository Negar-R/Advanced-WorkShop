class A:
    def __init__(self):
        pass

    __instance = None

    def __new__(cls):
        if not A.__instance:
            A.__instance = super().__new__(cls) 
        return A.__instance
        #super : is used to call the constructor, methods and properties of parent class.
        #You may also use the super keyword in the sub class when you want to 
        #invoke a method from the parent class when you have overridden it in the subclass.

        
a1 = A()
print(hex(id(a1)))

a2 = A()
print(hex(id(a2)))
print(type(a2))
print(type(a1))
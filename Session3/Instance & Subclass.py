from abc import ABC , abstractmethod

class A:
    pass

class B(A):
    pass

class MyAbstract(ABC):

    @abstractmethod
    def myMethod(self):
        pass

# a = MyAbstract()
b = B()
print("b instance A : " , isinstance(b , A))

print("A subclass object : " , isinstance(A , object))
print("A instance object : " , issubclass(A , object))

print("A instance type : " , isinstance(A , type))
print("A subclass type : " , issubclass(A , type))

print("MyAbstract instance object : " , isinstance(MyAbstract , object))
print("MyAbstract subclass object : " , issubclass(MyAbstract , object))


print("MyAbstract instance type : " , isinstance(MyAbstract , type))
print("MyAbstract subclass type : " , issubclass(MyAbstract , type))


print("object instance type : " , isinstance(object , type))
print("object subclass type : " , issubclass(object , type))

print("type instance object : " , isinstance(type , object))
print("type subclass object : " , issubclass(type , object))

def f(self):
    pass

print(A)
print(A.__class__) #__class__ : meta class on ra midahad

print(B.__class__)

print(f.__class__)  
print(f)

print(MyAbstract)
print(MyAbstract.__class__)

print(type)
print(type.__class__)

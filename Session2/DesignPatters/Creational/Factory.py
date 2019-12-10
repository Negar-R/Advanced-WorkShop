from abc import ABC , abstractmethod

class IranKhodro(ABC):
    @abstractmethod
    def engine(self):
        pass

class Samand(IranKhodro):
    # @override
    def engine(self):
        print("I'm Samand")

class Pejo207(IranKhodro):
    # @override
    def engine(self):
        print("I'm 207")

class IranKhodroFactory():
    def __init__(self):
        self.typeEngine = input("che motory mikhaye(Samand , Pejo207)?")
        return eval(self.typeEngine)().engine()

f = IranKhodroFactory()
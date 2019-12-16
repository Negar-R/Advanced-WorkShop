from abc import ABCMeta , abstractmethod

class Bank(metaclass = ABCMeta):
    @abstractmethod
    def valid(self , passWord , cash):
        pass 


class RealBank(Bank):
    def valid(self , passWord , cash):
        print("Every thing is OK :)")

class Proxy(Bank):
    def __init__(self):
        self.bank = RealBank()

    def valid(self , passWord , cash):
        if passWord == '6712':
            print("valid input")
            if cash > 10000:
                print("Sufficient !!")
                self.bank.valid(passWord , cash)  
            else:
                print("Insufficient cash")    
        else:
            print("Invalid Input ://")        

class Client():
    def __init__(self):
        self.check = Proxy()
        
    def connect(self , passWord , cash):
        self.check.valid(passWord , cash)

if __name__ == "__main__":
    # a = Client()
    # a.connect('1234' , 10000)

    b = Client()
    b.connect('6712' , 20000)       


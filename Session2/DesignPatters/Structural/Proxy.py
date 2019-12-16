from abc import ABCMeta , abstractmethod


class Internet(metaclass = ABCMeta):
    @abstractmethod
    def connecting(self , URL):
        pass 

class RealInternet(Internet):
    def connecting(self , URL):
        print("Connected")

class Proxy(Internet):
    def __init__(self):
        self.internet = RealInternet()
        self.__banneddList = []

    def appendBanned(self):
        self.__banneddList.append("google.com")

    def connecting(self , URL):
        if URL in self.__banneddList:
            print(":///")
        else:
            self.internet.connecting(URL) 

class Client():
    def __init__(self):
        self.internet = Proxy()
        
    def connect(self , URL):
        self.internet.connecting(URL)

if __name__ == "__main__":
    internet = Client()
    internet.connect("google.com")


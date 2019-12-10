from abc import ABC , abstractmethod

class Context():
    def __init__(self , **kwargs):
        for name , impl in kwargs.items():
            setattr(self , name , impl) #self.name = impl -> esme attribute ro mizare name Ei ke dadim 
            getattr(self , name).strategyInterface()                         #va set mikone ba impl un   
            #getattr(self , name , impl.strategyInterface) ham doroste
            
        # self.chagu.strategyInterface() : kode get attribute moadel(mosavi) in hast 
        #dar vaghe un paranteze (self , name) ye object az name(hamun chagu ...) ast ke function 
        # strategyInterface ro barash seda mizanim

class Strategy(ABC):
    @abstractmethod
    def strategyInterface(self):
        pass


class Bomb(Strategy):
    def strategyInterface(self):
        print("Bomb andaz")


class Chaghu(Strategy):
    def strategyInterface(self):
        print("chagu kesham")

class Tank(Strategy):
    def strategyInterface(self):
        print("Khompare andaz")


def client():
    bomb = Bomb()
    chaghu = Chaghu()
    ashkan = Context(bomb = bomb , chaghu = chaghu) #avali ye variable E va dovomi call class emune


if __name__ == "__main__":
    client()
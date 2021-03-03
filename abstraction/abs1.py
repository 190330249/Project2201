from abc import ABC,abstractmethod
class Vechile(ABC):
    @abstractmethod
    def getNoWheels(self):
        pass
class Bus(Vechile):
    def getNoWheels(self):
        pass
    def col(self):
        return 'White'
    pass
b=Bus()
print(b.col())
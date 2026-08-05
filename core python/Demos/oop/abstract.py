from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def stop():
            pass

class Bike(Vehicle):
    
    def start(ABC):
        print("bike started")
    
    def stop(ABC):
        print("bike stop")


b1 = Bike()
b1.start()
b1.stop()

# v1 = Vehicle()         error occured...
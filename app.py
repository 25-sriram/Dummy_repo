from abc import ABC, abstractmethod

# 1. Base Class (Inheritance: An ElectricCar "is-a" Vehicle)
class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._is_running = False

    @abstractmethod
    def start(self):
        pass

# 2. Component (Composition: A Car "owns" its Battery)
class Battery:
    def __init__(self, capacity=75):
        self.capacity = capacity
        self.charge_level = 100

    def consume(self, amount):
        self.charge_level = max(0, self.charge_level - amount)
        print(f"Battery at {self.charge_level}%")

    print(f"Result: {driver1.name} is still available for a new job.")

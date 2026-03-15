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

# 3. Component (Aggregation: A Fleet "has" Drivers)
class Driver:
    def __init__(self, name, license_id):
        self.name = name
        self.license_id = license_id

    def __str__(self):
        return f"Driver: {self.name} (ID: {self.license_id})"

# 4. Derived Class (Implementing relationships)
class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        # Composition: Battery is created inside ElectricCar
        self.battery = Battery(battery_size)
        self.current_driver = None  # Aggregation placeholder

    def assign_driver(self, driver):
        # Aggregation: Driver exists independently
        self.current_driver = driver
        print(f"{driver.name} is now behind the wheel of the {self.model}.")

    def start(self):
        if self.battery.charge_level > 0:
            self._is_running = True
            print(f"{self.brand} {self.model} hums to life silently.")
        else:
            print("Battery dead. Cannot start.")

    def drive(self, distance):
        if self._is_running:
            print(f"Driving {distance}km...")
            self.battery.consume(distance * 0.5)
        else:
            print("Start the car first!")

# 5. Management Class (High-level Aggregation)
class FleetManager:
    def __init__(self, company_name):
        self.company_name = company_name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def status_report(self):
        print(f"\n--- {self.company_name} Fleet Report ---")
        for v in self.vehicles:
            driver_name = v.current_driver.name if v.current_driver else "Unassigned"
            print(f"{v.brand} {v.model} | Driver: {driver_name} | Charge: {v.battery.charge_level}%")

# --- Main Execution ---
if __name__ == "__main__":
    # Create independent Driver objects
    driver1 = Driver("Sarah Connor", "SC-1984")
    driver2 = Driver("T-800", "CYBER-101")

    # Create the Fleet Manager
    my_fleet = FleetManager("Future Logistics")

    # Create ElectricCars (Composition: Batteries are built-in)
    car_a = ElectricCar("Tesla", "Model 3", 75)
    car_b = ElectricCar("Rivian", "R1T", 135)

    # Establish Aggregation relationships
    car_a.assign_driver(driver1)
    car_b.assign_driver(driver2)

    # Add to fleet
    my_fleet.add_vehicle(car_a)
    my_fleet.add_vehicle(car_b)

    # Simulate usage
    print("\n--- Simulation Start ---")
    car_a.start()
    car_a.drive(40)
    
    car_b.start()
    car_b.drive(20)

    # Show final status
    my_fleet.status_report()

    # Demonstrate Aggregation (Deleting the car doesn't delete the driver)
    print(f"\nSystem: Scrapping the {car_a.model}...")
    del car_a
    print(f"Result: {driver1.name} is still available for a new job.")

import java.util.*;

// Component 1: Engine (Owned by Car)
class Engine {
    private String type;
    public Engine(String type) { this.type = type; }
    public String getType() { return type; }
}

// Component 2: Driver (Exists independently of Car)
class Driver {
    private String name;
    public Driver(String name) { this.name = name; }
    public String getName() { return name; }
}

// Main Component: Car (Maintains relationships)
class Car {
    private String model;
    // Composition: The Car "owns" the Engine. 
    // If the Car is destroyed, the Engine is too.
    private final Engine engine; 

    // Aggregation: The Car "has a" Driver.
    // The Driver can exist even if the Car is gone.
    private Driver driver;       

    public Car(String model, String engineType) {
        this.model = model;
        this.engine = new Engine(engineType); // Created inside the Car
    }

    public void setDriver(Driver driver) {
        this.driver = driver;
    }

    public void showDetails() {
        System.out.println("Car Model: " + model);
        System.out.println("Engine Type: " + engine.getType());
        String dName = (driver != null) ? driver.getName() : "No driver";
        System.out.println("Current Driver: " + dName);
        System.out.println("---------------------------");
    }
}

public class Main {
    public static void main(String[] args) {
        // Create an independent Driver object
        Driver alice = new Driver("Alice");

        // Create a Car object
        Car myCar = new Car("Tesla Model S", "Dual-Motor Electric");

        // Establish the Aggregation relationship
        myCar.setDriver(alice);
        myCar.showDetails();

        // Demonstrating that the Driver survives the Car
        System.out.println("System: Car is being scrapped...");
        myCar = null; 
        System.out.println("Driver " + alice.getName() + " is still safe!");
    }
}

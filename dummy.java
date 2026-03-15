import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class TaskManager {

    // Global list to store task names
    private ArrayList<String> tasks = new ArrayList<>();

    // Function to add a task to the list
    public void addTask(String taskName) {
        tasks.add(taskName);
        System.out.println("Task added: " + taskName);
    }

    // Function to display tasks in alphabetical order

    public static void main(String[] args) {
        TaskManager manager = new TaskManager();
        Scanner scanner = new Scanner(System.in);
        String input;

        System.out.println("Welcome to the Java Task Manager!");
        System.out.println("Type 'exit' to finish or enter your tasks below:");

        // Loop to take user input
        while (true) {
            System.out.print("Enter task: ");
            input = scanner.nextLine();

            if (input.equalsIgnoreCase("exit")) {
                break;
            }
            manager.addTask(input);
        }

        // Final output
        manager.showSortedTasks();
        System.out.println("\nProgram closed. Happy productivity!");
        scanner.close();
    }
}

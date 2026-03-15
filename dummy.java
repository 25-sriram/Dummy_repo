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
    public void showSortedTasks() {
        if (tasks.isEmpty()) {
            System.out.println("The list is currently empty.");
            return;
        }
        Collections.sort(tasks);
        System.out.println("\n--- Your To-Do List (Sorted) ---");
        for (int i = 0; i < tasks.size(); i++) {
            System.out.println((i + 1) + ". " + tasks.get(i));
        }
    }

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

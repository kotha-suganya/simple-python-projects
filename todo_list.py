class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description):
        task = Task(task_description)
        self.tasks.append(task)
        print(f'Task "{task_description}" added to the list.')

    def remove_task(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                self.tasks.remove(task)
                print(f'Task "{task_description}" removed from the list.')
                return
        print(f'Task "{task_description}" not found in the list.')

    def mark_task_completed(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.mark_completed()
                print(f'Task "{task_description}" marked as completed.')
                return
        print(f'Task "{task_description}" not found in the list.')

    

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Mark Task as Completed")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            task = input("Enter the task to mark as completed: ")
            todo_list.mark_task_completed(task)
       
        elif choice == '6':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
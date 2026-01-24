#Entry point for student productivity system
from task import Task
from task_manager import TaskManager
def main():
    
    manager=TaskManager()
    manager.load_tasks()

    while True:
        print("\nStudent Task Tracker")
        print("1.Add Task")
        print("2.View Tasks")
        print("3.Mark Task as Completed")
        print("4.View Pending Tasks")
        print("5.View Completed Tasks")
        print("6.View Productivity Insights")
        print("7.Exit")

        choice=input("Enter your choice:")
        if choice=="1":
            title=input("Enter task title:")
            deadline=input("Enter deadline:")
            priority=input("Enter priority(Low/Medium/High):")

            task=Task(title,deadline,priority)
            manager.add_task(task)
            print("Task added succesfully!")

        elif choice=="2":
            manager.view_tasks()

        elif choice=="3":
            manager.view_tasks()
            number=int(input("Enter task number to be marked completed:"))
            manager.complete_task(number)

        elif choice=="4":
            manager.view_tasks_by_status(False)
        
        elif choice=="5":
            manager.view_tasks_by_status(True)

        elif choice=="6":
            manager.show_productivity_insights()

        elif choice=="7":
            manager.save_tasks()
            print("Tasks saved.Exiting Task Tracker...Goodbye!")
            break

        else:
            print("Invalid choice.Please try again.")



if __name__=="__main__":
    main()
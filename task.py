class Task:
    def __init__(self,title,deadline,priority):
        self.title=title 
        self.deadline=deadline
        self.priority=priority
        self.completed=False

    def mark_completed(self):
        self.completed=True

    def display(self):
        status="Completed" if self.completed else "Pending"
        print(f"Task:{self.title}")
        print(f"Deadline: {self.deadline}")        
        print(f"Priority: {self.priority}")        
        print(f"Status: {status}")   
        print("-"*20)  

class TaskManager:
    def __init__(self):
        self.tasks=[]
    
    def add_task(self,task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No Tasks Available")
            return
        for index,task in enumerate(self.tasks,start=1):
            print(f"Task:{index}:")
            task.display()

    def complete_task(self,task_number):
        if 1<=task_number<=len(self.tasks):
            self.tasks[task_number-1].mark_completed()
            print("Task marked as completed.")
        else:
            print("Invalid Task Number.")  
            
    def save_tasks(self):
        with open("task.txt","w")as file:
            for task in self.tasks:
                line=f"{task.title}|{task.deadline}|{task.priority}|{task.completed}\n"
                file.write(line)

    def load_tasks(self):
        
        try:
            with open("task.txt","r")as file:
                for line in file:
                    title,deadline,priority,completed=line.strip().split("|")
                    task=Task(title,deadline,priority)
                    task.completed=completed=="True"
                    self.tasks.append(task)
        except FileNotFoundError:
            print("No previous tasks found.")

def main():
    
    manager=TaskManager()
    manager.load_tasks()

    while True:
        print("\nStudent Task Tracker")
        print("1.Add Task")
        print("2.View Tasks")
        print("3.Mark Task as Completed")
        print("4.Exit")

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
            manager.save_tasks()
            print("Tasks saved.Exiting Task Tracker...Goodbye!")
            break

        else:
            print("Invalid choice.Please try again.")



if __name__=="__main__":
    main()

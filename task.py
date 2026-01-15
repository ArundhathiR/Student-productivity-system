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

task1=Task("Math Assignment","15 Jan","High")
task2=Task("DSA Practice","Daily","Medium")   

manager=TaskManager()

manager.add_task(task1)
manager.add_task(task2)
#task1.display()
#task2.display()        
manager.view_tasks()

manager.complete_task(1)

manager.view_tasks()

#task1.mark_completed()
#task1.display()

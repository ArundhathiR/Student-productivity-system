from task import Task
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
            status="Completed" if task.completed else "Pending"
            print(f"{index}.{task.title} | Deadline:{task.deadline} | "
                  f"Priority:{task.priority} | Status:{status}")

    def view_tasks_by_status(self,completed):
        filtered_tasks=[task for task in self.tasks if task.completed == completed]
        if not filtered_tasks:
            print("No matching tasks found.")
            return

        for index,task in enumerate(filtered_tasks,start=1):
            status="Completed" if task.completed else "Pending"
            print(f"{index}.{task.title}|Deadline:{task.deadline}|"
                  f"Priority:{task.priority}|Status:{status}")      

    def show_productivity_insights(self):
        total=len(self.tasks)
        completed=sum(task.completed for task in self.tasks)
        pending=total-completed

        high_priority_pending=sum(1 for task in self.tasks if task.priority.lower()=="high" and not task.completed)

        print("\nProductivity Insights:")
        print(f"Total tasks: {total}")
        print(f"Completed tasks: {completed}")
        print(f"Pending tasks: {pending}")

        if high_priority_pending>0:
            print(f" !! You have {high_priority_pending} high-priority tasks PENDING")



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
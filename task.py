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

task1=Task("Math Assignment","15 Jan","High")
task2=Task("DSA Practice","Daily","Medium")   

task1.display()
task2.display()        

task1.mark_completed()
task1.display()

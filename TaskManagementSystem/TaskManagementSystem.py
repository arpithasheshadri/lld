from enum import Enum
from datetime import datetime

class Role(Enum):
    ADMIN = "Admin"
    MEMBER = "Member"

class Status(Enum):
    TODO = "To-Do"
    INPROGRESS = "In-Progress"
    DONE = "Done"

class TaskPriority(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class User:
    def __init__(self, username: str, role:Role):
        self.username = username
        self.tasks = []
        self.role = role

    def create_task(self,title:str, description:str,priority:TaskPriority, due_date:str):
        task = Task(self,title,description,priority,due_date)
        return task
    
    def __str__(self):
        return f"username: {self.username} - role: {self.role}"
    
class Comments:
    def __init__(self,user:User, content:str):
        self.content = content
        self.user = user
        self.created_at = datetime.now()

    def __str__(self):
        return f"{self.user.username} - {self.content}"

class Task:
    def __init__(self,user,title,description,priority,due_date):
        self.user = user
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority
        self.status = Status.TODO
        self.comments = []
        self.assignees = []

    def assign_user(self,user:User):
        self.assignees.append(user)

    def add_comment(self,comment:Comments):
        self.comments.append(comment)

    def update_status(self,status:Status):
        self.status = status

    def __str__(self):
        return f"Task: {self.title} - Priority: {self.priority} - Status: {self.status}"
    
class Project:
    def __init__(self,name:str, user:User):
        self.name = name
        self.owner = user
        self.tasks = []

    def add_task(self, task:Task):
        self.tasks.append(task)

    def get_task_by_status(self, status:Status):
        return [task for task in self.tasks if task.status == status]
    
    def __str__(self):
        return f"Project: {self.name} - Owner: {self.owner}"
    
class Board:
    def __init__(self,project:Project):
        self.project = project
        self.columns = {
            Status.TODO: [],
            Status.INPROGRESS: [],
            Status.DONE: []
        }
        self.refresh_board()

    def refresh_board(self):
        for status in self.columns:
            self.columns[status] = self.project.get_task_by_status(status)

    def display_board(self):
        self.refresh_board()
        print(f"Board for project - {self.project.name}")
        for status,tasks in self.columns.items():
            print(f"{status.value}")
            for task in tasks:
                print(f" {task.title}")

class Notification:
    def __init__(self,user:User, message:str):
        self.user = user
        self.message = message
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"


class TaskManagementSystem:
    def __init__(self):
        self.users = []
        self.projects = []

    def register_user(self, username, role):
        user = User(username, role)
        self.users.append(user)
        return user
    
    def create_project(self, name, owner):
        project = Project(name,owner)
        self.projects.append(project)
        return project
    
    def assign_task(self, task, user):
        task.assign_user(user)
        return Notification(user,f"Task {task.title} has been assigned")

    def show_projects(self):
        for project in self.projects:
            print(project)

    def show_users(self):
        for user in self.users:
            print(user)


def main():
    system = TaskManagementSystem()

    admin = system.register_user("Alice",Role.ADMIN)
    user1 = system.register_user("Bob",Role.MEMBER)
    user2 = system.register_user("Kathy",Role.MEMBER)

    proj1 = system.create_project("PMS",admin)

    task1 = user1.create_task("Build UI","Create UI for login",TaskPriority.HIGH,"2024-01-02")
    task2 = user2.create_task("Build backend","Create backend for login",TaskPriority.MEDIUM,"2024-06-02")

    proj1.add_task(task1)
    proj1.add_task(task2)

    notif1 = system.assign_task(task1,user2)
    notif2 = system.assign_task(task2,user2)

    print(notif1)
    print(notif2)

    print("Project")
    print(proj1)

    board = Board(proj1)
    board.display_board()

    task1.update_status(Status.INPROGRESS)

    board.display_board()

    comment = Comments(user1,"Started working on UI")
    task1.add_comment(comment)

    print("Comments")
    for comment in task1.comments:
        print(comment)

if __name__ == "__main__":
    main()




class Register:
    def __init__(self):
        self.tasks = dict()

    def register(self, task):
        self.tasks[task.__name__] = task
        def wrapper():
            return task
        return wrapper()

    def get(self, task_name):
        task = self.tasks.get(task_name)
        if not task:
            raise Exception(f"Unable to find a task with name {task_name}")
        
        return task

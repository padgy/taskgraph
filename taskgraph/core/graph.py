
from taskgraph.core.task import Task


class Graph:
    def __init__(self, registry):
        self.registry = registry
        self.task_map = []

    def create_task_map(self, task: Task):
        if not task.dependencies:
            self.task_map.append(task)
            return

        for dependency in task.dependencies:
            self.task_map.append(dependency)
            self.task_map.append(task)

    def execute(self):
        for task in self.task_map:
            print(f"Running task {task.__name__}")
            task.run()

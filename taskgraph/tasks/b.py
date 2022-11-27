from taskgraph.core.task import Task
from taskgraph import register

@register.register
class TaskB(Task):
    def run():
        print("hey from func b")

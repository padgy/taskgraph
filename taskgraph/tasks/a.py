from taskgraph.core.task import Task
from taskgraph import register
from taskgraph.tasks.b import TaskB

@register.register
class TaskA(Task):
    dependencies = (TaskB,)
    def run():
        print("hey from func a")

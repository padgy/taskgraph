import fire

from taskgraph.core.graph import Graph
from taskgraph import register
from taskgraph.tasks import *

def run_task(task=None):
    if not task:
        print("No task entered")

    task = register.get(task)

    graph = Graph(register)
    graph.create_task_map(task)
    graph.execute()

print(register.tasks)

if __name__ == "__main__":
    fire.Fire(run_task)
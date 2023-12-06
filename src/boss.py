from queueClient import QueueClient
import time
from task import Task

class Boss:
    def __init__(self) -> None:
        self.client = QueueClient()

    def add_task(self, task):
        self.client.task_queue.put(task)
        print("Boss added a new Task to the queue.")

if __name__ == "__main__":
    boss = Boss()

    task_id = 0
    while True:
        task_id += 1
        boss.add_task(
            Task(str(task_id), 10)
        )
        time.sleep(0.1)
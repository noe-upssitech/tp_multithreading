from queueClient import QueueClient
import time
from task import Task

class Boss(QueueClient):
    def __init__(self, task_size = 10) -> None:
        super().__init__()
        self.task_size = task_size

    def add_task(self, task):
        self.task_queue.put(task)
        print(f"Boss added new Task {task.getId()} to the queue.")

    def read_results(self):
        while True:
            print(f"Boss is waiting for results...")
            result = self.result_queue.get()
            print(f"Boss got result from Task {result.getId()} in {result.getTime()}")
            print(result.x)

    def run(self, number_of_tasks = 10):
        task_id = 0
        while task_id < number_of_tasks:
            task_id += 1
            boss.add_task(
                Task(str(task_id), self.task_size)
            )
            time.sleep(0.1)

if __name__ == "__main__":
    boss = Boss(task_size=2000)
    boss.run()
    boss.read_results()

    
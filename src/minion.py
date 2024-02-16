from queueClient import QueueClient
from task import Task
import time 

class Minion(QueueClient):
    def __init__(self, id : int) -> None:
        super().__init__()
        self.id = id

    def work(self):
        while True:
            print(f"No task in the queue. Minion {self.id} is waiting...")
            task = self.task_queue.get()
            
            print(f"Minion {self.id} got task {task.getId()} and is working.")
            task.work()
            self.result_queue.put(task)
            print(f"Minion {self.id} finished task {task.getId()} in {task.getTime()} and put it in the result queue.")

if __name__ == "__main__":
    minion = Minion(id = 1)
    minion.work()
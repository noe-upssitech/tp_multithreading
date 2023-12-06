from queueClient import QueueClient
import time 

class Minion:
    def __init__(self, id : int) -> None:
        self.queue = QueueClient()
        self.id = id

    def work(self):
        while True:
            try:
                task = self.queue.task_queue.get_nowait()           
            except self.queue.Empty:
                print("No task in the queue. Minion is waiting...")
                time.sleep(1)    

            task.work()
            self.queue.result_queue.put(task)
            print(f"Minion {self.id} finished task {task.getId()} in {task.getTime()} and put it in the result queue.")


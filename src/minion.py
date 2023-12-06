from queueClient import QueueClient
import time 

class Minion:
    def __init__(self) -> None:
        self.queue = QueueClient()

    def work(self):
        while True:
            try:
                task = self.queue.task_queue.get_nowait()           
            except self.queue.Empty:
                print("No task in the queue. Minion is waiting...")
                time.sleep(1)    

            task.work()
            self.queue.result_queue.put(task)


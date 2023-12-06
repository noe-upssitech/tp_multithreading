from queueClient import QueueClient

class Boss:
    def __init__(self) -> None:
        self.client = QueueClient()

    def add_task(self, task):
        self.client.task_queue.put(task)

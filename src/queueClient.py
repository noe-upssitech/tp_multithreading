from queueManager import QueueManager

class QueueClient:
    def __init__(self) -> None:
        
        self.manager = QueueManager(address=('localhost', 50000), authkey=b'abc123')
        self.manager.connect()

        self.manager.register("get_task_queue")
        self.task_queue = self.manager.get_task_queue()
        
        self.manager.register("get_result_queue")
        self.result_queue = self.manager.get_result_queue()

if __name__ == "__main__":
    client = QueueClient()
    print(client.task_queue)
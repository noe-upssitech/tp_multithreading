from queueManager import QueueManager

class QueueClient:
    def __init__(
            self, 
            adress: str = ("localhost", 50000),
            authkey: bytes = b"abc123",
        ) -> None:
        
        self.task_queue = QueueManager.register("get_tasks")
        self.result_queue = QueueManager.register("get_results")

        self.manager = QueueManager(address=adress, authkey=authkey)

        self.manager.connect()

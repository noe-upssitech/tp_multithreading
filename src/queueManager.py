from multiprocessing import Queue
from multiprocessing.context import BaseContext
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    def __init__(
        self,
        address,
        authkey: bytes | None = None,
        serializer: str = "pickle",
        ctx: BaseContext | None = None,
    ) -> None:
        
        super().__init__(address, authkey, serializer, ctx)

        self.task_queue = Queue()
        self.result_queue = Queue()

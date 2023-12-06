from multiprocessing import Queue
from multiprocessing.context import BaseContext
from multiprocessing.managers import BaseManager
from task import Task


class QueueManager(BaseManager):
    def __init__(
        self,
        address,
        authkey: bytes,
        serializer: str = "pickle",
        ctx: BaseContext | None = None,
    ) -> None:
        
        super().__init__(address, authkey, serializer, ctx)

        self.task_queue = Queue()
        self.result_queue = Queue()

        self.register('get_task', callable = lambda: self.task_queue)
        self.register('get_results', callable = lambda: self.result.queue)

        self.get_server().serve_forever()
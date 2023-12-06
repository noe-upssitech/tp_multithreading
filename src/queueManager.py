from multiprocessing import Queue
from multiprocessing.context import BaseContext
from multiprocessing.managers import BaseManager
from task import Task

import sys
import itertools
import time
import threading


class QueueManager(BaseManager):
    def __init__(
        self,
        address,
        authkey: bytes,
        serializer: str = "pickle",
        ctx: BaseContext | None = None,
    ) -> None:

        self.task_queue = Queue()
        self.result_queue = Queue()

        self.register('get_task', callable = lambda: self.task_queue)
        self.register('get_results', callable = lambda: self.result.queue)

        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                sys.stdout.write('\rManager created and serving forever ' + c)
                sys.stdout.flush()
                time.sleep(0.3)

        t = threading.Thread(target=animate)
        t.start()
        self.get_server().serve_forever()

if __name__ == "__main__":
    manager = QueueManager(
        address = ('127.0.0.1', 50000),
        authkey = b'abc'
    )


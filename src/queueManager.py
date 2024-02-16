from multiprocessing import Queue
from multiprocessing.managers import BaseManager

import sys
import itertools
import time
import threading


class QueueManager(BaseManager):
    def __init__(self, address, authkey):
        super().__init__(address=address, authkey=authkey)

        self.task_queue = Queue()
        self.result_queue = Queue()

        self.register('get_task_queue', callable = lambda: self.task_queue)
        self.register('get_results_queue', callable = lambda: self.result_queue)

    def serve(self):

        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                sys.stdout.write('\rManager created and serving forever at ' + f"{self.address[0]}:{self.address[1]}" + " " + c)
                sys.stdout.flush()
                time.sleep(0.3)
        
        t = threading.Thread(target=animate)
        t.start()
        self.get_server().serve_forever()

if __name__ == "__main__":
    manager = QueueManager(
        address = ('localhost', 50000),
        authkey = b'abc123'
    )

    manager.serve()


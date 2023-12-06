from Boss import Boss
from Minion import Minion


class QueueClient:
    def __init__(self) -> None:
        self.Boss = Boss()
        self.Minion = Minion()

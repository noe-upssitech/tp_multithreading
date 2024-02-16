import numpy as np
from time import perf_counter
import json

import unittest

class Task:
    def __init__(self, identifier : str, size : int = 10) -> None:
        self.identifier = identifier
        self.size = size
        
        # Input matrices
        self.a = np.random.rand(size, size)
        self.b = np.random.rand(size, size)
        
        # Output matrice
        self.x = np.zeros((size, size)) # Results
        
        self.time = 0

    def work(self):
        t0 = perf_counter()
        self.x = np.dot(self.a, self.b)
        self.time = perf_counter() - t0

    def to_json(self) -> str:
        return json.dumps(
            {
                "id": self.identifier,
                "size": self.size,
                "a": self.a.tolist(),
                "b": self.b.tolist(),
                "x": self.x.tolist(),
                "time": self.time
            }
        )
    
    @classmethod
    def from_json(self, txt : str):
        txt = json.loads(txt)
        task = Task(txt["id"], txt["size"])

        task.a = np.array(txt["a"])
        task.b = np.array(txt["b"])
        task.x = np.array(txt["x"])
        task.time = txt["time"]
        return task
    
    def __eq__(self, other: "Task") -> bool:
        if not isinstance(other, Task):
            return False
        
        return (
            self.identifier == other.identifier and
             self.size == other.size and
            np.array_equal(self.a, other.a) and
            np.array_equal(self.b, other.b) and
            np.array_equal(self.x, other.x) and
            self.time == other.time
            )

    def getId(self):
        return self.identifier
    
    def getTime(self):
        return self.time

class TestTask(unittest.TestCase):
    def test_task_json(self):
        a = Task("1", 10)
        a.work()
        b = a.from_json(a.to_json())
        self.assertEqual(a, b)

if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
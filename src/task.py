import numpy as np
from time import perf_counter

class Task:
    def __init__(self, identifier : str, size : int = 10) -> None:
        self.identifier = identifier
        self.size = size
        
        # Input matrices
        self.a = np.random.rand(size, size)
        self.b = np.random.rand(size, size)
        
        # Output matrice
        self.x = np.zeros(size, size) # Results
        
        self.time = 0

    def work(self):
        t0 = perf_counter()
        self.x = np.dot(self.a, self.b)
        self.time = perf_counter() - t0

    def getId(self):
        return self.identifier
    
    def getTime(self):
        return self.time

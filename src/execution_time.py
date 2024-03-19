import time

class ExecutionTime:
    total_time: float
    start_time: float
    end_time: float
    
    def __init__(self):
        self.total_time = 0
    
    def start(self):
        self.start_time = time.time()
    
    def stop(self):
        self.end_time = time.time()
        self.total_time += (self.end_time * 1000) - (self.start_time * 1000)
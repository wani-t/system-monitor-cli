import threading
import time
import psutil

class Monitor:
    def __init__(self, buffer):
        self._running =False 
        self._thread = None 
        self.buffer = buffer
        #using deque to prevent unbounded memory usage

    def _collect(self):
        while self._running:
            stats = {
                "timestamp": time.time(),
                "cpu": psutil.cpu_percent(interval = 1),
                "memory": psutil.virtual_memory().percent
            }
            self.buffer.append(stats) #10k entries ~ 30MB
            time.sleep(1)

    def start(self):
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._collect, daemon=True)
            self._thread.start()
            print("Monitor has started collecting data")
        else:
            print("Monitor is already running.")

    def stop(self):
        if self._running:
            self._running= False
            self._thread.join()
            print("Monitor has stopped collecting data.")
        else:
            print("Monitor is not running.")


import time
import threading

def worker():
    print("Worker has started")
    time.sleep(10)
    print("Worker has finished")

t = threading.Thread(target=worker, daemon=False)
t.start()

print("Main thread has finished")

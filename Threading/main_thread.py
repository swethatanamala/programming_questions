import time
import threading

def worker(id):
    print("Thread %d has started" % id)
    time.sleep(5)
    print("Thread %d has finished" % id)

threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to finish their execution
for t in threads:
    t.join()

print("All threads have finished")

import threading

def worker(num):
    """Thread worker function"""
    print(f"Worker {num} started")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

print(threads)
for t in threads:
    t.join()

print("All worker threads completed")
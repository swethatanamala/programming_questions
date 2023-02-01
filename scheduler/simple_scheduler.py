import schedule
import time

def job():
    print("Job running...")

def run_scheduler():
    # Schedule the job to run every 10 seconds
    schedule.every(10).seconds.do(job)

    # Start the scheduler
    while True:
        start_time = time.time()
        schedule.run_pending()
        time.sleep(1)
        end_time = time.time()
        print('diff', end_time - start_time)

def run_whileloop():
    while True:
        start_time = time.time()
        job()
        time.sleep(1)
        end_time = time.time()
        print('diff', end_time - start_time)

run_scheduler()

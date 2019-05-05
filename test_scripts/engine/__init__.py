import schedule
import time

def job():
    print('aaa')

schedule.every(1/60).minutes.do(job)

def start():
    while True:
        schedule.run_pending()
        time.sleep(1)

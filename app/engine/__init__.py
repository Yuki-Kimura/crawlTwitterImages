import time

import schedule
from modules.run import run


def job():
    run()


schedule.every(1).minutes.do(job)


def start():
    while True:
        schedule.run_pending()
        time.sleep(1)

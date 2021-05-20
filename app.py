import schedule
import time
import os
os.system('python app/coinscrap/appscrap.py')
print('Scheduler initialised')
schedule.every(1).minutes.do(lambda: os.system('python app/coinscrap/appscrap.py'))
print('Next job is set to run at: ' + str(schedule.next_run()))

while True:
    schedule.run_pending()
    time.sleep(1)

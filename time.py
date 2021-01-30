import datetime as dt
from threading import Timer
def my_job():
    print("hello world")

print(dt.datetime.now())
nextDay = dt.datetime.now() + dt.timedelta(days=1)
# dateString = nextDay.strftime('%d-%m-%Y') + " 01-00-00"
dateString = '29-01-2021 16-40-25'
newDate = nextDay.strptime(dateString,'%d-%m-%Y %H-%M-%S')

delay = (newDate - dt.datetime.now()).total_seconds()

Timer(delay,my_job,()).start()
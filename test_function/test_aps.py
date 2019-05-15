from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

def job():
    print("HELLO !")


Scheduler=BackgroundScheduler()
# 每年的1-2.9-12每周6.7每天8:16: 10.15
#Scheduler.add_job(job, "cron", month="1-2,9-12", day_of_week="5-6", hour="8", minute=17, second="45,50")
Scheduler.add_job(job, "interval", seconds=3, start_date=datetime(2019,5,15,2,20,40))
Scheduler.start()

while True:
    pass
# interval
# weeks (int) – number of weeks to wait
# days (int) – number of days to wait
# hours (int) – number of hours to wait
# minutes (int) – number of minutes to wait
# seconds (int) – number of seconds to wait
# start_date (datetime|str) – starting point for the interval calculation
# end_date (datetime|str) – latest possible date/time to trigger on

# date
# run_date (datetime|str) – the date/time to run the job at

# cron
# year (int|str) – 4-digit year
# month (int|str) – month (1-12)
# day (int|str) – day of the (1-31)
# week (int|str) – ISO week (1-53)
# day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
# hour (int|str) – hour (0-23)
# minute (int|str) – minute (0-59)
# second (int|str) – second (0-59)
# start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
# end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
# timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)year (int|str) – 4-digit year

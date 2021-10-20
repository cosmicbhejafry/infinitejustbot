from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=42)
# def timed_job():
#     print('This job is run every 42 minutes.')

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=1)
def scheduled_job():
    print('This job is run every weekday at 1am')

# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=3)
# def scheduled_job():
#     print('This job is run every weekday at 3am')

# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=5)
# def scheduled_job():
#     print('This job is run every weekday at 5am.')

# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=8)
# def scheduled_job():
#     print('This job is run every weekday at 8am.')

# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=13)
# def scheduled_job():
#     print('This job is run every weekday at 13pm.')

# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=21)
# def scheduled_job():
#     print('This job is run every weekday at 21pm.')

sched.start()
